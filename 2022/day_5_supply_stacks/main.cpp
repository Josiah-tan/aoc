#include"template.h"
#include<iostream>
#include<vector>
#include<array>
#include<algorithm>
#include<climits>
#include<string>


#include<ext/rope>
#include<iostream>
#include<cassert>

void part1() {
    	unsigned int stack_number;
    	std::cin >> stack_number;
    	std::vector<std::vector<char>> stacks(stack_number, std::vector<char>(100, 'A'));
    	std::vector<unsigned int> stacks_pointer(stack_number, 0);
    	std::string temporary_string;
    	for (unsigned int i = 0; i < stack_number; i++)
    	{
    		std::cin >> temporary_string;
    		for (unsigned int j = 0; j < temporary_string.size(); j++)
    		{
    			stacks[i][j] = temporary_string[temporary_string.size() - j - 1];
    		}
    		stacks_pointer[i] = temporary_string.size();
    	}
    	
    	unsigned int number_commands;
    	std::cin >> number_commands;
    	for (unsigned int i = 0; i < number_commands; i++)
    	{
    		unsigned int number_move;
    		unsigned int from_stack;
    		unsigned int to_stack;
    		std::cin >> number_move >> from_stack >> to_stack;
    		from_stack--;
    		to_stack--;

    		for (unsigned int i = 0; i < number_move; i++)
    		{
    			stacks[to_stack][stacks_pointer[to_stack]++] = stacks[from_stack][--stacks_pointer[from_stack]];
    		}
    	}

    	for (unsigned int i = 0; i < stack_number; i++)
    	{
    		std::cout << stacks[i][stacks_pointer[i] - 1];
    	}
}

void part2()
{
	// O(number_commands * log(how_many_average))
	unsigned int number_stacks;
	std::cin >> number_stacks;
	std::vector<__gnu_cxx::crope> stacks(number_stacks, "");
	for (unsigned int stack_index = 0; stack_index < number_stacks; stack_index++)
	{
		std::string temporary_string;
		std::cin >> temporary_string;
		for (unsigned int string_index = 0; string_index < temporary_string.size(); string_index++)
		{
			stacks[stack_index].push_back(temporary_string[temporary_string.size() - 1 - string_index]);
		}
	}
	unsigned int number_commands;
	std::cin >> number_commands;
	for (unsigned int command_index = 0; command_index < number_commands; command_index++)
	{
		unsigned int how_many;
		unsigned int from_stack;
		unsigned int to_stack;
		std::cin >> how_many >> from_stack >> to_stack;
		from_stack--;
		to_stack--;
		stacks[to_stack] += stacks[from_stack].substr(stacks[from_stack].size() - how_many, how_many);
		stacks[from_stack].erase(stacks[from_stack].size() - how_many, how_many);
	}
	for (unsigned int stack_index = 0; stack_index < number_stacks; stack_index++)
	{
		assert(stacks[stack_index].size() != 0);
		if (stacks[stack_index].size() != 0){
			std::cout << stacks[stack_index][stacks[stack_index].size() - 1];
		}
	}
}

int main(void){
	// part1();
	part2();
}

