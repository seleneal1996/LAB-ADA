// Selene Barrios Cornejo
#include <bits/stdc++.h> //Importa todas las librerias
using namespace std;
//declaracion de variables 
long long tt,vecss,n,m,s,t,u,v,c;
vector<long long> g[20004],cost[20004];
long long vecs[20004];

struct nodo
{
    long long u,c;
};

bool com(nodo a,nodo b)
{
    return a.c>b.c;
}
typedef bool (*comp)(nodo,nodo);
priority_queue<nodo, vector<nodo>, comp> q(com);

void dijktra()
{
    nodo A,B;
    long long k,sz,z;

    while(!q.empty())
    {
        A = q.top();
        q.pop();
        if(A.u==t)
            return;
        sz = g[A.u].size();

        for(k = 0; k<sz; k++)
        {
            z = g[A.u][k];
            if(vecs[z]> vecs[A.u]+cost[A.u][k])
            {
                vecs[z]=vecs[A.u]+cost[A.u][k];
                B.u = z;

                B.c = vecs[z];
                q.push(B);
            }
        }

    }

}

int main()
{
    cin>>tt;
    while(tt--)
    {
        
        cin>>n>>m>>s>>t;
        long long i;
        for(i=0; i<n; i++)
        {
            g[i].clear();
            cost[i].clear();
            vecs[i] = LONG_LONG_MAX;
        }
        vecs[s] = 0;

        while(m--)
        {
            cin>>u>>v>>c;
            g[u].push_back(v);
            g[v].push_back(u);
            cost[u].push_back(c);
            cost[v].push_back(c);
        }
        nodo x;
        x.u = s;
        x.c = 0;
        q.push(x);
        dijktra();
        cout<<"Case #"<<vecss;
        if(vecs[t]==LONG_LONG_MAX)
            cout<<"unreachable\n";
        else 
            cout<<vecs[t];
        while(!q.empty())
        q.pop();

    }

}

