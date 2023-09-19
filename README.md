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
```

> Django Project Environment Setup and run in `windows`
```commandline
python -m venv venv
/venv/bin/activate
pip install -r requirements.txt
```

> pytest and pytest-cov command
```commandline
pytest
pytest --cov
```