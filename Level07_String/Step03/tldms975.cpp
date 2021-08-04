// 알고리즘 스터디 - 문자열(3) : 백준 10809
// 알파벳 찾기
// 0ms
#include <iostream>
#include <string>
using namespace std;

int main(void) {
	string str;
	int pos;
	cin >> str;

	for (int i = 97; i <= 122;i++) {
		pos = -1;
		for (int j = 0; j < str.length(); j++) {
			if (str[j] == i)
			{
				pos = j;
				break;
			}
		}
		cout << pos << " ";
	}
	return 0;
}
