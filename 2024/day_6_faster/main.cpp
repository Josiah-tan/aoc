#include <iostream>
#include <vector>
#include <string>
#include "template.h"
#include <unordered_set>

int main() {
	// Define a vector to hold the 2D matrix
	std::vector<std::vector<char>> matrix;

	// Read the grid line by line
	std::string line;
	while (std::getline(std::cin, line)) {
		if (!line.empty()) { // Ignore empty lines
			std::vector<char> row(line.begin(), line.end());
			matrix.push_back(row);
		}
	}
	// Print the matrix to verify
	// for (const auto& row : matrix) {
	// 	for (const auto& cell : row) {
	// 		std::cout << cell;
	// 	}
	// 	std::cout << '\n';
	// }

	int height = matrix.size();
	int width = matrix[0].size();
	
	Point initial_pos, pos, new_pos;
	for (int i = 0; i < height; i++){
		for (int j = 0; j < width; j++){
			if (matrix[i][j] == '^'){
				initial_pos.y = i;
				initial_pos.x = j;
			}
		}
	}

	Point orientation = Point(-1, 0);
	int answer_1;
	answer_1 = 0;
	int answer_2 = 0;
	for (int i = 0; i < height; i++){
		for (int j = 0; j < width; j++){
			std::cout << "i = " << i << std::endl;
			std::cout << "j = " << j << std::endl;
			pos = initial_pos;
			orientation = Point(-1, 0);
			std::unordered_set<Point, PointHash> position_set;
			std::unordered_set<std::pair<Point, Point>, PairOfPointsHash> direction_set;
			while (true){
				if (direction_set.find(std::pair<Point, Point>(pos, orientation)) != direction_set.end()){
					answer_2++;
					break;
				}
				direction_set.insert(std::pair<Point, Point>(pos, orientation));
				position_set.insert(pos);
				new_pos = pos + orientation;
				if (new_pos.y >= height or new_pos.y < 0 or new_pos.x >= width or new_pos.x < 0){
					if (matrix[i][j] == '#'){
						answer_1 = position_set.size();
					}
					break;
				}
				else if (new_pos == Point(i, j) or matrix[new_pos.y][new_pos.x] == '#'){
					orientation = orientation.rotateClockwise90();
				}
				else {
					pos = new_pos;
				}
			}
		}
	}
	std::cout << answer_1 << '\n';
	std::cout << answer_2;
	return 0;
}
