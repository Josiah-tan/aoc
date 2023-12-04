#include"template.h"
#include<unordered_map>
#include<unordered_set>
#include<iostream>
#include<vector>
#include<algorithm>
#include<climits>
#include<string>
#include<cassert>
#include<numeric>
#include<queue>

using namespace std;

int main(void){
	vector<string> array;
	unordered_set<int> gears;
	unordered_map<int, vector<int>> numbers;
	string line;
	while(getline(cin, line)){
		array.push_back(line);
	}
	int height, width;
	height = array.size();
	width = array[0].size();
	int summation = 0;
	for (int i = 0; i < height; i++){
		int number = 0;
		bool valid = false;
		for (int j = 0; j < width + 1; j++){
			if (j < width and isdigit(array[i][j])){
				number = number * 10 + array[i][j] - '0';
				for (int y = -1 + i; y < 2 + i; y++){
					for (int x = -1 + j; x < 2 + j; x++){
						if (x >= 0 && y >= 0 && x < width && y < height){
							if (!isdigit(array[y][x]) && array[y][x] != '.'){
								valid = true;
							}
							if (array[y][x] == '*'){
								gears.insert(y * width + x);
							}
						}
					}
				}
			}
			else if (number > 0){
				for (auto & gear: gears){
					numbers[gear].push_back(number);
				}
				gears = unordered_set<int>();
				if (valid){
					summation += number;
				}
				number = 0;
				valid = false;
			}
		}
	}
	cout << summation << endl;
	summation = 0;
	for (auto &number: numbers){
		if (number.second.size() == 2){
			summation += number.second[0] * number.second[1];
		}
	}
	cout << summation;
}

