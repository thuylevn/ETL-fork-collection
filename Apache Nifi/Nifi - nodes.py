#################### Start/stop NiFi process-groups ####################
##### syntax
curl -i -X PUT -H 'Content-Type: application/json' -d '{"id":"<processor_group_id>","state":"STOPPED"}' http://<nifi_url>/nifi-api/flow/process-groups/<processor_group_id>;

curl -i -X PUT -H 'Content-Type: application/json' -d '{"id":"<processor_group_id>","state":"RUNNING"}' http://<nifi_url>/nifi-api/flow/process-groups/<processor_group_id>;




processor_group_id  =>  aab7ce98-0180-1000-9d1f-d505bb8fe2c3
nifi_url            =>  http://192.168.99.100:8080


curl -i -X PUT -H 'Content-Type: application/json' -d '{"id":"aab7ce98-0180-1000-9d1f-d505bb8fe2c3","state":"STOPPED"}' http://192.168.99.100:8080/nifi-api/flow/process-groups/aab7ce98-0180-1000-9d1f-d505bb8fe2c3


curl -i -X PUT -H 'Content-Type: application/json' -d '{"id":"aab7ce98-0180-1000-9d1f-d505bb8fe2c3","state":"RUNNING"}' http://192.168.99.100:8080/nifi-api/flow/process-groups/aab7ce98-0180-1000-9d1f-d505bb8fe2c3



### curl --tlsv1.2 -i -H 'Content-Type: application/json' -XPUT -d '{"id":"PG ID","state":"STOPPED"}'  http://nifi-server-ip:port/nifi-api/flow/process-groups/PG ID 

curl --tlsv1.2 -i -H 'Content-Type: application/json' -XPUT -d '{"id":"aab7ce98-0180-1000-9d1f-d505bb8fe2c3","state":"STOPPED"}' http://192.168.99.100:8080/nifi-api/flow/process-groups/aab7ce98-0180-1000-9d1f-d505bb8fe2c3


curl --tlsv1.2 -i -H 'Content-Type: application/json' -XPUT -d '{"id":"aab7ce98-0180-1000-9d1f-d505bb8fe2c3","state":"RUNNING"}' http://192.168.99.100:8080/nifi-api/flow/process-groups/aab7ce98-0180-1000-9d1f-d505bb8fe2c3


#################### Start/stop NiFi processors ####################