import json
import pybtex
import requests
import os
from pybtex.database import BibliographyData, Entry, Person
from dateutil.parser import parse
import math

def load_configuration():
    zotero_bibtex_config = dict()
    zotero_conf_filename = 'zotero_bibtex_configuration.json'
    zotero_conf_dir = os.path.join(os.path.dirname(os.getcwd()), 'source', 'configuration')
    # zotero_conf_dir = os.path.join(os.getcwd(), 'src', 'content')
    json_path = os.path.join(zotero_conf_dir, zotero_conf_filename)

    with open(json_path) as json_string:
        zotero_bibtex_config = json.load(json_string)

    return zotero_bibtex_config
def downlaod_zotero_datas(URL, API_KEY):
    zotero_result = list
    response = requests.get(URL, headers={'Zotero-API-Key': API_KEY})
    response = response.json()
    zotero_raw = json.dumps(response, ensure_ascii=False)  # json.loads(response)
    zotero_result = json.loads(zotero_raw)
    return zotero_result

def get_data(zotero_bibtex_config):
    # result_limit = 100
    # access_type = 'groups'
    # zotero_access_id = '5245833'
    # collection_id = 'USSFDCEH'
    result_limit = int(zotero_bibtex_config.get('result_limit'))
    access_type = zotero_bibtex_config.get('access_type')
    zotero_access_id = zotero_bibtex_config.get('zotero_access_id')
    collection_id = zotero_bibtex_config.get('collection_id')
    API_KEY = zotero_bibtex_config.get('api_key')
    zotero_data = list()
    URL = 'https://api.zotero.org/' + str(access_type) + '/' + str(zotero_access_id) + '/collections/' + str(
        collection_id) + '/items?limit=1?format=json?sort=dateAdded?direction=asc'

    # API_KEY = '6Xgb3XhGjQXwA8NuZgu3bw3s'
    response = requests.get(URL, headers={'Zotero-API-Key': API_KEY})

    header_dict = response.headers
    total_elemets = int(header_dict.get('Total-Results'), 0)

    if total_elemets < result_limit:
        URL_ALL_ITEMS = 'https://api.zotero.org/' + str(access_type) + '/' + str(
            zotero_access_id) + '/collections/' + str(collection_id) + '/items?limit=' + str(
            result_limit) + '?format=json?sort=dateAdded?direction=asc'
        zotero_result = downlaod_zotero_datas(URL_ALL_ITEMS, API_KEY)

        zotero_data.extend(zotero_result)
    else:
        runs = int(math.ceil(total_elemets / result_limit))
        index = 0
        start_index = 0
        while index < runs:
            URL_Separated = 'https://api.zotero.org/' + str(access_type) + '/' + str(
                zotero_access_id) + '/collections/' + str(collection_id) + '/items?limit=' + str(
                result_limit) + '?format=json?sort=dateAdded?direction=asc' + '&start=' + str(start_index)
            zotero_result = downlaod_zotero_datas(URL_Separated, API_KEY)

            zotero_data.extend(zotero_result)

            start_index += result_limit
            index += 1

    return zotero_data

def convert_to_datetime(input_str, parserinfo=None):
    return parse(input_str, parserinfo=parserinfo)
def get_dates(date, bibtex_item_type, bibtex_month_attributes):
    dated_date = convert_to_datetime(date)
    return_value = dict()
    if bibtex_item_type in bibtex_month_attributes:
        year = dated_date.year
        month = dated_date.month
        return_value = {'year': year, 'month':month}
    else:
        year = dated_date.year
        return_value = {'year': year}

    return return_value

def split_creators(creators):
    if creators != []:

        creatorlist = ''
        for index, creator in enumerate(creators):
            type = creator.get('creatorType')
            firstname = creator.get('firstName')
            lastname = creator.get('lastName')
            name = creator.get('name')
            if type == 'author':

                if name and not (firstname or lastname):
                    creatorlist = creatorlist + name
                    if index != len(creators) - 1:
                        creatorlist = creatorlist + ' and '
                else:
                    creatorlist = creatorlist + lastname + ',' + firstname
                    if index != len(creators) - 1:
                        creatorlist = creatorlist + ' and '
    else:
        creatorlist = 'unknown author'

    bib_entry = 'author=' + '\"' + creatorlist + '\"'

    return bib_entry


def write_bibliography(zotero_data, zotero_bibtex_config):
    # file_json = 'keystore.json'
    file_json = zotero_bibtex_config.get('keystore_file')
    keystore_path = zotero_bibtex_config.get('keystore_filepath')
    # tex_dir = os.path.join(os.path.dirname(os.getcwd()), 'source', 'configuration')
    tex_dir = os.path.join(os.path.dirname(os.getcwd()), keystore_path)
    # tex_dir = os.path.join(os.getcwd(), 'src', 'content')
    json_path = os.path.join(tex_dir, file_json)

    with open(json_path) as json_string:
        zotero_bibtex_keys = json.load(json_string)

    zotero_bibtex_keys_specials = {
        'thesis': {'phdthesis': ['dissertation', 'phd', 'doctorial', 'doctor', 'doktor', 'doktorarbeit'],
                   'masterthesis': ['ma', 'master', 'masters']}
    }
    zotero_bibtex_attributes_special = {
        'date': 'get_dates',
        'creators': 'split_creators'
    }
    bibtex_month_attributes = ['booklet', 'mastersthesis', 'phdthesis', 'techreport']
    # Bibliography
    # tex_dir = os.path.join(os.path.dirname(os.getcwd()), 'source')
    bibtex_path = zotero_bibtex_config.get('bibtex_filepath')
    tex_dir = os.path.join(os.path.dirname(os.getcwd()), bibtex_path)
    # tex_dir = os.path.join(os.getcwd(), 'src', 'content')
    # file_name = 'Datenbank_Projektauftrag_Michael_Graber.bib'
    file_name = zotero_bibtex_config.get('bibtex_filename')

    file_path = os.path.join(tex_dir, file_name)

    # bib_datas = BibliographyData()
    listKeys = list()
    bib_data = ''
    for zotero_items in zotero_data:
        biblio_item = zotero_items.get('data')
        itemkeys = biblio_item.keys()
        listKeys.extend(biblio_item.keys())
        zotero_item_key = biblio_item.get('key')
        zotero_item_title = biblio_item.get('title')
        zotero_item_nameofact = biblio_item.get('nameOfAct')
        zotero_item_nameofcase = biblio_item.get('caseName')
        zotero_item_subject = biblio_item.get('subject')
        zotero_item_type = biblio_item.get('itemType')

        # some item types have no titles
        # set the special names instead of the title
        if zotero_item_title:
            bibtex_item_titel = zotero_item_title
        else:
            if zotero_item_type == 'statute':
                biblio_item['title'] = zotero_item_nameofact
                bibtex_item_titel = zotero_item_nameofact
            elif zotero_item_type == 'case':
                biblio_item['title'] = zotero_item_nameofcase
                bibtex_item_titel = zotero_item_nameofcase
            elif zotero_item_type == 'email':
                biblio_item['title'] = zotero_item_subject
                bibtex_item_titel = zotero_item_subject

        if zotero_item_type == 'thesis':
            master_list = zotero_bibtex_keys_specials.get(zotero_item_type).get('masterthesis')
            phd_list = zotero_bibtex_keys_specials.get(zotero_item_type).get('phdthesis')

            # First Master thesis
            if any(item in bibtex_item_titel for item in master_list):
                bibtex_item_key = 'masterthesis'
            # Second PHD Thesis
            elif any(item in bibtex_item_titel for item in phd_list):
                bibtex_item_key = 'phdthesis'
            else:
                bibtex_item_key = 'masterthesis'
        else:
            if zotero_bibtex_keys.get(zotero_item_type).get('key'):
                bibtex_item_key = zotero_bibtex_keys.get(zotero_item_type).get('key')
            else:
                bibtex_item_key = 'misc'

        # get all Keys for the zotero item type
        entryset = '\n'
        entry = ''

        zotero_item_attributes = zotero_bibtex_keys.get(zotero_item_type).get('attributes').keys()
        item_attributes = sorted(zotero_item_attributes, reverse=True)

        for index, item_attribute in enumerate(item_attributes):
            bibtex_item_attribute = zotero_bibtex_keys.get(zotero_item_type).get('attributes').get(item_attribute)
            zotero_item_value = biblio_item.get(item_attribute)
            zotero_item_value_extra = ''
            bibtex_item_attribute_extra = ''

            # Special Cases
            if bibtex_item_attribute == 'SPECIALCHECK' and zotero_item_value not in ['', None]:
                bibtex_special_attribute = zotero_bibtex_attributes_special.get(item_attribute)

                match bibtex_special_attribute:
                    case 'get_dates':
                        zotero_item_value = get_dates(zotero_item_value, bibtex_item_key, bibtex_month_attributes)
                        if zotero_item_value.get('month'):
                            zotero_item_value_extra = zotero_item_value.get('month')
                            bibtex_item_attribute_extra = 'month'

                        zotero_item_value = zotero_item_value.get('year')
                        bibtex_item_attribute = 'year'
                    case 'split_creators':
                        authors = split_creators(zotero_item_value)
                        entryset = entryset + authors
            elif bibtex_item_attribute == 'howpublished':
                if zotero_item_value not in ['', None, []]:
                    zotero_item_value = '\\url{' + zotero_item_value + '}'

            if bibtex_item_attribute not in ['', 'None', 'author', 'SPECIALCHECK'] and zotero_item_value not in ['', None, []]:
                if zotero_item_value_extra:

                    if type(zotero_item_value_extra) == "string":
                        entryset = entryset + str(bibtex_item_attribute_extra) + '=\"' + str(zotero_item_value_extra) + '\"'
                    else:
                        entryset = entryset + str(bibtex_item_attribute_extra) + '=' + str(zotero_item_value_extra)

                    if index != len(item_attributes) - 1:
                        entryset = entryset + ',\n'
                    else:
                        entryset = entryset + '\n'

                if type(zotero_item_value) == str and not zotero_item_value.isnumeric():
                    entryset = entryset + str(bibtex_item_attribute) + '=\"' + str(zotero_item_value) + '\"'
                else:
                    entryset = entryset + str(bibtex_item_attribute) + '=' + str(zotero_item_value)

                if index != len(item_attributes) - 1:
                    entryset = entryset + ',\n'
                else:
                    entryset = entryset + '\n'

        # create the Entry
        entry = '@' + bibtex_item_key + '{' + zotero_item_key + ',\n'
        entry = entry + entryset + '}'
        bib_data = bib_data + '\n' + entry

    # parse String to pybtex.database Object
    # bib_datas = pybtex.database.parse_string(bib_data, bib_format="bibtex", encoding='ISO-8859-1')
    bib_datas = pybtex.database.parse_string(bib_data, bib_format="bibtex", encoding='Iutf-8')
    # Save pybtex.database to file
    # BibliographyData.to_file(bib_datas, file_path, bib_format="bibtex", encoding='ISO-8859-1')
    BibliographyData.to_file(bib_datas, file_path, bib_format="bibtex", encoding='utf-8')


zotero_bibtex_config = load_configuration()
zotero_data = get_data(zotero_bibtex_config)
write_bibliography(zotero_data, zotero_bibtex_config)