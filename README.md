# Docker, FastAPI, Elasticsearch, Kafka, Zookeeper, Kafka Connect

This experimental repository, consisting of two main parts, is designed to demonstrate technologies as microservices for their use in data pipeline engineering workflows.

## FastAPI -> ElasticSearch
A list of movies and their plots are stored in an ElasticSearch index (`movies`) and can be queried via FastAPI. This aspect of the project demonstrates indexing of data from static sources, e.g., CSV files.

## Kafka + Zookeeper -> Kafka Connect -> ElasticSearch
Using the same ElasticSearch instance as used above, another index (`chitcat`) stores real-time streaming input through a Kafka Consumer and stored in ElasticSearch via a Kafka Connector. This part of the project demonstrates handling just-in-time data.

## Running the repo
* For details, read `run_fastapi_app.md` and `run_kafka_zk.md`
