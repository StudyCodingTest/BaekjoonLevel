// 알고리즘 스터디 - 기본수학1(9) : 백준 1011
// Fly me to the Alpha Centauri
// 8ms
#include <iostream>
#include <cmath>
using namespace std;

int main(void) {
	unsigned int t, x, y, cnt, d;
	cin >> t;
	while (t--) {
		cin >> x >> y;
		d = y - x;
		cnt = 0;
		for (int i = 1; i*i<=d+i ; i++) { // i<=d로 하면 시간 초과됨
			if (d >= i*i + 1) // i*i+1 <= d <= i*(i+1)
				cnt++;
			if( d >= (i-1)*(i-1) + i) // (i-1)^2 + (i-1) + 1 <= d <= i^2
				cnt++;
		}
		cout << cnt << "\n";
	}
	return 0;
}