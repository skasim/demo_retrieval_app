# Running FastAPI app to store data in ElasticSearch
* clone this repo
* run `docker-compose up -d`
* access swagger ui at [http://localhost:8000/docs](http://localhost:8000/docs). If getting 500 error when making requests, run `docker-compose down api` and restart the api with `docker-compose up -d api`
* access elasticsearch at [http://localhost:9200/movies/_search?pretty](http://localhost:9200/movies/_search?pretty) and [http://localhost:9200/chitchat/_search?pretty](http://localhost:9200/chitchat/_search?pretty)
* access kafka connectors at [http://localhost:8083/connectors](http://localhost:8083/connectors)
