
install:
	pip3 install -e .

uninstall:
	python3 setup.py develop --uninstall

test:
	nbdev_test_nbs --timing=true

test-slow:
	nbdev_test_nbs --flags=slow --timing=true

build-all:
	nbdev_build_lib
	nbdev_build_docs --force_all=true
	nbdev_clean_nbs
	nbdev_trust_nbs