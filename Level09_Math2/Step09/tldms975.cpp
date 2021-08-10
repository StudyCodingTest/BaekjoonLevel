// 알고리즘 스터디 - 기본수학2(9) : 백준 4153
// 직각삼각형
// 0ms
#include <iostream>
#include <cmath>
using namespace std;


int main(void) {
	int a, b, c;

	while (1) {
		cin >> a >> b >> c;
		if (a == 0 && b == 0 && c == 0)
			break;
		if (a * a == b * b + c * c || b * b == a * a + c * c || c * c == a * a + b * b)
			cout << "right" << "\n";
		else
			cout << "wrong" << "\n";

	}


	return 0;
}