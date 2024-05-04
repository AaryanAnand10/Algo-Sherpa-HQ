#include<iostream>
#include<string>
using namespace std;
int main(){
  string stringA;
  int a;
  cin >> stringA;
  a = stringA.length();
  a-=1;
  for (int i=a;i>-1;i--){
    cout << stringA[i];
  }
  return 0;
}
