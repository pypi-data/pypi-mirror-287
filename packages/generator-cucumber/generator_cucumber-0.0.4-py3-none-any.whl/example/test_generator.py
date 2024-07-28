import sys
import os
sys.path.append('..')
from dotenv import load_dotenv, find_dotenv

from generator_cucumber.api_gitlab import Gitlab_api

load_dotenv(find_dotenv())
URL_GITLAB = os.environ.get('URL_GITLAB')
PRIVATE_TOKEN_GITLAB = os.environ.get('PRIVATE_TOKEN_GITLAB')

Gitlab_api.URL_GITLAB = URL_GITLAB
Gitlab_api.PRIVATE_TOKEN_GITLAB = PRIVATE_TOKEN_GITLAB

Gitlab_api.create_cumber(
    project_id='59216833',
    issue_iid=1,
    name_file='test_generator',
    scenario_number='scr-1-1'
)
