import sys

def main():
    N, X, Y = map(int, input().split())
    A = list(map(int, input().split()))
    
    min_w = max(X * a for a in A)
    max_w = min(Y * a for a in A)
    
    if min_w > max_w:
        print(-1)
        return
    
    mod = Y - X
    r = (X * A[0]) % mod
    for a in A:
        if (X * a) % mod != r:
            print(-1)
            return
    
    W = max_w - ((max_w - r) % mod)
    if W < min_w:
        print(-1)
        return
    
    total_large = 0
    for a in A:
        total_large += (W - X * a) // mod
    
    print(total_large)

if __name__ == '__main__':
    main()