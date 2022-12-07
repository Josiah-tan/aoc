#include"template.h"
#include<iostream>
#include<vector>
#include<algorithm>
#include<climits>
#include<string>
#include<unordered_set>

void part1Naive()
{
	unsigned int number_test_cases;
	std::cin >> number_test_cases;
	std::string input_string;
	for (unsigned int case_index = 0; case_index < number_test_cases; case_index++)
	{
		std::cin >> input_string;
		for (unsigned int i = 13; i < input_string.size(); i++)
		{
			std::unordered_set<unsigned int> set;
			for (unsigned int j = 0; j < 14; j++)
			{
				set.insert(input_string[i - j]);
			}
			if (set.size() == 14)
			{
				std::cout << i + 1 << std::endl;
				break;
			}
		}
	}
}

int main(void){
	part1Naive();
}

