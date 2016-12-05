def cound_diff(y_predict, y_test):
	calculations = {}
	calculations['negative'] = {'tp': 0, 'tn': 0, 'fp': 0, 'fn':0}
	calculations['positive'] = {'tp': 0, 'tn': 0, 'fp': 0, 'fn':0}	
	for predict, test in zip(y_predict, y_test):
		if predict == test:
			if test > 0:
				calculations['positive']['tp'] += 1
			else:
				calculations['negative']['tp'] += 1
		if predict != test:
			if test <= 0:
				if predict == 1:
					calculations['positive']['fp'] += 1
			
			if test >= 0:
				if predict == -1:
					calculations['negative']['fp'] += 1

			if test > 0:
				calculations['positive']['fn'] += 1
			elif test < 0:
				calculations['negative']['fn'] += 1

		if test != 1:
			if predict != 1:
				calculations['positive']['tn'] += 1

		if test != -1:
			if predict != -1:
				calculations['negative']['tn'] += 1

	return calculations

def precision(calculations):
	if calculations['positive']['tp'] + calculations['positive']['fp'] > 0:
		pos = 1.0 * calculations['positive']['tp']/(calculations['positive']['tp'] + calculations['positive']['fp'])
	else:
		pos = 0.0

	if calculations['negative']['tp'] + calculations['negative']['fp'] > 0:
		neg = 1.0 * calculations['negative']['tp']/(calculations['negative']['tp'] + calculations['negative']['fp'])
	else:
		neg = 0.0
		
	return {'positive': pos, 'negative': neg}

def recall(calculations):
	pos = 1.0 * calculations['positive']['tp']/(calculations['positive']['tp'] + calculations['positive']['fn'])
	neg = 1.0 * calculations['negative']['tp']/(calculations['negative']['tp'] + calculations['negative']['fn'])
	return {'positive': pos, 'negative': neg}

def f_score(calculations):
	_precision = precision(calculations)
	_recall = recall(calculations)
	if (_precision['positive'] + _recall['positive']) > 0:
		pos = 2.0 * ((_precision['positive'] * _recall['positive'])/(_precision['positive'] + _recall['positive']))
	else:
		pos = 0.0
	if (_precision['negative'] + _recall['negative']) > 0:
		neg = 2.0 * ((_precision['negative'] * _recall['negative'])/(_precision['negative'] + _recall['negative']))
	else:
		neg = 0.0
	return {'positive': pos, 'negative': neg}

def f_macro(calculations):
	f = f_score(calculations)
	return (f['positive'] + f['negative'])/2.0

