#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n,q;
    cin>>n>>q;
    vector<int> arr[n+1];
    
    for(int i=0;i<n;i++)
    {
        int t,tmp;
        cin>>t;
        while(t--)
        {
            cin>>tmp;
            arr[i].push_back(tmp);
        }
    }
    int a,b;
    for(int i=0;i<q;i++)
    {
        cin>>a>>b;
        cout<<arr[a][b]<<endl;
    }
    
    return 0;
}

