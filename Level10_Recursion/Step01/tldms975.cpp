// 알고리즘 스터디 - 재귀(1) : 백준 10872
// 팩토리얼
// 0ms
#include <iostream>
#include <cmath>
using namespace std;

int factorial(int n) {
	if (n <= 1)
		return 1;
	else
		return n * factorial(n - 1);
	
}

int main(void) {
	int n;
	cin >> n;
	cout << factorial(n);
	return 0;
}