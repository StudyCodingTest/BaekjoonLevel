// 알고리즘 스터디 - 재귀(2) : 백준 10870
// 피보나치 수 5
// 0ms
#include <iostream>
#include <cmath>
using namespace std;

int fibo(int n) {
	if (n == 0)
		return 0;
	else if (n == 1)
		return 1;
	else
		return fibo(n - 1)+fibo(n-2);
	
}

int main(void) {
	int n;
	cin >> n;
	cout << fibo(n);
	return 0;
}