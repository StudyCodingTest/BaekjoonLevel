// 알고리즘 스터디 - 정렬(10) : 백준 18870
// 좌표 압축
// 880ms
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void) {
	int n,same=0;
	vector<pair<int,int>> vec;
	vector<int> result;
	cin >> n;
	vec.resize(n);
	result.resize(n);
	for(int i=0;i<n;i++)
	{
		int num;
		cin >> num;
		vec[i].first=num;
		vec[i].second = i;
	}
	sort(vec.begin(),vec.end());
	int cnt = 0;
	for (int i = 1; i < n; i++) {
		if (vec[i].first==vec[i-1].first) {
			result[vec[i].second] = result[vec[i - 1].second]; //result의 idx를 vec.sec으로 접근해야 i로 0부터 n-1까지 접근할 수 있으므로 
			cnt++;
		} else
			result[vec[i].second] = i - cnt;	
	}
	for (int i = 0; i < n; i++)
		cout << result[i]<< " ";

	return 0;
}



