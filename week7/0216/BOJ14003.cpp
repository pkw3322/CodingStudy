#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int n;
int arr[1000010];
int indexOfArr[1000010];
vector<int> LIS;
vector<int> answer;

int main(){
    cin >> n;
    for(int k = 1; k <= n; k++){
        cin >> arr[k];
    }

    for(int i = 1; i <= n; i++){
        if(LIS.size() == 0 || LIS[LIS.size()-1] < arr[i]){
            LIS.push_back(arr[i]);
            indexOfArr[i] = LIS.size()-1;
        }
        else{
            int left = 0;
            int right = LIS.size() - 1;
            int mid;
            while(left < right){
                mid = (left + right)/2;
                if(LIS[mid] >= arr[i])
                    right = mid;
                else
                    left = mid + 1;
            }
            LIS[left] = arr[i];
            indexOfArr[i] = left;
        }
    }

    cout << LIS.size() << '\n';
    int find = LIS.size() - 1;
    for(int i = n; i > 0; i--){
        if(indexOfArr[i] == find){
            find--;
            answer.push_back(arr[i]);
        }
    }
    for(int k = answer.size()-1; k >= 0; k--){
        cout << answer[k] << " ";
    }
    return 0;
}