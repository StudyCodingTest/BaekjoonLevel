// 알고리즘 스터디 - 재귀(3) : 백준 2447
// 별 찍기 - 10
// 304ms
#include <iostream>
#include <cmath>
using namespace std;

void pattern(int i, int j, int n) {
	if ((i / n) % 3 == 1 && (j / n) % 3 == 1)
		cout << " ";
	else if (n/3==0)
		cout << "*";
	else
		pattern(i, j, n / 3); //n/3==0일떄까지
}

int main(void) {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++)
			pattern(i, j, n);
		cout << "\n";
	}
	return 0;
}