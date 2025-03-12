#include <iostream>
#include <string>
#include <algorithm>
#include <utility>
using namespace std;

bool binary_search(int arr[], int size, int target){
    int low = 0;
    int high = size - 1;
    int mid;
    
    while (low <= high){
        mid = (low + high) / 2;
        if (target < arr[mid]){ // 타겟이 mid 보다 작으면 high 를 mid - 1 로 수정
            high = mid - 1;
        }
        else if (target > arr[mid]){    // 타겟이 mid 보다 크면 low 를 mid + 1 로 수정
            low = mid + 1;
        }
        else{   // 계속 나누다보면 target == mid 인 때가 올거임. 그러면 mid 반환
            return true;
        }
    }
    return false; // 타겟이 배열에 없을 때

}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;
    int arr[N];
    for (int i = 0; i < N; i++){
        cin >> arr[i];
    }
    // 정적 배열일 땐 sizeof 를 이용해 배열의 크기를 구한다.
    // 전체 배열의 크기를 자료형 크기로 나누면 된다.
    int arr_size = (sizeof(arr) / sizeof(*arr));

    sort(arr, arr + arr_size); // arr 을 일단 정렬해 놔.

    int M;
    cin >> M;
    int arr2[M];    // 비교군 만듦.
    for (int i = 0; i < M; i++){
        cin >> arr2[i];
    }
    // int arr2_size = (sizeof(arr2) / sizeof(*arr));

    int answer[M];

    for (int i = 0; i < M; i++){
        if (binary_search(arr, arr_size, arr2[i])){
            answer[i] = 1;
        }
        else{
            answer[i] = 0;
        }
    }

    for (int i = 0; i < M; i++){
        cout << answer[i] << "\n";
    }
    cout << endl;

    return 0;
}