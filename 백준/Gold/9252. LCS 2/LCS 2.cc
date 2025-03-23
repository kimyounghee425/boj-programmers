#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

const int MAX = 1000;
int dp[MAX + 1][MAX + 1]; 

pair<int, string> LCS(const string &X, const string &Y) {
    int m = X.size();
    int n = Y.size();

    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            if (i == 0 || j == 0) {
                dp[i][j] = 0; 
            } else if (X[i - 1] == Y[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    int index = dp[m][n];
    string lcsStr(index, ' ');

    int i = m, j = n;
    while (i > 0 && j > 0) {
        if (X[i - 1] == Y[j - 1]) {
            lcsStr[index - 1] = X[i - 1];
            i--;
            j--;
            index--;
        } else if (dp[i - 1][j] > dp[i][j - 1]) {
            i--;
        } else {
            j--;
        }
    }

    return {dp[m][n], lcsStr};
}

int main() {

    string X, Y;
    cin >> X >> Y;

    auto result = LCS(X, Y);
    int lcsLength = result.first;
    string lcsStr = result.second;

    cout << lcsLength << endl;
    cout << lcsStr << endl;

    return 0;
}