// 알고리즘 스터디 - 백트래킹(2) : 백준 15650
// N과 M(2)
// 0ms
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n, m;
int arr[10];
// 오름순 중복x
void f(int x,int start) {
	if (x==m) {
		for (int i = 0; i < m; i++) 
				cout << arr[i] << " ";
		cout << "\n";
		return;
	}
	
	for (int i = start; i <= n; i++) {
		arr[x] = i;
		f(x + 1,i+1);
	}
}

int main(void) {
	cin >> n >> m;
	f(0,1);
	return 0;
}
