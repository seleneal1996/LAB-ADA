#include<iostream> 
#include<math.h>
#include<iomanip>
using namespace std;
double anterior,actual,proximo,a,b,c;

int fib(int n)
{
	if(n==0)
		return 0;
	if(n==1)
		return 1;
	return fib(n-1)+fib(n-2);
}

double fibbo_iterativo(double n)
{
  if (n==0)
  	return 0;
  anterior =0;
  actual =1;
  proximo=0;
  for (int i=1;i<n;i++)
  {
  	proximo= anterior+ actual;
  	anterior= actual;
  	actual=proximo;
  }
  return actual;
}

double fibbo_iterativo_mod(double n, double modulo)
{
  if (n==0)
    return 0;
  anterior =0;
  actual =1;
  proximo=0;
  for (int i=1;i<n;i++)
  {
    a=fmod(actual,modulo);
    b=fmod(anterior,modulo);
    c=a+b;
    proximo=fmod(c,modulo);
    anterior= actual;
    actual=proximo;
  }
  return actual;
}


int main()
{
  cout<<fibbo_iterativo_mod(1073741824,1048576)<<endl;
}
