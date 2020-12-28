import pandas as pd

result = pd.read_csv("E:\GitHub\AdventOfCode\Day1 - input.txt", sep="\s+", header=None, names = ["Value"])


value1 = 0
value2 = 0
value3 = 0

# Two numbers that added sum up 2020
for i in range(0, len(result) - 2):
    if i <= len(result) - 2:
        for j in range (i + 1, len(result) - 1):
            if result.values[i] + result.values[j] == 2020:
                value1 = result.values[i]
                value2 = result.values[j]

print(value1)
print(value2)

# Three numbers that added sum up 2020
for i in range(0, len(result) - 3):
    if i <= len(result) - 3:
        for j in range (i + 1, len(result) - 2):
            if j <= len(result) - 2:
                for k in range (i + 2, len(result) - 1):
                    if result.values[i] + result.values[j] + result.values[k] == 2020:
                        value1 = result.values[i]
                        value2 = result.values[j]
                        value3 = result.values[k]

print(value1)
print(value2)
print(value3)