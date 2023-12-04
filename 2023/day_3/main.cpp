#include"template.h"
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
	string line;
	while(getline(cin, line)){
		array.push_back(line);
	}
	// for(auto line: array){
	// 	cout << line << endl;
	// }
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
						}
					}
				}
			}
			/* for (int j = 0; j < width; j++){
			   char character = array[i][j];
			   if (character <= '9' && character >= '0'){
			   number = number * 10 + character - '0';
			   for (int x = -1; x < 2; x++){
			   for (int y = -1; y < 2; y++){
			   if (y + j >= 0 && y + j < width && x + i >= 0 && x + i < height){
			   char query = array[x + i][y + j];
			   valid |= (query > '9' || query < '0') && query != '.';
			   }
			   }
			   }
			   }
			   else {
			   summation += number * valid;
			   number = 0;
			   valid = false;
			   }
			   if (j == width - 1){
			   summation += number * valid;
			   number = 0;
			   valid = false;
			   }
			   } */
			else if (number > 0){
				if (valid){
					summation += number;
				}
				number = 0;
				valid = false;
			}
		}
	}
	cout << summation;
}

