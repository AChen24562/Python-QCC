#include <iostream>
using namespace std;

int main(){
  const int dim_1 = 2;
  const int dim_2 = 5;

  int matrix[dim_1][dim_2];

  int counter = 1;
  for(int i = 0; i < dim_1; i++){
    for (int j = 0; j < dim_2; j++){
      matrix[i][j] = counter;
      counter ++;
    }
  }

  for(int i=0; i<dim_1; i++) {
      for(int j=0; j<dim_2; j++) {
          cout << matrix[i][j] << " ";
      }
      cout << endl;
  }
  cout << endl << endl;




      return 0;
}
