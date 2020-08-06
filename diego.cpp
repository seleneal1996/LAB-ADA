#include <iostream>
#include <vector>

using namespace std;

vector<vector <int> > multMatrix2(vector<vector <int> > a, vector<vector <int> > b) {
    vector<vector <int> > c;
    c.resize(2);
    c[0].resize(2);
    c[1].resize(2);

    c[0][0] = a[0][0]*b[0][0] + a[0][1]*b[1][0];
    c[0][1] = a[0][0]*b[0][1] + a[0][1]*b[1][1];
    c[1][0] = a[1][0]*b[0][0] + a[1][1]*b[1][0];
    c[1][1] = a[1][0]*b[0][1] + a[1][1]*b[1][1];

    return c;
}

vector<vector <int> > powMatrix(vector<vector <int> > a, int potencia) {
    vector<vector <int> > rpta;
    if(potencia == 2) {
        return multMatrix2(a,a);
    }
    else {
        return multMatrix2(powMatrix(a,potencia/2),powMatrix(a,potencia/2));
    }

}
int main() {
    vector<vector <int> > a;/* 
    vector<vector <int> > b; */
    a.resize(2);
    a[0].resize(2);
    a[1].resize(2);/* 
    b.resize(2);
    b[0].resize(2);
    b[1].resize(2); */
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            cin>>a[i][j];
        }
    }/* 
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            cin>>b[i][j];
        }
    } */

    vector<vector <int> > c = powMatrix(a,4);
    
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            cout<<c[i][j]<<' ';
        }
        cout<<endl;
    }
    return 0;
}