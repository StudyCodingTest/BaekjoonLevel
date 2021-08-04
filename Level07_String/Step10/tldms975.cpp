// 알고리즘 스터디 - 문자열(10) : 백준 1316
// 그룹단어 체커
// 0ms
#include <iostream>
#include <string>
using namespace std;

bool check(string s) {
	bool alphabet[26] = { false };
	char ch;

	for (int j = 0; j < s.length(); j++) {
		if (alphabet[s[j] - 97] == false) { // 한 번도 나오지 않았었다면		
			ch = s[j];
			alphabet[ch - 97] = true;
			while (1) {
				if (s[++j] != ch) {
					j--;
					break;
				}		
			}
		}
		else { // 이미 나왔었다면
				return false;
		}
	}
	return true;
}
																																																																																																												
int main(void) {
	int n,cnt=0;
	string s;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> s;
		if(check(s))
			cnt++;
	}

	cout << cnt;
	return 0;
}