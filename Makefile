test:
	pytest -q
lint:
	flake8 .
sec:
	bandit -r .
bench:
	python benchmark/IA2IA_bench.py
load:
	python loadtest.py --messages 1000 --concurrency 200
