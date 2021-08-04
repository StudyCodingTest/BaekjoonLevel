// 알고리즘 스터디 - 문자열(8) : 백준 5622
// 다이얼
// 0ms
#include <iostream>
#include <cstring>
using namespace std;

int main(void) {
	string s;
	int sum = 0;
	cin >> s;

	for (int j = 0; j < s.length(); j++) {
		if (s[j] >= 65 && s[j] <= 67) // ABC 2
			sum += 3;
		else if (s[j] >= 68 && s[j] <= 70) // DEF 3
			sum += 4;
		else if (s[j] >= 71 && s[j] <= 73) // GHI 4
			sum += 5;
		else if (s[j] >= 74 && s[j] <= 76) // JKL 5
			sum += 6;
		else if (s[j] >= 77 && s[j] <= 79) // MNO 6
			sum += 7;
		else if (s[j] >= 80 && s[j] <= 83) // PQRS 7
			sum += 8;
		else if (s[j] >= 84 && s[j] <= 86) // TUV 8
			sum += 9;
		else if (s[j] >= 87 && s[j] <= 90) // WXYZ 9
			sum += 10;
	}

	cout << sum ;

	return 0;
}