#include<iostream>
using namespace std;
void fibonacci(int n){
  int first = 0;
  int second = 1;
  cout << first << " " << second << " ";
  for(int i = 2; i < n; i++){
    int next = first + second;
    first = second;
    second = next;
    cout << next << " ";
  }
}
int main(){
  int num;
  cout << "Enter the number of terms: ";
  cin >> num;
  fibonacci(num);
  return 0;
}