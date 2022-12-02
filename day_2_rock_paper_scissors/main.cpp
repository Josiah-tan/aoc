#include"template.h"
#include<iostream>
#include<vector>
#include<algorithm>
#include<climits>
#include<string>

using namespace std;

void firstPart() {
  unsigned int number_games;
  char opponent, you;
  number_games = 2500; // hardcode this cause why not lol;
  unsigned int total_score = 0;
  for (unsigned int t = 0; t < number_games; t++) {
    cin >> opponent >> you;
    unsigned int outcome = (((you - 'X') - (opponent - 'A') + 4) % 3) * 3;
    unsigned int reward_choice = you - 'W';
    total_score += outcome + reward_choice;
  }
  std::cout << "total_score = " << total_score << std::endl;
}

void secondPart() {
	unsigned int number_games;
	char opponent, outcome;
	number_games = 2500; 
	// number_games = 1; 
	unsigned int total_score = 0;
	unsigned int reward_choice = 0;
	unsigned int outcome_processed = 0;
	for (unsigned int t = 0; t < number_games; t++) {
		cin >> opponent >> outcome;
		outcome_processed = (outcome - 'X') * 3;
		reward_choice = (((opponent - 'A') + (outcome - 'X') + 2) % 3) + 1;
		total_score += outcome_processed + reward_choice;
	}
	std::cout << "total_score = " << total_score << std::endl;
}

int main(void) {
	// firstPart(); 
	secondPart();
}
