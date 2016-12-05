from nltk import ngrams

def get_ngrams(sentence, n=2, is_join=False):
	ngrams_generator = ngrams(list(sentence), n)
	ngrams_list = []
	for i in ngrams_generator:
		ngrams_list.append(''.join(list(i)))

	if is_join:
		return ' '.join(ngrams_list)
	return ngrams_list
