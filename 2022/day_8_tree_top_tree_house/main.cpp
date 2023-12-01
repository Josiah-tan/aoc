#include"template.h"
#include<iostream>
#include<vector>
#include<algorithm>
#include<climits>
#include<string>

using namespace std;

int main(void){
	int number_cases;
	cin >> number_cases;
	std::vector<std::vector<int>> trees(number_cases);
	string temporary_string;
	for (unsigned int case_number = 0; case_number < number_cases; case_number++)
	{
		cin >> temporary_string;
		for (unsigned int i = 0; i < temporary_string.size(); i++)
		{
			trees[case_number].push_back(temporary_string[i]-'0');
		}
	}

	std::vector<std::vector<bool>> visible (number_cases, std::vector<bool>(temporary_string.size(), false));

	// looking to the left
	for (unsigned int i = 0; i < number_cases; i++)
	{
		int max_left = -1;
		for (unsigned int j = 0; j < temporary_string.size(); j++)
		{
			if (trees[i][j] > max_left)
			{
				max_left = trees[i][j];
				visible[i][j] = 1;
			}
		}
	}

	// looking to the right
	for (int i = 0; i < number_cases; i++)
	{
		int max_right = -1;
		for (int j = temporary_string.size() - 1; j >= 0; j--)
		{
			if (trees[i][j] > max_right)
			{
				max_right = trees[i][j];
				visible[i][j] = 1;
			}
		}
	}

	// looking up
	for (int j = 0; j < temporary_string.size() - 1; j++)
	{
		int max_up = -1;
		for (int i = 0; i < number_cases; i++)
		{
			if (trees[i][j] > max_up)
			{
				max_up = trees[i][j];
				visible[i][j] = 1;
			}
		}
	}
	
	// looking down
	for (int j = 0; j < temporary_string.size() - 1; j++)
	{
		int max_down = -1;
		for (int i = number_cases - 1; i >= 0; i--)
		{
			if (trees[i][j] > max_down)
			{
				max_down = trees[i][j];
				visible[i][j] = 1;
			}
		}
	}

	int sum = 0;
	for (int i = 0; i < number_cases; i++)
	{
		for (int j = 0; j < temporary_string.size(); j++)
		{
			sum += visible[i][j];	
		}
	}

	unsigned int multiplication_max = 0;
	for (unsigned int i = 0; i < number_cases; i++)
	{
		for (unsigned int j = 0; j < temporary_string.size(); j++)
		{
			// part 2
			unsigned int down = 0;
			for (unsigned int x = i+1; x < number_cases; x++)
			{
				down += 1;
				if (trees[i][j] <= trees[x][j]){
					break;
				}
			}
			unsigned int left = 0;
			for (unsigned int y = j+1; y < temporary_string.size(); y++)
			{
				left += 1;
				if (trees[i][j] <= trees[i][y]){
					break;
				}
			}
			unsigned int up = 0;
			for (int x = i-1; x >= 0; x--){
				up += 1;
				if (trees[i][j] <= trees[x][j]){
					break;
				}
			}
			unsigned int right = 0;
			for (int y = j-1; y >= 0; y--){
				right += 1;
				if (trees[i][j] <= trees[i][y]){
					break;
				}
			}
			unsigned int multiplication = up * left * right * down;
			multiplication_max = max(multiplication, multiplication_max);
		}
	}
	std::cout << "sum = " << sum << std::endl;
	std::cout << "multiplication_max = " << multiplication_max << std::endl;
}

