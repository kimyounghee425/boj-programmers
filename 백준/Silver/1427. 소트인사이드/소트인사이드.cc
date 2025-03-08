#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(){
    int N;
    string str;
    cin >> str; // 스트링 타입으로 입력받기
    N = str.length();    // 입력받은 숫자 길이
    int arr[N];
    int num = stoi(str);  // 숫자를 스트링에서 int 로 변환

    for (int i = 0; i < N; i++){
        arr[i] = num % 10;
        num /= 10;
    }



    for (int i = 0; i < N; i++){
        for (int j = 0; j < N-i-1; j++){
            if (arr[j] < arr[j+1]){
                swap(arr[j], arr[j+1]);
            }
        }
    }
    for (int i = 0; i < N; i++){
        cout << arr[i];
    }
    cout << endl;

}