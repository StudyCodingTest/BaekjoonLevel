// 알고리즘 스터디 - 브루트 포스(3) : 백준 7568
// 덩치
// 0ms
#include <iostream>
#include <cmath>
using namespace std;

class Build {
public:
	int  h, w, k=1; // k=1등부터 시작하니까 (0등은없음)
};

int main(void) {
	int n;
	cin >> n;
	Build* arr = new Build[n];

	for (int i = 0; i < n; i++)
		cin >> arr[i].w >> arr[i].h;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (arr[i].w < arr[j].w && arr[i].h < arr[j].h)
				arr[i].k++;
		}
	}

	// 출력
	for (int i = 0; i < n; i++) 
		cout << arr[i].k << " ";
	
	return 0;
}