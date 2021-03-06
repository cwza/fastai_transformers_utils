# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/02_transforms.ipynb (unless otherwise specified).

__all__ = ['TransformersNumericalize', 'Pad2Max']

# Cell
#export
from fastcore.all import *
from fastai2.basics import *
from fastai2.text.all import *

from transformers import PreTrainedTokenizer, AutoTokenizer

# Cell
class TransformersNumericalize(Transform):
    def __init__(self, tokenizer: PreTrainedTokenizer):
        self.tokenizer = tokenizer
    def encodes(self, o):
        ''' o: list of string token, returns: tensored list of int token '''
        return TensorText(
            self.tokenizer.build_inputs_with_special_tokens(
                self.tokenizer.convert_tokens_to_ids(o)
            )
        )
    def decodes(self, o):
        return TitledStr(self.tokenizer.decode(list(o)))

# Cell
class Pad2Max(Transform):
    ''' pad rank one tensor by pad_idx to max_len, if original len is larger than max_len, truncate it
    '''
    def __init__(self, max_len, pad_idx):
        self.max_len = max_len
        self.pad_idx = pad_idx
    def encodes(self, o):
        ori_len = len(o)
        result = o
        if ori_len > self.max_len:
            result = o[:self.max_len]
        elif ori_len < self.max_len:
            result = nn.functional.pad(o, [0, self.max_len-ori_len], value=self.pad_idx)
        assert len(result) == self.max_len, f'len(o): {len(o)}, max_len: {self.max_len}'
        return result
    def decodes(self, o):
        return TensorText([v for v in o if v != self.pad_idx])