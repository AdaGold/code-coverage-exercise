# Code Coverage Exercise #

In this exercise you will work with your group to get to full code coverage and fix any bugs that you find.

You will need to clone this project and do your normal Python environment setup (`venv`, instaling packages, etc).

To check the code coverage you can run:
```
pytest --cov=student --cov-report html
```

To see the detailed report (after running the above) you can open it in your default browser with:

```
open htmlcov/index.html
```

The above commands need to be run from the root folder of the project.

Once you've loaded the detailed report you can click on the file names to see information about what lines are missing code coverage.

To read more about pytest-cov you can consult the [pytest-cov documentation](https://pytest-cov.readthedocs.io/en/latest/).
