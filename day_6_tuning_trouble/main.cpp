#include"template.h"
#include<iostream>
#include <ostream>
#include<vector>
#include<algorithm>
#include<climits>
#include<string>
#include<unordered_set>
#include<unordered_map>
#include<cstring>
#include<bitset>

void naive()
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

void skip()
{
	unsigned int number_test_cases;
	std::cin >> number_test_cases;
	std::string input_string;
	int window_size = 14;
	for (int case_index = 0; case_index < number_test_cases; case_index++)
	{
		std::cin >> input_string;
		int i = 0;
		while (i < input_string.size() - window_size + 1)
		{
			std::unordered_map<char, int> tracker;
			bool skip = false;
			for (int j = 0; j < window_size; j++)
			{
				if (!tracker[input_string[i + j]]){
					tracker[input_string[i + j]] = i + j + 1;
				}
				else {
					i = tracker[input_string[i + j]];
					skip = true;
					break;

				}
			}
			if (!skip) {
				std::cout << i + window_size << std::endl;
				break;
			}
		}
	}
}

void arrayMethod()
{
	int tracker[26];
	unsigned int number_test_cases;
	std::cin >> number_test_cases;
	std::string input_string;
	int window_size = 14;
	for (int case_index = 0; case_index < number_test_cases; case_index++)
	{
		std::cin >> input_string;
		int i = 0;
		while (i < input_string.size() - window_size + 1)
		{
			std::memset(tracker, 0, sizeof(tracker));
			bool skip = false;
			for (int j = i; j < window_size + i; j++)
			{
				int character = input_string[j] - 'a';
				if (!tracker[character]){
					tracker[character] = j + 1;
				}
				else {
					i = tracker[character];
					skip = true;
					break;
				}
			}
			if (!skip) {
				std::cout << i + window_size << std::endl;
				break;
			}
		}
	}
}

void Benny()
{
	int number_test_cases;
	std::cin >> number_test_cases;
	std::string input_string;
	int window_size = 14;
	for (int case_index = 0; case_index < number_test_cases; case_index++){
		std::cin >> input_string;
		std::bitset<32> tracker(0);
		for (int i = 0; i < window_size - 1; i++)
		{
			tracker ^= 1 << (input_string[i] - 'a');
		}
		for (int i = 0; i < input_string.size() - window_size + 1; i++)
		{
			tracker ^= 1 << (input_string[i + window_size - 1] - 'a');
			if (tracker.count() == window_size){
				std::cout << i + window_size << std::endl;
				break;
			}
			tracker ^= 1 << (input_string[i] - 'a');
		}
	}
}

void DavidAPerez()
{
	int number_test_cases;
	std::cin >> number_test_cases;
	std::string input_string;
	int window_size = 14;
	for (int case_index = 0; case_index < number_test_cases; case_index++){
		std::cin >> input_string;
		int index = 0;
		while (index <= input_string.size() - window_size){
			int tracker = 0;
			bool skip = false;
			for (int j = index + window_size - 1; j >= index; j--){
				if ((tracker & (1 << (input_string[j] - 'a'))) == 0){
					tracker |= (1 << (input_string[j] - 'a'));
				}
				else {
					index = j + 1;
					skip = true;
					break;
				}
			}
			if (!skip){
				std::cout << index + window_size << std::endl;
				break;
			}
		}
	}
}

int main(void){
	// naive();
	// perform a skip:
	// skip();
	// using literally just an array
	// arrayMethod();
	// a lot faster: bit sliding window
	// Benny();
	// even faster: backward skipping bit sliding window
	DavidAPerez();
}
