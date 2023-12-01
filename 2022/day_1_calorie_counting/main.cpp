#include<queue>
#include"template.h"
#include<iostream>
#include<vector>
#include<algorithm>
#include<climits>
#include<string>

std::priority_queue<unsigned int, std::vector<unsigned int>, std::greater<unsigned int>> minimum_heap;
const unsigned int maximum_number_items = 3;

void chuckIntoHeap(unsigned int thing_to_chuck)
{
	// time complexity O(log(maximum_number_items)), space complexity O(maximum_number_items)
	minimum_heap.push(thing_to_chuck);
	if (minimum_heap.size() > maximum_number_items){
		minimum_heap.pop();
	}
}

int main(void){
	// time complexity O(number_lines * log(maximum_number_items))
	std::string line;
	unsigned int maximum_number = 0;
	unsigned int maximum_number_3 = 0;
	unsigned int number = 0;
	unsigned int sum = 0;
	while(std::getline(std::cin, line)) {
		if (line == ""){
			chuckIntoHeap(sum);
			sum = 0;
		}
		else {
			number = (unsigned int) std::stoi(line);
			sum += number;
		}
	}
	chuckIntoHeap(sum);
	while(!minimum_heap.empty())
	{
		maximum_number = minimum_heap.top();
		minimum_heap.pop();
		maximum_number_3 += maximum_number;
	}
	std::cout << "maximum_number = " << maximum_number << std::endl;
	std::cout << "maximum_number_3 = " << maximum_number_3 << std::endl;
}

