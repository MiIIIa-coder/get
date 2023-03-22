#!/bin/python3
import sys
import csv

data = []

with open(sys.argv[1], newline="") as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        try:
            data.append((float(row[0]), float(row[1])))
        except:
            pass

if len(sys.argv) > 2:
    data = data[:int(sys.argv[2])]

print(data)

n = len(data)

x = 0
y = 0
xx = 0
xy = 0
yy = 0

for dat in data:
    x += dat[0]
    y += dat[1]
    xy += dat[0] * dat[1]
    xx += dat[0] * dat[0]
    yy += dat[1] * dat[1]

x /= n
y /= n
xx /= n
xy /= n
yy /= n

a = (xy - x * y) / (xx - x * x)
b = y - a * x
delta_a = ((yy - y * y) / (xx - x * x) - a * a)**0.5 / n ** 0.5
delta_b = delta_a * ((xx - x * x) ** 0.5)
print(f"a = {a} # a / 6 = {a / 6}")
print(f"b = {b}")
print(f"delta_a = {delta_a} # delta_a / 6 = {delta_a / 6}")
print(f"delta_b = {delta_b}")
print("########################")
print(f"{0}, {b}")
print(f"{data[-1][0]}, {data[-1][0] * a + b}")
