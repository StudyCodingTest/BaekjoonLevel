// 알고리즘 스터디 - 브루트 포스(2) : 백준 2231
// 분해합
// 0ms
#include <iostream>
#include <cmath>
using namespace std;

int digitSum(int n) {
	int sum = 0;
	while (n) {
		sum += n % 10;
		n /= 10;
	}
	return sum;
}

int main(void) {
	int n,cpn,generator;
	cin >> n;
	cpn = n;
	int digitsum = 0, digit = 0;
	
	// n의 자리수 구하기
	while (cpn) {
		cpn /= 10;
		digit++;
	}

	for (generator= n - 9 * digit;generator<=n-1 ; generator++) {
		//cout << generator << "\n";
		if (n == digitSum(generator) + generator)
		{
			cout << generator;
			return 0;
		}
	}
	cout << 0;
	return 0;
}