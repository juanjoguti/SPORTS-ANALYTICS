import re
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup


class Scraper():

    def __get_table_headers(self, table):

        headers = table.find('thead').findAll('tr')
        if len(headers) == 1:
            return [header.text for header in headers[0].findAll('th')]
        else:
            over_headers = [header.text for header in headers[0].findAll('th')]
            cols = [header.text for header in headers[1].findAll('th')]
            for over_header in list(set(over_headers)):
                attrs = {'data-over-header': over_header}
                for header in headers[1].findAll('th', attrs):
                    cols[cols.index(header.text)] = (over_header, header.text)
            return pd.MultiIndex.from_tuples(cols)

    def __get_table_data(self, table, headers):

        data = []
        body = table.find('tbody')
        for row in body.findAll('tr'):
            for col in row.findAll('th', {'scope': 'row'}):
                data.append(col.text.strip().encode().decode('utf-8'))
            for col in row.findAll('td'):
                data.append(col.text.strip().encode().decode('utf-8'))
        data = np.asarray(data)
        data = data.reshape((len(data)//len(headers), len(headers)))
        return data.tolist()

    def get_table_by_identifier(self, url, table_identifier, headers=None):

        response = requests.get(url)
        comm = re.compile('<!--|-->')
        soup = BeautifulSoup(comm.sub('', response.text), 'lxml')
        table = soup.find('table', table_identifier)
        if headers is None:
            headers = self.__get_table_headers(table)
        data = self.__get_table_data(table, headers)
        return pd.DataFrame(data, columns=headers)
