// 알고리즘 스터디 - 기본수학1(7) : 백준 2839
// 설탕 배달
// 0ms

#include <iostream>
using namespace std;

int main(){
	int input;
	int count = 0;
	
	cin>>input;
	
	while(input > 0){
		if(input % 5 == 0){
			input -=5;
			count++;
		}
		else if(input % 3 ==0){
			input -=3;
			count++;
		}
    else if(input>5) {
      input-=5;
      count++;
    }
		else{
			count = -1;
			break;
		}
		
	}
	cout << count;

  return 0;
}