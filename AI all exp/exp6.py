from itertools import permutations

def solve_cryptarithmetic(equation):
    letters = set(c for c in equation if c.isalpha())
    if len(letters) > 10:
        return "Too many unique letters for a single-digit solution."
    if '=' not in equation:
        return "The equation must contain an '=' sign."

    left_side, right_side = equation.split('=')
    left_side = left_side.strip()
    right_side = right_side.strip()
    for perm in permutations(range(10), len(letters)):
        letter_to_digit = dict(zip(letters, perm))
       
        def replace_letters(expression, mapping):
            return ''.join(str(mapping.get(c, c)) for c in expression)

        try:
            left_value = replace_letters(left_side, letter_to_digit)
            right_value = replace_letters(right_side, letter_to_digit)

            left_eval = sum(int(replace_letters(part, letter_to_digit)) for part in left_value.split('+'))
            right_eval = int(right_value)
            
            def has_leading_zero(s):
                return s[0] == '0' and len(s) > 1

            if all(not has_leading_zero(part) for part in left_value.split('+') + [right_value]):
                if left_eval == right_eval:
                    return letter_to_digit
        except Exception as e:
            continue
   
    return "No solution found."

print("Enter your cryptarithmetic problem (e.g., SEND + MORE = MONEY):")
equation = input().strip()
solution = solve_cryptarithmetic(equation)
if isinstance(solution, dict):
    print("Solution found:")
    for letter, digit in sorted(solution.items()):
        print(f"{letter} = {digit}")
else:
    print(solution)
