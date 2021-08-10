// 알고리즘 스터디 - 기본수학2(8) : 백준 3009
// 네 번째 점
// 0ms
#include <iostream>
#include <cmath>
using namespace std;

int main(void) {
	int x[3], y[3];
	int x4, y4;
	
	if (x[0] == x[1] || x[0] == x[2]) {
		if (x[0] == x[1])
			x4 = x[2];
		else
			x4 = x[1];
	}
	else
		x4 = x[0];
	if (y[0] == y[1] || y[0] == y[2]) {
		if (y[0] == y[1])
			y4 = y[2];
		else
			y4 = y[1];
	}
	else
		y4= y[0];
	cout << x4 << " " << y4;
	return 0;
}