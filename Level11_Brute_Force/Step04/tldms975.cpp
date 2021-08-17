// 알고리즘 스터디 - 브루트 포스(4) : 백준 1018
// 체스판 다시 칠하기
// 0ms
#include <iostream>
using namespace std;

int main(void) {
	int n, m, cnt = 0, min = 64;
	
	// set array chess
	char chess[8][8];
	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 8; j++)
			if (i % 2 == 0 && j % 2 == 1 || i%2==1&&j%2==0)
				chess[i][j] = 'W'; // W B W B ..
			else
				chess[i][j] = 'B';
	}

	// set array arr
	cin >> n >> m;
	char**arr=new char *[n];
	for (int i = 0; i < n; i++)
		arr[i] = new char[m];
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++)
			cin >> arr[i][j];
	}

	// compare arr with chess
	// (x,y)는 arr의 chess와 비교할 시작좌표
	// precondition: i<=n-8 && j<=m-8
	for (int x = 0; x <= n-8; x++) {
		for (int y = 0; y <= m-8; y++) {
			cnt = 0;
			
			for (int i=0; i < 8; i++) {
				for (int j=0; j < 8; j++) {
					if (arr[i+x][j+y] != chess[i][j])
						cnt++; // 바꿔야 하는 횟수
				}
			}

			if (cnt > 32) // B W 나 W B 두 가지가 있으므로
				cnt = 64-cnt;

			if (min > cnt)
				min = cnt;
		}
	}


	cout << min;
	return 0;
}
