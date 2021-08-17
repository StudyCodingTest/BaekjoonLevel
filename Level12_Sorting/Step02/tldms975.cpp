// 알고리즘 스터디 - 정렬(2) : 백준 2751
// 수 정렬하기 2
// 744ms
#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
	int n;
	cin >> n;

	int* arr = new int[n];
	for (int i = 0; i < n; i++)
		cin >> arr[i];

	sort(arr, arr + n);

	for (int i = 0; i < n; i++)
		cout << arr[i] << "\n";

	return 0;
}
