// 알고리즘 스터디 - 기본수학2(2) : 백준 2581
// 소수 
// 20ms
#include <iostream>
#include <cmath>
using namespace std;

bool prime(int n) {
	if (n == 1)
		return false;
	for (int i = 2; i < n; i++) {
		if (n % i == 0) // 1과 n자기자신 이외에 나눠진다면
			return false;
	}
	return true;
}

int main(void) {
	unsigned int m,n, sum = 0,ele,j=0;
	cin >> m>>n;
	ele = n - m + 1;
	int* arr = new int[n];
	int* prr = new int[ele];
	for (int i = 0; i < ele; i++)
		prr[i] = 0;
	for (int i = 0; i < ele; i++) {
		arr[i] = m++;
		if (prime(arr[i]))
		{
			//cout << "arr["<<i<<"]: " << arr[i]<<endl;		
			sum += arr[i];
			prr[j++] = arr[i];
		}
	}
	if (prr[0] == 0)
		cout << -1;
	else {
		cout << sum << endl;
		cout << prr[0] << endl;
	}
	return 0;
}