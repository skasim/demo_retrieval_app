# Running Kafka and Zookeeper
1. Run Kafka, ZK, and Kafka-Connector with `docker-compose.yml`
2. Check that connector is running in [http://localhost:8083/](http://localhost:8083/)

# Create an ES index
ES index must have same index name as topic, i.e., `chitchat`
```
curl -X PUT "localhost:9200/chitchat?pretty"
```

## Create an ES-Kafka Connector
```
POST http://localhost:8083/connectors
Content-Type: application/json
{
 "name": "elasticsearch-connector",
 "config": {
   "connector.class": "io.confluent.connect.elasticsearch.ElasticsearchSinkConnector",
   "connection.url": "http://elasticsearch:9200",
   "tasks.max": "1",
   "topics": "chitchat",
   "type.name": "_doc",
    "value.converter": "org.apache.kafka.connect.json.JsonConverter",
    "value.converter.schemas.enable": "false",
     "schema.ignore": "true",
    "key.ignore": "true"
 }
}
```
Check in [http://localhost:8083/connectors](http://localhost:8083/connectors) for connector.
`connection.url` is referencing within the docker network so must call the container name and not `localhost`

## Create a topic
`$topic_name==chitchat``
1. `docker exec -it kafka bash`
2. create a topic: `kafka-topics --create --topic chitchat --bootstrap-server localhost:9092`

## Send messages
1. produce message `kafka-console-producer --topic chitchat --bootstrap-server localhost:9092`
Example messages:
```
{"sentence": "Just joined the forum \u2013 excited to be here!","timestamp": "2023-11-14T12:19:08.487416"}

{"sentence": "is it sunny out?","timestamp": "2023-11-24T12:19:08.487416"}
```
2. check message insertion into

## Consume message
Just for fyi, consume message `kafka-console-consumer --topic chitchat --from-beginning --bootstrap-server localhost:9092`
