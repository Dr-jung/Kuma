fruits = ['감', '감', '감', '감', '감', '감', '감', '감', '감', '김', '감', '감', '감', '감', '감', '감']
count1 = 0
count2 = 0
for fruit in fruits:
    if fruit == '감':
        count1 += 1
    else:
        count2 += 1


# 사과의 갯수를 출력합니다.
print(count1)
print(count2)
