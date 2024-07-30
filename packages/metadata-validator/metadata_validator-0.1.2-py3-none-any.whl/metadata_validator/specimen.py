import requests
import re
from bs4 import BeautifulSoup

def check_taxonomy_name(taxonomy_id, species, errormsg):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    summary_url = f"{base_url}esummary.fcgi"
    
    # Get summary information for the taxonomy ID
    summary_params = {
        'db': 'taxonomy',
        'id': taxonomy_id,
        'retmode': 'json'
    }
    summary_response = requests.get(summary_url, params=summary_params)
    summary_data = summary_response.json()
    
    # Extract and return the common name if available
    if 'result' in summary_data and str(taxonomy_id) in summary_data['result']:
        taxonomy_info = summary_data['result'][str(taxonomy_id)]
        if 'commonname' in taxonomy_info:
            commonName = taxonomy_info['commonname']
            if species not in commonName:
                errormsg.append(f'{species} is not apart of {commonName} which is the common name for the species through NCIB.')
    return errormsg

def all_lowercase(ncid, errormsg):
    pattern_for_ncid = re.compile(r'^[a-z]+$')
    if not pattern_for_ncid.match(ncid):
        errormsg.append(f'{ncid} is not lowercase. Please resubmit')
    return errormsg
def is_a_string(string, errormsg):
    if not isinstance(string, str):
        errormsg.append(f'{string} is not a string. Please resubmit a string.')
    return errormsg