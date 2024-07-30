import requests 
from bs4 import BeautifulSoup
import re

def organizational_valid(organization, errormsg):
    pattern_for_organ = re.compile(r'^[a-zA-Z][a-zA-Z\d]*((?<=[a-z])[A-Z][a-zA-Z\d]*)*$')
    status = bool(pattern_for_organ.match(organization))
    if status == False: 
        errormsg.append(f'{organization} is listed incorrectly. Correct: camelCaseNotation')
    return errormsg

def is_string(award_desc, errormsg, nih_value): 
    status = isinstance(award_desc, str)
    if status == False:
        errormsg.append("The values within award title are incorrect. Make sure this is a string of characters.")
    parts = nih_value.split('-')
# Join the first parts with spaces and keep the last part with a hyphen
    formatted_id = ("".join(parts[:-1]) + '-' + parts[-1]).strip()
    base_url = "https://api.reporter.nih.gov/v2/projects/search"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "criteria": {
            "project_nums":[formatted_id],
            "advanced_text_search": {   "operator": "and", 
                                        "search_field": "projecttitle,terms", 
                                        "search_text": str({award_desc})
                                    } 
                    }     
    }
    try:
        response = requests.post(base_url, json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()            
            if 'results' in data and len(data['results']) > 0:
                project_title = str(data['results'][0].get('project_title'))
                if project_title != award_desc:
                    errormsg.append(f'{project_title} and {award_desc} do not match. Please enter correct award title.')
            else:
                errormsg.append("No results found in the API response for NIH award number.")
        else:
            response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        errormsg.append(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        errormsg.append(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        errormsg.append(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        errormsg.append(f"An unexpected error occurred: {err}")

def affiliationIdentity_valid(cv_affiden, errormsg):
    cv_values_affiden = ['ORCID', 'ISNI', 'ROR', 'GRID', 'RRID']
    saved_affiden = False   
    for cv in cv_values_affiden:
        if cv_affiden == cv: 
            saved_affiden = True 
    if saved_affiden == False:
        errormsg.append('CV value for Affiliation indentifier scheme is incorrect. Please verify cell information')
    return errormsg 
    
def validate_nih(nih_value, errormsg):
    nih_pattern =r'^[A-Z0-9]+-\d{2}$'
    parts = nih_value.split('-')
    formatted_id = ("".join(parts[:-1]) + '-' + parts[-1]).strip()
    if not re.match( nih_pattern ,formatted_id):
        errormsg.append("The NIH award number is incorrect. Please fix and resubmit.")   

    return errormsg  
