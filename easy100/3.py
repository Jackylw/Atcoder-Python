N, A, B = map(int, input().split())
s = str(input())
passed_count = 0
b_rank = 0
for person in s:
    if person == 'a':
        if passed_count < A + B:
            print('Yes')
            passed_count += 1
        else:
            print('No')

    elif person == 'b':
        b_rank += 1
        if passed_count < A + B and b_rank <= B:
            print('Yes')
            passed_count += 1
        else:
            print('No')

    else:
        print('No')
