from src.html_table_reader.parser_html import html_to_python, list_to_dict, extract_header, extract_body, extract_table


def test_extract_header(content):
    expected = ['ID CBX', 'Nome', 'UF', 'ID FIDE', 'Data Pagto.', 'Data Nasc.']
    got = extract_header(content)
    assert got == expected


def test_extract_body(content):
    expected = [['81179', 'Jonatan Rodrigues da Silva', 'DF', '44749996', 'Pendente', '12/12/1991']]
    got = extract_body(content)
    assert got == expected


def test_list_to_dict(content):
    expected = [{'ID CBX': '81179',
                 'Nome': 'Jonatan Rodrigues da Silva',
                 'UF': 'DF',
                 'ID FIDE': '44749996',
                 'Data Pagto.': 'Pendente',
                 'Data Nasc.': '12/12/1991',
                 }]
    keys = ['ID CBX', 'Nome', 'UF', 'ID FIDE', 'Data Pagto.', 'Data Nasc.']
    data = [['81179', 'Jonatan Rodrigues da Silva', 'DF', '44749996', 'Pendente', '12/12/1991']]
    got = [list_to_dict(keys, rows) for rows in data]
    assert got == expected


def test_html_to_python(content):
    expected = [{'ID CBX': '81179',
                 'Nome': 'Jonatan Rodrigues da Silva',
                 'UF': 'DF',
                 'ID FIDE': '44749996',
                 'Data Pagto.': 'Pendente',
                 'Data Nasc.': '12/12/1991',
                 }]

    got = html_to_python(content)
    assert got == expected


def test_extract_table(content):
    expected = [{'ID CBX': '81179',
                 'Nome': 'Jonatan Rodrigues da Silva',
                 'UF': 'DF',
                 'ID FIDE': '44749996',
                 'Data Pagto.': 'Pendente',
                 'Data Nasc.': '12/12/1991',
                 }]

    got = extract_table(content)
    assert got == expected
