// 알고리즘 스터디 - 브루트 포스(5) : 백준 1436
// 영화감독 숌
// 68ms
#include <iostream>
#include <string>
using namespace std;


int main(void) {
	int series = 666,cnt=0,n;
	cin >> n;
	while (1) {

		if (to_string(series).find("666")!=-1) // 666이 포함되어있는 경우
			cnt++;
		if (n == cnt)
			break;

		series++;
	}
	
	cout << series;
	return 0;
}