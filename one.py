#one.py 

def one_func():
	print("one_func in one.py")

print("top level in one.py")

if __name__ == '__main__':
	print('one.py is being run directly')
else:
	print('one.py has been imported')
