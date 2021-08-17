// 알고리즘 스터디 - 정렬(5) : 백준 1427
// 소트인사이드
// ms
#include <iostream>
using namespace std;

int main(void) {
	string str;
	cin >> str;

	for (int i = 0; i < str.length(); i++) {
		for (int j = 0; j < str.length()-1; j++) {
			if (str[j] < str[j + 1])
				swap(str[j], str[j + 1]);
		}
	}
	cout << str;
	return 0;
}
