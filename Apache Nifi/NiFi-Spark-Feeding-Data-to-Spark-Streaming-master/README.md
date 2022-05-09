# NiFi Site-to-Site Direct Streaming to Spark for Log Ingestion

## Index

* [Short Description](https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming#short-description)
* [Introduction](https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming#introduction)
* [Prerequisites](https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming#prerequisites)
* [Configuring and Creating Table in Hbase via Phoenix](https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming#configuring-and-creating-table-in-hbase-via-phoenix)
* [Configuring and Restarting Spark](https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming#configuring-and-restarting-spark)
* [Configuring and Starting NiFi](https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming#configuring-and-starting-nifi)
* [Building a Flow in NiFi to fetch and parse nifi-app.log](https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming#building-a-flow-in-nifi-to-fetch-and-parse-nifi-applog)
* [Building Spark application](https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming#building-spark-application)
* [Extending NiFi Flow to ingest data directly to Phoenix using PutSql processor](https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming#extending-nifi-flow-to-ingest-data-directly-to-phoenix-using-putsql-processor)
* [References](https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming#references)

## Short Description

Sample Application for Log Ingestion with NiFi and Spark into Phoenix using NiFi Site-to-Site on HW Sandbox.

## Introduction

Using NiFi, data can be exposed in such a way that a receiver can pull from it by adding an Output Port to the root process group. 
For Spark, we will use this same mechanism - we will use the Site-to-Site protocol to pull data from NiFi's Output Ports. In this tutorial we learn to capture NiFi app log from the Sandbox and parse it using Java regex and ingest it to Phoenix via Spark or Directly using NiFi PutSql Processor.

## Prerequisites

1) Assuming you already have latest version of NiFi-1.x/HDF-2.x downloaded as zip file (HDF and HDP cannot be managed by Ambari on same nodes as of now) on to your HW Sandbox Version 2.5, else execute below after ssh connectivity to sandbox is established:

```
# mkdir /opt/HDF-2.1.1
# cd /opt/HDF-2.1.1
# wget http://public-repo-1.hortonworks.com/HDF/2.1.1.0/nifi-1.1.0.2.1.1.0-2-bin.tar.gz
# tar -xvf nifi-1.1.0.2.1.1.0-2-bin.tar.gz
```
2) Spark, Zeppelin, YARN and HDFS are Installed on your VM and started.

3) Hbase is Installed with phoeix Query Server.

4) Download Compatible version [in our case 1.1.0] of "nifi-spark-receiver" and "nifi-site-to-site-client" to Sandbox in a specific location:
```
# mkdir /opt/spark-receiver
# cd /opt/spark-receiver
# wget http://central.maven.org/maven2/org/apache/nifi/nifi-spark-receiver/1.1.0/nifi-spark-receiver-1.1.0.jar
# wget http://central.maven.org/maven2/org/apache/nifi/nifi-site-to-site-client/1.1.0/nifi-site-to-site-client-1.1.0.jar
```

5) Make sure Git is installed on the VM:
```
# yum install git -y
```

## Configuring and Creating Table in Hbase via Phoenix

1) Make sure Hbase components as well as phoenix query server is started.

2) Make sure Hbase is up and running and out of maintenance mode, below properties are set(if not set it and restart the services):
	
	- Enable Phoenix --> Enabled
	
	- Enable Authorization --> Off
3) Create Phoenix Table after connecting to phoenix shell (or via Zeppelin):
	
```
# /usr/hdp/current/phoenix-client/bin/sqlline.py sandbox.hortonworks.com:2181:/hbase-unsecure
```

4) Execute below in the Phoenix shell to create tables in Hbase:

```
CREATE TABLE NIFI_LOG( UUID VARCHAR NOT NULL, EVENT_DATE VARCHAR, BULLETIN_LEVEL VARCHAR, EVENT_TYPE VARCHAR, CONTENT VARCHAR CONSTRAINT pk PRIMARY KEY(UUID));
CREATE TABLE NIFI_DIRECT( UUID VARCHAR NOT NULL, EVENT_DATE VARCHAR, BULLETIN_LEVEL VARCHAR, EVENT_TYPE VARCHAR, CONTENT VARCHAR CONSTRAINT pk PRIMARY KEY(UUID));

```

## Configuring and Restarting Spark

1) Login to Ambari UI and Navigate to Services --> Spark --> Configs --> Custom spark-defaults and add 2 below properties with given values:

```
spark.driver.extraClassPath			/opt/HDF-2.1.1/nifi-1.1.0.2.1.1.0-2/lib/nifi-framework-api-1.1.0.2.1.1.0-2.jar:/opt/spark-receiver/nifi-site-to-site-client-1.1.0.jar:/opt/spark-receiver/nifi-spark-receiver-1.1.0.jar:/opt/HDF-2.1.1/nifi-1.1.0.2.1.1.0-2/lib/nifi-api-1.1.0.2.1.1.0-2.jar:/opt/HDF-2.1.1/nifi-1.1.0.2.1.1.0-2/lib/bootstrap/nifi-utils-1.1.0.2.1.1.0-2.jar:/opt/HDF-2.1.1/nifi-1.1.0.2.1.1.0-2/work/nar/framework/nifi-framework-nar-1.1.0.2.1.1.0-2.nar-unpacked/META-INF/bundled-dependencies/nifi-client-dto-1.1.0.2.1.1.0-2.jar:/opt/HDF-2.1.1/nifi-1.1.0.2.1.1.0-2/work/nar/framework/nifi-framework-nar-1.1.0.2.1.1.0-2.nar-unpacked/META-INF/bundled-dependencies/httpcore-nio-4.4.5.jar:/usr/hdp/current/phoenix-client/phoenix-client.jar
spark.driver.allowMultipleContexts = true
```
![alt tag](https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming/blob/master/resources/images/Spark-Config.jpg)

2) Once properties are add, restart Spark.

	
## Configuring and Starting NiFi

1) Open **nifi.properties** for updating configurations:

```
# vi /opt/HDF-2.1.1/nifi-1.1.0.2.1.1.0-2/conf/nifi.properties
```

2) Change NIFI http port to run on 9090 as default 8080 will conflict with Ambari web UI

```
# web properties #
nifi.web.http.port=9090
```

3) Configure NiFi instance to run site-to site by changing below configuration : add a port say 8055 and set "nifi.remote.input.secure" as "false"

```
# Site to Site properties #
nifi.remote.input.socket.port=8055
nifi.remote.input.secure=false
```

4) Now Start [Restart if already running for configuration change to take effect] NiFi on your Sandbox.

```
# /opt/HDF-2.1.1/nifi-1.1.0.2.1.1.0-2/bin/nifi.sh start
```
5) Make sure NiFi is up and running by connecting to its Web UI from your browser:

```
http://your-vm-ip:9090/nifi/ 
```
## Building a Flow in NiFi to fetch and parse nifi-app.log

1) Let us build a small flow on NiFi canvas to read app log generated by NiFi itself to feed to Spark:
	
2) Drop a  "**TailFile**" Processor to canvas to read lines added to "**/opt/HDF-2.1.1/nifi-1.1.0.2.1.1.0-2/logs/nifi-app.log**". Auto Terminate relationship Failure. 
![alt tag](https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming/blob/master/resources/images/TailFile.jpg)

3) Drop a  "**SplitText**" Processor to canvas to split the log file into separate lines. Auto terminate Original and Failure Relationship for now. Connect TailFile processor to SplitText Processor for Success Relationship.
![alt tag](https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming/blob/master/resources/images/SplitText.jpg)

4) Drop a  "**ExtractText**" Processor to canvas to extract portions of the log content to attributes as below. Connect SplitText processor to ExtractText Processor for splits relationship.

```
	- BULLETIN_LEVEL	:	([A-Z]{4,5})
	- CONTENT			:	(^.*)
	- EVENT_DATE		:	([^,]*)
	- EVENT_TYPE		:	(?<=\[)(.*?)(?=\])
```	
![alt tag](https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming/blob/master/resources/images/ExtractText.jpg)

5) Drop an OutputPort to the canvas and Name it "**spark**", Once added, connect "ExtractText" to the port for matched relationship. The Flow would look similar as below:
![alt tag](https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming/blob/master/resources/images/Spark-Flow.jpg)

6) Start the flow on NiFi and notice data is stuck in the connection before the output port "spark"


## Building Spark application 

1) To begin with, lets clone the git repo below:

```
# cd /opt/
# git clone https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming.git
```

2) Feel free the inspect Spark application code:

```
# vi /opt/NiFi-Spark-Feeding-Data-to-Spark-Streaming/src/main/Spark+NiFi+Phoenix.sh

```

3) Now let us go ahead and submit the Spark Application to YARN or can run locally via spark-shell

```
# spark-shell --master yarn --deploy-mode client -i /opt/NiFi-Spark-Feeding-Data-to-Spark-Streaming/src/main/Spark+NiFi+Phoenix.sh

OR 

# spark-shell -i /opt/NiFi-Spark-Feeding-Data-to-Spark-Streaming/src/main/Spark+NiFi+Phoenix.sh
```

![alt tag](https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming/blob/master/resources/images/Spark-Shell.jpg)

4) Make sure the application is submitted and it prints out statistics. 

5) Lets Go ahead and verify that the Application is submitted and started in YARN (you can drill down and see the Application-Master spark UI as well): 

```
YARN UI: http://your-vm-ip:8088
```
![alt tag](https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming/blob/master/resources/images/YARN-UI.jpg)

Or if you Submit the application locally you can verify that by accessing spark shell application UI:

```
http://sandbox.hortonworks.com:4040/executors/
```
![alt tag](https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming/blob/master/resources/images/Spark-UI.jpg)

6) Lets Go back to the NiFi Web UI, if everything worked fine, the data which was pending on the port 'spark' will be gone as it was consumed by Spark.

7) Now Lets Connect to Phoenix and check out the data populated in tables, you can either use Phoenix sqlline command line or Zeppelin 

 - via phoenix sqlline
 
```
# /usr/hdp/current/phoenix-client/bin/sqlline.py localhost:2181:/hbase-unsecure 

SELECT EVENT_DATE,EVENT_TYPE,BULLETIN_LEVEL FROM NIFI_LOG WHERE BULLETIN_LEVEL='INFO' ORDER BY EVENT_DATE LIMIT 20;
```

![alt tag](https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming/blob/master/resources/images/sqlline.jpg)

 - via Zeppelin for better visualization 
 
```
Zeppelin UI: http://your-vm-ip:9995/
```
![alt tag](https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming/blob/master/resources/images/Zeppelin.jpg)


## Extending NiFi Flow to ingest data directly to Phoenix using PutSql processor

1) Lets go ahead and kill the Spark Application by pressing cntrl+c from command-line:

2) Log back to NiFi UI currently running the flow, and stop the entire flow.

3) Drop a RouteOnAttribute processor to canvas for Matched relation from ExtractText processor and configure it with below property and auto terminate unmatched relation.
```
DEBUG  : ${BULLETIN_LEVEL:equals('DEBUG')}
ERROR  : ${BULLETIN_LEVEL:equals('ERROR')}
INFO   : ${BULLETIN_LEVEL:equals('INFO')}	
WARN   : ${BULLETIN_LEVEL:equals('WARN')}
```
![alt tag](https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming/blob/master/resources/images/RouteOnAttribute.jpg)

4) Drop an AttributesToJSON processor to canvas with below configuration and connect RouteOnAttribute's DEBUG,ERROR,INFO,DEBUG relations to it.

```
Attributes List : uuid,EVENT_DATE,BULLETIN_LEVEL,EVENT_TYPE,CONTENT
Destination : flowfile-content
```
![alt tag](https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming/blob/master/resources/images/AttributesToJSON.jpg)

5) Create and enable DBCPConnectionPool with name "Phoenix-Spark" with below configuration:

```
Database Connection URL : jdbc:phoenix:sandbox.hortonworks.com:2181:/hbase-unsecure
Database Driver Class Name : org.apache.phoenix.jdbc.PhoenixDriver
Database Driver Location(s) : /usr/hdp/current/phoenix-client/phoenix-client.jar	
```
![alt tag](https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming/blob/master/resources/images/Phoenix-Spark.jpg)

6) Drop a ConvertJSONToSQL to canvas with below configuration, connect AttributesToJSON's success relation to it, auto terminate Failure relation for now after connecting to Phoenix-Spark DB Controller service.

![alt tag](https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming/blob/master/resources/images/ConvertJSONToSQL.jpg)

7) Drop a ReplaceText processor canvas to update INSERT statements to UPSERT for Phoenix with below configuration, connect sql relation of ConvertJSONToSQL auto terminate original and Failure relation.

![alt tag](https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming/blob/master/resources/images/ReplaceText.jpg)

8) Finally add a PutSQL processor with below configurations and connect it to ReplaceText's success relation and auto terminate all of its relations.

![alt tag](https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming/blob/master/resources/images/PutSQL.jpg)

9) The final flow including both ingestion via Spark and direct to phoenix using PutSql is complete, it should look similar to below:

![alt tag](https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming/blob/master/resources/images/Final_Flow.jpg)

10) Now go ahead and start the flow to ingest data to both Tables via Spark and directly from NiFi.

11) Login back to Zeppelin to see if data is populated in the NIFI_DIRECT table.
```
%jdbc(phoenix)
SELECT EVENT_DATE,EVENT_TYPE,BULLETIN_LEVEL FROM NIFI_DIRECT WHERE BULLETIN_LEVEL='INFO' ORDER BY EVENT_DATE
```
![alt tag](https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming/blob/master/resources/images/Zeppelin_Final.jpg)

* Too Lazy to create flow??? download my flow template [here] (https://github.com/jobinthompu/NiFi-Spark-Feeding-Data-to-Spark-Streaming/blob/master/resources/templates/Spark_NiFi_Phoenix.xml)

#### This completes the tutorial,  You have successfully:

* Installed and Configured HDF 2.1 on your HDP-2.5 Sandbox.
* Created a Data flow to pull logs and then to Parse it and make it available on a Site-to-site enabled NiFi port.
* Created a Spark Application to consume data from NiFi via Site-to-Site and Ingest it to Hbase via Phoenix.
* Directly Ingested Data to Phoenix with PutSQL Processor in NiFi with out using Spark.
* Viewed the Ingested data from Phoenix command line and Zeppelin


### References:

* [ Mark Payne's - NiFi-Spark](https://blogs.apache.org/nifi/entry/stream_processing_nifi_and_spark)
* [ My HCC Article](https://community.hortonworks.com/articles/12708/nifi-feeding-data-to-spark-streaming.html)

Thanks,

Jobin George
