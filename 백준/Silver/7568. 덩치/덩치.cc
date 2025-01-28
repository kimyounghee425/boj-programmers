#include <iostream>
#include <utility>
using namespace std;
 
 
int main(void)
{
    int N;
    int x[50] = { 0 };
    int y[50] = { 0 };
    cin >> N;
 
    for (int i = 0; i < N; i++) {
        cin >> x[i] >> y[i];
    }
 
    for (int i = 0; i < N; i++) {
        int rank = 1;
        for (int j = 0; j < N; j++) {
            if (x[i] < x[j] && y[i] < y[j])
                rank++;
        }
        cout << rank << " ";
    }
 
    return 0;
}
