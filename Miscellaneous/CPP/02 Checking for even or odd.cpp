#include<iostream>
using namespace std;

string oddeven(int n){
    if (n % 2 == 0){
        return "Even";
    }
    else
        return "Odd";
}

int main(){
    int num;
    cout << "Enter a number ";
    cin >> num;
    cout << "The number is " << oddeven(num) << endl;
}