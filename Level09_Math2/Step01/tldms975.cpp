// 알고리즘 스터디 - 기본수학2(1) : 백준 1978
// 소수 찾기
// 0ms
#include <iostream>
#include <cmath>
using namespace std;

bool prime(int n) {
	if (n == 1)
		return false;
	for (int i = 2; i < n; i++) {
		if (n % i == 0) // 1과 n자기자신 이외에 나눠진다면
			return false;
	}
	return true;
}

int main(void) {
	int n,cnt=0;
	cin >> n;
	int* arr = new int[n];

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
		if (prime(arr[i]))
			cnt++;
	}
	cout << cnt;
	return 0;
}