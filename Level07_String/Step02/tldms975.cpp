// 알고리즘 스터디 - 문자열(2) : 백준 11720
// 숫자의 합
// 0ms
#include <iostream>
#include <string>
using namespace std;

int main(void) {
	int inum = 0, sum = 0;;
	string strnum;
	
	cin >> inum;
	cin >> strnum;
	
	for (int i = 0; i < inum; i++) {
		sum += (strnum[i]-48);
	}

	cout << sum;
	
	return 0;
}
