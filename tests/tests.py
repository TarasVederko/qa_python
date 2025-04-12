import pytest
from main import BooksCollector
from data import *
from conftest import *


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        # создаем экземпляр (объект) класса BooksCollector
        #collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь get_books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # проверям, что две книги с одинаковым названием добавить не получится
    def test_add_new_book_add_same_book(self, collector):
        #collector = BooksCollector()
        collector.add_new_book(BOOK_TITLE)
        collector.add_new_book(BOOK_TITLE)
        assert len(collector.books_genre) == 1

    # проверяем, что книгу нелья добавть книги без названия ипи больше 40 символов
    @pytest.mark.parametrize('book_title_wrong', WRONG_BOOK_TITLE)
    def test_add_new_book_wrong_name(self, collector, book_title_wrong):
        collector.add_new_book(book_title_wrong)
        assert len(collector.books_genre) == 0

    #проверям, что можно добавть жанр книги
    @pytest.mark.parametrize('book_genre', GENRE)
    def test_set_book_genre_from_genre(self, collector_with_one_book, book_genre):
        collector_with_one_book.set_book_genre(BOOK_TITLE, book_genre)
        assert collector_with_one_book.get_book_genre(BOOK_TITLE) == book_genre

    #check set genre not from GENRE
    @pytest.mark.parametrize('book_genre_wrong', WRONG_GENRE)
    def test_set_book_genre_not_from_genre(self, collector_with_one_book, book_genre_wrong):
        collector_with_one_book.set_book_genre(BOOK_TITLE, book_genre_wrong)
        assert collector_with_one_book.get_book_genre(BOOK_TITLE) == ''