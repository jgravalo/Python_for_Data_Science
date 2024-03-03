import sys
import ft_filter

def main():
	if len(sys.argv) != 3:
		print("AssertionError: the arguments are bad")
		exit()
	S = sys.argv[1].split()
	print(S)
	N = int(sys.argv[2])
	print(type(N).__name__)
	def isbig(x):
		if len(x) > N:
			return True
		return False
	newlist = []
	print("aqui")
	newlist = ft_filter(isbig, S)
	print(newlist)

if __name__ == "__main__":
	main()