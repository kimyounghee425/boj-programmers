#include <iostream>
#include <string>
#include <algorithm>
#include <utility>
using namespace std;



int main(){
    int N;
    cin >> N;

    int count2 = 0;
    int count5 = 0;
    for (int i = 1; i < N + 1; i++){
        int temp = i;
        while (temp % 2 == 0){
            count2++;
            temp /= 2;
        }
        temp = i;
        while (temp % 5 == 0){
            count5++;
            temp /= 5;
        }
    }

    cout << min(count2, count5) << endl;



    return 0;
}