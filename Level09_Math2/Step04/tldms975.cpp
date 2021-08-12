// 알고리즘 스터디 - 기본수학2(4) : 백준 1929
// 소수 구하기
// ms
#include <iostream>
#include <cmath>
using namespace std;

int main(void) {
	int m, n;
	cin >> m >> n;
	bool* arr = new bool [n + 3]; // i=2로 시작했기 때문에 0, 1을 의미하는 추가적인 공간 필요 (+2)
	
	arr[0] = false;
	arr[1] = false;
	for (int i = 2; i <= n; i++) {
		arr[i] = true;
	}
	for (int i = 2; i*i <= n; i++) {// i : 2 3 4 5 6 ...
		// i=2부터 해야 1의 배수(전체)가 지워지는걸 막을 수 있다.
		if (arr[i]) { // 아직 안지워진것들 중에서
			for (int j = i*2;j<=n;j+=i) // 해당수 제외하고(소수니까) 그 다음배수부터
			{
				arr[j] = false;
			}
		}
	}

	for (int i = m; i <= n; i++) { // m부터 n까지 중의 소수 출력
		if (arr[i])
			cout << i << "\n"; // endl으로 하면 버퍼 강제종료라 시간 더 오래걸린댔음
	}
	return 0;
}