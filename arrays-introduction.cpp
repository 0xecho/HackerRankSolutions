#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int m;
    cin>>m;
    int arr[m+10];
    for(int i=0;i<m;i++)
    {
        cin>>arr[i];
    }
    reverse(arr,arr+m);
    for(int i=0;i<m;i++)
    {
        cout<<arr[i]<<" ";
    }
    return 0;
}
