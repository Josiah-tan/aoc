#include"template.h"
#include<iostream>
#include<vector>
#include<algorithm>
#include<climits>
#include<string>

using namespace std;

unsigned int part1(unsigned int number_pairs)
{
	unsigned int sum = 0;
	for (unsigned int pair_index = 0; pair_index < number_pairs; pair_index++)
	{
		pair<unsigned int, unsigned int> elf_a;
		pair<unsigned int, unsigned int> elf_b;
		cin >> elf_a.first >> elf_a.second >> elf_b.first >> elf_b.second;
		sum += (elf_a.first <= elf_b.first && elf_a.second >= elf_b.second) 
			|| (elf_a.first >= elf_b.first && elf_a.second <= elf_b.second);
	}
	return sum;
}

unsigned int part2(unsigned int number_pairs)
{
	unsigned int sum = 0;
	for (unsigned int pair_index = 0; pair_index < number_pairs; pair_index++)
	{
		pair<unsigned int, unsigned int> elf_a;
		pair<unsigned int, unsigned int> elf_b;
		cin >> elf_a.first >> elf_a.second >> elf_b.first >> elf_b.second;
		sum += (elf_a.first >= elf_b.first && elf_a.first <= elf_b.second)
			|| (elf_b.first >= elf_a.first && elf_b.first <= elf_a.second);
	}
	return sum;
}

int main(void){
	unsigned int number_pairs;
	cin >> number_pairs;
	
	// unsigned int sum = part1(number_pairs);
	// cout << sum;
	// 
	unsigned int sum = part2(number_pairs);
	cout << sum;
}

