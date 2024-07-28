import os
import difflib 
from simple_term_menu import TerminalMenu 

from bs4 import BeautifulSoup
from .cucumber_text import create_cucumber_text
from .cache_file import feature_cache_file, changes_cache_file
from .bdd_generator import generator

def create_cucumber_file(**params):
    print('!!!!!!!!!!\n\n', params)
    create_cucumber_text()
    feature_cache_file()
    changes_cache_file()
    generator()
# import
# OS
# from simple term menu import TerminalMenu import difflib
# from bs4 import BeautifulSoup
# from
# • cumber_text import create cumber text.
# from
# •cache_file import feature cache_file, changes_cache_file
# from
# bdd generator import generator
# 10
# 12
# 16
# 17
# 24
# 25
# 26
# 27
# 28
# 29
# 30
# 31
# 32
# 33
# 132415
# 181920212223
# 33536
# 37383
# 34 55 56 57 58
# 40
# 41
# 42
# 43
# 44
# 45.
# 46
# 47
# 48
# 49
# 50
# 51
# 52
# 53
# 59
# 60
# 61
# 62
# 63
# 64
# 65
# 66
# 67
# it Graph
# # Создаем файл
# feature u cache . txt
# def create cumber.
# file(**params) :
# # меню выбора при измение в еріс
# options.=
# обновить не менять
# {params ("name file". feature', {params ["name file"]}.feature'
# soup
# BeautifulSoup(str (params["description"]), 'html parser')
# if params["all epic"] == True:
# description html = params ["description"]
# else:*
# description html = soup. find (params ["scenario _number"])
# # проверяем создат ли файл
# if os.path. isfile(f'{params ["name file"]}.feature'):
# print( \n) Такой
# уже есть
# f'{params ["name_file"]}. feature')
# file. = open( f' (params ["name_file"]}. feature')
# # записываем дату обновления
# file date = file readlines ()[21. replace("#", "*). replacel '\n',
# •11)
# updated at = params ["updated at"]
# # Сравниваем дату последнего обновления в локальном txt и epic gitlab
# if file date
# updated at:
# print(t'
# Еріс НЕ менялся')
# else:
# print(f
# Еріс именялся\п').
# # сравниваем локальный файл (txt) с еріс
# cache_file_ read = open(f'src/static/cache_feature/[params ["name_file"]}.txt', 'r')
# cache_text = f"""{cache_file_read.read()}"»™,
# epic_text = f"""{description html}".
# diff = difflib.ndiff(cache_text splitlines(), epic_text.splitlines())
# # показываем только изменения в
# epic
# print(f'
# Изменения в еріс
# changes
# • join(line for line in diff
# print (changes diff)
# if not line.startswith(* '))
# print(f.
# END
# \n')
# # вывод терминального меню
# terminal menu = TerminalMenu (options)
# menu_ entry index = terminal menu, show()
# else:
# # если согласились на изменения => обновлением . feature и записываем изменения в cache txt
# menu entry_index
# -=0.
# # cache еріс для фиксации изменений
# feature_cache_file(**params,
# # формирование текста
# description_html=description_html)
# create_cumber_text(**params)
# print(f'e
# Файл (params["name_file"]}. feature изменен
# # фиксируем изменения в .txt с датоай
# else:
# changes cache_file(**params, changes diff=changes diff.)
# perintef
# • Отмена обновлений-файла (params ["name_f1le"1), feature.











# else:
# если согласились на изменения = обновлением . feature и записываем изменения в cache
# if menu_ entry_index ==
# 0:
# # cache еріс для фиксации изменений
# feature_cache_file(**params, description_html=description_html)
# # формирование текста
# create
# cumber_text (**params)
# print(f'e
# Файл {params ["name_file"]}. feature изменен
# # фиксируем изменения в .txt с датоай
# else:
# changes_cache_file(**params, changes _diff=changes_diff)
# print(f
# OTMeHa OOHOBneHM Daina (parans [name fileNT) feature.
# # формирование текста
# create_cumber_text(**params)
# # nposepsen cospar onganncache
# changes
# if os path. isfile(f'src/static/cache_feature/(params ["name_
# print('\n) Такой
# file"］｝.txt'）：
# уже есть.
# else:
# f'src/static/cache_feature/(params ["name_file"l}. txt')
# # файла . feature нет, создаем
# feature _cache_file(**params, description_html=description_html)
# if params ['generator'] = True:
# generator (**params)
