# Grammar rules as a dictionary
grammar = {
  "E": ["TQ"],
  "Q": ["+TQ", "-TQ", "ε"],
  "T": ["FR"],
  "R": ["*FR", "/FR", "ε"],
  "F": ["(E)", "a"],
}

# Parsing table as a dictionary
parsing_table = {}

# Function to parse the input string
def parse(input_string):
    stack = ['$', "E"]
    input_string += '$'
    index = 0


# Test cases of 1, 2 and 3
test_cases = ["(a+a)*a$", "a*(a/a)$", "a(a+a)$"]

for test_case in test_cases:
    print(f"\nInput: {test_case}")
    if parse(test_case):
      print("String is accepted or valid.")
    else:
      print("strig is not accepted or valid.")