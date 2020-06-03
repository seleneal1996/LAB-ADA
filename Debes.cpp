#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
using namespace std;
 
long dim = 1000;
const long max_dim = 300000;
 
int list[max_dim];
 
void read()
{
    ifstream fin("random.dat", ios::binary);
    for (long i = 0; i < dim; i++)
    {
        fin.read((char*)&list[i], sizeof(int));
    }
    fin.close();
}
 
void bubbleSort()
{
    int temp;
    for(long i = 0; i < dim; i++)
    {
        for(long j = 0; j < dim-i-1; j++)
        {
            if (list[j] > list[j+1])
            {
                temp        = list[j];
                list[j]     = list[j+1];
                list[j+1]   = temp;
            }
        }
    }
}
void insertionSort()
{
    int temp;
    for(long i = 1; i < dim; i++)
    {
        temp = list[i];
        long j;
        for(j = i-1; j >= 0 && list[j] > temp; j--)
        {
            list[j+1] = list[j];
        }
        list[j+1] = temp;
    }
}

int main()
{
    double t1, t2;
 
    for (dim = 1000; dim <= max_dim; )
    {
        cout << "\ndim\t: " << dim << '\n';
 
        read();
        t1 = clock();
        bubbleSort();
        t2 = clock();
        cout << "Burbuja\t: " << (t2 - t1)/CLK_TCK << " sec\n";
 
        read();
        t1 = clock();
        insertionSort();
        t2 = clock();
        cout << "Insercion\t: " << (t2 - t1)/CLK_TCK << " sec\n";
         
        switch (dim)
        {
        case 500 :
            dim = 500;
            break;
        case 1000 :
            dim = 1000;
            break;
        case 2000 :
            dim = 2000;
            break;
        case 5000 :
            dim = 5000;
            break;
        case 10000 :
            dim = 10000;
            break;
        case 20000 :
            dim = 20000;
            break;
        }
    }
 
    return 0;
}
