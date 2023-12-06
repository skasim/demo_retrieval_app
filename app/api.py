from fastapi import FastAPI
from es_connector import ElasticsearchConnector

import os

app = FastAPI()
es = ElasticsearchConnector()

@app.get("/")
def read_root():
    return {"This is a demo retrieval app to showcase some interesting technologies."}

@app.post("/search/cast/{name}")
async def search_cast(name: str):
    query = {
    "bool": {
        "must": {
            "match_phrase": {
                "cast": f"{name}",
            }
        },
    },
}
    search_results = es.search_documents(index_name=os.getenv("ES_MOVIES_INDEX_NAME"), _query=query)
    return {"results": search_results.body}

@app.post("/search/plot/{term}")
async def search_plot(term: str):
    query = {
        "match": {
            "plot": f"{term}"
        }
    }
    search_results = es.search_documents(index_name=os.getenv("ES_MOVIES_INDEX_NAME"), _query=query)
    return {"results": search_results.body}
