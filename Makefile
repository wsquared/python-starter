init:
	pipenv install

test:
	pipenv run pytest

test-watch:
	pipenv run ptw

coverage-run:
	coverage run -m pytest

coverage-report:
	coverage report
