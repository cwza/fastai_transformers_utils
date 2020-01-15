## Install nbdev and Clone nbdev_template
``` bash
pip3 install nbdev
git clone https://github.com/fastai/nbdev_template.git
mkdir nbs
mv 00_core.ipynb nbs
```

## Edit settings.ini
```
lib_name = fastai_transformers_utils
user = cwza
description = training huggingface transformers by fastai2
keywords = fastai2 transformers
author = cwza
author_email = cwz0205a@gmail.com
copyright = cwza

nbs_path = nbs
tst_flags = slow
```

## Edit setup.py
``` python
# requirements = cfg.get('requirements','').split()
setuptools.setup(
    # install_requires = requirements,
    install_requires=[
        'transformers @ git+https://github.com/huggingface/transformers.git',
        'fastai2', 'nbdev'
    ],
```


## Add Makefile
```
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
```

## Generate root package and Add git hooks for nb clean
``` bash
nbdev_build_lib
nbdev_install_git_hooks
```

## Add dependencies
Edit setup.py
``` python
setuptools.setup(
    install_requires=[
        'transformers @ git+https://github.com/huggingface/transformers.git',
        'fastai2', 'nbdev'
    ],
```

## Install
``` bash
make install
```

## Develop
1. Modify notebooks in nbs folder (Write unit tests in the same notebook and create new notebook to write integration test)
3. `make build-lib` to update python files
2. `make test` to run unit test
3. `make test-slow` to run integration test
3. `make build-all` to run build-lib, build-docs, clean-nbs
4. `git add commit and push`
