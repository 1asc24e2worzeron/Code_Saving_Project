#include <stdio.h>

int main()
{
    int m, n, cnt;
    int u, d, mid, l, r, val, ans;
    while(scanf("%d%d", &m, &n) != -1){
        ans = 1e9;
        cnt = 0;
        while(cnt < n){
            scanf("%d%d", &u, &d);
            l = 0;
            r = m;
            while(l <= r){
                mid = (l + r)/2;
                val = mid*u - (m - mid)*d;
                if(val > 0){
                    r = mid - 1;
                    ans = val < ans ? val : ans;
                }
                else
                    l = mid + 1;
            }
            ++cnt;
        }
        printf("%d\n", ans);
    }

    return 0;
}