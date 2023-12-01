#include"template.h"
#include<unordered_set>
#include<iostream>
#include<vector>
#include<algorithm>
#include<climits>
#include<string>

using namespace std;
struct pair_hash {
    inline std::size_t operator()(const std::pair<int,int> & v) const {
        return v.first*31+v.second;
    }
};

unordered_set<pair<int, int>, pair_hash> visited;
int m = 10;
vector<int> x(m, 0);
vector<int> y(m, 0);


void move(int m, int N, int direction_x, int direction_y)
{
	for (int i = 0; i < N; i++)
	{
		x[m] += direction_x;
		y[m] += direction_y;
		if (m)
		{
			int vector_x = x[m] - x[m-1];
			int vector_y = y[m] - y[m-1];

			if (abs(vector_x) == 2 || abs(vector_y) == 2)
			{
				vector_x = vector_x ? abs(vector_x) / vector_x : 0;
				vector_y = vector_y ? abs(vector_y) / vector_y : 0;
				move(m-1, 1, vector_x, vector_y);
			}
		}
		else
		{
			// cout << m << " " << x[m] << " " << y[m] << endl;
			visited.insert(make_pair(x[m], y[m]));
		}
	}
}

int main(void){
	int T;
	cin >> T;
	visited.insert(make_pair(x[m - 1], y[m - 1]));
	for (int t = 0; t < T; t++)
	{
		char d;
		int N;
		cin >> d >> N;

		int direction_x = 0;
		int direction_y = 0;

		if (d == 'R')
		{
			direction_x = 1;
		}
		else if (d == 'L')
		{
			direction_x = -1;
		}
		else if (d == 'U')
		{
			direction_y = 1;
		}
		else if (d == 'D')
		{
			direction_y = -1;
		}
		move(m - 1, N, direction_x, direction_y);
	}
	cout << visited.size();
}
