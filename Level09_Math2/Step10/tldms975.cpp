// 알고리즘 스터디 - 기본수학2(10) : 백준 3053
// 택시 기하학
// 0ms
#include <iostream>
#include <cmath>
#define PI 3.14159265358979
using namespace std;

int main(void) {
	int r;
	double uArea, tArea;

	cin >> r;
	uArea = r * r * PI;
	tArea = 2 * r*r;

	cout << fixed;
	cout.precision(6);
	cout << (double)uArea << "\n";
	cout << (double)tArea << "\n";
	return 0;
}