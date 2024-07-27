import re 
import requests 
from bs4 import BeautifulSoup

def validate_doi(doi_url, errormsg):
    try:
        response = requests.get(doi_url)
        response.raise_for_status()
        if response.status_code != 200:
            errormsg.append(f'{doi_url} is not validated. Please use real DOI id.')
    except requests.exceptions.HTTPError as errh:
        errormsg.append(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        errormsg.append(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        errormsg.append(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        errormsg.append(f"An unexpected error occurred: {err}")

    return errormsg 

