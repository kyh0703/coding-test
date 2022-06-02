#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
#include <string.h>
using namespace std;

// 정점의 개수 1 - 1000
const int MAX_VALUE = 1001;

int N, M, V;
vector<int> graph[MAX_VALUE];
bool visited[MAX_VALUE];

void DFS(int V)
{
    visited[V] = true;
    cout << V << " ";

    for (int i = 0; i < graph[V].size(); i++)
    {
        int next = graph[V][i];
        if (visited[next])
            continue;
        DFS(next);
    }
}

void BFS(int V)
{
    queue<int> q;
    q.push(V);
    visited[V] = true;

    while (!q.empty())
    {
        int v = q.front();
        q.pop();
        cout << v << " ";
        for (int i = 0; i < graph[v].size(); i++)
        {
            int next = graph[v][i];
            if (visited[next])
                continue;
            q.push(next);
            visited[next] = true;
        }
    }
}

int main()
{
    // 정점 == 노드
    cout << "==============================================" << endl;
    cout << "N 정점의 개수, M: 간선의 개수, V: 시작할 정점의 번호" << endl;
    cout << "==============================================" << endl;
    cin >> N >> M >> V;
    cout << "N:" << N << " ";
    cout << "M:" << M << " ";
    cout << "V:" << V << endl;

    int x, y;
    for (int i = 0; i < M; ++i)
    {
        // 양방향
        cin >> x >> y;
        graph[x].push_back(y);
        graph[y].push_back(x);
    }

    // 작은거부터 접근하기 위해
    for (int i = 1; i <= N; i++)
        sort(graph[i].begin(), graph[i].end());

    memset(visited, 0x00, sizeof(visited));
    DFS(V);
    cout << endl;

    memset(visited, 0x00, sizeof(visited));
    BFS(V);
    cout << endl;

    return 0;
}