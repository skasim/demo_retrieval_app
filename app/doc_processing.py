from es_connector import ElasticsearchConnector
import uuid

es = ElasticsearchConnector()

# create index
es.create_index(index_name="movies")

# index doc
for i in range(0, 10):
    print("inserting doc")
    es.insert_document("movies", uuid.uuid4(), f"this is a doc {i}")
