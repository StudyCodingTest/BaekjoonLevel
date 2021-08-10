// 알고리즘 스터디 - 기본수학1(5) : 백준 10250
// ACM 호텔
// 4ms
#include <iostream>
#include <cmath>
using namespace std;

int main(void) {
	int t, h, w, n,layer,room;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> h >> w >> n;
		
		layer= int(ceil(n % h));
		if (layer == 0)
			layer = h;
		room = ceil((float)n /h) ; // 주의:float로 해야 의도한대로 나온다^^
		
		cout << layer*100 + room << endl;;
	}

	return 0;
}