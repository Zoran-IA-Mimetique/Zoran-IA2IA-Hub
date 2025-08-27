test:
	pytest -q
lint:
	flake8 .
sec:
	bandit -r .
bench:
	python bench.py
load:
	python loadtest.py --messages 1000 --concurrency 200
