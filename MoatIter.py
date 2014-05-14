def incr_dict(dct,tpl):
	def createdict(tplin):
		if len(tplin) == 0:
			return 1
		out = {tplin[-1]:1}
		for i in xrange(len(tplin)-2,-1,-1):
			out = {tplin[i]:out}
		return out
	if type(dct) is not dict:
		raise TypeError("First argument needs to be a dict.")
	elif type(tpl) is not tuple:
		raise TypeError("Second argument needs to be a tuple.")
	a=0
	cur = dct
	c = 0
	dictlist = []
	if not dct.has_key(tpl[0]):
		dct[tpl[0]] = createdict(tpl[1:])
		return dct
	while c < len(tpl):
		if type(cur) is int:
			dictlist.append(createdict(tpl[c:]))
			break
		if c == len(tpl)-1 and cur.has_key(tpl[c]):
			a=1
			if type(cur[tpl[c]]) is not int:
				a=2
				cur[tpl[c]] = 1
				dictlist.append(cur)
				dct[tpl[0]] = dictlist[1]
				return dct
			cur[tpl[c]] += 1
			dictlist.append(cur)
			dct[tpl[0]] = dictlist[1]
			return dct
		dictlist.append(cur)
		if cur.has_key(tpl[c]):
			cur = cur[tpl[c]]
			c += 1
			continue
		else:
			cur[tpl[c]] = createdict(tpl[c+1:])
			dictlist.append(cur)
			break
	output = dictlist[-1]
	for key,value in dictlist[c].iteritems():
		output[key] = value
	for i in xrange(c-1,0,-1):
		dictlist[i][tpl[i]] = output
		output = dictlist[i]
	dct[tpl[0]] = output
	return dct