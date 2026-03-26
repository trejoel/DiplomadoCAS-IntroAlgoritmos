//The following program look for an element in an unsorted vector
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define bool int
#define true 1
#define false 0

double *generateRandomArray(int numberOfElements);

double *ordenamientoBurbuja(int numberOfElements);


int main(int argc, char *argv[]){
   double *A;
   int n;
   printf("De cuantos elementos son los arreglos\n");
   scanf("%d",&n);
   A=generateRandomArray(n);
   free(A);
}


double *generateRandomArray(int numberOfElements){
   double *myArray;
   srand(time(NULL));
   myArray=malloc(numberOfElements*sizeof(double));
   for (int i=0;i<numberOfElements;i++){
       //myArray[i]=rand() % 100 + 1;
         myArray[i]=i;
   }
   return myArray;
}


double *ordenamientoBurbuja(int numberOfElements){
	double *sortedVector;
	srand(time(NULL));
   	sortedVector=malloc(numberOfElements*sizeof(double));
	return sortedVector;

}

