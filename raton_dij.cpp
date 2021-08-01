#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;
//BARRIOS CORNEJO SELENE

//Declaracion de vriables
int cases;
int n, e, t, m, u, v, w;
int M[105][105];

int main() 
{
	cin>> cases;
	while (cases--) 
	{
		cin>>n>>e>>t>>m;
		memset(M, 63, sizeof M);
		n++;
		for (int i = 0; i < m; i++) 
		{
			cin>> u>>v>>w;
			M[u][v] = w;
		}

		//Warshall
		for (int k = 0; k < n; k++)
			for (int i = 0; i < n; i++)
				for (int j = 0; j < n; j++)
					M[i][j] = min(M[i][j],
						M[i][k] + M[k][j]);

		int rpta = 0;
		for (int i = 0; i < n; i++)
			if (M[i][e] <= t || (i == e))
				rpta++;

		cout<<rpta<<endl;
		if (cases)
			cout<<"\n";
	}

	return 0;
}
