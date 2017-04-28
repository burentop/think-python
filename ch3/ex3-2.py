def do_twice(f, value):
	f(value)
	f(value)

def print_spam(toPrint):
	print(toPrint)

def print_twice(toPrint):
	print(toPrint)
	print(toPrint)

def do_four(f, value):
	do_twice(f, value)
	do_twice(f, value)

do_four(print_twice, "spam")
