from bs4 import BeautifulSoup
import requests
import re 

def creator_valid(cv_creator,errormsg): 
    if cv_creator != 'Yes' and cv_creator != 'No':
        errormsg.append('There is no CV for Creator section of sheet')
    return errormsg 

def contributorType_valid(cv_conTypy, errormsg):
    cv_values = ['ProjectLeader', 'ResearchGroup', 'ContactPerson', 'DataCollector', 'DataCurator', 'ProjectManager', 'ProjectMember', 'RelatedPerson', 'Researcher', 'ResearchGroup', 'Other']
    saved_con = False
    for cv in cv_values: 
        if cv_conTypy == cv:
            saved_con = True 
    if saved_con == False: 
        errormsg.append('CV value for contributor Type is incorrect please fix.')
    return errormsg

def nameType_valid(cv_nameType, errormsg): 
    if cv_nameType != 'Organizational' and cv_nameType != 'Personal':
        errormsg.append('CV is incorrect please specify if Personal or Organizational')
    return errormsg 

def personal_valid(name, errormsg): 
    pattern_for_name = re.compile(r'^[a-zA-Z]+, [a-zA-Z]+$')
    status = bool(pattern_for_name.match(name))
    if status == False:
        errormsg.append("Warning last name and first name are incorrect. Correct: (Last, First)")
    return errormsg 

def organizational_valid(organization, errormsg):
    pattern_for_organ = re.compile(r'^[a-zA-Z][a-zA-Z\d]*((?<=[a-z])[A-Z][a-zA-Z\d]*)*$')
    status = bool(pattern_for_organ.match(organization))
    if status == False: 
        errormsg.append(f'{organization} is listed incorrectly. Correct: camelCaseNotation')
    return errormsg

def nameIdentification_valid(cv_nameiden , errormsg):
    cv_values_nameiden = ['ORCID', 'ISNI', 'ROR', 'GRID', 'RRID']  
    saved_nameiden = False   
    for cv in cv_values_nameiden:
        if cv_nameiden == cv: 
            saved_nameiden = True 
    if saved_nameiden == False:
        errormsg.append('CV value for name indentifier scheme is incorrect. Please verify cell information')
    return errormsg

def affiliationIdentity_valid(cv_affiden, errormsg):
    cv_values_affiden = ['ORCID', 'ISNI', 'ROR', 'GRID', 'RRID']
    saved_affiden = False   
    for cv in cv_values_affiden:
        if cv_affiden == cv: 
            saved_affiden = True 
    if saved_affiden == False:
        errormsg.append('CV value for Affiliation indentifier scheme is incorrect. Please verify cell information')
    return errormsg 
    
def validate_orcid(org_url, errormsg):
    org_pattern = r'^https:\/\/orcid\.org\/[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]$'  
    org_regex = re.compile(org_pattern)
    if not org_regex.match(org_url):
        errormsg.append('ORCID url is formatted incorrectly. Please Fix and Resubmit.')
    #check connectivity to orcid
    orcid_id = org_url.strip('https://orcid.org/')
    url = f'https://pub.orcid.org/v3.0/{orcid_id}'
    headers = {
        "Accept": "application/json"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for errors

        data = response.json()
        if "orcid-identifier" not in data:
            errormsg.append('Cannot pull data from ORCID page. Please resubmit correct ORCID ID.')
    except requests.exceptions.HTTPError as errh:
        errormsg.append(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        errormsg.append(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        errormsg.append(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        errormsg.append(f"An unexpected error occurred: {err}")

    return errormsg

def validate_ror(ror_url, errormsg):
    ror_pattern = r'^https:\/\/ror\.org\/[a-zA-Z0-9\-]+$'  
    ror_regex = re.compile(ror_pattern)
    if not ror_regex.match(ror_url):
        errormsg.append('ROR url is formatted incorrectly. Please Fix and Resubmit.')
    
    
    ror_id = ror_url.strip('https://ror.org/')
    url = f"https://api.ror.org/organizations/{ror_id}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for errors

        data = response.json()
        if 'id' not in data and data['id'] != ror_url:
            errormsg.append("ID mismatch in response")
    except requests.exceptions.HTTPError as errh:
        errormsg.append(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        errormsg.append(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        errormsg.append(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        errormsg.append(f"An unexpected error occurred: {err}")
    return errormsg

def validate_isni(isni_url, errormsg):
    isni_pattern = r'^https:\/\/isni\.org\/isni\/[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]$'  
    isni_regex = re.compile(isni_pattern)
    if not isni_regex.match(isni_url):
        errormsg.append('ISNI url is formatted incorrectly. Please Fix and Resubmit.')
    else:
        print('ISNI url formatted correctly.')
    #check connectivity to orcid
    
    isni_id = isni_url.strip('https://isni.org/isni/')
    url = f'https://isni.oclc.org/cbs/DB=1.2/SET=1/TTL=1/CMD?ACT=SRCH&IKT=8006&SRT=LST_nd&TRM={isni_id}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for errors
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            isni = soup.find('span', class_='highlight' ).string
            if isni_id == isni:
                print(f'{isni} matches connection is successful')
            else:
                print(f'{isni} does not match {isni_id}. Please resubmit correct id.')
    except requests.exceptions.HTTPError as errh:
        errormsg.append(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        errormsg.append(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        errormsg.append(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        errormsg.append(f"An unexpected error occurred: {err}")
    

    return errormsg

def validate_grid(grid_url, errormsg):
    headers = {
        "Accept": "application/json"
    }
    grid_pattern = r'^https:\/\/www\.grid\.ac\/[a-zA-Z0-9\-]+$'  
    grid_regex = re.compile(grid_pattern)
    if not grid_regex.match(grid_url):
        errormsg.append('GRID url is formatted incorrectly. Please Fix and Resubmit.')
    else:
        print('GRID url formatted correctly.')
    #check connectivity to orcid
    
    connection = requests.get(grid_url, headers=headers)
    if connection.status_code == 404: 
        print(connection.status_code)
        errormsg.append("There is no connection to GRID. Please change URL id.")
    return errormsg



    