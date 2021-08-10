// 알고리즘 스터디 - 기본수학1(4) : 백준 2869
// 달팽이는 올라가고 싶다
// 0ms
#include <iostream>
using namespace std;

int main(void) {
	int a, b, v, day = 0;
	cin >> a >> b >> v;
	day = (v-b) / (a - b); // v가 아닌 v-b로 나누어서 최종 길이를 줄인다
	if ((v-b) % (a-b) != 0)
		day++;
	cout << day;
	return 0;
}