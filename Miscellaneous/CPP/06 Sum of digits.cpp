#include<iostream>
using namespace std;
int sumofdigits(int a){
  int sum=0;
  while(a!=0){
    sum+=a%10;
    a/=10;
  }
  return sum;
}
int main(){
  int number;
  cout<<"Enter the number: ";
  cin >> number;
  cout<<"Sum of digits of "<<number<<" is "<<sumofdigits(number);
  return 0;
}