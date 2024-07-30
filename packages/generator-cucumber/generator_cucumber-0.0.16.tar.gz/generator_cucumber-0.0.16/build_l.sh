# del old build
rm -rf build
rm -rf dist
rm -rf generator_cucumber.egg-info
# setuptools
python3.8 -m pip install setuptools
# twine
python3.8 -m pip install twine
# error: invalid command 'bdist_wheel'
python3.8 -m pip install wheel
# generate file for public
python3.8 setup.py sdist bdist_wheel
# public on https://pypi.org
twine upload --repository pypi dist/*