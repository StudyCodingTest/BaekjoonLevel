// 알고리즘 스터디 - DP1(1) : 백준 1003
// 피보나치 함수
// 4ms
#include <iostream>
using namespace std;

int cnt_0=0, cnt_1=0,n;

void fibo(int n) {
	cnt_0 = 1;
	cnt_1 = 0;
	int sum0w1 = 1;
	for (int i = 0; i < n; i++) {
		cnt_0 = cnt_1;
		cnt_1 = sum0w1;
		sum0w1 = cnt_0 + cnt_1;
	}
}

int main(void) {
	int t;
	cin >> t;

	for (int i = 0; i < t; i++) {
		cin >> n;
		
		fibo(n);
		cout << cnt_0 << " " << cnt_1 << "\n";
	}

	return 0;
}