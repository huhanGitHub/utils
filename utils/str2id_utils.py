from utils.tokenization import convert_tokens_to_ids

def buildDicFromVocab(path):
    try:
        f = open(path, encoding='UTF-8')
        word_dict = dict()
        list= f.readlines()
        for i in range(len(list)):
            list[i] = list[i].replace('\n', '')
            word_dict[i] = list[i]
        reversed_dict = dict(zip(word_dict.values(), word_dict.keys()))
        return reversed_dict, word_dict

    except IOError:
        print(path+"not found")

def str2id(vocab, path):
    try:
        f = open(path, encoding='UTF-8')
        output = []
        list= f.readlines()
        for i in range(len(list)):
            list[i] = list[i].replace('\n', '')
            list[i] = list[i].split(' ')
            output.append(convert_tokens_to_ids(vocab, list[i]))
        return output

    except IOError:
        print(path+"not found")

"""
surpose delimiter is '|'
'a b c | A B C' 
'aa bb cc | AA BB CC'
--> 
[[a b c][A B C]]
[[aa bb cc][AA BB CC]]
"""
def str2id_delimiter(vocab, path, delimiter):
    try:
        f = open(path, encoding='UTF-8')
        output = []
        list= f.readlines()
        for i in range(len(list)):
            list[i] = list[i].replace('\n', '')
            l = list[i].split(delimiter)
            line = []
            for ii in l:
                ii = ii.strip()
                ii = ii.split(' ')
                line.append(convert_tokens_to_ids(vocab, ii))
            output.append(line)
        return output

    except IOError:
        print(path+"not found")