// 알고리즘 스터디 - 기본수학2(5) : 백준 4948 
// 베르트랑 공준
// 592ms
#include <iostream>
#include <cmath>
using namespace std;

bool isprime(int n) {
	if (n == 1)
		return false;
	for (int i = 2; i*i <= n; i++) {
		if (n % i == 0) // 1과 n자기자신 이외에 나눠진다면
			return false;
	}
	return true;
}
int main(void) {
	int n,cnt;
	while (1) {
		cnt = 0;
		cin >> n;
		if (n == 0)
			break;
		for (int i = n+1; i<= 2 * n; i++) {
			if (isprime(i))
				cnt++;
		}
		cout << cnt << "\n";
	}
	return 0;
}