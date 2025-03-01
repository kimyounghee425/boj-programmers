#include<iostream>
using namespace std;
long long A, B, C;

long long divide(long long a, long long b, long long c) {
	if (b == 1) {
		return a % c;
	}
	long long tmp = divide(a, b/2, c) % c;
	if( b % 2 == 0 ){
		return tmp * tmp % c;
	}
	else {
		return tmp * tmp % c * a % c;
	}
}
int main() {
	cin >> A >> B >> C;
	cout << divide(A, B, C);
}