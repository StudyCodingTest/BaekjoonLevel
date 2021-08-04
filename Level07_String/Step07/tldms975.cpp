// 알고리즘 스터디 - 문자열(7) : 백준 2908
// 상수
// 0ms
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(void) {
	string s1, s2;
	cin >> s1 >> s2;

	//reverse 한 뒤에 int형으로 변환하기
	reverse(s1.begin(), s1.end());
	reverse(s2.begin(), s2.end());

	stoi(s1);
	stoi(s2);

	if (s1 > s2)
		cout << s1;
	else
		cout << s2;

	return 0;
}