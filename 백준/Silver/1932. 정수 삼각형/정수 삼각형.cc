#include <iostream>
#include <algorithm>
using namespace std;

int triangle[505][505];
int dp[505][505];

int main() {
    int answer = 0;
    int n;

    cin >> n;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < i + 1; ++j) {
            cin >> triangle[i][j];
        }
    }
	
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < i + 1; ++j) {
            if (i == 0 && j == 0)
                dp[i][j] = triangle[i][j];

            dp[i][j] = max(dp[i][j], triangle[i][j] + dp[i - 1][j]);

            if (j != 0)
                dp[i][j] = max(dp[i][j], triangle[i][j] + dp[i - 1][j - 1]);
        }
    }
	
    for (int i = 0; i < n; ++i) {
        answer = max(dp[n - 1][i], answer);
    }

    cout << answer;

    return 0;
}