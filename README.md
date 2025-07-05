# qa_python

1. test_add_new_book_add_two_books
Проверяет, что после добавления двух разных книг количество книг в коллекции равно 2.

2. test_add_new_book_adds_book_with_empty_genre
Проверяет, что после добавления книги она есть в коллекции, а жанр у неё изначально пустой.

3. test_add_new_book_does_not_add_duplicates
Проверяет, что при попытке добавить книгу с одинаковым именем дважды, в коллекции она хранится только один раз.

4. test_add_new_book_checks_name_length_limits
Проверяет добавление книг с разной длиной названия: пустая строка и строка длиннее 40 символов не добавляются, строка длиной 40 символов добавляется.

5. test_get_books_with_specific_genre_returns_only_matching_books
Проверяет, что метод возвращает книги только с указанным жанром, исключая книги с другими жанрами.

6. test_get_books_with_specific_genre_returns_empty_for_invalid_genre
Проверяет, что при запросе несуществующего жанра возвращается пустой список.

7. test_get_books_for_children_returns_only_children_books
Проверяет, что метод возвращает только книги с жанрами, разрешёнными для детей, исключая книги с «взрослыми» жанрами.

8. test_add_book_in_favorites_adds_book_to_favorites
Проверяет, что после добавления книги в избранное, она действительно появляется в списке избранных.

9. test_delete_book_from_favorites_removes_book
Проверяет, что книга корректно удаляется из списка избранных.

10. test_add_book_in_favorites_does_not_add_duplicates
Проверяет, что одна и та же книга не может быть добавлена в избранное более одного раза.

11. test_add_book_in_favorites_ignores_nonexistent_books
Проверяет, что нельзя добавить в избранное книгу, которой нет в коллекции.

12. test_get_book_genre_returns_correct_genre
Проверяет, что для добавленной книги корректно возвращается установленный жанр.

13. test_get_list_of_favorites_books_returns_all_favorites
Проверяет, что метод возвращает список книг из избранного, включая добавленную книгу.

14. test_set_book_genre_sets_correct_genre_for_various_books
Проверяет установку жанров для разных книг и корректное получение жанра для каждой из них.