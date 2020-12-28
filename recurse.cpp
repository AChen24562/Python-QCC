#include <iostream>

using namespace std;

int recurs(int num){
  if(num < 1){
    cout << num;
  }

  else{
    cout << num << " ";
    num --;
    return recurs(num);
  }
  return 0;
}


int main(){
int num = 10;

recurs(num);



      return 0;
}
