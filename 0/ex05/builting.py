import sys

def main():
	if len(sys.argv) > 2:
		print("AssertionError: Too much arguments")
		exit()
	elif len(sys.argv) < 2:
		print("What is the text to count?")
		text = input()
	else:
		text = sys.argv[1]
	characters = 0
	upper = 0
	lower = 0
	marks = 0
	spaces = 0
	digits = 0
	for x in text:
		characters += 1
		if x >= 'A' and x <= 'Z':
			upper += 1
		if x >= 'a' and x <= 'z':
			lower += 1
		if x >= '0' and x <= '9':
			digits += 1
		if x == '.' or x == ',' or x == ':' or x == ';' \
			or x == '-' or x == '!' or x == '?':
			marks += 1
		if x == ' ':
			spaces += 1
	print("The text contains", characters, "characters")
	print(upper, "upper letters")
	print(lower, "lower letters")
	print(marks, "punctuation marks")
	print(spaces, "spaces")
	print(digits, "digits")

if __name__ == "__main__":
	main()
