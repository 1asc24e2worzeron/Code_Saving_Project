#include <iostream>
#include <queue>

using namespace std;

struct point
{
    int x, y, d;
    point(int xin, int yin, int din)
    {
        x = xin;
        y = yin;
        d = din;
    }
    bool operator<(const point& rhs)const {return d > rhs.d;}
};

int main()
{
    int n, rows, columns, dir[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    int next[2];
    int i, j, k;
    priority_queue<point> q;

    cin >> n;

    for(i = 0;i < n; ++i){
        cin >> rows >> columns;
        int maze[rows][columns], sp[rows][columns];
        bool visit[rows][columns];
        for(j = 0; j < rows; ++j)
        for(k = 0; k < columns; ++k){
            cin >> maze[j][k];
            sp[j][k] = 1e7;
            visit[j][k] = false;
        }

        sp[0][0] = maze[0][0];
        q.push(point(0, 0, maze[0][0]));
        while(!q.empty()){
            point t = q.top();
            q.pop();

            if(visit[t.x][t.y])
                continue;
            visit[t.x][t.y] = true;
            for(j = 0; j < 4; ++j){
                next[0] = t.x + dir[j][0];
                next[1] = t.y + dir[j][1];
                if(next[0] >= 0 && next[0] < rows)
                if(next[1] >= 0 && next[1] < columns)
                    if(sp[next[0]][next[1]] > sp[t.x][t.y] + maze[next[0]][next[1]]){
                        sp[next[0]][next[1]] = sp[t.x][t.y] + maze[next[0]][next[1]];
                        q.push(point(next[0], next[1], sp[next[0]][next[1]]));
                    }
            }
        }
        cout << sp[rows-1][columns-1] << endl;
    }

    return 0;
}