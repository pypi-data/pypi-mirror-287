import sys
import os
sys.path.append('..')
from dotenv import load_dotenv, find_dotenv

from generator_cucumber.generator import Generator

load_dotenv(find_dotenv())
URL_GIT = os.environ.get('URL_GIT')
PRIVATE_TOKEN_GIT = os.environ.get('PRIVATE_TOKEN_GIT')

Generator.URL_GIT = URL_GIT
Generator.PRIVATE_TOKEN_GIT = PRIVATE_TOKEN_GIT

Generator.create_cucumber(
    project_id='59216833',
    issue_iid=1,
    name_file='test_generator',
    scenario_number='src-1-1'
)