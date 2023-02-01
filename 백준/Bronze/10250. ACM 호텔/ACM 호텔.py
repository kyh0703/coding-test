T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    loop_count = N // H if N % H == 0 else N // H + 1
    height = H if N % H == 0 else N % H
    print(f"{height}{loop_count:02d}")
