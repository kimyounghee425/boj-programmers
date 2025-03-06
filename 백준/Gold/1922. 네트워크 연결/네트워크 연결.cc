#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 간선 정보 구조체
struct Edge {
    int u, v, cost;
    Edge(int _u, int _v, int _cost) : u(_u), v(_v), cost(_cost) {}
};

// 부모 노드를 찾는 함수 (Union-Find 알고리즘)
int findParent(int node, int parent[]) {
    if (parent[node] == node) return node;
    return parent[node] = findParent(parent[node], parent);
}

// 두 노드를 연결하는 함수 (Union-Find 알고리즘)
bool unionNodes(int u, int v, int parent[], int rank[]) {
    int rootU = findParent(u, parent);
    int rootV = findParent(v, parent);

    if (rootU == rootV) return false;

    if (rank[rootU] > rank[rootV]) {
        parent[rootV] = rootU;
    } else if (rank[rootU] < rank[rootV]) {
        parent[rootU] = rootV;
    } else {
        parent[rootV] = rootU;
        rank[rootU]++;
    }

    return true;
}

int main() {
    int N, M; // 컴퓨터 수와 간선 수
    cin >> N >> M;

    vector<Edge> edges;
    for (int i = 0; i < M; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        edges.push_back(Edge(a, b, c));
    }

    // 간선을 비용 기준으로 오름차순 정렬
    sort(edges.begin(), edges.end(), [](Edge a, Edge b) {
        return a.cost < b.cost;
    });

    // Union-Find 초기화
    int parent[N + 1], rank[N + 1];
    for (int i = 1; i <= N; i++) {
        parent[i] = i;
        rank[i] = 0;
    }

    int mstCost = 0; // 최소 스패닝 트리의 비용
    int edgeCount = 0;

    // 크루스칼 알고리즘
    for (Edge e : edges) {
        if (unionNodes(e.u, e.v, parent, rank)) {
            mstCost += e.cost;
            edgeCount++;

            // MST가 완성되었으면 종료
            if (edgeCount == N - 1) break;
        }
    }

    cout << mstCost << endl;

    return 0;
}