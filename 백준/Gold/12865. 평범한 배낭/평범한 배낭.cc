#include <iostream>
#include <algorithm>
using namespace std;


int n, k;
int w[100001] = { 0, };
int v[1001] = { 0, };
int dp[101][100001] = { 0, };

int main() {

	ios_base::sync_with_stdio(false);
	cin.tie(0);

	cin >> n >> k;

	for (int i = 1; i <= n; i++) 
		cin >> w[i] >> v[i];
	
	for(int i=1;i<=n;i++)
		for (int j = 1; j <= k; j++) {
			if (w[i] <= j) {
				dp[i][j] = max(dp[i - 1][j], v[i] + dp[i - 1][j - w[i]]);
			}
			else
				dp[i][j] = dp[i - 1][j];
		}
	cout << dp[n][k] << endl;


	return 0;
}