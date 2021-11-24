from typing import List
import requests

def query_solr(key: str, mx_depth: int, data_type: str, sites: List[str]):
    """
    Queries solr and returns query result
    """
    
    cluster = "save_cluster"
    sites_list = " or ".join(sites)

    query = ""
    sites_list = "url:(" + sites_list + ")"
    depth_query = "depth:[ * TO " + str(mx_depth) + " ]"
    data_type = "data_type:"+data_type

    payload = "fq=" + key + "&fq=" + sites_list + \
        "&fq=" + depth_query + "&fq=" + data_type

    print(sites_list)

    print(payload)
    url = "http://localhost:8983/solr/{cluster}/select?{payload}&indent=false&q.op=OR&q=*%3A*"

    response = requests.get(url)

    return response.json()


print(query_solr("hello", 5, "text", ["goose.com", "gdd.com", "jd.com"]))
