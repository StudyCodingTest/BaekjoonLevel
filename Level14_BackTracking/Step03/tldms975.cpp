// 알고리즘 스터디 - 백트래킹(3) : 백준 15651
// N과 M(3)
// ms
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n, m;
int arr[10];
// 순서x 중복o
void f(int x) {
	if (x==m) {
		for (int i = 0; i < m; i++) 
				cout << arr[i] << " ";
		cout << "\n";
		return;
	}
	
	for (int i = 1; i <= n; i++) {
		arr[x] = i;
		f(x + 1);
	}
}

int main(void) {
	cin >> n >> m;
	f(0);
	return 0;
}
