from bs4 import BeautifulSoup

# Наполняем данными файл
def create_cucumber_text(**params):

    with open(f'{params["name_file"]}.feature', 'w') as f:
        # url epic
        f.write(f'# {params["web_url"]}\n')
        # автор еріс
        f.write(f'# {params["author"]}\n')
        # дата последнего обновления
        f.write(f'# {params["updated_at"]}\n\n')
    # Feature
        f.write(f'Feature: {params["title"]}\n')
        # поиск по тегам
        soup_Fist = BeautifulSoup(str(params["description"]), 'html.parser')
        # переходим в нужное место в epic
        scenario_out = soup_Fist.find(params["scenario_number"])
        # Разбираем tag, которые используем
        tags = scenario_out.find_all(["background", "scenario", "scenariooutline", "given", "when", "then", "and", "but", "rule", "examples", "group", "groupin"])
        
        # Для проверки есть ли tag в группе
        group_tag = scenario_out.find("group")
        # Счетчик example
        counter_example = 0

        # Перебираем не нарушая порядок html
        for tag in tags:
            arr_examples = []

            soup = BeautifulSoup(str(tag), 'html.parser')    
        # Backaround
            if soup.find("background") and group_tag.find("background") == None: 
                f.write(f'\n    Background: {soup.find( "background").text}\n')
        # Scenario
            if soup.find("scenario") and group_tag.find("scenario") == None:
                f.write(f'\n    Scenario: {soup.find( "scenario").text}\n')            
        # Scenario Outline
            if soup.find("scenariooutline") and group_tag.find("scenariooutline") == None:
                f.write(f'\n    Scenario Outline: {soup.find("scenariooutline").text}\n')
        # Given
            if soup.find("given") and group_tag.find("given") == None:
                f.write(f'\n        Given {soup.find("given").text}\n')
        # When
            if soup.find("when") and group_tag.find("when") == None:
                f.write(f'\n        When {soup.find("when").text}\n')
        # Then
            if soup.find("then") and group_tag.find("then") == None:
                f.write(f'\n        Then {soup.find("then").text}\n')
        # And
            if soup.find("and") and group_tag.find("and") == None:
                f.write(f'\n            And {soup.find("and").text}\n')
        # But
            if soup.find("but") and group_tag.find("but") == None:
                f.write(f'\n            But {soup.find("but").text}\n')
        # Rule
            if soup.find("rule") and group_tag.find("rule") == None:
                f.write(f'\n            Rule {soup.find("rule").text}\n')

        # group (для работы с example)
            if soup.find("group"):
                group_exm_tag = soup.find("group")
                # Cкладываем в массив example
                for index, i_group_exm in enumerate(group_exm_tag):
                    groupexm_html = BeautifulSoup(str(i_group_exm), 'html.parser')
                    examples_tags = groupexm_html.find("examples")
                    if examples_tags is not None:
                        arr_examples.append(examples_tags.text)
                # Ищем место вставки example в tag (groupin)
                if soup.find(["background", "scenario", "scenariooutline", "given", "when", "then", "and", "but", "rule"]):
                    # TODO !!! (сделать для всех tag)
                    f.write(f'\n        Then {soup.find("then").text} ')
                    if soup.find("groupin"):
                        for index, i_arr in enumerate(arr_examples):
                            # Счетчик
                            counter_example += 1
                            # Создаем перменую для списка с номером
                            f.write(f'"<col_{counter_example}>"')
                            if index <= len(arr_examples)-2:
                                f.write(f', ')
                    f.write(f'\n ')
                    
        # В конце добавляем Examples
        f.write(f'\n            Examples: ')

        counter_example = 0
        tags_ex = scenario_out.find_all("examples")

        # Создаем переменные и добавляем номера
        for tag in tags_ex:
            soup = BeautifulSoup(str(tag), 'html.parser')

            if soup.find ("examples"):
                counter_example += 1
                f.write(f'col_{counter_example}')
                if counter_example <= len(tags_ex)-1:
                    f.write(f', ')
                    
        counter_example = 0
        # Создаем переменные и добавляем номера для таблицы
        f.write(f'\n                ')
        for tag in tags_ex:
            soup = BeautifulSoup(str(tag), 'html.parser')

            if soup.find("examples"):
                counter_example += 1
                f.write(f'| col_{counter_example} ')
                if counter_example > len(tags_ex)-1:
                    f.write(f'|')

        counter_example = 0
        # Записываем, значения полученные из еріс в, таблицу
        f.write(f'\n                ')
        for tag in tags_ex:
            soup = BeautifulSoup(str(tag), 'html.parser')

            if soup.find("examples"):
                counter_example += 1
                f.write(f'| {soup.find("examples").text} ') 
                if counter_example > len(tags_ex)-1:
                    f.write(f'|')
        
        print('\n Создаем новый', f'{params["name_file"]}.feature')