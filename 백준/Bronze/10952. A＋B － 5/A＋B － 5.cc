#include <iostream>
using namespace std;

int main (){
    int num1, num2;
    int result =0;

    while(true){

        cin >> num1 >> num2;

        if ((num1==0) && (num2 ==0)){
            break;
        }

        result = num1+num2;
        cout << result<<endl;
    }



}