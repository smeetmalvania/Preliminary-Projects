import itertools

def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

def crack():

	import sys
	import crypt
	import itertools

	if len(sys.argv) <> 2:
		print "Usage: python crack.py hash"
		sys.exit()

	hash_input = sys.argv[1]

	char_list = []
	for i in itertools.chain(range(65, 65+26), range(97, 97+26)):
		char_list.append(chr(i))

	charset = ''.join(char_list)
	
	checklist = list(bruteforce(charset, 4))

	for j, val in enumerate(checklist):
		if crypt.crypt(val, '50') == hash_input:
			print "Your password is %s" % val
			sys.exit()
	
	print "No hash found"

crack()

