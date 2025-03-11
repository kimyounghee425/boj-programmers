#include <iostream>
#include <string>
#include <algorithm>
#include <utility>
#include <queue>
using namespace std;


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;

    queue<int> que;

    for (int i = 1; i < N + 1; i++){
        que.push(i);
    }

    int size = que.size();
    // cout << size << endl;
    for (int i = 0; i < size; i++){
        if (que.size() > 1){
            que.pop();
            int k = que.front();
            // cout << k << endl;
            que.pop();
            que.push(k);
        }
        else{
            break;
        }
    }

    cout << que.front() << endl;

    return 0;
}