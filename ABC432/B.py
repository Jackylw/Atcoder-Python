x = str(input())
digits = list(x)
digits.sort()
for i, d in enumerate(digits):
    if d != '0':
        digits[0], digits[i] = digits[i], digits[0]
        break
print(''.join(digits))
