/*BURBUJA*/

#include <iostream>
#include <ctime> 
using namespace std;
unsigned t0, t1;

int main()
{
int num, aux;
int comparaciones = 0;
int intercambios = 0;
int* arreglo;
cin>>num;
arreglo = new int[num];

t0=clock();
for(int x = 0; x < num; x++)
{
	cout << "a[" << x << "]: ";
    cin >> arreglo[x];
}

 for(int z = 1; z < num; ++z)
 {
      for(int v = 0; v < (num - z); v++)
      {
         comparaciones++;
         if(arreglo[v] > arreglo[v+1])
         {
            aux = arreglo[v];
            arreglo[v] = arreglo[v + 1];
            arreglo[v + 1] = aux;
            intercambios++;
         }
         
      }
    
 }

for(int w = 0; w < num; w++)
{
  cout <<arreglo[w]<<"-";
}
t1 = clock();

double time = (double(t1-t0)/CLOCKS_PER_SEC);
cout <<endl<< "Execution Time: " << time << endl;
cout << "Numero de comparaciones: " << comparaciones << endl;
cout << "Numero de intercambios: " << intercambios << endl;
delete[] arreglo;
return 0;
}
