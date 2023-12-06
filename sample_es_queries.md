# Match All
{"match_all": {}}

# Match Phrase
{
    "bool": {
        "must": {
            "match_phrase": {
                "cast": "jack nicholson",
            }
        },
    },
}

# Filter
{
    "bool": {
        "must": {
            "match_phrase": {
                "cast": "jack nicholson",
            }
        },
        "filter": {"bool": {"must_not": {"match_phrase": {"director": "stephen spielberg"}}}},
    },
}
