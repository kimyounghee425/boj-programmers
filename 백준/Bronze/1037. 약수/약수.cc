#include <iostream>
using namespace std;

int main() {
    int num_divisors; 
    cin >> num_divisors;

    int first, min_val, max_val;
    cin >> first;
    min_val = max_val = first;

    for (int i = 1; i < num_divisors; i++) {
        int d;
        cin >> d;
        if (d < min_val) min_val = d;
        if (d > max_val) max_val = d;
    }

    int N = min_val * max_val;
    
    cout << N << endl;

    return 0;
}
