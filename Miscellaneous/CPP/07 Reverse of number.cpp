#include<iostream>
using namespace std;
int reversenumber(int n){
  int rev=0;
  while(n>0){
    int lastdigit=n%10;
    rev=rev*10+lastdigit;
    n=n/10;
  }
  return rev;
}
int main(){
  int n;
  cout << "Enter a number ";
  cin >> n;
  cout << "Reverse of the number is " << reversenumber(n);
  return 0;
}