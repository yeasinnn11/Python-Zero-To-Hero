# nested loop = The "inner loop" will finish all of it's iteration's before
#               finishing one iteration of the "outer loop"

rows = int(input("Enter the rows: "))
columns = int(input("Enter the columns: "))
symbol = input("Enter the symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()