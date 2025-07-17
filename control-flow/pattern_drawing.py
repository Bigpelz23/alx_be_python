# pattern_drawing.py

# Prompt user for pattern size
size = input("Enter the size of the pattern: ")

# Validate that the input is a positive integer
if not size.isdigit() or int(size) <= 0:
    print("Please enter a valid positive integer.")
else:
    size = int(size)
    row = 0

    # Outer loop using while
    while row < size:
        # Inner loop using for to print stars in a row
        for col in range(size):
            print("*", end="")  # Stay on the same line
        print()  # Move to the next line after each row
        row += 1
