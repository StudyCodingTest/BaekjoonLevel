// 알고리즘 스터디 - 정렬(1) : 백준 2750
// 수 정렬하기
// ms
#include <iostream>
#include <cmath>
using namespace std;

int main(void) {
	int n,tmp=0;
	cin >> n;
	int* arr = new int[n];
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	for (int i = 0; i < n ; i++) {
		for (int j = 0; j < n-1; j++){
			if (arr[j] > arr[j + 1]) {
				tmp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = tmp;
			}
		}
	}
	for (int i = 0; i < n; i++) {
		cout << arr[i] << "\n";
	}

	return 0;
}