def create_cucumber_text():
    print('\n\nTEST - create_cucumber_text\n\n')


# нить
# Терминал
# e cucmber textpy X
# src› utils › cucmber_text.py > create_cucmber text
# bs4 import BeautifulSoup
# 10111213141516
# # Наполняем данными файл
# def create cumber text(**params):
# with open(f' (paramsI"name_file"|). feature', 'W') as f:
# # url epic
# f.write(f'# (params ["web _url"]}\n')
# # автор еріс
# f.write(f'# (params["author"|/\n')
# # дата последнего обновления
# f.write(f'# {params ["updated at"1/\n\n')
# # Feature
# f.write(f' Feature: (params["title"]}\n')
# soup_Fist = BeautifulSoup(str (params ["description"]), 'html.parser')
# * переходим в нужное место в едіс
# scenario out = soup_Fist. find(params ["scenario number*]):
# # Разбираем tag, которые используем
# tags = scenario _out.find_all(["background",
# "scenario", "scenariooutline",
# "given", "when", "then", "and", "but", "rule", "examples",
# "gr
# # Для проверки есть ли tag в группе
# group tag = scenario_out. find ("group")
# # Счетчик example
# counter example = 0
# 359088666
# 2202222425 26228230313233343536373839 4
# # Перебираем не нарушая порядок html
# for tag in tags:
# arr_examples =
# soup = BeautifulSoup(str (tag),
# "html'.parser')
# # Backaround
# soup. find("background") and group_tag.find( "background") == None: f.write(f'\n
# Background: {soup. find( "background").text/\n')
# if soup. find("scenario") and group_tag. find("scenario") == None:
# f.write(f'\n
# Out line,
# Scenario: {soup. find ( "scenario").text/\n')
# if soup. find("scenariooutline") and group tag. find("scenariooutline") == None:
# f.write(f'\n
# # Given
# Scenario Outline: {soup.find( "scenariooutline").text}\n')
# if soup. find("given") and group_tag. find("given*) == None:
# f.write(f'\n
# Given
# When
# {soup. find("given") .text}\n')
# if soup. find ("when") and group_tag. find ("when") == None:
# f.write(f*\n
# * Then
# when tsoup.find（"when"）・text｝\n'）
# if soup, find("then") and group_tag. find ("then") = None:
# fawrite(f'\n
# f.write(f'\n')
# Then {soup. find ("then") .texti')
# # And.
# if soup, find("and") and group_tag.find("and") == None:
# f.write(f'\n
# * But
# And {soup. find ("and"). text}\n')
# if soup, find("but") and group tag. find ("but") == None:
# f.write(f'\n.
# * Rule
# But {soup. find ("but").text}\n*)
# if soup, find("rule") and group_tag, find("rule") == None:
# f.write(f'\n
# group (для работы с example).
# I if-soup, find ("group*):
# Rule soup, find ("rule"), text)\n')
# group exm_tag = soup, find ("group")
# moccub exampl
# for index, 4 group exm in enumerate(group_exm_tag):
# groupexm html = BeautifulSoup(str(1 group exm),
# examples tags = groupexm_html, find("examples*)








# 62
# group_exm_tag = soup. find ("group")
# # Складываем в массив example
# for index,
# i group_exm in enumerate(group_exm_tag):
# groupexm_html = BeautifulSoup(str (i_group_exm),
# 'html parser')
# 66
# examples
# tags = groupexm_ html. find( "examples")
# if examples tags is not None:,
# 68
# arr examples.append (examples_tags.text)
# 69
# # Ищем место вставки example в tag (groupin)
# if soup. find( ["background",
# "scenario",
# "scenariooutline", "given",
# "when",
# "then", "and", "but", "rule"]):
# 723324
# # TODO !!! (сделать для всех tag).
# f.write(f'\n
# Then {soup. find ("then").text) ')
# if soup. find("groupin"):
# for index, i arr in enumerate(arr_examples):
# 75
# # Счетчик
# counter example += 1
# # Создаем перменую для списка с номером
# f.write(f'"<col
# _(counter_example}»"*)
# if index < len(arr_examples) -2:
# f write(f',
# f.write（f'\n
# # В конце добавляем Examples
# f.write(f'\n
# 8888r8
# Examples: *)
# 87
# 838990919
# 100
# 101
# 102
# 112
# 期924151617
# 118
# 910113
# 124
# Git Graph
# counter example = 0
# tags_ex = scenario out. find all ("examples")
# # Создаем переменные и добавляем номера
# for tag in tags ex:
# soup = BeautifulSoup(str(tag), 'html.parser')
# if soup. find ("examples"):
# counter _example += 1
# f. write(f'col_{counter_example}')
# if counter example <= lenItags ex)-1:
# f.write(f',
# counter example = 0
# Создаем переменные и добавляем номера для таблицы
# for Lag tags_ex:
# soup = BeautifulSoup(str (tag),
# 'html parser')
# if soup. find("examples"):
# counter_example +=
# fiwrite(f'| col_{counter example) ')
# if counter_example > len(tags_ex) -1:
# f.write(f'')
# counter _example = 0
# # Записываем, значения полученные из еріс в, таблицу
# f,write(f'\n
# for tag in tags_ex:
# soup = BeautifulSoup(str(tag),
# 'html,parser')
# if soup. find ("examples");
# counter_example += 1
# f,write(f'| (soup, find ("examples"), text) ') if counter example > len(tags_ex) -1:
# f,write(f' |')
# Создаем новый
# , f' (params ("name_file"|), feature')