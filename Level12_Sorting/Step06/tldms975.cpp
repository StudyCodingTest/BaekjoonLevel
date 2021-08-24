// 알고리즘 스터디 - 정렬(6) : 백준 11650
// 좌표 정렬하기
// 128ms
#include <iostream>
#include <algorithm>
using namespace std;
class Point {
public:
	int x;
	int y;
};

bool compare(Point a, Point b) {
	if (a.x == b.x)
		return a.y < b.y;
	else
		return a.x < b.x; // 기본적으로는 이 둘을 비교 it should be this: a.x is smaller than a.y
}
int main(void) {
	int n;
	cin >> n;
	Point* point = new Point[n];

	for (int i = 0; i < n; i++) 
		cin >> point[i].x >> point[i].y;
	
	// sort함수를 이용한 사용자 정의 정렬
	sort(point, point + n,compare);

	for (int i = 0; i < n; i++) {
		cout << point[i].x << " " << point[i].y << "\n";
	}
}