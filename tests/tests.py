#import pytest
#from main import BooksCollector
#from data import *
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
    def test_add_new_book_add_same_name_book(self, collector):
        #collector = BooksCollector()
        collector.add_new_book(BOOK_TITLE_1)
        collector.add_new_book(BOOK_TITLE_1)
        result = len(collector.books_genre)
        assert result == 1

    # проверяем, что книгу нелья добавть книги без названия ипи больше 40 символов
    @pytest.mark.parametrize('book_title_wrong', WRONG_BOOK_TITLE)
    def test_add_new_book_wrong_name(self, collector, book_title_wrong):
        collector.add_new_book(book_title_wrong)
        result = len(collector.books_genre)
        assert result == 0

    #проверям, что можно добавить жанр книги
    @pytest.mark.parametrize('book_genre', GENRE)
    def test_set_book_genre_from_genre(self, collector_one_book, book_genre):
        collector_one_book.set_book_genre(BOOK_TITLE_1, book_genre)
        result = collector_one_book.get_book_genre(BOOK_TITLE_1)
        assert result == book_genre

    #check set genre not from GENRE
    @pytest.mark.parametrize('book_genre_wrong', WRONG_GENRE)
    def test_set_book_genre_not_from_genre(self, collector_one_book, book_genre_wrong):
        collector_one_book.set_book_genre(BOOK_TITLE_1, book_genre_wrong)
        result = collector_one_book.get_book_genre(BOOK_TITLE_1)
        assert result == ''

    #check re genre by name
    @pytest.mark.parametrize('book_genre', GENRE)
    def test_get_book_genre_from_book_genre(self, collector_one_book, book_genre):
        collector_one_book.set_book_genre(BOOK_TITLE_1, book_genre)
        result = collector_one_book.get_book_genre(BOOK_TITLE_1)
        assert result == book_genre

    #вывод списка книг по жанру
    def test_get_books_with_specific_genre(self, collector_two_books_one_genre):
        collector_two_books_one_genre.set_book_genre(BOOK_TITLE_2, BOOK_GENRE_2)
        result = collector_two_books_one_genre.get_books_with_specific_genre(BOOK_GENRE_2)
        assert result[0] == BOOK_TITLE_2


    #вывод словаря books_genre
    def test_get_books_genre(self, collector_two_books_one_genre):
        result = collector_two_books_one_genre.get_books_genre()
        expected = {BOOK_TITLE_1:BOOK_GENRE_1, BOOK_TITLE_2:''}
        assert result == expected

    #возвращаем книги, подходящие детям
    @pytest.mark.parametrize('genre_age_rating', GENRE_AGE_RATING)
    def test_get_books_for_children(self, collector_two_books_one_genre, genre_age_rating):
        collector_two_books_one_genre.set_book_genre(BOOK_TITLE_2, genre_age_rating)
        result = collector_two_books_one_genre.get_books_for_children()
        expected = [BOOK_TITLE_1]
        assert result == expected

    #проверяес возможность добавления книги в избранное
    def test_add_book_in_favorite_one_book(self, collector_two_books_one_genre):
        collector_two_books_one_genre.add_book_in_favorites(BOOK_TITLE_1)
        result = collector_two_books_one_genre.favorites
        expected = [BOOK_TITLE_1]
        assert result == expected

    #проверяем возможеость удаления книги из избранного
    def test_delete_book_from_favorites(self, two_books_added_to_favorite):
        two_books_added_to_favorite.delete_book_from_favorites(BOOK_TITLE_1)
        result = two_books_added_to_favorite.favorites
        expected = [BOOK_TITLE_2]
        assert result == expected

    #проверяем возможность получения списка избранных
    def test_get_list_of_favorites_books(self, two_books_added_to_favorite):
        result = two_books_added_to_favorite.get_list_of_favorites_books()
        expected = [BOOK_TITLE_1, BOOK_TITLE_2]
        assert result == expected