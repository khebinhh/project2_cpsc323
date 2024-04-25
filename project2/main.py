# Grammar rules as a dictionary
grammar = {
  "E": ["TQ"],
  "Q": ["+TQ", "-TQ", "ε"],
  "T": ["FR"],
  "R": ["*FR", "/FR", "ε"],
  "F": ["(E)", "a"],
}

# Parsing table as a dictionary
parsing_table = {
  ("E", "a"): "TQ",
  
}

# Function to parse the input string
def parse(input_string):
    stack = ['$', "E"]
    input_string += '$'
    index = 0

    while len(stack) > 0:
      top = stack.pop()
      current_symbol = input_string[index]
  
      print(f"Stack: {stack}")
  
      if top == current_symbol:
        index += 1
      elif top in grammar:
        production = parsing_table.get((top, current_symbol))
        if production:
          stack.extend(reversed(production))
        else:
          return False
      else:
        return False
  
    return True


# Test cases of 1, 2 and 3
test_cases = ["(a+a)*a$", "a*(a/a)$", "a(a+a)$"]

for test_case in test_cases:
    print(f"\nInput: {test_case}")
    if parse(test_case):
      print("String is accepted or valid.")
    else:
      print("String is not accepted or invalid.")