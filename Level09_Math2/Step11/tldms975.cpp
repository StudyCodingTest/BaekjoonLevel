// 알고리즘 스터디 - 기본수학2(11) : 백준 1002
// 터렛
// 8ms
#include <iostream>
#include <cmath>
using namespace std;

int main(void) {
	int t, x1, y1, r1, x2, y2, r2, JtoB, rp, rm;
	cin >> t;
	while (t--) {
		cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
		JtoB = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
		rp = (r1 + r2) * (r1 + r2);
		rm = (r1 - r2) * (r1 - r2);
		
		// 제곱으로 해줘야 오류 안남
		// 교점 0개 d > r1+r2 || d < r1-r2
		// 교점 1개 d = r1+r2 || d=r1-r2
		// 교점 2개 d < r1+r2 && d>r1-r2
		// 무한 d=0 r1=r2 => r1-r2=0
		//

		// 출력
		if (JtoB==0&&rm==0) // 무한대일 경우
			cout << -1 << '\n';
		else if (JtoB==rp||JtoB==rm)
			cout << 1 << '\n';
		else if (JtoB < rp && JtoB > rm)
			cout << 2 << '\n';
		else 
			cout << 0 << '\n';
	}
	
	return 0;
}