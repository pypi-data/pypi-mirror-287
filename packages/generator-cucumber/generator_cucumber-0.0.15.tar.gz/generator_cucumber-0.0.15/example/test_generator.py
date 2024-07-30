import sys
import os
sys.path.append('..')
from dotenv import load_dotenv, find_dotenv

from generator_cucumber.api_gitlab import Gitlab_api

load_dotenv(find_dotenv())
URL_GIT = os.environ.get('URL_GIT')
PRIVATE_TOKEN_GIT = os.environ.get('PRIVATE_TOKEN_GIT')

Gitlab_api.URL_GIT = URL_GIT
Gitlab_api.PRIVATE_TOKEN_GIT = PRIVATE_TOKEN_GIT

Gitlab_api.create_cucumber(
    project_id='59216833',
    issue_iid=1,
    name_file='test_generator',
    scenario_number='src-1-1'
)