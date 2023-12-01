#include<queue>
#include"template.h"
#include<iostream>
#include<vector>
#include<algorithm>
#include<climits>
#include<string>

using namespace std;


int h, w;
vector<vector<int>> matrix;
vector<vector<int>> steps;
pair<int, int> S;
pair<int, int> E;

void part1()
{
	steps = vector<vector<int>> (h, vector<int>(w, INT_MAX));
	queue<pair<int, int>> visiting;
	steps[S.first][S.second] = 0;
	visiting.push(S);
	while (!visiting.empty())
	{
		pair<int, int> current = visiting.front();
		visiting.pop();

		vector<pair<int, int>> checkouts = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
		for (auto checkout: checkouts)
		{
			pair<int, int> next = make_pair(current.first + checkout.first, current.second + checkout.second);
			if (next.first >= 0 && next.first < h && next.second < w && next.second >= 0 && steps[next.first][next.second] == INT_MAX && matrix[next.first][next.second] - matrix[current.first][current.second] <= 1)
			{
				steps[next.first][next.second] = steps[current.first][current.second] + 1;
				visiting.push(next);
			}
		}
	}
	cout << steps[E.first][E.second]; // part 1
}

void part2()
{
	steps = vector<vector<int>> (h, vector<int>(w, INT_MAX));
	queue<pair<int, int>> visiting;
	steps[E.first][E.second] = 0;
	visiting.push(E);
	while (!visiting.empty())
	{
		pair<int, int> current = visiting.front();
		visiting.pop();

		vector<pair<int, int>> checkouts = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
		for (auto checkout: checkouts)
		{
			pair<int, int> next = make_pair(current.first + checkout.first, current.second + checkout.second);
			if (next.first >= 0 && next.first < h && next.second < w && next.second >= 0 && steps[next.first][next.second] == INT_MAX && matrix[next.first][next.second] - matrix[current.first][current.second] >= -1)
			{
				steps[next.first][next.second] = steps[current.first][current.second] + 1;
				visiting.push(next);
			}
		}
	}
	int min_value = INT_MAX;
	for (int i = 0; i < h; i++)
	{
		for (int j = 0; j < w; j++)
		{
			if (matrix[i][j] == 'a')
			{
				min_value = min(steps[i][j], min_value);
			}
		}
	}
	cout << min_value; // part 2
}

int main(void){
	cin >> h;
	for (int i = 0; i < h; i++)
	{
		string input_string;
		cin >> input_string;
		w = input_string.size();
		matrix.push_back(vector<int>());
		for (int j = 0; j < w; j++)
		{
			matrix[i].push_back(input_string[j]);

			if (input_string[j] == 'S')
			{
				S.first = i;
				S.second = j;
				matrix[i][j] = 'a';
			}
			else if (input_string[j] == 'E')
			{
				E.first = i;
				E.second = j;
				matrix[i][j] = 'z';
			}
		}
	}
	part1();
	cout << endl;
	part2();
}

