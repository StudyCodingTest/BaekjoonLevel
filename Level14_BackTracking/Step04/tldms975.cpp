// 알고리즘 스터디 - 백트래킹(4) : 백준 15652
// N과 M(4)
// 4ms
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
// 오름순(체크필요없음) 중복o
int n, m;
int arr[10];

void f(int x,int start) {
	if (x==m) { // 출력
		for (int i = 0; i < m; i++) 
				cout << arr[i] << " ";
		cout << "\n";
		return;
	}
	
	for (int i =start; i <= n; i++) {
	
			arr[x] = i;
			f(x+1,i); // 비내림차순이므로 중복도 허용하기때문에 i+1이 아닌 i로 호출
	}
}

int main(void) {
	cin >> n >> m;
	f(0,1);
	return 0;
}
