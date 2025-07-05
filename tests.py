import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2 # исправил ошибку, был использован несуществующий метод

    def test_add_new_book_adds_book_with_empty_genre(self, collector):
        collector.add_new_book("Гарри Поттер")
        assert "Гарри Поттер" in collector.books_genre
        assert collector.books_genre["Гарри Поттер"] == ''

    def test_add_new_book_does_not_add_duplicates(self, collector):
        collector.add_new_book("Охотник")
        collector.add_new_book("Охотник")
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize("book_name, expected_added",[
        ("", False),
        ("X"*41, False),
        ("X"*40, True)])
    def test_add_new_book_checks_name_length_limits(self, collector, book_name, expected_added):
        collector.add_new_book(book_name)
        assert (book_name in collector.books_genre) == expected_added

    def test_get_books_with_specific_genre_returns_only_matching_books(self, collector):
        collector.add_new_book("Камеди")
        collector.set_book_genre("Камеди", "Комедии")
        collector.add_new_book("Космос")
        collector.set_book_genre("Космос", "Фантастика")

        books = collector.get_books_with_specific_genre("Комедии")
        assert "Камеди" in books
        assert "Космос" not in books

    def test_get_books_with_specific_genre_returns_empty_for_invalid_genre(self, collector):
        collector.add_new_book("Камеди")
        collector.set_book_genre("Камеди", "Комедии")

        books = collector.get_books_with_specific_genre("Кулинария")
        assert books == []

    def test_get_books_for_children_returns_only_children_books(self, collector):
        collector.add_new_book("Детская книга")
        collector.set_book_genre("Детская книга", "Мультфильмы")
        collector.add_new_book("Страшилка")
        collector.set_book_genre("Страшилка", "Ужасы")

        children_books = collector.get_books_for_children()
        assert "Детская книга" in children_books
        assert "Страшилка" not in children_books

    def test_add_book_in_favorites_adds_book_to_favorites(self, collector):
        collector.add_new_book("Любимая книга")
        collector.add_book_in_favorites("Любимая книга")
        assert "Любимая книга" in collector.favorites

    def test_delete_book_from_favorites_removes_book(self, collector):
        collector.add_new_book("Любимая книга")
        collector.add_book_in_favorites("Любимая книга")
        collector.delete_book_from_favorites("Любимая книга")
        assert "Любимая книга" not in collector.favorites

    def test_add_book_in_favorites_does_not_add_duplicates(self, collector):
        collector.add_new_book("Повторение")
        collector.add_book_in_favorites("Повторение")
        collector.add_book_in_favorites("Повторение")
        assert collector.favorites.count("Повторение") == 1

    def test_add_book_in_favorites_ignores_nonexistent_books(self, collector):
        collector.add_book_in_favorites("Шрек")
        assert "Шрек" not in collector.favorites

    def test_get_book_genre_returns_correct_genre(self, collector):
        collector.add_new_book("Смешарики")
        collector.set_book_genre("Смешарики", "Мультфильмы")
        assert collector.get_book_genre("Смешарики") == "Мультфильмы"

    def test_get_list_of_favorites_books_returns_all_favorites(self, collector):
        collector.add_new_book("Фаворит")
        collector.add_book_in_favorites("Фаворит")
        favorites = collector.get_list_of_favorites_books()
        assert "Фаворит" in favorites

    @pytest.mark.parametrize("book_name, expected_genre", [
        ("Пила", "Фантастика"),
        ("Шерлок", "Детективы"),
        ("Воронины", "Комедии")])
    def test_set_book_genre_sets_correct_genre_for_various_books(self, collector, book_name, expected_genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, expected_genre)
        assert collector.get_book_genre(book_name) == expected_genre
