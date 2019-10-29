from utils.str2id_utils import *

path = '../data/test.s2s.txt'
vocab_path = '../vocab.txt'

word_dict, reversed_dict = buildDicFromVocab(vocab_path)
output = str2id_delimiter(word_dict, path, '|||')
print(output)
