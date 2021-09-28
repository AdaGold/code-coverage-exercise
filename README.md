# Code Coverage Exercise #

In this exercise you will work with your group to get to full code coverage and fix any bugs that you find.

## Setup
1. Clone a copy of this exercise. This command makes a new folder called `code-coverage-exercise`, and then puts the exercise into this new folder. You do not need to fork the repository.

```bash
$ git clone ...
```

Use `ls` to confirm there's a new project folder

2. Move your location into this project folder

```bash
$ cd code-coverage-exercise
```

3. Create a virtual environment named `venv` for this project:

```bash
$ python3 -m venv venv
```

4. Activate this environment:

```bash
$ source venv/bin/activate
```

Verify that you're in a python3 virtual environment by running:

- `$ python --version` should output a Python 3 version
- `$ pip --version` should output that it is working with Python 3

5. Install dependencies once at the beginning of this exercise with

```bash
# Must be in activated virtual environment
$ pip install -r requirements.txt
```

6. Exit and re-enter the virtual enviornment with the following command. This is needed to ensure the correct version of pytest is used in the terminal.

```bash
$ deactivate && source venv/bin/activate
```

## Checking Code Coverage

To check the code coverage you can run:
```
pytest --cov=student --cov-report html --cov-report term
```

To see the detailed report (after running the above) you can open it in your default browser with:

```
open htmlcov/index.html
```

The above commands need to be run from the root folder of the project.

Once you've loaded the detailed report you can click on the file names to see information about what lines are missing code coverage.

To read more about pytest-cov you can consult the [pytest-cov documentation](https://pytest-cov.readthedocs.io/en/latest/).
