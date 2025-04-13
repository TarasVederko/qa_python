import pytest
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

@pytest.fixture()
def collector_two_books_one_genre(collector_one_book):
    collector_one_book.set_book_genre(BOOK_TITLE_1, BOOK_GENRE_1)
    collector_one_book.add_new_book(BOOK_TITLE_2)
    return collector_one_book

@pytest.fixture()
def two_books_added_to_favorite(collector_two_books_one_genre):
    collector_two_books_one_genre.add_book_in_favorites(BOOK_TITLE_1)
    collector_two_books_one_genre.add_book_in_favorites(BOOK_TITLE_2)
    return collector_two_books_one_genre
