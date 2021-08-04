// 알고리즘 스터디 - 문자열(5) : 백준 1157
// 단어 공부
// 68ms
#include <iostream>
using namespace std;

int main(void) {
	string s;
	int alphabet[26] = { 0 }, max = 0,spot=0;
	char result = '?';
	cin >> s;

	for (int i = 0; i < 26; i++) {
		for (int j = 0; j < s.length(); j++) {
			if (s[j] == i+65 || s[j] == i +97) 
			{
				alphabet[i]++;
			}
		}
	}
	//제일 큰 거
	for (int i = 0; i < 26;i++) {
		if (max < alphabet[i])
		{
			max = alphabet[i];
			spot = i;
			result = (char)(i + 65);
		}
		else if (max == alphabet[i])
			result = '?';
	}

	cout << result;
	
	return 0;
}