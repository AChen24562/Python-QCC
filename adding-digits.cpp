#include <iostream>
using namespace std;

void add_digits(int num, int sum){
  if (num < 10){
    sum += num;
    cout << "Sum is finally: " << sum ;
  }
  else{
    sum += num % 10;
    cout << "Sum is now:" << sum << endl;
    add_digits(num / 10, sum);
  }
}


int main(){
int num = 345;
int sum = 0;
add_digits(num, sum);



      return 0;
}
