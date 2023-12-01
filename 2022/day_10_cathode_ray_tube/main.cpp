#include"template.h"
#include<iostream>
#include<vector>
#include<algorithm>
#include<climits>
#include<string>

using namespace std;
int cycle = 0;
int x = 1;
int sum = 0;

int crt = 0;
int width = 40;
int height = 6;
vector<vector<char>> matrix (height, vector<char>(width));
void check()
{
	// part 1
	if ((cycle + 20) % 40 == 0 && cycle <= 220)
	{
		int signal_strength = cycle * x;
		sum += signal_strength;
	}

	// part 2
	int crt_x = crt % width;
	char draw = crt_x >= (x-1) && crt_x <= (x+1) ? '#' : '.';
	matrix[crt / width][crt % width] = draw;

	crt += 1;
	crt = crt % (width * height);
}

int main(void){
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		string command;
		int number;
		cin >> command;
		if (command == "noop")
		{
			cycle += 1;
			check();
		}
		else if (command == "addx")
		{
			cin >> number;
			cycle += 1;
			check();
			cycle += 1;
			check();
			x += number;
		}
	}
	std::cout << "sum = " << sum << std::endl;
	for (int i = 0; i < height; i++)
	{
		for (int j = 0; j < width; j++)
		{
			cout << matrix[i][j];
		}
		cout << endl;
	}
}

