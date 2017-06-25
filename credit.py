def credit():
	
	import sys

	user_input_prompt = "Your credit card number: "
	amex_valid_start = ('34', '37')
	master_valid_start = ('51', '52', '53', '54', '55')
	visa_valid_start = ('4',)
	
	# Condition 1: Valid positive number starting with right 
	while True:
		try:
			credit_num = long(raw_input(user_input_prompt))
			if credit_num < 0:
				print "That's a negative number, provide proper input: "
				continue
			break
		except ValueError:
			print "Oops! That's not a valid input. Try again!"

	# Condition 2: Valid credit card start and corresponding length
	if str(credit_num).startswith(amex_valid_start) and len(str(credit_num)) == 15:
		pass
	elif str(credit_num).startswith(master_valid_start) and len(str(credit_num)) == 16:
		pass
	elif str(credit_num).startswith(visa_valid_start) and (len(str(credit_num)) == 13 or len(str(credit_num)) == 16):
		pass
	else:
		print "INVALID"

	# Condition 3: Satisfy Luhn's algorithm

	
	x = []
	for i in range(0, len(str(credit_num))):
		if i % 2 == 1:
			x.append(int(str(credit_num)[i]) * 2)
			
	# the longer way
	'''y = []
	for j in x:
		k = 0
		for l in range(0, len(str(j))):
			y.append(int(str(j)[k]))
			k += 1

	z = []
	for i in range(0, len(str(credit_num))):
		if i % 2 == 0:
			z.append(int(str(credit_num)[i]))
	print sum(z)'''
	
	the_even_sum = sum(int(char) for n in x for char in str(n))
	the_odd_sum = sum(int(char) for i, char in enumerate(str(credit_num)) if i % 2 == 0)
	
	total_sum = the_odd_sum+the_even_sum

	if total_sum % 10 == 0 and str(credit_num).startswith(amex_valid_start):
		print "AMEX"
	elif total_sum % 10 == 0 and str(credit_num).startswith(master_valid_start):
		print "MASTERCARD"
	elif total_sum % 10 == 0 and str(credit_num).startswith(master_valid_start):
		print "VISA"
	else:
		print "INVALID"
	


credit()
