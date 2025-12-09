x = int(input())

total_bits = 0
total_ones = 0
num = 1

while total_bits < x:
    binary = bin(num)[2:]
    needed = x - total_bits

    if total_bits + len(binary) <= x:
        total_ones += binary.count('1')
        total_bits += len(binary)
    else:
        partial = binary[:needed]
        total_ones += partial.count('1')
        break

    num += 1

print(total_ones)