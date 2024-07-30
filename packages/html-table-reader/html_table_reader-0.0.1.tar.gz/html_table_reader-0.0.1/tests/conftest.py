from pathlib import Path

import pytest


@pytest.fixture
def content():
    with open(Path('tests/fixtures/data.txt'), mode='r', encoding='utf8') as fp:
        return fp.read()
