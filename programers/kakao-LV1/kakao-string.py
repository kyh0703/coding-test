def solution(s):
    answer = 0
    number_dic = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
                  "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    pos = 0
    number_list = []
    for i in range(len(s)):
        number = s[pos:i+1]
        if number in number_dic:
            number_list.append(str(number_dic[number]))
            pos = i + 1
        if number.isdigit():
            number_list.append(str(number))
            pos = i + 1
    answer = int("".join(number_list))
    return answer


print(solution("one4seveneight"))

"""
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)
 """
"""
def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
 """
