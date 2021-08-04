// 알고리즘 스터디 - 문자열(9) : 백준 2941
// 크로아티아 알파벳
// 0ms
#include <iostream>
#include <string>
using namespace std;

int main(void) {
	string s;
	int cnt = 0;
	cin >> s;

	for (int i = 0; i < s.length(); i++) {
		if (i<s.length()-1&&s[i] == 'c' && (s[i + 1] == '=' || s[i + 1] == '-')) // c= c-
		{
			i++;
			cnt++;
		} else if(i < s.length() - 1&&s[i] == 'd' && s[i + 1] == '-') // d-
		{
			i++;
			cnt++;
		}
		else if (i < s.length() - 2&&s[i] == 'd' && s[i + 1] == 'z' && s[i + 2] == '=') // dz-
		{
			i+=2;
			cnt++;
		}
		else if (i < s.length() - 1 && (s[i] == 'l'|| s[i] == 'n') && (s[i + 1] == 'j')) // lj nj
		{
			i++;
			cnt++;
		}
		else if (i < s.length() - 1 && (s[i] == 's' ||s[i]=='z') && (s[i + 1] == '=')) // s= z=
		{
			i++;
			cnt++;
		}
		else
			cnt++;
	}
	cout << cnt;
	return 0;
}