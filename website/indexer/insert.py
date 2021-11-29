import json
import os
from dotenv import load_dotenv
import requests

load_dotenv()

solr_url = os.getenv("SOLR_URL")


def insert_into_solr_text(text: str, depth: int, url: str, page_url: str, data_type: str):
    """
    Inserts into solr
    Return: true if succesfull false otherwise
    """
    send_url = f"{solr_url}/update/json/docs"

    payload = {"text": text, "depth": depth, "url": url,
               "page_url": page_url, "data_type": data_type}
    
    response = requests.post(send_url, json=payload)

    response = response.json()
    
    if (response["responseHeader"]["status"] >= 400):
        return False
    return True

# def insert_into_solr_json(json_file: str):
#     """
#     For future work
#     """
#     send_url = f"{solr_url}/update"

#     response = requests.post(send_url, json=json_file)

#     response = response.json()
    
#     print(json_file)
    
#     print(response)
    
#     if (response["responseHeader"]["status"] >= 400):
#         return False
#     return True

#insert_into_solr_text(text = "this is a text", depth= 2, url = "this is a url", page_url = 'This is a page url', data_type = 'non html')
