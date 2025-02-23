#include <iostream>
#include <vector>
using namespace std;

int n;
int lc[27]; // a가 1번
int rc[27];

void preOrder(int node) {
    if (node == 0)
        return;
    cout << (char)(node + 'A' - 1);
    preOrder(lc[node]);
    preOrder(rc[node]);
}

void inOrder(int node) {
    if (node == 0)
        return;
    inOrder(lc[node]);
    cout << (char)(node + 'A' - 1);
    inOrder(rc[node]);
}

void postOrder(int node) {
    if (node == 0)
        return;
    postOrder(lc[node]);
    postOrder(rc[node]);
    cout << (char)(node + 'A' - 1);
}

int main() {
    cin >> n;

    char alpha, l, r;
    for (int i = 0; i < n; i++) {
        cin >> alpha >> l >> r;
        if (l != '.')
            lc[(alpha - 'A' + 1)] = (l - 'A' + 1);
        if (r != '.')
            rc[(alpha - 'A' + 1)] = (r - 'A' + 1);
    }

    preOrder(1);
    cout << "\n";
    inOrder(1);
    cout << "\n";
    postOrder(1);
}