#include <iostream>
#include <algorithm>

using namespace std;

long long _x1, _x2, _x3, _x4;
long long _y1, _y2, _y3, _y4;
long long ccw(long long x1, long long y1,long long x2, long long y2,long long x3, long long y3){
    long long tmp = (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1);

	if (tmp > 0) 
        return 1;
	else if (tmp == 0) 
        return 0;
	else if (tmp < 0) 
        return -1;
}

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cin >> _x1 >> _y1 >> _x2 >> _y2 >> _x3 >> _y3 >> _x4 >> _y4;

  long long ans1 = ccw(_x1,_y1,_x2,_y2,_x3,_y3) * ccw(_x1,_y1,_x2,_y2,_x4,_y4);
  long long ans2 = ccw(_x3,_y3,_x4,_y4,_x1,_y1) * ccw(_x3,_y3,_x4,_y4,_x2,_y2);

  long long mx1,my1,mx2,my2;
  mx1 = min(_x1,_x2);
  my1 = min(_y1,_y2);
  mx2 = max(_x1,_x2);
  my2 = max(_y1,_y2);
  long long mx3,my3,mx4,my4;
  mx3 = min(_x3,_x4);
  my3 = min(_y3,_y4);
  mx4 = max(_x3,_x4);
  my4 = max(_y3,_y4);
  if(ans1 == 0 && ans2 == 0) {
	if(mx1 <= mx4 && mx3 <= mx2 && my1 <= my4 && my3 <= my2){
        cout << 1;
        exit(0);
    }
  } 
  else{
    if (ans1 <= 0 && ans2 <= 0){
    cout << 1;
    exit(0);
    }
  }
  cout << 0 << "\n";
  return 0;
}