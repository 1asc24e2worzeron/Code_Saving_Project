#include <stdio.h>
#include <math.h>

int main()
{
    double n, val, ans;

    while(scanf("%lf%lf", &n, &val) != -1){
        ans = pow(val, 1/n);
        printf("%.0lf\n", ans);
    }

    return 0;
}