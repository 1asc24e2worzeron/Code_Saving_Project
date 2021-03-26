#include <stdio.h>

int pairs[100005], refuse;

int find(int x)
{
    if(pairs[x] < 0)
        return x;
    pairs[x] = find(pairs[x]);
    return pairs[x];
}

void Union(int x, int y)
{
	x = find(x);
	y = find(y);

	if(x == y){
        ++refuse;
		return;
	}

	if(pairs[x] <= pairs[y])
	{
		pairs[x] += pairs[y];
		pairs[y] = x;
	}
	else
	{
		pairs[y] += pairs[x];
		pairs[x] = y;
	}
}
int main()
{
        int check[2];
        int i;
        while(1){
            for(i = 0; i < 100005; ++i)
                pairs[i] = -1;
            refuse = 0;

            if(scanf("%d %d", &check[0], &check[1]) != 2)
                break;
            Union(check[0], check[1]);

            while(scanf("%d", &check[0]) != -1){
                if(check[0] == -1)
                    break;
                scanf("%d", &check[1]);
                Union(check[0], check[1]);
            }
            printf("%d\n", refuse);
        }
    return 0;
}