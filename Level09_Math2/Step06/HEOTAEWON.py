#문제: 골드바흐의 추측
#번호: 9020
#시간:

nums = []
for _ in range(int(input())):
    num = int(input())
    nums.append(num)

for i in range(len(nums)):
    nums_sosu = []
    num_test = nums[i]
    for n in range(2, num_test+1):
        if n == 1:
            continue
        for x in range(2, int(n**0.5)+1):
            if n%x == 0:
                break
        else:
            nums_sosu.append(n)
    #print(nums_sosu)

    index = -1
    ans = []

    while num_test != 0:
        x = num_test - nums_sosu[index]
        if x in nums_sosu and x > 0:
            num_test -= nums_sosu[index]
            ans.append(nums_sosu[index])
        if x < 0:
            index -= 1
            x += nums_sosu[index]
        elif x == 0:
            num_test -= nums_sosu[index]
            ans.append(nums_sosu[index])
        else:
            x += nums_sosu[index]
            index -= 1
        #print(index, num_test, x)
    ans.sort()
    for i in range(len(ans)):
        print(ans[i], end=' ')
