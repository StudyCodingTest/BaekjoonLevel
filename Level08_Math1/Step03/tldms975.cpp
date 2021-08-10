// 알고리즘 스터디 - 기본수학1(3) : 백준 1193
// 분수찾기
// 0ms
#include <iostream>
using namespace std;

int main(void) {
	int x, numer = 0, denom = 0, sum = 0, i = 1;
	cin >> x;

	for (i; i <= x;i+=sum) // sum구하는거 어려웠당
		++sum;
	sum++;
	i -= sum;

	if (sum % 2 == 0) { // 짝수면

		numer = sum;
		denom = 0;
		do {
			numer--;
			denom++;
		} while (++i < x);
	}
	else { // 홀수면
		numer = 0;
		denom = sum;
		do  {
			numer++;
			denom--;
		} while (++i < x);
	}

	cout << numer << '/' << denom;

	return 0;
}
