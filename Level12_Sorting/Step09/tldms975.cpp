// 알고리즘 스터디 - 정렬(9) : 백준 10814
// 나이순 정렬
// 116ms
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

class Member {
public:
	string name;
	int age;
	int order;
};

// compare를 class 밑에다가 만들어야함 ;;;;
// order 꼭 해야함;;;
bool compare(Member m1, Member m2) {
	if (m1.age == m2.age)
		return m1.order < m2.order;
	else
		return m1.age < m2.age;
}

int main(void) {
	int n;
	cin >> n;

	Member* mem = new Member[n];

	for (int i = 0; i < n; i++)
	{
		cin >> mem[i].age >> mem[i].name;
		mem[i].order = i;
	}

	sort(mem, mem + n,compare);
	
	for (int i = 0; i < n; i++)
		cout << mem[i].age << " " << mem[i].name << "\n";

	return 0;

}