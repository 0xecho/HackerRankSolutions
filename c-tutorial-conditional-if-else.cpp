#include <bits/stdc++.h>

using namespace std;



int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

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
    if(n<=9)
        cout<<m[n]<<endl;
    else
        cout<<"Greater than 9"<<endl;

    return 0;
}
