// 알고리즘 스터디 - 함수(3) : 백준 1065
// 한수
// 0ms
#include <iostream>
using namespace std;

int main(void) {
	int i=1,cnt=0,a,a1,a2,a3,n;
	cin >> n;
	while(i <= n) {
		if (i <= 99)
			cnt++;
		else if (i <= 999)
		{ // 100~999
			a = i; //100
			a3 = a % 10; //0
			a /= 10; //10
			a2 = a % 10; //0
			a /= 10; //1
			a1 = a % 10; //1
			if (a1-a2==a2-a3)
				cnt++;
		}

		//cout << "cnt: "<<cnt << ", i: " << i << endl;
		i++;
	}

	cout << cnt;
	return 0;
}