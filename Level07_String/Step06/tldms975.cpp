// 알고리즘 스터디 - 문자열(6) : 백준 1152
// 단어의 개수
// 44ms
#include <iostream>
#include <string>
using namespace std;
// 97대신 공백으로하고 공백을 포함하여 받는 문자열로 고치기
int main(void) {
	string s;
	int cnt = 0;
	bool isword = false;
	getline(cin, s); // 공백 포함하여 문자열 받기위해

	for (int i = 0; i < s.length(); i++)
	{
		if (s[i] != ' ' && isword == false) {
			isword = true;
			cnt++;
		} else if(s[i]==' ') {
			isword = false;
		}
	}
	cout << cnt;
	return 0;
}