// 알고리즘 스터디 - 기본수학1(1) : 백준 1712
// 손익분기점
// 0ms
#include <iostream>
#include <string>
using namespace std;

int main(void) {
	int a,b,c;

	cin >> a>> b>> c;
	if (b<c) {
		cout << a / (c - b) + 1;
	}
	else
		cout << -1;
	return 0;
}