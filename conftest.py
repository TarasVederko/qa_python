import pytest
#from helpers import generate_random_book_title
from main import *
from data import *

@pytest.fixture()
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture()
def collector_with_one_book(collector):
    collector.add_new_book(BOOK_TITLE)
    return collector