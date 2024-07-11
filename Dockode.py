def print_maze(rows, columns):
    for i in range(rows * 2):
        if i % 2 == 0:
            for j in range(columns):
                if j == 0:
                    print(" ___ ", end="")
                else:
                    print("    ___ ", end="")
            print()
        else:
            for j in range(columns):
                print("/   \___", end="")
            print("/")
            for j in range(columns):
                print("\___/   ", end="")
            print("\\")

rows1, columns1 = 4, 7
print("Design for rows =", rows1, "and columns =", columns1)
print_maze(rows1, columns1)

print("\n")

rows2, columns2 = 3, 5
print("Design for rows =", rows2, "and columns =", columns2)
print_maze(rows2, columns2)
