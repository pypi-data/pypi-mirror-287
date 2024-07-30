from typing import List, Dict

import bs4


def extract_header(content: str) -> List[str]:
    s = bs4.BeautifulSoup(content, 'html.parser')
    return [el.text.strip() for el in s.find_all('th')]


def extract_body(content: str) -> List[List]:
    data = []
    s = bs4.BeautifulSoup(content, 'html.parser')
    rows = s.find_all('tr')
    for row in rows[1:]:
        cells = row.find_all('td')
        data.append([el.text.strip() for el in cells])
    return data


def list_to_dict(keys: List[str], values: List[str]) -> Dict:
    return {k: v for k, v in zip(keys, values)}


def html_to_python(content: str) -> List[Dict]:
    keys = extract_header(content)
    return [list_to_dict(keys, values) for values in extract_body(content)]


def extract_table(content: str) -> List[Dict]:
    return html_to_python(content)
