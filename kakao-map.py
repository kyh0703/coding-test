def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        temp = bin(arr1[i] | arr2[i])[2:].zfill(n)
        temp = temp.replace("1", "#")
        temp = temp.replace("0", " ")
        answer.append(temp)
    return answer


print("answer", solution(
    6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))

# ["######", "###  #", "##  ##", "#### ", "#####", "### # "]
# ["######", "###  #", "##  ##", " #### ", " #####", "### # "]

print("22:", str(bin(22)[2:]).zfill(6))
print("14:", str(bin(14)).zfill(6))
print("14:", bin(22 | 14)[2:].zfill(6))
'#### '
