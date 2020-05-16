#include <iostream>
#include <chrono>
#include <fstream>
using namespace std;
typedef chrono::microseconds micros;
void insertionSort(int v[], int N)
{
    int index;
    
    for (int i=1; i < N; i++)
    {
        index = v[i];
        
        int j = i-1;
        
        while (j >= 0 && v[j] > index)
        {
            v[j + 1] = v[j];
            j--;
        }
        
        v[j+1] = index;
    }
    
}

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

//-------------TIEMPO DEL ALGORITMO------------
void Imprimir_Algoritmo(string alg, micros dur)
{
    cout << alg << ": " << dur.count()<< " microsegundos" <<endl;
}

void fillFile(fstream & file)
{
    srand((int) time(NULL));
    for (int i = 0; i < 10000000000; ++i) {
        file << rand() % 10000 << endl;
    }
}

//-----------Open File-------------
void openFile(fstream & log)
{
    if (fopen("./valores.txt", "r"))
    {
        log.open("./valores.txt", fstream::in);//abrir o crear el archivo
        return;
    }
    else
    {
        cout << "Error!!... Creando uno nuevo" <<endl;
        log.open("./valores.txt", fstream::out);//abrir o crear el archivo
        cout << "llenando valores" <<endl;
        fillFile(log);
    }
    
}

void readValues(int* arr, int max,string path)
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

int main() 
{
    
    int N = 10;
    fstream textFile;
    openFile(textFile);
    int alto = 1000000;
    
    //Repetir desde N=10 hasta N=1000000
    while(N <= alto)
    {
        cout << "-------- " << N << " datos --------" <<endl; 
        //-----------------------------------Merge Sort-----------------------//
        int* a= new int[N];
        readValues(a, N, "./valores.txt");
        auto begin = chrono::high_resolution_clock::now();
        mergeSort(a, 0, N-1, N);
        auto end  = chrono::high_resolution_clock::now();
        auto merge = chrono::duration_cast<micros>(end-begin);
        Imprimir_Algoritmo("Merge Sort", merge);
        delete a;

        //-----------------------------------Insertion Sort-----------------------//
        a = new int[N];
        readValues(a, N, "./valores.txt");
        begin = chrono::high_resolution_clock::now();
        insertionSort(a, N);
        end = chrono::high_resolution_clock::now();
        auto insertion = chrono::duration_cast<micros>(end-begin);
        Imprimir_Algoritmo("Insertion Sort", insertion);
        delete a;
        N*=5;
    }
    return 0;
}
