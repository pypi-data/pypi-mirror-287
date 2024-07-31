import os 
import re
from .functions import is_valid_cell
from .contributors import validate_ror, validate_orcid, validate_grid, validate_isni, contributorType_valid, personal_valid, nameIdentification_valid, nameType_valid, creator_valid
from .funders import is_string, organizational_valid, affiliationIdentity_valid, validate_nih
from .publication import validate_doi
from .dataset import validate_rights
from .specimen import all_lowercase, is_a_string, check_taxonomy_name
import pandas as pd
import warnings

def descriptive_metadata_upload(file_path, ingest_method):
    """ Upload a spreadsheet containing image metadata information. """
    if os.path.exists(file_path):     
        version1 = metadata_version_check(file_path)
            # using new metadata model
        if version1 == False:
            errormsg = check_all_sheets(file_path, ingest_method)
            if errormsg != []:
                print( errormsg)
                               
def metadata_version_check(filename):
    warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")
    version1 = False
    df = pd.ExcelFile(filename)

    try:
        if 'README' in df.sheet_names:
            version1 = False
    except:
        version1 = True
    return version1 

def check_all_sheets(filename, ingest_method):
    ingest_method = ingest_method
    errormsg = check_contributors_sheet(filename)
    if errormsg != []:
        print('Contributor sheet error(s):')
        for e in errormsg:
            print(f'{e}\n')
        errormsg = []
    else: 
        print('Contributer sheet has been checked.')
    errormsg = check_funders_sheet(filename)
    if errormsg != []:
        print('Funder sheet error(s):')
        for e in errormsg:
            print(f'{e}\n')
        errormsg = []
    else: 
        print('Funders sheet has been checked.')
    errormsg = check_publication_sheet(filename)
    if errormsg != []:
        print('Publication sheet error(s):')
        for e in errormsg:
            print(f'{e}\n')
        errormsg = []
    else: 
        print('Publication sheet has been checked.')
    errormsg = check_instrument_sheet(filename)
    if errormsg != []:
        print('Instrument sheet error(s):')
        for e in errormsg:
            print(f'{e}\n')
        errormsg = []
    else: 
        print('Instrument sheet has been checked.')
    errormsg = check_dataset_sheet(filename)
    if errormsg != []:
        print('Dataset sheet error(s):')
        for e in errormsg:
            print(f'{e}\n')
        errormsg = []
    else: 
        print('Dataset sheet has been checked.')

    errormsg = check_specimen_sheet(filename)
    if errormsg != []:
        print('Specimen sheet error(s):')
        for e in errormsg:
            print(f'{e}\n')
        errormsg = []
    else: 
        print('Specimen sheet has been checked.')
    if ingest_method != 'ingest_5':
        errormsg = check_image_sheet(filename)
        if errormsg != []:
            print('Image sheet error(s):')
            for e in errormsg:
                print(f'{e}\n')
            errormsg = []
        else: 
            print('Image sheet has been checked.')
    if ingest_method == 'ingest_5':
        errormsg = check_swc_sheet(filename)
        if errormsg != []:
            print('SWC sheet error(s):')
            for e in errormsg:
                print(f'{e}\n')
            errormsg = []
        else: 
            print('SWC sheet has been checked.')
    return errormsg

def check_contributors_sheet(filename):
    errormsg = []
    sheetname = 'Contributors'
    column_num = []
    contributors_sheet = pd.read_excel(filename, sheet_name=sheetname)
    total_col = (contributors_sheet.columns.get_loc(contributors_sheet.columns[-1]))
    for i in range(0, total_col + 1):
        column_num.append(i)
    contributors_sheet.columns = column_num
    contributors_sheet = contributors_sheet.where(pd.notna(contributors_sheet), None)
    #ASCII only in sheet
    for row in contributors_sheet.iterrows():
        for cell in row:
            if isinstance(cell, str):
                if not is_valid_cell(cell):
                    print(f"Non-ASCII characters found in: '{cell}'")

    colheads=['contributorName','Creator','contributorType',
                 'nameType','nameIdentifier','nameIdentifierScheme',
                 'affiliation', 'affiliationIdentifier', 'affiliationIdentifierScheme']
    creator = ['Yes', 'No']
    contributortype = ['ProjectLeader','ResearchGroup','ContactPerson', 'DataCollector', 'DataCurator', 'ProjectLeader', 'ProjectManager', 'ProjectMember','RelatedPerson', 'Researcher', 'ResearchGroup','Other' ]
    nametype = ['Personal', 'Organizational']
    nameidentifierscheme = ['ORCID','ISNI','ROR','GRID','RRID' ]
    affiliationidentifierscheme = ['ORCID','ISNI','ROR','GRID','RRID' ]
    cellcols=['A','B','C','D','E','F','G','H','I']
    cols=[cell for cell in contributors_sheet.iloc[1]]
    for i in range(0,len(colheads)):
        if cols[i] != colheads[i]:
            errormsg.append(' Tab: "Contributors" cell heading found: "' + cols[i] + \
                       '" but expected: "' + colheads[i] + '" at cell: "' + cellcols[i] + '3". ')
    if errormsg != []:
        return [ True, errormsg ]
    last_row = contributors_sheet.index[-1]
    for i in range(5, (last_row + 1)):
        cols=[cell for cell in contributors_sheet.iloc[i]]
        if cols[0] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[0] + '" value expected but not found in cell: "' + cellcols[0] + str(i+1) + '". ')
        if cols[1] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[1] + '" value expected but not found in cell: "' + cellcols[1] + str(i+1) + '". ')
        if cols[1] not in creator:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[1] + '" incorrect CV value found: "' + cols[1] + '" in cell "' + cellcols[1] + str(i+1) + '". ')
        if cols[2] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[2] + '" value expected but not found in cell "' + cellcols[2] + str(i+1) + '". ')
        if cols[2] not in contributortype:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[2] + '" incorrect CV value found: "' + cols[2] + '" in cell "' + cellcols[2] + str(i+1) + '". ')
        if cols[3] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[3] + '" value expected but not found in cell "' + cellcols[3] + str(i+1) + '". ')
        if cols[3] not in nametype:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[3] + '" incorrect CV value found: "' + cols[3] + '" in cell "' + cellcols[3] + str(i+1) + '". ')
                   
        if cols[4] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[4] + '" value expected but not found in cell "' + cellcols[4] + str(i+1) + '". ')
        if cols[5] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[5] + '" value expected but not found in cell "' + cellcols[5] + str(i+1) + '". ')
        if cols[5] not in nameidentifierscheme:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[5] + '" incorrect CV value found: "' + cols[5] + '" in cell "' + cellcols[5] + str(i+1) + '". ')
        #else:
            #check nameIdentifier and nameIdentifierScheme ensure they are empty
        if cols[6] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[6] + '" value expected but not found in cell "' + cellcols[6] + str(i+1) + '". ')
        if cols[7] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[7] + '" value expected but not found in cell "' + cellcols[7] + str(i+1) + '". ')
        if cols[8] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[8] + '" value expected but not found in cell "' + cellcols[8] + str(i+1) + '". ')
        if cols[8] not in affiliationidentifierscheme:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[8] + '" Incorrect CV value found: "' + cols[8] + '" in cell "' + cellcols[8] + str(i+1) + '". ')
    columns = []
    rows_2 = []
    total_row = (contributors_sheet.index[-1])
    for i in range(0, (total_col + 1)):  
        columns.append(i)
    for i in range(5, (total_row + 1)):  
        rows_2.append(i)
    for col in columns:
        for row in rows_2:
            cell_value = contributors_sheet.iat[row, col]
        
            if col == 1:
                if cell_value is not None:
                    cv_creator = str(cell_value)
                    creator_valid(cv_creator, errormsg)
                elif row == rows_2[0]:
                    errormsg.append('Creator is empty. Please resubmit with information.')

            elif col == 2:
                if cell_value is not None:
                    cv_conTypy = str(cell_value)
                    contributorType_valid(cv_conTypy, errormsg)
                elif row == rows_2[0]:
                    errormsg.append('Contributor type is empty. Please resubmit with information.')

            elif col == 3:
                if cell_value is not None:
                    cv_nameType = str(cell_value)
                    nameType_valid(cv_nameType, errormsg)
                    if cv_nameType == nametype[0]:
                        col_2 = col - 3
                        name = contributors_sheet.iat[row, col_2]
                        personal_valid(name, errormsg)
                    if cv_nameType == nametype[1]:
                        col_2 = col - 3
                        organization = contributors_sheet.iat[row, col_2]
                        organizational_valid(organization, errormsg)
                elif row == rows_2[0]:
                    errormsg.append('Name Type is empty. Please resubmit with information.')

            elif col == 4:
                if cell_value is not None:
                    col2 = col + 1
                    cell_value_col2 = contributors_sheet.iat[row, col2]
                    if cell_value_col2 is not None:
                        cv_nameiden = str(cell_value_col2)
                        nameIdentification_valid(cv_nameiden, errormsg)
                        cv_values_nameiden = ['ORCID', 'ISNI', 'ROR', 'GRID', 'RRID']
                        if cv_nameiden == cv_values_nameiden[0]:
                            org_url = str(cell_value).strip()
                            validate_orcid(org_url, errormsg)
                        elif cv_nameiden == cv_values_nameiden[2]:
                            ror_url = str(cell_value).strip()
                            validate_ror(ror_url, errormsg)
                        elif cv_nameiden == cv_values_nameiden[1]:
                            isni_url = str(cell_value).strip()
                            validate_isni(isni_url, errormsg)
                        elif cv_nameiden == cv_values_nameiden[3]:
                            grid_url = str(cell_value).strip()
                            validate_grid(grid_url, errormsg)
                    elif row == rows_2[0]:
                        errormsg.append('Url for Name Identifier is empty. Please resubmit with information.')
                elif row == rows_2[0]:
                    errormsg.append('Name Identifier is empty. Please resubmit with information.')

            elif col == 6:
                if cell_value is not None:
                    col2 = col + 1
                    col3 = col + 2
                    cell_value_col2 = contributors_sheet.iat[row, col2]
                    cell_value_col3 = contributors_sheet.iat[row, col3]
                    if cell_value_col3 is not None and cell_value_col2 is not None:
                        cv_aff = str(cell_value)
                        organizational_valid(cv_aff, errormsg)
                        cv_values_affiden = ['ORCID', 'ISNI', 'ROR', 'GRID', 'RRID']
                        cv_affiden = str(cell_value_col3).strip()
                        affiliationIdentity_valid(cv_affiden, errormsg)
                        if cv_affiden == cv_values_affiden[0]:
                            org_url = str(cell_value_col2).strip()
                            validate_orcid(org_url, errormsg)
                        elif cv_affiden == cv_values_affiden[2]:
                            ror_url = str(cell_value_col2).strip()
                            validate_ror(ror_url, errormsg)
                        elif cv_affiden == cv_values_affiden[1]:
                            isni_url = str(cell_value_col2).strip()
                            validate_isni(isni_url, errormsg)
                        elif cv_affiden == cv_values_affiden[3]:
                            grid_url = str(cell_value_col2).strip()
                            validate_grid(grid_url, errormsg)
                    elif row == rows_2[0]:
                        errormsg.append('Url for Affiliation Identifier is empty. Please resubmit with information.')
                elif row == rows_2[0]:
                    errormsg.append('Affiliation Identifier is empty. Please resubmit with information.')

    return errormsg

def check_funders_sheet(filename):
    errormsg= []
    column_num = []
    sheetname = 'Funders'
    funders_sheet = pd.read_excel(filename, sheet_name=sheetname)
    total_col = (funders_sheet.columns.get_loc(funders_sheet.columns[-1]))
    for i in range(0, total_col + 1):
        column_num.append(i)
    funders_sheet.columns = column_num
    funders_sheet = funders_sheet.where(pd.notna(funders_sheet), None)
    #ASCII only in sheet
    for row in funders_sheet.iterrows():
        for cell in row:
            if isinstance(cell, str):
                if not is_valid_cell(cell):
                    print(f"Non-ASCII characters found in: '{cell}'")
    colheads=['funderName','fundingReferenceIdentifier','fundingReferenceIdentifierType',
                 'awardNumber','awardTitle']
    fundingReferenceIdentifierType = ['ROR', 'GRID', 'ORCID', 'ISNI']
    cellcols=['A','B','C','D','E']
    cols=[cell for cell in funders_sheet.iloc[2]]
    for i in range(0,len(colheads)):
        if cols[i] != colheads[i]:
            errormsg.append( ' Tab: "Funders" cell heading found: "' + cols[i] + \
                       '" but expected: "' + colheads[i] + '" at cell: "' + cellcols[i] + '3". ')
    if errormsg != []:
        return [ True, errormsg ]
    last_row = funders_sheet.index[-1]
    for i in range(5,(last_row + 1)):
        cols=[cell for cell in funders_sheet.iloc[i]]
        if cols[0] == None:
            errormsg.append( 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[0] + '" value expected but not found in cell: "' + cellcols[0] + str(i+1) + '". ')
        
        if cols[1] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[1] + '" value expected but not found in cell: "' + cellcols[1] + str(i+1) + '". ')
        if cols[2] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[2] + '" value expected but not found in cell "' + cellcols[2] + str(i+1) + '". ')
        if cols[2] not in fundingReferenceIdentifierType:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[2] + '" incorrect CV value found: "' + cols[2] + '" in cell "' + cellcols[2] + str(i+1) + '". ')
        if cols[3] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[3] + '" value expected but not found in cell "' + cellcols[3] + str(i+1) + '". ')
        if cols[4] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[4] + '" value expected but not found in cell "' + cellcols[4] + str(i+1) + '". ')
    columns = []
    rows_2 = []
    total_row = (funders_sheet.index[-1])
    for i in range(0, (total_col + 1)):  
        columns.append(i)
    for i in range(5, (total_row + 1)):  
        rows_2.append(i)
    for col in columns:
        for row in rows_2:
            cell_value = funders_sheet.iat[row, col]
            if col == 0:
                if cell_value is not None:
                    name_funders = cell_value
                    organizational_valid(name_funders, errormsg)  
                elif rows_2[0] == row:
                    errormsg.append('Name of Funder is empty. Please resubmit with information.')
            if col == 1:
                if cell_value is not None:
                    col2 = col + 1
                    cv_values_funders = ['ORCID', 'ISNI', 'ROR', 'GRID']
                    cell_value2 = funders_sheet.iat[row, col2]
                    if cell_value2 is not None:
                        cv_funders = str(cell_value2) 
                        affiliationIdentity_valid(cv_funders, errormsg)
                        if cv_funders == cv_values_funders[0]:
                            org_url = str(cell_value.strip())
                            validate_orcid(org_url, errormsg)
                        if cv_funders == cv_values_funders[2]:
                            ror_url = str(cell_value.strip())
                            validate_ror(ror_url, errormsg)
                        if cv_funders == cv_values_funders[1]:
                            isni_url = str(cell_value.strip())
                            validate_isni(isni_url, errormsg)
                        if cv_funders == cv_values_funders[3]:
                            grid_url = str(cell_value.strip())
                            validate_grid(grid_url, errormsg)
                    elif rows_2[0] == row:
                        errormsg.append('Funding Reference Identifier is empty. Please resubmit with information.')
                elif rows_2[0] == row:
                    errormsg.append('There is no url for Funding Reference is empty. Please resubmit with information.')
            if col == 3:
                if cell_value is not None:
                    nih_value = str(cell_value)
                    validate_nih(nih_value, errormsg)
                elif rows_2[0] == row:
                    errormsg.append('NIH value is empty. Please resubmit with information.')
            if col == 4:
                if cell_value is not None:
                    award_desc = cell_value
                    is_string(award_desc, errormsg, nih_value)
                elif rows_2[0] == row:
                    errormsg.append('Award description is empty. Please resubmit with information.')
    return errormsg

def check_publication_sheet(filename):
    errormsg=[]
    column_num = []
    sheetname = 'Publication'
    publication_sheet = pd.read_excel(filename, sheet_name=sheetname)
    total_col = (publication_sheet.columns.get_loc(publication_sheet.columns[-1]))
    for i in range(0, total_col + 1):
        column_num.append(i)
    publication_sheet.columns = column_num
    publication_sheet = publication_sheet.where(pd.notna(publication_sheet), None)
    for row in publication_sheet.iterrows():
        for cell in row:
            if isinstance(cell, str):
                if not is_valid_cell(cell):
                    print(f"Non-ASCII characters found in: '{cell}'")
    colheads=['relatedIdentifier','relatedIdentifierType','PMCID',
                 'relationType','citation']
    relatedIdentifierType = ['arcXiv', 'DOI', 'PMID', 'ISBN']
    relationType = ['IsCitedBy', 'IsDocumentedBy']
    cellcols=['A','B','C','D','E']
    cols=[cell for cell in publication_sheet.iloc[2]]
    for i in range(0,len(colheads)):
        if cols[i] != colheads[i]:
            errormsg = errormsg + ' Tab: "Publication" cell heading found: "' + cols[i] + \
                       '" but expected: "' + colheads[i] + '" at cell: "' + cellcols[i] + '3". '
    if errormsg != []:
        return [ True, errormsg ]
    # if 1 field is filled out the rest should be other than PMCID
    total_row = (publication_sheet.index[-1])
    for i in range(5,(total_row +1)):
        cols=[cell for cell in publication_sheet.iloc[i]]
        #if cols[0] == "":
        #     errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[0] + '" value expected but not found in cell: "' + cellcols[0] + str(i+1) + '". '
        #if cols[1] == "":
        #     errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[1] + '" value expected but not found in cell: "' + cellcols[1] + str(i+1) + '". '
        if cols[1] != None:
            if cols[1] not in relatedIdentifierType:
                errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[1] + '" incorrect CV value found: "' + cols[1] + '" in cell "' + cellcols[1] + str(i+1) + '". ')
        #if cols[2] == "":
            #errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[2] + '" value expected but not found in cell "' + cellcols[2] + str(i+1) + '". '
        #if cols[3] == "":
             #errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[3] + '" value expected but not found in cell "' + cellcols[3] + str(i+1) + '". '
        if cols[3] != None:
            if cols[3] not in relationType:
                errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[3] + '" incorrect CV value found: "' + cols[3] + '" in cell "' + cellcols[3] + str(i+1) + '". ')
        #if cols[4] == "":
           #errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[4] + '" value expected but not found in cell "' + cellcols[4] + str(i+1) + '". '
    columns = []
    rows_2 = []
    for i in range(0, total_col+1):
        columns.append(i)
    for i in range(5, total_row+1):
        rows_2.append(i)
    for col in columns:
        for row in rows_2:
            cell_value = publication_sheet.iat[row, col]
            if col == 0:
                if cell_value is not None:
                    col_2 = col + 1 
                    cell_value2 = publication_sheet.iat[row, col_2]
                    if cell_value2 is not None:
                        related_ident_type = str(cell_value2)
                        related_ident = ['arXiv', 'DOI', 'PMID', 'ISBN']
                        status_ident = False 
                        for cv in related_ident:
                            if cv == related_ident_type:
                                status_ident = True
                            if cv == 'DOI' and related_ident_type == 'DOI':
                                doi_url = str(cell_value)
                                validate_doi(doi_url, errormsg)
                        if status_ident == False: 
                            errormsg.append(f'{related_ident_type} is not within the list of acceptable values. {related_ident} are the allowed ways.')
                    elif rows_2[0] == row:
                        errormsg.append('Related Identifier is empty. Please resubmit with information.')
                elif rows_2[0] == row:
                    errormsg.append('Warning: DOI url is empty. Please resubmit with information if selection type is DOI. Ignore if else.')
            if col == 2:
                if cell_value is not None:
                    pmcid = cell_value
                    if not isinstance(pmcid, str) and pmcid != '':
                        errormsg.append(f'{pmcid} is not a integer value. Please fix and resubmit')
                elif rows_2[0] == row:
                    errormsg.append('Warning: PMCID is empty. If applicable, please submit PMCID number.')
            if col == 3:
                if cell_value is not None:
                    relationship = str(cell_value)
                    relationship_type = ['IsCitedBy', 'IsDocumentedBy']
                    statusrelation = False
                    for cv in relationship_type:
                        if relationship == cv: 
                            statusrelation = True 
                    if statusrelation == False:
                        errormsg.append(f'{relationship} is not within the list of acceptable values. {relationship_type} are the allowed ways.')
                elif rows_2[0] == row:
                    errormsg.append('Relationship is empty. Please resubmit with information')
            if col == 4:
                if cell_value is not None:
                    citation = cell_value 
                    if not isinstance(citation, str):
                        errormsg.append(f'{citation} is not a string for open text. Please resubmit with a string of open text.')
                elif rows_2[0] == row:
                    errormsg.append('Citation is empty. Please resubmit with information')
    return errormsg

def check_instrument_sheet(filename):
    instrument_count = 0
    errormsg=[]
    column_num= []
    sheetname = 'Instrument'
    instrument_sheet = pd.read_excel(filename, sheet_name=sheetname)
    total_col = (instrument_sheet.columns.get_loc(instrument_sheet.columns[-1]))
    for i in range(0, total_col + 1):
        column_num.append(i)
    instrument_sheet.columns = column_num
    instrument_sheet = instrument_sheet.where(pd.notna(instrument_sheet), None)
    for row in instrument_sheet.iterrows():
        for cell in row:
            if isinstance(cell, str):
                if not is_valid_cell(cell):
                    print(f"Non-ASCII characters found in: '{cell}'")
    colheads=['MicroscopeType','MicroscopeManufacturerAndModel','ObjectiveName',
                 'ObjectiveImmersion','ObjectiveNA', 'ObjectiveMagnification', 'DetectorType', 'DetectorModel', 'IlluminationTypes', 'IlluminationWavelength', 'DetectionWavelength', 'SampleTemperature']
    cellcols=['A','B','C','D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
    cols=[cell for cell in instrument_sheet.iloc[2]]
    for i in range(0,len(colheads)):
        if cols[i] != colheads[i]:
            errormsg = errormsg + ' Tab: "Instrument" cell heading found: "' + cols[i] + \
                       '" but expected: "' + colheads[i] + '" at cell: "' + cellcols[i] + '3". '
    if errormsg != []:
        return [ True, errormsg ]
    total_row = (instrument_sheet.index[-1])
    for i in range(5,(total_row + 1)):
        instrument_count = instrument_count + 1
        cols=[cell for cell in instrument_sheet.iloc[i]]
        if cols[0] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[0] + '" value expected but not found in cell: "' + cellcols[0] + str(i+1) + '". ')
        #if cols[1] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[1] + '" value expected but not found in cell: "' + cellcols[1] + str(i+1) + '". '
        #if cols[2] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[1] + '" value expected but not found in cell: "' + cellcols[1] + str(i+1) + '". '
        #if cols[3] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[3] + '" value expected but not found in cell "' + cellcols[3] + str(i+1) + '". '
        #if cols[4] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[4] + '" value expected but not found in cell "' + cellcols[4] + str(i+1) + '". '
        #if cols[5] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[5] + '" value expected but not found in cell "' + cellcols[5] + str(i+1) + '". '
        #if cols[6] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[6] + '" value expected but not found in cell "' + cellcols[6] + str(i+1) + '". '
        #if cols[7] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[7] + '" value expected but not found in cell "' + cellcols[7] + str(i+1) + '". '
        #if cols[8] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[8] + '" value expected but not found in cell "' + cellcols[8] + str(i+1) + '". '
        #if cols[9] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[9] + '" value expected but not found in cell "' + cellcols[9] + str(i+1) + '". '
        #if cols[10] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[10] + '" value expected but not found in cell "' + cellcols[10] + str(i+1) + '". '
        #if cols[11] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[11] + '" value expected but not found in cell "' + cellcols[11] + str(i+1) + '". '
    columns = []
    rows = []
    for i in range(0,total_col + 1):
        columns.append(i)
    for i in range(5, total_row + 1):
        rows.append(i)
    pattern_for_cell = re.compile(r'^[a-z0-9.,\s-]+$')
    for col in columns:
        for row in rows:
            cell_value = instrument_sheet.iat[row, col]
            if cell_value is not None:
                cell = str(cell_value)
                status = bool(pattern_for_cell.match(cell))
                if isinstance(cell,str):
                    if status == False and cell != '':
                        errormsg.append(f'{cell} is not all lowercase please fix and resubmit.')
                else:
                    errormsg.append(f'{cell} is not a string. Please resubmit a lowercase string.')
    return errormsg

def check_dataset_sheet(filename):
    dataset_count = 0
    errormsg=[]
    column_num = []
    sheetname = 'Dataset'
    dataset_sheet = pd.read_excel(filename, sheet_name=sheetname)
    total_col = (dataset_sheet.columns.get_loc(dataset_sheet.columns[-1]))
    for i in range(0, total_col + 1):
        column_num.append(i)
    dataset_sheet.columns = column_num
    dataset_sheet = dataset_sheet.where(pd.notna(dataset_sheet), None)
    for row in dataset_sheet.iterrows():
        for cell in row:
            if isinstance(cell, str):
                if not is_valid_cell(cell):
                    print(f"Non-ASCII characters found in: '{cell}'")
    colheads=['BILDirectory','title','socialMedia','subject',
                 'Subjectscheme','rights', 'rightsURI', 'rightsIdentifier', 'Image', 'GeneralModality', 'Technique', 'Other', 'Abstract', 'Methods', 'TechnicalInfo']
    GeneralModality = ['cell morphology', 'connectivity', 'population imaging', 'spatial transcriptomics', 'other', 'anatomy', 'histology imaging', 'multimodal']
    Technique = ['anterograde tracing', 'retrograde transynaptic tracing', 'TRIO tracing', 'smFISH', 'DARTFISH', 'MERFISH', 'Patch-seq', 'fMOST', 'other', 'cre-dependent anterograde tracing','enhancer virus labeling', 'FISH', 'MORF genetic sparse labeling', 'mouselight', 'neuron morphology reconstruction', 'Patch-seq', 'retrograde tracing', 'retrograde transsynaptic tracing', 'seqFISH', 'STPT', 'VISor', 'confocal microscopy']
    cellcols=['A','B','C','D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    cols=[cell for cell in dataset_sheet.iloc[2]]
    for i in range(0,len(colheads)):
        if cols[i] != colheads[i]:
            errormsg = errormsg + ' Tab: "Dataset" cell heading found: "' + cols[i] + \
                       '" but expected: "' + colheads[i] + '" at cell: "' + cellcols[i] + '3". '
    if errormsg != []:
        return [ True, errormsg ]
    total_row = (dataset_sheet.index[-1])
    for i in range(5,(total_row + 1)):
        dataset_count = dataset_count + 1
        cols=[cell for cell in dataset_sheet.iloc[i]]
        if cols[0] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[0] + '" value expected but not found in cell: "' + cellcols[0] + str(i+1) + '". ')
        if cols[1] == None:
            errormsg.append( 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[1] + '" value expected but not found in cell: "' + cellcols[1] + str(i+1) + '". ')
        #if cols[2] == "":
             #errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[1] + '" value expected but not found in cell: "' + cellcols[1] + str(i+1) + '". '
        #if cols[3] == "":
            #errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[3] + '" value expected but not found in cell "' + cellcols[3] + str(i+1) + '". '
        #if cols[4] == "":
            #errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[4] + '" value expected but not found in cell "' + cellcols[4] + str(i+1) + '". '
        if cols[5] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[5] + '" value expected but not found in cell "' + cellcols[5] + str(i+1) + '". ')
        if cols[6] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[6] + '" value expected but not found in cell "' + cellcols[6] + str(i+1) + '". ')
        if cols[7] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[7] + '" value expected but not found in cell "' + cellcols[7] + str(i+1) + '". ')
        #if cols[8] == "":
            #errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[8] + '" value expected but not found in cell "' + cellcols[8] + str(i+1) + '". '
        #if cols[9] == "":
            #errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[9] + '" value expected but not found in cell "' + cellcols[9] + str(i+1) + '". '
        if cols[9] != None:
            if cols[9] not in GeneralModality:
                errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[9] + '" incorrect CV value found: "' + cols[9] + '" in cell "' + cellcols[9] + str(i+1) + '". ')
        if cols[10] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[10] + '" value expected but not found in cell "' + cellcols[10] + str(i+1) + '". ')
        if cols[10] != None:
            if cols[10] not in Technique:
                errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[10] + '" incorrect CV value found: "' + cols[10] + '" in cell "' + cellcols[10] + str(i+1) + '". ')
        if cols[9] == "other" or cols[10] == "other":
            if cols[11] == None:
        #change to if GeneralModality and Technique = other
                errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[11] + '" value expected but not found in cell "' + cellcols[11] + str(i+1) + '". ')
        if cols[12] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[12] + '" value expected but not found in cell "' + cellcols[12] + str(i+1) + '". ')
        #if cols[13] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[13] + '" value expected but not found in cell "' + cellcols[13] + str(i+1) + '". '
        #if cols[14] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[14] + '" value expected but not found in cell "' + cellcols[14] + str(i+1) + '". '
    columns = []
    rows = []
    bil_start = '/bil/lz/'
    for i in range(0,total_col +1):
        columns.append(i)
    for i in range(5, total_row+1):
        rows.append(i)
    for col in columns:
        for row in rows:
            cell_value = dataset_sheet.iat[row, col]
            if col == 0:
                if cell_value is not None:
                    bil_direct = cell_value
                    status = bil_direct.startswith(bil_start)
                    if status == False:
                        errormsg.append(f'{bil_direct} needs to begin with {bil_start}. Please resubmit.')
                elif rows[0] == row:
                    errormsg.append('Bil directory is empty. Please resubmit')
            if col == 1:
                if cell_value is not None:
                    title = cell_value
                    if not isinstance(title, str) and title != '':
                        errormsg.append(f'{title} is not a sentence. Please resubmit a string.')
                elif rows[0] == row:
                    errormsg.append('Title is empty. Please resubmit')
            if col == 2:
                if cell_value is not None:
                    socialmedia = cell_value
                    if not isinstance(socialmedia, str) and socialmedia != '':
                        errormsg.append(f'{socialmedia} is not a string. Please resubmit a string.')
                elif rows[0] == row:
                    errormsg.append('Warning: Social Media is empty. Please resubmit if applicable with additional information.')
            if col == 3: 
                if cell_value is not None:
                    keywords = cell_value
                    if not isinstance(keywords, str) and keywords != '':
                        errormsg.append(f'{keywords} is not a string. Please resubmit a string.')
                elif rows[0] == row:
                    errormsg.append('Warning: Subject keyword section is empty. Please resubmit if applicable with additional information.')
            if col == 4:
                if cell_value is not None:
                    scheme = cell_value
                    if not isinstance(scheme, str) and scheme != '':
                        errormsg.append(f'{scheme} is not a string. Please resubmit a string.')
                elif rows[0] == row:
                    errormsg.append('Warning: Subject Scheme is empty. Please resubmit if applicable with additional information.')
            if col == 5: 
                if cell_value is not None:
                    rights = cell_value
                    validate_rights(rights, errormsg)
                elif rows[0] == row:
                    errormsg.append('Rights section is empty. Please resubmit')
            if col == 6:
                if cell_value is not None:
                    rights_url = cell_value 
                    remove = 'https://'
                    webaddress = rights_url.strip(remove)
                    if not isinstance(webaddress , str):
                        errormsg.append(f'{webaddress} is not a valid string. Please fix and resubmit.')
                elif rows[0] == row:
                    errormsg.append('Rights url is empty. Please resubmit')
            if col == 7:
                if cell_value is not None:
                    rights_ident = cell_value
                    if not isinstance(rights_ident, str):
                        errormsg.append(f'{rights_ident} is not a valid string. Please fix and resubmit.')
                elif rows[0] == row:
                    errormsg.append('Rights Identifier is empty. Please resubmit')
            if col == 8:
                if cell_value is not None:
                    image_url = cell_value 
                    image = image_url.strip(remove)
                    if not isinstance(image , str):
                        errormsg.append(f'{image} is not a valid string. Please fix and resubmit.')
                elif rows[0] == row:
                    errormsg.append('Warning: Image section is empty. Please resubmit if applicable with additional information. ')
            if col == 9:
                if cell_value is not None:
                    modality = cell_value
                    if modality not in GeneralModality:
                        errormsg.append(f'{modality} is not in the list of acceptable options. Please resubmit')
                elif rows[0] == row:
                    errormsg.append('Modality is empty. Please resubmit')
            if col == 10:
                if cell_value is not None:
                    tech = cell_value
                    if tech not in Technique:
                        errormsg.append(f'{tech} is not in the list of acceptable options. Please resubmit')
                elif rows[0] == row:
                    errormsg.append('Technique is empty. Please resubmit')
            if col == 11:
                if cell_value is not None:
                    other = cell_value
                    if not isinstance(other , str):
                        errormsg.append(f'{other} is not a valid string. Please fix and resubmit.')
                elif rows[0] == row:
                    errormsg.append('Other section is empty. Please resubmit')
            if col == 12:
                if cell_value is not None:
                    abstract = cell_value
                    abstract2 = rf'{abstract}'
                    if not isinstance(abstract2 , str):
                        errormsg.append(f'{abstract2} is not a valid string. Please fix and resubmit.')   
                elif rows[0] == row:
                    errormsg.append('Abstract is empty. Please resubmit')   
            if col == 13:
                if cell_value is not None:
                    methods = cell_value
                    methods2 = rf'{methods}'
                    if not isinstance(methods2 , str):
                        errormsg.append(f'{methods2} is not a valid string. Please fix and resubmit.')
                elif rows[0] == row:
                    errormsg.append('Warning : Methods section is empty. Please resubmit if applicable with additional information.')
            if col == 14:
                if cell_value is not None:
                    technical = cell_value
                    technical2 = rf'{technical}'
                    if not isinstance(technical2 , str):
                        errormsg.append(f'{technical2} is not a valid string. Please fix and resubmit.')
                elif rows[0] == row:
                    errormsg.append('Warning: Technical Info section is empty. Please resubmit if applicable with additional information.')              
    return errormsg

def check_specimen_sheet(filename):
    specimen_count = 0
    errormsg=[]
    column_num=[]
    sheetname = 'Specimen'
    specimen_sheet = pd.read_excel(filename, sheet_name=sheetname)
    total_col = (specimen_sheet.columns.get_loc(specimen_sheet.columns[-1]))
    for i in range(0, total_col + 1):
        column_num.append(i)
    specimen_sheet.columns = column_num
    specimen_sheet = specimen_sheet.where(pd.notna(specimen_sheet), None)
    for row in specimen_sheet.iterrows():
        for cell in row:
            if isinstance(cell, str):
                if not is_valid_cell(cell):
                    print(f"Non-ASCII characters found in: '{cell}'")
    colheads=['LocalID', 'Species', 'NCBITaxonomy', 'Age', 'Ageunit', 'Sex', 'Genotype', 'OrganLocalID', 'OrganName', 'SampleLocalID', 'Atlas', 'Locations']
    Sex = ['Male', 'Female', 'Unknown']
    cellcols=['A','B','C','D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
    cols=[cell for cell in specimen_sheet.iloc[2]]
    for i in range(0,len(colheads)):
        if cols[i] != colheads[i]:
            errormsg.append(' Tab: "Specimen" cell heading found: "' + cols[i] + \
                       '" but expected: "' + colheads[i] + '" at cell: "' + cellcols[i] + '3". ')
    if errormsg != []:
        return [ True, errormsg ]
    total_row = (specimen_sheet.index[-1])
    for i in range(5, (total_row + 1) ):
        specimen_count = specimen_count + 1
        cols=[cell for cell in specimen_sheet.iloc[i]]
        #if cols[0] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[0] + '" value expected but not found in cell: "' + cellcols[0] + str(i+1) + '". '
        if cols[1] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[1] + '" value expected but not found in cell: "' + cellcols[1] + str(i+1) + '". ')
        if cols[2] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[1] + '" value expected but not found in cell: "' + cellcols[1] + str(i+1) + '". ')
        if cols[3] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[3] + '" value expected but not found in cell "' + cellcols[3] + str(i+1) + '". ')
        if cols[4] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[4] + '" value expected but not found in cell "' + cellcols[4] + str(i+1) + '". ')
        if cols[5] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[5] + '" value expected but not found in cell "' + cellcols[5] + str(i+1) + '". ')
        if cols[5] not in Sex:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[5] + '" incorrect CV value found: "' + cols[5] + '" in cell "' + cellcols[6] + str(i+1) + '". ')
        #if cols[6] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[6] + '" value expected but not found in cell "' + cellcols[6] + str(i+1) + '". '
        #if cols[7] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[7] + '" value expected but not found in cell "' + cellcols[7] + str(i+1) + '". '
        #if cols[8] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[8] + '" value expected but not found in cell "' + cellcols[8] + str(i+1) + '". '
        if cols[9] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[9] + '" value expected but not found in cell "' + cellcols[9] + str(i+1) + '". ')
        #if cols[10] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[10] + '" value expected but not found in cell "' + cellcols[10] + str(i+1) + '". '
        #if cols[11] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[11] + '" value expected but not found in cell "' + cellcols[11] + str(i+1) + '". '
    columns = []
    rows = []
    for i in range(0, total_col +1):
        columns.append(i)
    for i in range(5, total_row + 1):
        rows.append(i)
    for col in columns:
        for row in rows:
            cell_value = specimen_sheet.iat[row, col]
            if col == 0:
                if cell_value is not None:
                    local_id = cell_value
                    is_a_string(local_id, errormsg)
            if col == 1:
                if cell_value is not None:
                    species = cell_value
                    all_lowercase(species, errormsg) 
            if col == 2:
                if cell_value is not None:
                    ncid= cell_value
                    id = ncid.strip('NCBI:txid')
                    check_taxonomy_name(id, species, errormsg)
                    #hold off along with col 1
            if col == 3: 
                if cell_value is not None:
                    age = cell_value
                    if not isinstance(age, float):
                        if isinstance(age, int):
                            float(age)
                        else:
                            errormsg.append(f'{age} is not a float value or an integer value. Please resubmit a float value.')
            if col == 4:
                if cell_value is not None:
                    ageunit = cell_value
                    is_a_string(ageunit, errormsg)        
            if col == 5: 
                if cell_value is not None:
                    sexid = cell_value
                    if sexid not in Sex:
                        errormsg.append(f'{sexid} is not within the listed acceptable values. Please resubmit with an accepted value.')
                        
            if col >= 6:
                if cell_value is not None:
                    string = cell_value
                    is_a_string(string, errormsg)
    return errormsg

def check_image_sheet(filename):
    image_count = 0
    errormsg=[]
    column_num=[]
    sheetname = 'Image'
    image_sheet = pd.read_excel(filename, sheet_name=sheetname)
    total_col = (image_sheet.columns.get_loc(image_sheet.columns[-1]))
    for i in range(0, total_col + 1):
        column_num.append(i)
    image_sheet.columns = column_num
    image_sheet = image_sheet.where(pd.notna(image_sheet), None)
    for row in image_sheet.iterrows():
        for cell in row:
            if isinstance(cell, str):
                if not is_valid_cell(cell):
                    print(f"Non-ASCII characters found in: '{cell}'")
    colheads=['xAxis','obliqueXdim1','obliqueXdim2',
                 'obliqueXdim3','yAxis', 'obliqueYdim1', 'obliqueYdim2', 'obliqueYdim3', 'zAxis', 'obliqueZdim1', 'obliqueZdim2', 'obliqueZdim3', 'landmarkName', 'landmarkX', 'landmarkY', 'landmarkZ', 'Number', 'displayColor', 'Representation', 'Flurophore', 'stepSizeX', 'stepSizeY', 'stepSizeZ', 'stepSizeT', 'Channels', 'Slices', 'z', 'Xsize', 'Ysize', 'Zsize', 'Gbytes', 'Files', 'DimensionOrder']
    ObliqueZdim3 = ['Superior', 'Inferior']
    ObliqueZdim2 = ['Anterior', 'Posterior']
    ObliqueZdim1 = ['Right', 'Left']
    zAxis = ['right-to-left', 'left-to-right', 'anterior-to-posterior', 'posterior-to-anterior', 'superior-to-inferior', 'inferior-to-superior', 'oblique',  'NA', 'N/A', 'na', 'N/A']
    obliqueYdim3 = ['Superior', 'Inferior']
    obliqueYdim2 = ['Anterior', 'Posterior']
    obliqueYdim1 = ['Right', 'Left']
    yAxis = ['right-to-left', 'left-to-right', 'anterior-to-posterior', 'posterior-to-anterior', 'superior-to-inferior', 'inferior-to-superior', 'oblique',  'NA', 'N/A', 'na', 'N/A']
    obliqueXdim3 = ['Superior', 'Inferior']
    obliqueXdim2 = ['Anterior', 'Posterior']
    obliqueXdim1 = ['Right', 'Left']
    xAxis = ['right-to-left', 'left-to-right', 'anterior-to-posterior', 'posterior-to-anterior', 'superior-to-inferior', 'inferior-to-superior', 'oblique', 'NA', 'N/A', 'na', 'N/A']

    cellcols=['A','B','C','D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG']
    cols=[cell for cell in image_sheet.iloc[2]]
    for i in range(0,len(colheads)):
        if cols[i] != colheads[i]:
            errormsg.append( ' Tab: "Image" cell heading found: "' + cols[i] + \
                       '" but expected: "' + colheads[i] + '" at cell: "' + cellcols[i] + '3". ')
    if errormsg != []:
        return [ True, errormsg ]
    total_row = (image_sheet.index[-1])
    for i in range(5,(total_row + 1)):
        image_count = image_count + 1
        cols=[cell for cell in image_sheet.iloc[i]]
        #if xAxis is oblique, oblique cols should reflect 
        if cols[0] == None:
            errormsg.append('On spreadsheet tab:' + sheetname + 'Column: "' + colheads[0] + '" value expected but not found in cell: "' + cellcols[0] + str(i+1) + '". ')
        if cols[0] not in xAxis:
            errormsg.append( 'On spreadsheet tab:' + sheetname + 'Column: "' + colheads[0] + '" incorrect CV value found: "' + cols[0] + '" in cell "' + cellcols[0] + str(i+1) + '". ')
        #if cols[1] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname + 'Column: "' + colheads[1] + '" value expected but not found in cell: "' + cellcols[1] + str(i+1) + '". '
        if cols[1] != None:
            if cols[1] not in obliqueXdim1:
                errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[1] + '" incorrect CV value found: "' + cols[1] + '" in cell "' + cellcols[1] + str(i+1) + '". ')
        #if cols[2] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[1] + '" value expected but not found in cell: "' + cellcols[2] + str(i+1) + '". '
        if cols[2] != None:
            if cols[2] not in obliqueXdim2:
                errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[2] + '" incorrect CV value found: "' + cols[2] + '" in cell "' + cellcols[2] + str(i+1) + '". ')
        #if cols[3] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[3] + '" value expected but not found in cell "' + cellcols[3] + str(i+1) + '". '
        if cols[3] != None:
            if cols[3] not in obliqueXdim3:
                errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[3] + '" incorrect CV value found: "' + cols[3] + '" in cell "' + cellcols[3] + str(i+1) + '". ')
        if cols[4] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[4] + '" value expected but not found in cell "' + cellcols[4] + str(i+1) + '". ')
        if cols[4] not in yAxis:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[4] + '" incorrect CV value found: "' + cols[4] + '" in cell "' + cellcols[4] + str(i+1) + '". ')
        #if cols[5] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[5] + '" value expected but not found in cell "' + cellcols[5] + str(i+1) + '". '
        if cols[5] != None:
            if cols[5] not in obliqueYdim1:
                errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[5] + '" incorrect CV value found: "' + cols[5] + '" in cell "' + cellcols[5] + str(i+1) + '". ')
        #if cols[6] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[6] + '" value expected but not found in cell "' + cellcols[6] + str(i+1) + '". '
        if cols[6] != None:
            if cols[6] not in obliqueYdim2:
                errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[6] + '" incorrect CV value found: "' + cols[6] + '" in cell "' + cellcols[6] + str(i+1) + '". ')
        #if cols[7] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[7] + '" value expected but not found in cell "' + cellcols[7] + str(i+1) + '". '
        if cols[7] != None:
            if cols[7] not in obliqueYdim3:
                errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[7] + '" incorrect CV value found: "' + cols[7] + '" in cell "' + cellcols[7] + str(i+1) + '". ')
        if cols[8] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[8] + '" value expected but not found in cell "' + cellcols[8] + str(i+1) + '". ')
        if cols[8] not in zAxis:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[8] + '" incorrect CV value found: "' + cols[8] + '" in cell "' + cellcols[8] + str(i+1) + '". ')
        #if cols[9] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[9] + '" value expected but not found in cell "' + cellcols[9] + str(i+1) + '". '
        if cols[9] != None:
            if cols[9] not in ObliqueZdim1:
                errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[9] + '" incorrect CV value found: "' + cols[9] + '" in cell "' + cellcols[9] + str(i+1) + '". ')
        #if cols[10] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[10] + '" value expected but not found in cell "' + cellcols[10] + str(i+1) + '". '
        if cols[10] != None:
            if cols[10] not in ObliqueZdim2:
                errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[10] + '" incorrect CV value found: "' + cols[10] + '" in cell "' + cellcols[10] + str(i+1) + '". ')
        #if cols[11] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[11] + '" value expected but not found in cell "' + cellcols[11] + str(i+1) + '". '
        if cols[11] != None:
            if cols[11] not in ObliqueZdim3:
                errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[11] + '" incorrect CV value found: "' + cols[11] + '" in cell "' + cellcols[11] + str(i+1) + '". ')
        #if cols[12] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[12] + '" value expected but not found in cell "' + cellcols[12] + str(i+1) + '". '
        #if cols[13] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[13] + '" value expected but not found in cell "' + cellcols[13] + str(i+1) + '". '
        #if cols[14] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[12] + '" value expected but not found in cell "' + cellcols[12] + str(i+1) + '". '
        # if cols[15] == "":
        #     errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[15] + '" value expected but not found in cell "' + cellcols[15] + str(i+1) + '". '
        if cols[16] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[12] + '" value expected but not found in cell "' + cellcols[12] + str(i+1) + '". ')
        if cols[17] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[12] + '" value expected but not found in cell "' + cellcols[12] + str(i+1) + '". ')
        #if cols[18] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[18] + '" value expected but not found in cell "' + cellcols[18] + str(i+1) + '". '
        #if cols[19] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[12] + '" value expected but not found in cell "' + cellcols[12] + str(i+1) + '". '
        if cols[20] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[20] + '" value expected but not found in cell "' + cellcols[20] + str(i+1) + '". ')
        if cols[21] == None:
            errormsg.append('On spreadsheet tab:' + sheetname +  'Column: "' + colheads[21] + '" value expected but not found in cell "' + cellcols[21] + str(i+1) + '". ')
        #if cols[22] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[22] + '" value expected but not found in cell "' + cellcols[22] + str(i+1) + '". '
        #if cols[23] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[23] + '" value expected but not found in cell "' + cellcols[23] + str(i+1) + '". '
        #if cols[24] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[24] + '" value expected but not found in cell "' + cellcols[24] + str(i+1) + '". '
        #if cols[25] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[25] + '" value expected but not found in cell "' + cellcols[25] + str(i+1) + '". '
        #if cols[26] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[26] + '" value expected but not found in cell "' + cellcols[26] + str(i+1) + '". '
        #if cols[27] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[27] + '" value expected but not found in cell "' + cellcols[27] + str(i+1) + '". '
        #if cols[28] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[28] + '" value expected but not found in cell "' + cellcols[28] + str(i+1) + '". '
        #if cols[29] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[29] + '" value expected but not found in cell "' + cellcols[29] + str(i+1) + '". '
        #if cols[30] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[30] + '" value expected but not found in cell "' + cellcols[30] + str(i+1) + '". '
        #if cols[31] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[31] + '" value expected but not found in cell "' + cellcols[31] + str(i+1) + '". '
        #if cols[32] == "":
        #    errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[32] + '" value expected but not found in cell "' + cellcols[32] + str(i+1) + '". '
    columns = []
    rows = []
    for i in range(0,total_col+1):
        columns.append(i)
    for i in range(5, total_row + 1):
        rows.append(i)
    for col in columns:
        for row in rows:
            cell_value = image_sheet.iat[row, col]
            if col == 0:
                if cell_value is not None:
                    x_axis = cell_value
                    if x_axis not in xAxis:
                        errormsg.append(f'{x_axis} is not one of the listed values. Please resubmit.')
            if col == 1:
                if x_axis == xAxis[6]:
                    if cell_value is not None:
                        xdim1 = cell_value
                        if xdim1 not in obliqueXdim1:
                            errormsg.append(f'{xdim1} is not an applicable answer. Please resubmit.')
            if col == 2:
                if x_axis == xAxis[6]:
                    if cell_value is not None:
                        xdim2 = cell_value
                        if xdim2 not in obliqueXdim2:
                            errormsg.append(f'{xdim2} is not an applicable answer. Please resubmit.')
            if col == 3:
                if x_axis == xAxis[6]:
                    if cell_value is not None:
                        xdim3 = cell_value
                        if xdim3 not in obliqueXdim3:
                            errormsg.append(f'{xdim3} is not an applicable answer. Please resubmit.')
            if col == 4:
                if cell_value is not None:
                    y_axis = cell_value
                    if y_axis not in yAxis:
                        errormsg.append(f'{y_axis} is not one of the listed values. Please resubmit.')
            if col == 5:
                if y_axis == yAxis[6]:
                    if cell_value is not None:
                        ydim1 = cell_value
                        if ydim1 not in obliqueYdim1:
                            errormsg.append(f'{ydim1} is not an applicable answer. Please resubmit.')
            if col == 6:
                if y_axis == yAxis[6]:
                    if cell_value is not None:
                        ydim2 = cell_value
                        if ydim2 not in obliqueYdim2:
                            errormsg.append(f'{ydim2} is not an applicable answer. Please resubmit.')
            if col == 7:
                if y_axis == yAxis[6]:
                    if cell_value is not None:
                        ydim3 = cell_value
                        if ydim3 not in obliqueYdim3:
                            errormsg.append(f'{ydim3} is not an applicable answer. Please resubmit.')        
            if col == 8:
                if cell_value is not None:
                    z_axis = cell_value
                    if z_axis not in zAxis:
                        errormsg.append(f'{z_axis} is not one of the listed values. Please resubmit.')
            if col == 9:
                if z_axis == zAxis[6]:
                    if cell_value is not None:
                        zdim1 = cell_value
                        if zdim1 not in ObliqueZdim1:
                            errormsg.append(f'{zdim1} is not an applicable answer. Please resubmit.')
            if col == 10:
                if z_axis == zAxis[6]:
                    if cell_value is not None:
                        zdim2 = cell_value
                        if zdim2 not in ObliqueZdim2:
                            errormsg.append(f'{zdim2} is not an applicable answer. Please resubmit.')
            if col == 11:
                if z_axis == zAxis[6]:
                    if cell_value is not None:
                        zdim3 = cell_value
                        if zdim3 not in ObliqueZdim3:
                            errormsg.append(f'{zdim3} is not an applicable answer. Please resubmit.')
            if col == 12:
                if cell_value is not None:
                    landmark = cell_value
                    pattern_for_land = r'^[a-z ]+$'
                    if bool(re.match(pattern_for_land, landmark)) != True:
                        errormsg.append(f'{landmark} is not all lowercase. Please resubmit with all lowercase letters.')
            if col == 13:
                if cell_value is not None:
                    landmarkx = cell_value 
                    if not isinstance(landmarkx, int):
                        errormsg.append(f'{landmarkx} is not an integer value. Please resubmit.')
            if col == 14:
                if cell_value is not None:
                    landmarky = cell_value 
                    if not isinstance(landmarky, int):
                        errormsg.append(f'{landmarky} is not an integer value. Please resubmit.')
            if col == 15:
                if cell_value is not None:
                    landmarkz = cell_value 
                    if not isinstance(landmarkz, int):
                        errormsg.append(f'{landmarkz} is not an integer value. Please resubmit.')
            if col == 16:
                if cell_value is not None:
                    number = cell_value
                    if not isinstance(number, str) and not isinstance(number, int):
                        errormsg.append(f'{number} is not a string. Please resubmit.')
            if col == 17:
                if cell_value is not None:
                    displayColor = cell_value
                    if not isinstance(displayColor, str):
                        errormsg.append(f'{displayColor} is not a string. Please resubmit.')
            if col == 18:
                if cell_value is not None:
                    representation = cell_value
                    if not isinstance(representation, str):
                        errormsg.append(f'{representation} is not a string. Please resubmit.')
            if col == 19:
                if cell_value is not None:
                    flurophore = cell_value
                    if not isinstance(flurophore, str):
                        errormsg.append(f'{flurophore} is not a string. Please resubmit.')
            if col == 20:
                if cell_value is not None:
                    stepSizeX = cell_value
                    if not isinstance(stepSizeX, float):
                        if isinstance(stepSizeX, int):
                            stepSizeX = float(stepSizeX)
                        else:
                            errormsg.append(f'{stepSizeX} is not a float value. Please resubmit.')
            if col == 21:
                if cell_value is not None:
                    stepSizeY = cell_value 
                    if not isinstance(stepSizeY, float):
                        if isinstance(stepSizeY, int):
                            stepSizeY = float(stepSizeY)
                        else:
                            errormsg.append(f'{stepSizeY} is not a float value. Please resubmit.')
            if col == 22:
                if cell_value is not None:
                    stepSizeZ = cell_value
                    if not isinstance(stepSizeZ, float):
                        if isinstance(stepSizeZ, int):
                            stepSizeZ = float(stepSizeZ)
                        else:
                            errormsg.append(f'{stepSizeZ} is not a float value. Please resubmit.')
            if col == 23:
                if cell_value is not None:
                    stepSizeT = cell_value
                    if not isinstance(stepSizeT, float):
                        if isinstance(stepSizeT, int):
                            stepSizeT = float(stepSizeT)
                        else:
                            errormsg.append(f'{stepSizeT} is not a float value. Please resubmit.')
            if col == 24:
                if cell_value is not None:
                    channels = cell_value
                    if not isinstance(channels, int):
                        if not channels.is_integer():
                            errormsg.append(f'{channels} is not an integer value. Please resubmit.')
            if col == 25:
                if cell_value is not None:
                    slices = cell_value
                    if not isinstance(slices, int):
                        if not slices.is_integer():
                            errormsg.append(f'{slices} is not an integer value. Please resubmit.')
            if col == 26:
                if cell_value is not None:
                    z = cell_value
                    if not isinstance(z, int):
                        errormsg.append(f'{z} is not an integer value. Please resubmit.')
            if col == 27:
                if cell_value is not None:
                    xSize = cell_value
                    if not isinstance(xSize, float):
                        errormsg.append(f'{xSize} is not a float value. Please resubmit.')
            if col == 28:
                if cell_value is not None:
                    ySize = cell_value
                    if not isinstance(ySize, int):
                        errormsg.append(f'{ySize} is not an integer value. Please resubmit.')
            if col == 29:
                if cell_value is not None:
                    zSize = cell_value
                    if not isinstance(zSize, int):
                        errormsg.append(f'{zSize} is not an integer value. Please resubmit.')
            if col == 30: 
                if cell_value is not None:
                    gBytes = cell_value
                    if not isinstance(gBytes, float):
                        errormsg.append(f'{gBytes} is not a floating point value. Please resubmit.')
            if col == 31: 
                if cell_value is not None:
                    files = cell_value
                    if not isinstance(files, int):
                        errormsg.append(f'{files} is not an integer value. Please resubmit.')
            if col == 32:
                if cell_value is not None:
                    dimensionOrder = cell_value
                    if not isinstance(dimensionOrder, str):
                        errormsg.append(f'{dimensionOrder} is not a string. Please resubmit.')
    return errormsg

def check_swc_sheet(filename):
    swc_count = 0
    errormsg=[]
    column_num = []
    sheetname = 'SWC'
    swc_sheet = pd.read_excel(filename, sheet_name=sheetname)
    total_col = (swc_sheet.columns.get_loc(swc_sheet.columns[-1]))
    for i in range(0, total_col + 1):
        column_num.append(i)
    swc_sheet.columns = column_num
    swc_sheet = swc_sheet.where(pd.notna(swc_sheet), None)
    for row in swc_sheet.iterrows():
        for cell in row:
            if isinstance(cell, str):
                if not is_valid_cell(cell):
                    print(f"Non-ASCII characters found in: '{cell}'")
    colheads=['tracingFile', 'sourceData', 'sourceDataSample', 'sourceDataSubmission', 'coordinates', 'coordinatesRegistration', 'brainRegion', 'brainRegionAtlas', 'brainRegionAtlasName', 'brainRegionAxonalProjection', 'brainRegionDendriticProjection', 'neuronType', 'segmentTags', 'proofreadingLevel', 'Notes']
    cellcols=['A','B','C','D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    coordinatesRegistration = ['Yes', 'No']
    cols=[cell for cell in swc_sheet.iloc[2]]
    for i in range(0,len(colheads)):
        if cols[i] != colheads[i]:
            errormsg = errormsg + ' Tab: "SWC" cell heading found: "' + cols[i] + \
                       '" but expected: "' + colheads[i] + '" at cell: "' + cellcols[i] + '3". '
    if errormsg != []:
        return [ True, errormsg ]
    total_row = (swc_sheet.index[-1])
    for i in range(5,(total_row + 1)):
        swc_count = swc_count + 1
        cols=[cell for cell in swc_sheet.iloc[i]]
        #if xAxis is oblique, oblique cols should reflect 
        if cols[0] == "":
            errormsg = errormsg + 'On spreadsheet tab:' + sheetname + 'Column: "' + colheads[0] + '" value expected but not found in cell: "' + cellcols[0] + str(i+1) + '". '
        if cols[5] == "":
           errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[5] + '" value expected but not found in cell "' + cellcols[5] + str(i+1) + '". '
        if cols[5] != "":
            if cols[5] not in coordinatesRegistration:
                errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[5] + '" incorrect CV value found: "' + cols[5] + '" in cell "' + cellcols[5] + str(i+1) + '". '
            if cols[5] == 'Yes':
              if cols[6] == "":
                errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[6] + '" value expected but not found in cell "' + cellcols[6] + str(i+1) + '". '
              if cols[7] == "":
                errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[7] + '" value expected but not found in cell "' + cellcols[7] + str(i+1) + '". '
              if cols[8] == "":
                errormsg = errormsg + 'On spreadsheet tab:' + sheetname +  'Column: "' + colheads[8] + '" value expected but not found in cell "' + cellcols[8] + str(i+1) + '". '
    return errormsg