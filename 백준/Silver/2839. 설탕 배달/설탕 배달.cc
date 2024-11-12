#include <iostream>

using namespace std;

int sugar(int n) {
	int result = n / 5;
	int balance = n % 5;
	
	if(balance==0){
		return result;
	}
	
	while (true){
        if(balance % 3 == 0){
            result += balance / 3;
            return result;
        }
        else {
            result -= 1;
            balance += 5;
            if (balance > n){
	            return -1;
            }
        }
  }
}

int main() {
    int n;
    cin >> n;
    cout << sugar(n) << endl;
    return 0;
}
