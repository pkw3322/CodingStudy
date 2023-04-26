#include<iostream>
#include <algorithm>
#include<vector>

using namespace std;

int n, d;

typedef struct{
    int num;
    vector<int> child;
} Node;

void deleteNode(Node arr[],int del){
    
    if(!arr[del].child.empty()){
        for (vector<int>::iterator iter = arr[del].child.begin(); iter != arr[del].child.end(); iter++) {
            deleteNode(arr,*iter);
        }
        arr[del].child.clear();
    }
    arr[del].num = -2;
}

int leaf(Node arr[],int n){
    int cnt = 0;
    for(int i = 0; i < n; i++){
        if(arr[i].num == -2)
            continue;
        if(arr[i].child.empty()){
            cnt++;
        }
    }
    return cnt;
}

int main(){
    cin >> n;
    Node arr[n];
    int parent;
    for (int i = 0; i < n; i++)
        cin >> arr[i].num;
    
    cin >> d;
    if(arr[d].num == -1){
        cout << 0;
        return 0;
    }
    for(int i = 0; i < n; i++){
        if(arr[i].num != -1){
            arr[arr[i].num].child.push_back(i);
        }
    }
    parent = arr[d].num;
    deleteNode(arr,d);
    arr[parent].child.erase(find(arr[parent].child.begin(),arr[parent].child.end(),d));
    cout << leaf(arr,n);
    return 0;
}