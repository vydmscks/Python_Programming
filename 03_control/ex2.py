# 반복문: while문, for문

# while문
# 1 ~ 10까지 반복 출력
i = 1
while i <= 10:
    print(i)
    i+=1
    if i == 5:
        break
else:
    print("End")
    
nums = [1,3,5,7,9]
target = 2
i=0
while i<len(nums):
    if nums[i] == target:
        print("FOUND")
    i+=1
else:
    print("NOT FOUND")
    
# 1 ~ 10까지의 합
i = 1
tot = 0
while i <= 10:
    tot += i
    i += 1
else:
    print(f"합: {tot}")
    
# 짝수일 때만 누적
i = 1
tot = 0
while i <= 10:
    if i % 2 == 0:
        tot += i
    i += 1
else:
    print(f"합: {tot}")

# 홀수면 건너뜀
i = 1
tot = 0
while i <= 10:
    i += 1
    if i % 2 != 0:
        continue
    tot += i
else:
    print(f"합: {tot}")