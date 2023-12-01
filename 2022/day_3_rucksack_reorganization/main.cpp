#include"template.h"
#include<unordered_set>
#include<iostream>
#include<vector>
#include<algorithm>
#include<climits>
#include<string>
#include<cassert>

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

unordered_set<unsigned int> findIntersection(unordered_set<unsigned int> first, unordered_set<unsigned int> second)
{
	unordered_set<unsigned int> result;
	for (unordered_set<unsigned int>::iterator item = second.begin(); item != second.end(); item++)
	{
		if (first.find(*item) != first.end())
		{
			result.insert(*item);
		}
	}
	return result;
}

unordered_set<unsigned int> findIntersection(vector<unordered_set<unsigned int>> sets)
{
	unordered_set<unsigned int> temporary = findIntersection(sets[0], sets[1]);
	for (unsigned int i = 2; i < sets.size(); i++)
	{
		temporary = findIntersection(temporary, sets[i]);
	}
	return temporary;
}

void part1() {
    	unsigned int number_rucksacks; 
    	cin >> number_rucksacks;
    	string items;
    	unsigned int sum = 0;
    	for (unsigned int rucksack_number = 0; rucksack_number < number_rucksacks; rucksack_number++)
    	{
    		cin >> items;
    		unsigned int number_items = items.size();
    		vector<unordered_set<unsigned int>> sets(2);
    		for (unsigned int item_number = 0; item_number < number_items / 2; item_number++)
    		{
    			sets[0].insert(getPriority(items[item_number]));
    		}	
    		for (unsigned int item_number = number_items / 2; item_number < number_items; item_number++)
    		{
    			sets[1].insert(getPriority(items[item_number]));
    		}	
    		unordered_set<unsigned int> result = findIntersection(sets);
    		assert(result.size() == 1);
    		sum += *result.begin();
    	}
    	cout << sum << endl;
}

void part2() {
	unsigned int number_rucksacks; 
	cin >> number_rucksacks;
	string items;
	unsigned int sum = 0;
	for (unsigned int rucksack_number = 0; rucksack_number < number_rucksacks / 3; rucksack_number++)
	{
		unsigned int number_groups = 3;
		vector<unordered_set<unsigned int>> sets(number_groups);
		for (unsigned int member_number = 0; member_number < number_groups; member_number++)
		{
			cin >> items;
			for (unsigned int item_number = 0; item_number < items.size(); item_number++)
			{
				sets[member_number].insert(getPriority(items[item_number]));
			}	
		}
		unordered_set<unsigned int> result = findIntersection(sets);
		assert(result.size() == 1);
		sum += *result.begin();
	}
	cout << sum << endl;
}


int main(void){
	/* part1(); */
	part2();
}

