#include <iostream>
#include <math.h>

using namespace std;

long long H(int n){
    long long res = 0, n_root = sqrt(n);
    int i;

    for(i = 1; i <= n_root; ++i)
        res += n/i;
    return 2*res - n_root*n_root;
}


int main()
{
    int t, c = 0, res;
    cin >> t;
    while(c < t){
        cin >> res;
        cout << H(res) << endl;
        ++c;
    }
    return 0;
}

/*
1

2       1
3       1 1

4 2     1 1
5 2     1 1 1
6 3     2 1 1 1
7 3     2 1 1 1 1
8 4     2 2 1 1 1 1

9 4 3   2 1 1 1 1 1
*/