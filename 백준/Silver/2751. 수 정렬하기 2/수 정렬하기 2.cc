#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

// 왼쪽 부분 배열과 오른쪽 부분 배열을 합치는 함수
void merge(int arr[], int left, int mid, int right){
    int n1 = mid - left + 1; // 왼쪽 부분 배열 크기
    int n2 = right - mid; // 오른쪽 부분 배열 크기

    int L[n1], R[n2]; // 왼쪽 배열, 오른쪽 배열 생성

    for (int i = 0; i < n1; i++){
        L[i] = arr[left + i]; // 왼쪽 배열에 원소 집어넣기
    }
    for (int i = 0; i < n2; i++){
        R[i] = arr[mid + 1 + i]; // 오른쪽 배열에 원소 집어넣기
    }
    
    // 두 배열이 만들어졌으니 앞에서부터 원소의 크기를 비교해가며 합쳐야 함
    int i = 0; // 왼쪽 배열의 현재 인덱스
    int j = 0; // 오른쪽 배열의 현재 인덱스
    int k = left; // 원본 배열의 현재 인덱스
    while (i < n1 && j < n2){
        if (L[i] <= R[j]){
            arr[k] = L[i];
            k++;
            i++;
        }
        else{
            arr[k] = R[j];
            k++;
            j++;
        }
    }
    while (i < n1){
        arr[k] = L[i];
        k++;
        i++;
    }
        while (j < n2){
        arr[k] = R[j];
        k++;
        j++;
    }
}

// 재귀로 머지 병합 수행
void mergeSort(int arr[], int left, int right){
    if (left < right){ // 분달된 리스트의 원소 수가 1개가 될 때까지 나눠야 하므로
        int mid = (left + right) / 2;

        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

int main(){
    int N;
    cin >> N;
    int arr[N];
    for (int i = 0; i < N; i++){
        cin >> arr[i];
    }
    int size = sizeof(arr) / sizeof(*arr);
    mergeSort(arr, 0, size - 1);

    for (int i=0; i < size; i++){
        cout << arr[i] << "\n";
    }
}