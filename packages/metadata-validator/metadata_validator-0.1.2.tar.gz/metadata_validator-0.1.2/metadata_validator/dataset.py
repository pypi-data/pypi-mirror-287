import re 
import requests 
from bs4 import BeautifulSoup 

def validate_rights(rights, errormsg):
    pattern = r'\s*\([^)]*\)$'
    rights = re.sub(pattern, '', rights)
    license_url = 'https://spdx.org/licenses/'
    response = requests.get(license_url)
    status = False
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', class_='sortable' )
        for row in table.find_all('tr'):
            cells = row.find_all('td')
            if cells and rights in cells[0].text:
                status = True
    if status == False:
        errormsg.append(f'{rights} was not found within the listed licenses. Please submit a valid license.')
    return errormsg