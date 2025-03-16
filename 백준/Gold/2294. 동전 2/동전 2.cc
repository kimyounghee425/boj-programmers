#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int main() {
    int n, k; // 동전 종류 수와 목표 금액
    cin >> n >> k;

    vector<int> coins(n);

    // 동전의 가치 입력
    for (int i = 0; i < n; i++) {
        cin >> coins[i];
    }

    // DP 배열 초기화
    vector<int> dp(k + 1, INT_MAX); // dp[i]: 금액 i를 만들기 위한 최소 동전 개수
    dp[0] = 0; // 금액 0을 만드는 데 필요한 동전 개수는 0

    // DP 계산
    for (int i = 0; i < n; i++) {
        for (int j = coins[i]; j <= k; j++) {
            if (dp[j - coins[i]] != INT_MAX) { // 이전 금액이 구성 가능하면
                dp[j] = min(dp[j], dp[j - coins[i]] + 1);
            }
        }
    }

    // 결과 출력
    if (dp[k] == INT_MAX) {
        cout << -1 << endl; // 목표 금액을 만들 수 없는 경우
    } else {
        cout << dp[k] << endl; // 최소 동전 개수 출력
    }

    return 0;
}