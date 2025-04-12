import pytest
#from helpers import generate_random_book_title
from main import *
from data import *

@pytest.fixture()
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture()
def collector_one_book(collector):
    collector.add_new_book(BOOK_TITLE_1)
    return collector

