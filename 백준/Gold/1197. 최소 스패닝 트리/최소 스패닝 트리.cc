#include <iostream>
#include <algorithm>

using namespace std;

const int MAX_V = 10001; // 최대 정점 수
const int MAX_E = 100000;// 최대 간선 수

struct Edge {
    int u, v, weight;
};


int parent[MAX_V]; // 부모 노드 저장
int rankArr[MAX_V]; // 트리의 랭크 저장
Edge edges[MAX_E];  // 간선 정보를 저장하는 배열

// 유니온 파인드 함수
int find(int x) {
    if (parent[x] == x) return x;
    return parent[x] = find(parent[x]);
}

void unionSets(int a, int b) {
    a = find(a);
    b = find(b);

    if (a != b) {
        if (rankArr[a] < rankArr[b]){
            swap(a, b);
        }
        parent[b] = a;
        if (rankArr[a] == rankArr[b]){
            rankArr[a]++;
        }
    }
}


// 간선 정렬을 위한 비교 함수
bool compareEdges(const Edge &a, const Edge &b) {
    return a.weight < b.weight;
}

void kruskal (int V, int E) {
    // 부모 배열과 랭크 배열 초기화
    for (int i = 0; i <= V; i++) {
        parent[i] = i;  // 각 정점은 처음에 자기 자신을 부모로 갖는다
        rankArr[i] = 0; // 모든 트리의 랭크는 초기값 0 으로 설정된다
    }

    // 간선을 가중치 기준으로 정렬
    sort(edges, edges + E, compareEdges);

    long long totalWeight = 0;
    int edgeCount = 0;

    // 간선을 하나씩 선택
    for (int i = 0; i < E; i++) {
        int u = edges[i].u;
        int v = edges[i].v;
        int weight = edges[i].weight;

        if (find(u) != find(v)) {   // 사이클이 발생하지 않으면
            unionSets(u, v);        // 두 정점을 연결
            totalWeight += weight;  // 가중치를 더함
            edgeCount++;
            if (edgeCount == V - 1) break;  // MST 완성
        }

    }

    cout << totalWeight << endl;
}



int main() {
    // V 는 노드 수, E 는 간선 수
    int V, E;
    cin >> V >> E;

    // 간선 입력
    for (int i = 0; i < E; i++) {
        cin >> edges[i].u >> edges[i].v >> edges[i].weight;
    }

    // 크루스칼 알고리즘 실행
    kruskal(V, E);
    return 0;
}