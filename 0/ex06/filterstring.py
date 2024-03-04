from ft_filter import ft_filter
import sys

def parse_arg(argv):
	for x in argv:
		if not (x >= 'a' and x <= 'x') and \
		not (x >= 'A' and x <= 'X') and \
		not (x >= '0' and x <= '9') and \
			x != ' ' :
#			print(x)
			error()

def error():
	print("AssertionError: the arguments are bad")
	exit()

def main():
	if len(sys.argv) != 3:
		error()
	parse_arg(sys.argv[1])
	S = sys.argv[1].split()
#	print(S)
	if (sys.argv[2].isdigit() == False):
		error()
	N = int(sys.argv[2])
#	print(type(N).__name__)
	def isbig(x):
		if len(x) > N:
			return True
		return False
	newlist = list(ft_filter(isbig, S))
	newlist2 = list(filter(isbig, S))
	print(newlist)
	print(newlist2)

if __name__ == "__main__":
	main()