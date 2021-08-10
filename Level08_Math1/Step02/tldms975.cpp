// 알고리즘 스터디 - 기본수학1(2) : 백준 2292
// 벌집
// 0ms
#include <iostream>
using namespace std;

int main(void) {
	int n, cnt = 1,i=1,m=1,tmp = 0;
	cin >> n;
	while (n>i) { // n>=i로 하고 cnt=0으로 해서 틀렸었음
		cnt++; //   
		i += 6 * (m++); // 1, ~7, ~19, ~37, ~61, ~91 ...
	}
	cout << cnt;
	return 0;
}