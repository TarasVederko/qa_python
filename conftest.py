import pytest
#from helpers import generate_random_book_title
from main import BooksCollector
@pytest.fixture()
def collector():
    collector = BooksCollector()
    return collector