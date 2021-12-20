from typing import List
import typing
import requests
import os
from dotenv import load_dotenv

from indexer.IndexResult import IndexResult

load_dotenv()


def query_solr(
        key: str,
        mx_depth: int,
        strategy: List[str],
        sites: List[str],
        start: int = 0,
        row: int = 10) -> typing.Tuple[List[IndexResult], str]:
    """
    Queries solr and returns query result
    """

    solr_url = os.getenv("SOLR_URL")

    newsite = []
    
    for site in sites:
        site = "\"" + site + "\""
        newsite.append(site)
        
    newstrategy = []
    
    for stra in strategy:
        stra = "\"" + stra + "\""
        newstrategy.append(stra)


    sites_list = "url:(" + " or " .join(newsite) + ")"
    depth_query = "depth:[ * TO " + str(mx_depth) + " ]"
    strategy_list = "data_type:(" + " or ".join(newstrategy) + ")"

    payload = f"q=text:{key}~&fq={sites_list}&fq={depth_query}&fq={strategy_list}"

    url = f"{solr_url}/select?{payload}&indent=false&q.op=OR&q=*%3A*&start={start}&row={row}"

    response = requests.get(url)
    error = ""

    print(url)

    response = response.json()

    if(response["responseHeader"]["status"] >= 400):
        error = "Error 404"
        response = []
    else:
        response = response["response"]["docs"]

    response_typed = []

    for res in response:
        response_typed.append(IndexResult(
            res["text"][0], res["depth"][0], res["url"][0], res["page_url"][0], res["data_type"][0]))

    response_set = set(response_typed)

    response_typed = list(response_set)

    return (response_typed, error)


# res = query_solr("antontrygubO_o", 2, ["nonhtml"], ["https://codeforces.com/blog/entry/97956"])
# for r in res[0]:
#     print(r.text + " " + r.url + " " + str(r.depth) + " " + r.data_type)
# print(res)
