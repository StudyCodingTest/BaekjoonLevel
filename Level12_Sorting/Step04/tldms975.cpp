// 알고리즘 스터디 - 정렬(4) : 백준 2108
// 통계학
// 224ms
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;
int main(void) {
	int n, sum = 0, min, max;
	cin >> n;
	vector<int> vec;
	int mode[8001] = { 0, };
	

	for (int i = 0; i < n;i++) {
		int num;
		cin>>num;
		vec.push_back(num); // vector에 하나씩 추가하는 방법
							// 메모리를 확보 먼저 하는 방법: vec.resize(n);
		
		sum += vec[i];
	}

	sort(vec.begin(), vec.end());
	max = vec[n - 1];
	min = vec[0];

	// 빈도수 측정
	for (int i = 0; i < n; i++)
			mode[vec[i]+4000]++;
	
	// mode: 빈도수, index: num
	
	// -2 1 2 3 8

	// 빈도의 최대값 구하기
	int m_value;
	int m_max = 0;
	for (int i = 0; i < 8001; i++) {
		if (m_max < mode[i])
		{
			m_max = mode[i]; // mode[0]: -4000의 빈도수
			m_value = i - 4000;
		}
	}

	int cnt = 0;
	// 빈도의 최대값이 같다면 그 것중에 두번째로 큰 걸 빈도값으로 정함
	for (int i = 0; i < 8001; i++) {
		if (m_max == mode[i]) {
			cnt++;
		}
		if (cnt == 2) {
			m_value = i - 4000;
			break;
		}
	}

	cout << floor((double)sum / n+0.5) << "\n";
	cout << vec[(int)(n / 2)] << "\n";
	cout << m_value<< "\n";
	cout << max - min << "\n";
	return 0;
}