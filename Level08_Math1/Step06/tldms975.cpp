// 알고리즘 스터디 - 기본수학1(6) : 백준 2775
// 부녀회장이 될테야
// 224ms
#include <iostream>
#include <cmath>
using namespace std;

int C(int n,int r) {

	if (n == r||r==0)
		return 1;
	else
		return C(n-1,r-1)+C(n-1,r);
	
}

int main(void) {
	int t, k, n, p; // p: 거주민 수
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> k >> n;
		
		//p = factorial(k + n) / (factorial(k + 1) * factorial(n - 1)); // 시간초과
		p = C(k + n, n - 1);
			
		cout << p << endl;
	}
	return 0;
}