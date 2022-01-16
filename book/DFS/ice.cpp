#include <iostream>
using namespace std;

/*
N X M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는것으로 간주한다.
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.
다음의 4 * 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성된다.
00110
00011
11111
00000

입력조건
* 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다. (1 <= M , M <= 1000)
* 두 번째 줄부터 N+1번째 줄까지 얼음 틀의 형태가 주어진다.
* 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.
*/

const int MAX_VALUE = 1001;
int N, M;
bool ice[MAX_VALUE][MAX_VALUE];

bool DFS(int y, int x) {
    if (x <= -1 || M <= x || y <= -1 || N <= y)
        return false;

    if (ice[y][x])
        return false;

    ice[y][x] = true;
    DFS(y - 1, x);
    DFS(y, x - 1);
    DFS(y + 1, x);
    DFS(y, x + 1);
    return true;
}

int solution() {
    int answer = 0;

    for (int i = 0; i < N; ++i)
        for (int j = 0; j < M; ++j)
            if (DFS(i, j))
                answer++;

    return answer;
}

int main() {
    cout << "세로 N, 가로 M" << endl;
    cin >> N >> M;

    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < M; ++j)
        {
            int input = 0;
            cin >> input;
            ice[i][j] = (input == 0 ? false : true);
        }
    }

    cout << solution() << endl;
    return 0;
}