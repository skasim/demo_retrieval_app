from typing import Union

from fastapi import FastAPI
from es_connector import ElasticsearchConnector

import os

app = FastAPI()
es = ElasticsearchConnector()

@app.get("/")
def read_root():
    return {"This is a demo retrieval app to showcase some interesting technologies."}

@app.get("/search/")
async def search(query: str):

    # Execute the search query

    print(f"connected to es?: {es.es_client.info().body}")
    search_results = es.search_documents(index_name=os.getenv("ES_MOVIES_INDEX_NAME"), _query=None)

    # Process and return the search results
    print(f"RESULT!: {search_results}")
    return {"results": search_results.body}



