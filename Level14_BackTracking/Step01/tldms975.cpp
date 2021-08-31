// 알고리즘 스터디 - 백트래킹(1) : 백준 15649
// N과 M
// 32ms
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n, m;
int arr[10];
bool chk[10] = {false,};

void f(int x) {
	if (x==m) {
		for (int i = 0; i < m; i++) 
			cout << arr[i] << " ";
		
		cout << "\n";
		return;
	}
	
	for (int i = 1; i <= n; i++) {
		if(chk[i]==0){
			chk[i] = true;
			arr[x] = i;
			f(x + 1);
			chk[i] = false;
		}
	}
}

int main(void) {
	cin >> n >> m;
	f(0);
	return 0;
}



