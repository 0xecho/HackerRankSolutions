#include <bits/stdc++.h>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.'
    int a,b;
    cin>>a>>b;

    map<int,string> m;

    m[1]="one";
    m[2]="two";
    m[3]="three";
    m[4]="four";
    m[5]="five";
    m[6]="six";
    m[7]="seven";
    m[8]="eight";
    m[9]="nine";
    for(int i=a;i<=b;i++)
    {
        if(i<=9)
            cout<<m[i]<<endl;
        else 
            cout<<((i%2)?"odd":"even")<<endl;
            
    }
    return 0;
}

