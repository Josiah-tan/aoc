#include"template.h"
#include<unordered_map>
#include<iostream>
#include<vector>
#include<algorithm>
#include<climits>
#include<string>
#include<cassert>
#include<numeric>
#include<queue>

using namespace std;

int main(void){
	int T;
	cin >> T;
	unordered_map<int, int> a;
	unordered_map<int, int> b;
	for (int t = 0; t < T; t++){
		int val;
		cin >> val;
		a[val]++;
		cin >> val;
		b[val]++;
	}

	int diff = 0;

	for (auto const& x: a){
		diff += x.first * x.second * b[x.first];
	}
	
	cout << diff;
}

