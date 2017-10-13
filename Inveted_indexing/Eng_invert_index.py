import os
from nltk.corpus import stopwords
import nltk
import json
from nltk.stem.porter import *
import collections
stop_words = list(stopwords.words('english'))
stemmer = PorterStemmer()

def make_index(name_folder):
	name_files = os.listdir(name_folder)
	inverted_index = {}
	for file in name_files:
		with open(os.path.join(name_folder,file)) as current_file:
			text =  current_file.read()
			words = nltk.word_tokenize(text)
			words = [stemmer.stem(word.lower()) for word in words if word not in stop_words]
			words_freq_dict = dict(collections.Counter(words))
			for unique_word in words_freq_dict.keys():
				if str(unique_word) in inverted_index:
					inverted_index[str(unique_word)].append((file,words_freq_dict[unique_word]))
				else:
					inverted_index[str(unique_word)] = []
					inverted_index[str(unique_word)].append((file,words_freq_dict[unique_word]))
	with open('inverted_index.json','w') as inverted_file:
		inverted_file.write(json.dumps(inverted_index))


if __name__ == '__main__':
	make_index('corp')