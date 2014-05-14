def incr_dict(dct,tpl):
	if type(dct) is not dict:
		raise TypeError("First argument needs to be a dict.")
	elif type(tpl) is not tuple:
		raise TypeError("Second argument needs to be a tuple.")
	if len(tpl) > 1:
		if not dct.has_key(tpl[0]):
			dct[tpl[0]] = {}
		elif type(dct[tpl[0]]) is int:
			dct[tpl[0]] = {}
		incr_dict(dct[tpl[0]],tpl[1:])
	else:
		if dct.has_key(tpl[0]):
			if type(dct[tpl[0]]) is not int:
				dct[tpl[0]] = 1
				return dct
			dct[tpl[0]] += 1
		else:
			dct[tpl[0]] = 1
		return dct