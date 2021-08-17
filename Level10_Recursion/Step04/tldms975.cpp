// 알고리즘 스터디 - 재귀(4) : 백준 11729
// 하노이 탑 이동 순서
// 180ms
#include <iostream>
#include <cmath>
using namespace std;

void hanoi(int n,int a,int b,int c) {
	if (n == 1)
	{
		cout << a << " " << c << "\n";
	}
	else { // n=3인 경우 총 7개 나와야 함
		hanoi(n - 1,a,c,b); // h(3).1 h(2).1 h(1).1
		cout << a << " " << c << "\n"; //.1
		hanoi(n - 1,b,a,c); // h(3).1 h(2).1 h(1).1
	}
	// 출력은 2^n-1번 되어야 하므로
}

int main(void) {
	int n;
	cin >> n;

	cout << int(pow(2, n)) - 1 << "\n"; // 공식, 오답:pow는 double으로 반환돼서 int로 형변환 해줘야 정확함
	hanoi(n,1,2,3);

	return 0;
}
