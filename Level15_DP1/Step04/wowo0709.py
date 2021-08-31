# 파도반 수열
# 92ms
wave = [0,1,1,1]
for _ in range(int(input())):
    n = int(input())
    if n >= len(wave):
        for i in range(len(wave),n+1):
            wave.append(wave[i-2]+wave[i-3])
    print(wave[n])