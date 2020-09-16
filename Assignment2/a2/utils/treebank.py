import pickle
import numpy as np
import os
import random

class StanfordSentiment:
	def __init__(self, path=None, tablesize=1000000):
		if not path:
			path = 'utils/datasets/stanfordSentimentTreebank'

		self.path = path
		self.tablesize = tablesize

	def tokens(self):
		if hasattr(self, "_tokens") and self._tokens:
			return self._tokens

		tokens = dict()
		tokenfreq = dict()
		wordcount = 0
		revtokens = []
		idx = 0

		for sentence in self.sentences():
			for w in sentence:
				wordcount += 1
				if not w in tokens:
					tokens[w] = idx
					revtokens += [w]
					tokenfreq[w] = 1
					idx += 1
				else:
					tokenfreq[w] += 1

		tokens['UNK'] = idx
		revtokens += ['UNK']
		tokenfreq['UNK'] = 1
		wordcount
