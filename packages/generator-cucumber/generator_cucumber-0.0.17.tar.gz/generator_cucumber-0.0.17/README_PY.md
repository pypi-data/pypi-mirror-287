Cucmber generator
------------

.. image:: https://gitlab.com/python_lib/generator_cucumber/-/raw/main/images/InnoLab.png?ref_type=heads
   :target: https://bdd-generator.readthedocs.io/ru/latest/usage.html
   :align: center
   :height: 200
   :alt: Innovation lab


------

.. image:: https://img.shields.io/pypi/v/pytest.svg
    :target: https://pypi.org/project/generator-cucumber/

Installation
------------

As of 0.0.17, ``generator-cucumber`` is compatible with Python 3.8.

Use ``pip`` to install the latest stable version of ``generator-cucumber``:

.. code-block:: console

   $ pip install --upgrade generator-cucumber


Structure
------------
```
# Проект по генерации .feature
├── 📁 generator_cucumber/
|   ├── 🐍 api_github.py        # для работы с github (не реализован)
|   ├── 🐍 api_gitlab.py        # Для работы с gitlab
|   ├── 🐍 bdd_generator.py     # Для работы с py и подготовка шаблона по cucmber
|   ├── 🐍 cache_file.py        # создание файлов cache
|   ├── 🐍 create_file.py       # Обработка файлов cache и .feature
|   ├── 🐍 cucumber_text.py     # Формирование .feature текст
|   └── 🐍 generator.py         # входная точка
└── ... 
```