#include<iostream>
using namespace std;
bool primenumber(int n){
    if (n < 2){
        return false;
    }
    else{
        for(int i = 2; i < n; i++){
            if (n % i == 0){
                return false;
            }
        }
        return true;
    }
}
int main(){
    int n;
    cout << "Enter the number ";
    cin >> n;
    if (primenumber(n)){
        cout << "Prime Number";
    }
    else{
        cout << "Not Prime Number";
    }
    return 0;
}
