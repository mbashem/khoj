from typing import List
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def query_solr(
        key: str,
        mx_depth: int,
        data_type: str,
        sites: List[str],
        start: int = 0,
        row: int = 10):
    """
    Queries solr and returns query result
    """

    solr_url = os.getenv("SOLR_URL")
    sites_list = " or ".join(sites)

    sites_list = "url:(" + sites_list + ")"
    depth_query = "depth:[ * TO " + str(mx_depth) + " ]"
    data_type = "data_type:"+data_type

    payload = f"q=text:{key}~&fq={sites_list}&fq={depth_query}&fq={data_type}"

    url = f"{solr_url}/select?{payload}&indent=false&q.op=OR&q=*%3A*&start={start}&row={row}"

    response = requests.get(url)
    error = ""

    response = response.json()

    if(response["responseHeader"]["status"] >= 400):
        error = "Error 404"
        response = []
    else:
        response = response["response"]["docs"]

    return (response, error)


#print(query_solr("hello", 5, "text", ["www.gose.com", "gdd.com", "jd.com"]))

