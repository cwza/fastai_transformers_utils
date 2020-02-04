
install:
	pip3 install -e .[dev]

uninstall:
	python3 setup.py develop --uninstall

test:
	nbdev_test_nbs --timing=true

test-slow:
	nbdev_test_nbs --flags=slow --timing=true

build-all:
	nbdev_build_lib
	rm -f ./docs/*.html
	nbdev_build_docs --force_all=true
	nbdev_trust_nbs
	nbdev_clean_nbs