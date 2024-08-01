# https://github.com/DemonDis/bdd_generator/issues/1
# OWNER
# 2024-07-31T08:37:57Z

Feature: Тестируем lib

    Scenario: Начало всех начал

        Given Начало всех начал

        When О и здесь еще

        Then Таблица THEN  "<col_1>", "<col_2>", "<col_3>"
 
            Examples: col_1, col_2, col_3
                | col_1 | col_2 | col_3 |
                | Первый | Второй | Третий |