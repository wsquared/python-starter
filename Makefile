init:
	pip install -r requirements.txt

test:
	pipenv run pytest

test-watch:
	pipenv run ptw

coverage-run:
	coverage run -m pytest

coverage-report:
	coverage report
