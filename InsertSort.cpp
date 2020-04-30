/*INSERCION */

#include <iostream>
#include <ctime> 
using namespace std;
unsigned t0, t1;
int main()
{
	int* a;
	int tam,pos,auxi;
	int comparaciones = 0;
	int intercambios = 0;

cin>>tam;
a=new int[tam];
t0=clock();
for(int i=0;i<tam;i++)
{
	cout<<"a["<<i<<"]:";
	cin>>a[i];
}

for (int i=0;i<tam;i++)
{
	pos=i;
	auxi=a[i];
	comparaciones++;
	while((pos>0)&&(a[pos-1]>auxi)) //numero a su izq
	{
		//intercambio
		a[pos]=a[pos-1];
		pos--; //posicion disminuye
		intercambios++;
	}

	a[pos]=auxi;
}
for(int i=0;i<tam;i++)
{
  cout<<a[i]<<"-";
}
t1 = clock();
double time = (double(t1-t0)/CLOCKS_PER_SEC);
cout <<endl<< "Execution Time: " << time << endl;
cout << "Numero de comparaciones: " << comparaciones << endl;
cout << "Numero de intercambios: " << intercambios << endl;
delete[] a;
return 0;	
}
