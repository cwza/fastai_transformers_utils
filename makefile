
edit-install:
	pip3 install -e .

edit-uninstall:
	python3 setup.py develop --uninstall

test:
	nbdev_test_nbs