#include <algorithm>
#include <iostream>
#include <queue>
#include <string.h>
using namespace std;

// 정점의 개수 1 - 1000
const int MAX_VALUE = 1001;

int N, M, V;
bool graph[MAX_VALUE][MAX_VALUE];
bool visited[MAX_VALUE];

void DFS(int v)
{
    visited[v] = true;
    cout << v << " ";

    for (int i = 1; i <= N; i++)
    {
        if (!graph[v][i] || visited[i])
            continue;
        DFS(i);
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
        for (int i = 1; i <= N; i++)
        {
            if (!graph[v][i] || visited[i])
                continue;
            q.push(i);
            visited[i] = true;
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
        cin >> x >> y;
        graph[x][y] = true;
        graph[y][x] = true;
    }

    memset(visited, 0x00, sizeof(visited));
    DFS(V);
    cout << endl;

    memset(visited, 0x00, sizeof(visited));
    BFS(V);
    cout << endl;

    return 0;
}