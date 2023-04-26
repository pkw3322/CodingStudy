#include<iostream>
#include<vector>
#include<cmath>

using namespace std;

class SegTree{
private:
    long long* nodes;
    long long* A;

    long long init(int idx,int start,int end){
        if(start == end)
            nodes[idx] = A[start];
        else
            nodes[idx] = init(2*idx+1,start,(start+end)/2) + init(2*idx+2,(start+end)/2+1,end);
        return nodes[idx];
    }

public:
    SegTree(int n,long long* A){
        int hight = (int)ceil(log2(n));
        int node_size = 1 << (hight+1);
        nodes = new long long[node_size];
        this->A = A;
        init(0,0,n-1);
    }

    ~SegTree(){
        delete [] nodes;
    }

    long long getSum(int idx,int start,int end,int left, int right){
        if(left > end || right < start)
            return 0;
        else if(left <= start && right >= end)
            return nodes[idx];
        
        return getSum(2*idx+1,start,(start+end)/2,left,right)+
               getSum(2*idx+2,(start+end)/2+1,end,left,right);
    }

    void update(int changed_idx,long long dif, int idx, int start, int end){
        if(changed_idx < start || changed_idx > end)
            return ;
        nodes[idx] += dif;

        if(start != end){
            update(changed_idx,dif,2*idx+1,start,(start+end)/2);
            update(changed_idx,dif,2*idx+2,(start+end)/2+1,end);
        }
    }
};

int n,m,k;
long long arr[1000001];
vector<long long int> ans;

int main(){
    cin >> n >> m >> k;
    int a,b,c;
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    SegTree segTree(n,arr);

    for(int i = 0; i < m+k; i++){
        cin >> a >> b;
        if(a == 1){
            long long c;
            cin >> c;

            long long dif = c - arr[b-1];
            arr[b-1] = c;
            segTree.update(b-1,dif,0,0,n-1);
        }
        else{
            int c;
            cin >> c;
            ans.push_back(segTree.getSum(0,0,n-1,b-1,c-1));
        }
    }

    for(int i = 0; i < ans.size(); i++){
        cout << ans[i] << '\n';
    }
    return 0;
}
