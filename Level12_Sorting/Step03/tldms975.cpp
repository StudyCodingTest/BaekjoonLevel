// 알고리즘 스터디 - 정렬(3) : 백준 10989
// 수 정렬하기 3
// 2984ms
#include <iostream>
#include <stdio.h> // 빠른연산을 위해 scanf와 printf 사용
using namespace std;

// counting sort
int main(void) {
	int n,input;
	int arr[10001] = { 0, };
	
	cin >> n;

	for (int i = 0; i < n; i++) {
		scanf("%d", &input);
		arr[input]++;
	}

	for (int i = 0; i < 10001; i++) {
		for (int j = 0; j < arr[i]; j++)
			printf("%d\n", i);
	}

	return 0;
}