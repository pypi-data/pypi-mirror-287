def feature_cache_file(**params):
    with open(f'__featurecache__/feature_cashe/{params["name_file"]}.txt', 'w') as cache_file:
        cache_file.writelines(f'{params["description_html"]}')
        print ('\n Создаем новый', f'__featurecache__/feature_cashe/{params["name_file"]}.txt')
        
def changes_cache_file(**params):
    with open(f'__featurecache__/feature_cashe_changes/changes_{params["name_file"]}.txt', 'a')as cache_file_changes:
        cache_file_changes.write(f'\n********')
        cache_file_changes.write(f'{params["updated_at"]}\n\n')
        cache_file_changes.writelines(params["changes_diff"])