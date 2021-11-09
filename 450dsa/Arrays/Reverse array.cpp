#include <bits/stdc++.h>
using namespace std;

void reverseArray(int arr[], int start, int end){
    if (start>=end){
        return;
    
    int temp = arr[start];
    arr[start] = arr[end];
    arr[end] = temp;

    reverseArray(arr, start+1, end-1);
    }
}

void printArray(int arr[], int size){
    for (int i=0; i<size; i++){
        cout << arr[i] << " ";
        cout << endl; 
    }
}