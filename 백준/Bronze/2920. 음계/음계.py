line = list(map(int, input().split()))
sort_line = sorted(line, reverse=False)
reverse_line = sorted(line, reverse=True)

if line == sort_line:
    print('ascending')
elif line == reverse_line:
    print('descending')
else:
    print('mixed')
