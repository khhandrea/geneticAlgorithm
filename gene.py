import random
import numpy as np
import copy
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import time


# 로그 생성
f = open("gene log.txt", "w")

# 유전자 5개
chromo = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
new_chromo = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# 각 염색체의 적합도 평가
evalution = [0, 0, 0, 0, 0]

# 우성 유전자
dominant = 1

# 돌연변이
mutation = 0.01

# 선택된 우성 염색체
select = [0, 0]

# 세대
gene = 0

# 최초의 세대 생성
for i in range(5):
    for j in range(10):
        chromo[i][j] = random.randint(0, 9)

print(gene, "Gen : ", chromo)

gene += 1

# 완전체가 나올때까지 반복
while(1):
    # 적합도 평가
    for i in range(5):
        m_sum = 0
        for j in range(10):
            m_sum += abs(chromo[i][j] - dominant)
        evalution[i] = m_sum

    # 우성 염색체 2쌍 선택
    for i in range(2):
        select[i] = np.argsort(evalution)[i]

    # 우성 염색체 로그 저장
    eval = 0
    for i in range(10):
        eval += abs(chromo[select[0]][i] - dominant)
    data = "%d, %d\n" % (gene, -eval)
    f.write(data)

    # 염색체 교차 & 돌연변이
    for i in range(5):
        for j in range(10):
            if random.random() < mutation:
                new_chromo[i][j] = random.randint(0, 9)  # 돌연변이 발생
            else:
                new_chromo[i][j] = chromo[select[random.randint(0, 1)]][j]

    print(gene, "Gen : ", chromo)
    print("upper : ", chromo[select[0]], chromo[select[1]])
    gene += 1

    # 목표 적합도가 있으면 종료
    done = False
    for i in range(5):
        if evalution[i] == 0:
            done = True
            break
    if done == True:
        break

    # 깊은 복사
    chromo = copy.deepcopy(new_chromo)

    # 1000세대 넘으면 종료
    if gene > 1000:
        break

f.close()
