def caesar():

	import sys
	
	if len(sys.argv) <> 2:
		print "Usage: python caesar.py k"
		sys.exit()

	k = int(sys.argv[1])

	while True:
		try:
			plain_text = raw_input("Plain text: ")
			if isinstance(plain_text, str):
				break
			continue
		except ValueError:
			print "Oops! Please enter a string."
			continue

	list_plain_text = list(plain_text)
	char_to_move = k % 26
	list_cipher_text = []
	
	for i in list_plain_text:
		if i.isupper():
			j = chr(65 + ((ord(i) - 65 + char_to_move) % 26))
			list_cipher_text.append(j)
		elif i.islower():
			j = chr(97 + ((ord(i) - 97 + char_to_move) % 26))
			list_cipher_text.append(j)
		else:
			list_cipher_text.append(i)

	cipher_text = ''.join(list_cipher_text)

	print "Cipher Text: %s" % cipher_text

caesar()