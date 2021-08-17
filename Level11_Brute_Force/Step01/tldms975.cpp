// 알고리즘 스터디 - 브루트 포스(1) : 백준 2798
// 블랙잭
// 968ms
#include <iostream>
#include <cmath>
using namespace std;



int main(void) {
	int n, m;
	cin >> n >> m;
	int* arr = new int[n];

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	// 합이 최대 m이어야 한다.
	while (m) {
		int sum = 0;

		// 더할 수 있는 모든 경우를 계산
		for (int i = 0; i < n - 2; i++) {
			for (int j = i + 1; j < n - 1; j++) {
				for (int k = j + 1; k < n; k++) {
					sum = arr[i] + arr[j] + arr[k];
					if (sum == m) { // m과 같다면 출력 후 종료
						cout << m;
						return 0; // 종료
					}
				}
			}
		}
		m--; // 합을 찾지 못했더라면 1 줄여서 시도해보기
	}
	

	return 0;
}
