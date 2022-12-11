#include<queue>
#include"template.h"
#include<iostream>
#include<vector>
#include<algorithm>
#include<climits>
#include<string>

using namespace std;

struct Monkey
{
	deque<long> items;
	char operation_symbol;
	long operation_operand;
	long divisible;
	long monkey_true;
	long monkey_false;
	long number_inspect;
	
	bool operator > (const Monkey& monkey) const
	{
		return (number_inspect > monkey.number_inspect);
	}
};

long calculate(long a, char operand, long b)
{
	return operand == '*' ? a * b : a + b;
}
int main(void){
	// helloWorld();
	long T;
	cin >> T;
	vector<Monkey> monkeys(T);
	for (long t = 0; t < T;t ++){
		long index;
		cin >> index;
		string items;
		cin >> items;
		std::string delimiter = ",";

		size_t pos = 0;
		std::string token;
		while ((pos = items.find(delimiter)) != std::string::npos) 
		{
			token = items.substr(0, pos);
			monkeys[index].items.push_back(stoi(token));
			items.erase(0, pos + delimiter.length());
		}
		monkeys[index].items.push_back(stoi(items));
		// cout << "items\n";
		// for (auto const& data : monkeys[index].items) 
		// {
		// 	cout << data << " ";
		// }
		// cout << endl;
		string operation;
		cin >> operation;
		monkeys[index].operation_symbol = operation[0];
		if (operation.size() == 1)
		{
			monkeys[index].operation_operand = 0;
		}
		else
		{
			monkeys[index].operation_operand = stoi(operation.substr(1, operation.size() - 1));
		}
		cin >> monkeys[index].divisible;
		cin >> monkeys[index].monkey_true;
		cin >> monkeys[index].monkey_false;
		monkeys[index].number_inspect = 0;
		// std::cout << "monkeys[index].divisible = " << monkeys[index].divisible << std::endl;
		// std::cout << "monkeys[index].monkey_true = " << monkeys[index].monkey_true << std::endl;
		// std::cout << "monkeys[index].monkey_false = " << monkeys[index].monkey_false << std::endl;
		// std::cout << "monkeys[index].operation_operand = " << monkeys[index].operation_operand << std::endl;
		// std::cout << "monkeys[index].operation_symbol = " << monkeys[index].operation_symbol << std::endl;
	}
	
	long common_multiple = 1;
	for (long index = 0; index < monkeys.size(); index++)
	{
		common_multiple *= monkeys[index].divisible;
	}
			
	long number_rounds = 10000;
	for (long round = 0; round < number_rounds; round++)
	{
		for (long index = 0; index < monkeys.size(); index++)
		{
			while (!monkeys[index].items.empty())
			{
				monkeys[index].number_inspect ++;
				long item = monkeys[index].items.front();
				monkeys[index].items.pop_front();
				item = calculate(item, monkeys[index].operation_symbol, monkeys[index].operation_operand ? monkeys[index].operation_operand : item);
				// std::cout << "index = " << index << std::endl;
				// std::cout << "item = " << item << std::endl;
				// item /= 3;
				item = item % common_multiple;
				monkeys[item % monkeys[index].divisible ? monkeys[index].monkey_false : monkeys[index].monkey_true].items.push_back(item);
			}
		}
		// cout << "items\n";
		// for (long index = 0; index < monkeys.size(); index++)
		// {
		// 	for (auto &item: monkeys[index].items)
		// 	{
		// 		cout << item << ' ';
		// 	}
		// 	cout << endl;
		// }
	}
	for (long index = 0; index < monkeys.size(); index++)
	{
		cout << monkeys[index].number_inspect << " ";
	}
	cout << endl;
	sort(monkeys.begin(), monkeys.end(), greater<Monkey>());
	for (long index = 0; index < monkeys.size(); index++)
	{
		cout << monkeys[index].number_inspect << " ";
	}
	cout << endl;
	long answer = long(monkeys[0].number_inspect) * monkeys[1].number_inspect;
	std::cout << "answer = " << answer << std::endl;
}

