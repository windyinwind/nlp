import os
from gensim.models import KeyedVectors
from gensim.test.utils import datapath
import random
import re


base_dir = os.getcwd()


model_path = datapath(base_dir + '/wiki-news-300d-1M-subword.vec')
model = KeyedVectors.load_word2vec_format(model_path, limit=50000)

model.most_similar('see')

# example sentence 
sentence = "There are some , pigeons in the park."

# tokenize
sentence = ' '.join(re.findall(r'\w+', sentence))
sens = sentence.split(" ")
repeater_say = []
for s in sens:
    rs = model.most_similar(s)
    cr = random.choice(rs)
    word = cr[0]
    repeater_say.append(word)
text = ' '.join(repeater_say)







