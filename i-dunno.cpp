#include <iostream>
using namespace std;

int main(){

const int capacity = 6;
int array[capacity];
  for(int i=1; i <= capacity; i++){
    array[i] = i;
    cout << array[i] << " ";
  }

int temp = array[capacity];
array[capacity] = array[0];
array[capacity] = temp;

for(int i=1; i <= capacity; i++){
  cout << array[i] << " ";
}


      return 0;
}
