#include"template.h"
#include <unordered_set>
#include<iostream>
#include<vector>
#include<algorithm>
#include<climits>
#include<string>

using namespace std;


unsigned int getPriority(char item)
{
	unsigned int answer;
	if (item <= 'Z' && item >= 'A')
	{
		answer = item - 'A' + 27;
	}
	else
	{
		answer = item - 'a' + 1;
	}
	return answer;
}

int main(void){
	unsigned int number_rucksacks; 
	cin >> number_rucksacks;
	string items;
	unsigned int sum = 0;
	for (unsigned int rucksack_number = 0; rucksack_number < number_rucksacks; rucksack_number++)
	{
		cin >> items;
		unsigned int number_items = items.size();
		unordered_set<unsigned int> set;
		for (unsigned int item_number = 0; item_number < number_items / 2; item_number++)
		{
			set.insert(getPriority(items[item_number]));
		}	
		for (unsigned int item_number = number_items / 2; item_number < number_items; item_number++)
		{
			unsigned int item_priority = getPriority(items[item_number]);
			if (set.find(item_priority) != set.end())
			{
				sum += item_priority;
				break;
			}

		}	
	}
	cout << sum << endl;
}

