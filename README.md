# school-management

> At first clone the repository command blew
```commandline
git clone https://github.com/mohammadanarul/school-management.git
cd school-management
```

> project file structure
- school-management
  - apps `app list blew`
    - users `django app`
    - helpers
    - institutes
  - core `project name`
  - requirements.txt `project using all package listed in file`
  - srs.md

> Django Project Environment Setup and run in `macbook and linux`
```commandline
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

> Django Project Environment Setup and run in `windows`
```commandline
python -m venv venv
/venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

> pytest and pytest-cov command
```commandline
pytest or pytest -rP
pytest --cov
```
> single test file run command bleow
```
pytest apps/app_name/tests/test_file_name.py -rP
```

> single function test run command bleow
```
pytest apps/app_name/tests/test_file_name.py::TestClassName::test_function_name -rP
```

> pytest-code coverage html report command
```
pytest --cov --cov-report=html:htmlcov
```