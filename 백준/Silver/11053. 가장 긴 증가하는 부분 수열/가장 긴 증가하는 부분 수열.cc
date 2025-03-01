#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

const int MN = 1001;

int dp[MN];
int arr[MN];

int main() {
    int N; cin >> N;
    int res = 0;

    for(int i = 0; i < N; i++)
        cin >> arr[i];

    for(int i = 0; i < N; i++) {
        dp[i] = 1;
        for(int j = 0; j < i; j++) {
            if(arr[i] > arr[j]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        res = max(res, dp[i]);
    }

    cout <<res;
}