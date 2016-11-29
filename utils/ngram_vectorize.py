from nltk import ngrams

def get_ngrams(sentence, n=2):
	ngrams_generator = ngrams(list(sentence), n)
	ngrams_list = []
	for i in ngrams_generator:
		ngrams_list.append(''.join(list(i)))

	print get_ngrams