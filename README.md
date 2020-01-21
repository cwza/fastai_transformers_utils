# fastai_transformers_utils
> Some utililties to help you using fastai2 to train huggingface transformers.


## Install

``` bash
pip3 install git+https://github.com/cwza/fastai_transformers_utils.git
```

## How to use

Please see the notebooks that named start with example and under nbs directory.

## How to develop

### Editable install

``` bash
git clone https://github.com/cwza/fastai_transformers_utils
cd fastai_transformers_utils
make install
```

### Develop pipeline

1. Modify notebooks in nbs folder (Write unit tests in the same notebook and create new notebook to write integration test)
3. `make build-lib` to update python files
2. `make test` to run unit test
3. `make test-slow` to run integration test
3. `make build-all` to run build-lib, build-docs, clean-nbs
4. `git add commit and push`
