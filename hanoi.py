def move(n, src, dest):
    print(f'{n}번 원반을 {src}에서 {dest}로 이동')


def hanoi(n, src, dest, via):
    if n == 1:
        move(1, src, dest)
    else:
        hanoi(n - 1, src, via, dest)
        move(n, src, dest)
        hanoi(n - 1, via, dest, src)


hanoi(3, 'A', 'C', 'B')
