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
   ("E", "("): ["TQ"],
   ("Q", "+"): ["+TQ"],
   ("Q", "-"): ["-TQ"],
   ("Q", ")"): ["ε"],
   ("Q", "$"): ["ε"],
   ("T", "a"): ["FR"],
   ("T", "("): ["FR"],
   ("R", "+"): ["ε"],
   ("R", "-"): ["ε"],
   ("R", "*"): ["*FR"],   
   ("R", "/"): ["/FR"],
   ("R", ")"): ["ε"],
   ("R", "$"): ["ε"],
   ("F", "a"): ["a"],
   ("F", "("): ["(E)"]
        }

# Function to parse the input string
def parse(input_string):
    stack = ['$', "E"]
    #input_string += '$'
    index = 0

    print(f"Input: {input_string}")
    while len(stack) > 0 and index < len(input_string):
      top = stack.pop()
      current_symbol = input_string[index]
  
      print(f"Stack: {stack}")
  
      if top == current_symbol:
        index += 1
      elif top in grammar:
        production = parsing_table.get((top, current_symbol), None)
        if production:
          if production != "ε":  # Don't push epsilon onto stack
            stack.extend(reversed(list(production))) # Convert production into list
        else:
          print("String is not accepted or invalid.")
          return False
      else:
        print("String is not accepted or invalid.")
        return False

    if len(stack) == 0 and index == len(input_string):
      print("String is accepted or valid.")
    else:
      print("String is not accepted or invalid.")

# Test cases of 1, 2 and 3
test_cases = ["(a+a)*a$", "a*(a/a)$", "a(a+a)$"]

for test_case in test_cases:
    parse(test_case)
