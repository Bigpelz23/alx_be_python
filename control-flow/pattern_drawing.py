def draw_pattern():
    try:
        size = int(input("Enter the size of the pattern: "))
        if size <= 0:
            print("Please enter a valid positive integer.")
            return
    except ValueError:
        print("Please enter a valid positive integer.")
        return

    row = 0
    while row < size:
        for col in range(size):
            print("*", end="")
        print()
        row += 1

if __name__ == "__main__":
    draw_pattern()
