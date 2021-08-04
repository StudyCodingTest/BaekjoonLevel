// 알고리즘 스터디 - 함수(1) : 백준 15596
// 아스키 코드
// 24ms

#include <vector>
long long sum(std::vector<int> &a) {
	long long ans = 0;
	for (int i = 0; i < a.size(); i++) {
		ans += a.at(i);
	}
	return ans;
}