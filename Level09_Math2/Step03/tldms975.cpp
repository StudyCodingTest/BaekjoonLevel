// 알고리즘 스터디 - 기본수학2(3) : 백준 11653
// 소인수분해 
// 0ms
#include <iostream>
#include <cmath>
using namespace std;


int main(void) {
	int n, i = 2;
	cin >> n;
	
	for (i; i * i <= n; i++) // 이게 핵심..!
	{
		while (n % i == 0) {
			cout << i << endl;
			n /= i;
		}
	}
	//n==1이 될때까지 이 작업을 계속해야하므로
	if (n!=1)
		cout << n;
	return 0;
}