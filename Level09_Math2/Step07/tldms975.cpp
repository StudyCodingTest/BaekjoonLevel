// 알고리즘 스터디 - 기본수학2(7) : 백준 1085
// 직사각형에서 탈출
// 0ms
#include <iostream>
#include <cmath>
using namespace std;

#include <iostream>
#include <cmath>
using namespace std;


int main(void) {
	int x = 0, y = 0, w = 0, h = 0, hor = 0, ver = 0, result = 0;
	cin >> x >> y >> w >> h;
	//cout << x << " " << y << " " << w << " " << h <<endl;
	(w - x >= x) ? hor = x : hor = w - x;
	//cout << "hor: " << hor << endl;
	(h - y >= y) ? ver = y : ver = h - y;
	//cout <<"ver: " << ver << endl;

	(ver >= hor) ? result = hor : result = ver;

	cout << result;

	return 0;
}