// 알고리즘 스터디 - 정렬(8) : 백준 1181
// 단어 정렬
// 88ms
#include <iostream>
#include <algorithm>
using namespace std;

bool cmp(string s1, string s2) {
	if (s1.length() == s2.length())
		return s1 < s2;
	else
		return s1.length() < s2.length();

}

int main(void) {
	int n;
	cin >> n;
	string* str = new string[n];
	for (int i = 0; i < n; i++)
		cin >> str[i];

	sort(str, str + n, cmp);

	for (int i = 0; i < n-1; i++) { 
		while (str[i] == str[i + 1])
			i++;

		cout << str[i] << "\n";
	}
	if(str[n-2]!=str[n-1])
		cout << str[n - 1]; // n-1미만까지 위에서 돌았으니 n-1은 따로 출력 
	return 0;
}