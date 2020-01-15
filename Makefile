
install:
	pip3 install -e .

uninstall:
	python3 setup.py develop --uninstall

test:
	nbdev_test_nbs

test-slow:
	nbdev_test_nbs --flags=slow

build-all:	build-lib build-docs
	nbdev_clean_nbs
	
build-lib:
	nbdev_build_lib

build-docs:
	nbdev_build_docs