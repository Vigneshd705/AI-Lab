# Cryptarithmetic Solver for SEND + MORE = MONEY

# Define the words in the puzzle
WORD1 = "SEND"
WORD2 = "MORE"
RESULT = "MONEY"

# List of unique letters
LETTERS = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']

# Total number of unique letters
NUM_LETTERS = len(LETTERS)

# Function to convert a word to its numerical representation based on the current mapping
def to_number(word, mapping):
    number = 0
    for letter in word:
        number = number * 10 + mapping[letter]
    return number

# Backtracking function to assign digits to letters
def solve(mapping, used_digits, index):
    # If all letters have been assigned
    if index == NUM_LETTERS:
        # Convert words to numbers
        send = to_number(WORD1, mapping)
        more = to_number(WORD2, mapping)
        money = to_number(RESULT, mapping)
        
        # Check if the equation holds
        if send + more == money:
            # Print the solution
            print("Solution Found:")
            for letter in LETTERS:
                print(f"{letter} = {mapping[letter]}")
            print(f"\n{WORD1} + {WORD2} = {RESULT}")
            print(f"{send} + {more} = {money}")
            print("-" * 20)
        return
    
    # Get the current letter to assign
    current_letter = LETTERS[index]
    
    # Try all possible digits for the current letter
    for digit in range(10):
        # Skip if the digit is already used
        if used_digits[digit]:
            continue
        
        # Leading letters cannot be zero
        if (current_letter == 'S' or current_letter == 'M') and digit == 0:
            continue
        
        # Assign the digit to the current letter
        mapping[current_letter] = digit
        used_digits[digit] = True
        
        # Recursive call to assign the next letter
        solve(mapping, used_digits, index + 1)
        
        # Backtrack: Unassign the digit
        mapping[current_letter] = None
        used_digits[digit] = False

# Main function to initiate the solving process
def main():
    # Initialize the mapping of letters to digits
    mapping = {}
    for letter in LETTERS:
        mapping[letter] = None
    
    # Initialize a list to keep track of used digits
    used_digits = [False] * 10
    
    # Start solving from the first letter
    solve(mapping, used_digits, 0)

# Entry point of the program
if __name__ == "__main__":
    main()
