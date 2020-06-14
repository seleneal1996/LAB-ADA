#include <iostream>
#include <fstream>
#include <stdlib.h>     
#include <time.h>      
#include <algorithm>
unsigned t0_qs, t1_qs,t0_s,t1_s,t0_ms,t1_ms;
using namespace std;

void merge(int v[], int l, int m, int n, int N)
{
    int i, j, k;
    int aux[N];  
    
    for(i=m+1;i>l;i--)
        aux[i-1] = v[i-1];
    
    for (j=m; j<n; j++)
        aux[n+m-j] = v[j+1];
    
    for(k=l;k<=n;k++)       
        if (!(aux[i]> aux[j])) 
            v[k] = aux[i++];
        else
            v[k] = aux[j--];
}

void mergeSort(int v[], int l, int n, int N)
{
    int m = (n+l)/2;
    if (n > l)
    {
        mergeSort (v, l, m, N);
        mergeSort (v, m+1, n, N);
        merge (v, l, m, n, N);
    }
}

void rellenar_Archivo(fstream & file)
{
    srand((int) time(NULL));
    for (int i = 0; i < 1000000; ++i) 
	{
        file << rand() % 100 << endl;
    }
}

void Abrir_Archivo(fstream & log)
{
    if (fopen("./valores.txt", "r"))
    {
        log.open("./valores.txt", fstream::in);
        return;
    }
    else
    {
        cout << "Error!!" <<endl;
        log.open("./valores.txt", fstream::out);
        cout << "llenando valores" <<endl;
        rellenar_Archivo(log);
    }
    
}

void lectura_Valores(int* arr, int max,string path)
{
    ifstream file(path);
    int cont = 0;
    string line;
    
    while ( getline (file,line) )
    {
        arr[cont] = stoi(line);
        cont++;
        if(cont >= max)
            return;
    }
}



int compare(const void * duf, const void * our) 
{ 
    return ( *(int*)duf - *(int*)our ); 
}

int main() 
{
    int N = 1000;
    fstream textFile;
    ofstream archivo("Comparando.txt");
    Abrir_Archivo(textFile);
    int alto = 400000;
    while(N <= alto)
    {
		cout << "-------- " << N << " datos --------" <<endl; 
        int* a= new int[N];
        lectura_Valores(a, N, "valores.txt");
        t0_qs=clock();
	    qsort(a, N, sizeof(int), compare); 
	    t1_qs = clock();
	    double time_Qs = (double(t1_qs-t0_qs)/CLOCKS_PER_SEC);
	    cout << "Usando qsort() - "<< time_Qs << endl; 
     	
     	delete a;
     	
     	a= new int[N];
     	lectura_Valores(a, N, "valores.txt");
	    t0_s=clock();
	    sort(a, a + N); 
	    t1_s = clock(); 
	    double time_s = (double(t1_s-t0_s)/CLOCKS_PER_SEC);
	    cout << "Usando sort() - "<< time_s << endl; 
	    
	    delete a;
	    
	    a= new int[N];
	    lectura_Valores(a, N, "valores.txt");
	    t0_ms = clock(); 
	    mergeSort(a, 0, N-1, N);
	    t1_ms = clock(); 
	    double time_ms = (double(t1_ms-t0_ms)/CLOCKS_PER_SEC);
	    cout << "Usando Merge sort() - "<< time_ms << endl; 
	    delete a;
     	N=N+1000;
     	archivo<<"qsort:"<<"  "<<time_Qs <<" "<<','<<"Sort:"<<" "<< time_s<<" "<<','<<"Merge:"<<" "<< time_ms<<endl;
    }
    return 0;
}
