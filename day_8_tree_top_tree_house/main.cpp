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
	std::vector<std::vector<int>> tallest_up(number_cases, std::vector<int>(temporary_string.size(), 0));
	std::vector<std::vector<int>> tallest_left(number_cases, std::vector<int>(temporary_string.size(), 0));
	std::vector<std::vector<int>> tallest_down(number_cases, std::vector<int>(temporary_string.size(), 0));
	std::vector<std::vector<int>> tallest_right(number_cases, std::vector<int>(temporary_string.size(), 0));
	
	for (unsigned int i = 0; i < number_cases; i++)
	{
		for (unsigned int j = 0; j < temporary_string.size(); j++)
		{
			tallest_up[i][j] = (i == 0) || trees[i][j] > tallest_up[i-1][j] ? trees[i][j] : tallest_up[i-1][j];
			tallest_left[i][j] = (j == 0) || trees[i][j] > tallest_left[i][j-1] ? trees[i][j] : tallest_left[i][j-1];
		}
	}
	
	for (int i = number_cases - 1; i >= 0; i--)
	{
		for (int j = temporary_string.size() - 1; j >= 0; j--)
		{
			tallest_down[i][j] = ((i == number_cases - 1) || trees[i][j] > tallest_down[i+1][j]) ? trees[i][j] : tallest_down[i+1][j];
			tallest_right[i][j] = ((j == temporary_string.size() - 1) || trees[i][j] > tallest_right[i][j+1]) ? trees[i][j] : tallest_right[i][j+1];
		}
	}
	unsigned int sum = 0;
	for (unsigned int i = 0; i < number_cases; i++)
	{
		for (unsigned int j = 0; j < temporary_string.size(); j++)
		{
			visible[i][j] = i == 0 || j == 0 || i == number_cases - 1 || j == temporary_string.size() - 1 || 
				trees[i][j] > tallest_up[i-1][j] || trees[i][j] > tallest_down[i+1][j] || trees[i][j] > tallest_left[i][j-1] ||
				trees[i][j] > tallest_right[i][j+1];
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

