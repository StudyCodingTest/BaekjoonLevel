// 알고리즘 스터디 - 백트래킹(5) : 백준 9663
// N-Queen
// 4736ms
#include <iostream>
#include <algorithm>
using namespace std;

int n,sum=0;
int col[15];

bool promising(int i) {
	int k=1;
	bool res=true;
	while (k < i && res) {
		if (col[i] == col[k] || abs(col[i]-col[k])==i-k) {
			res=false;
		}
		k++;
	}
	return res;
}

void queens(int i) {
	if (promising(i)) {
		if (i == n) {
			sum++;
		}
		else {
			for (int j = 1; j <= n; j++) {
				col[i + 1] = j;
				queens(i+1);
			}
		}
	}
}
int main(void) {
	cin >> n;

	queens(0);
	cout << sum;
	return 0;
}
