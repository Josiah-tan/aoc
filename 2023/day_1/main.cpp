#include"template.h"
#include<iostream>
#include<vector>
#include<algorithm>
#include<climits>
#include<string>
#include<cassert>
#include<numeric>
#include<queue>
#include<unordered_map>

using namespace std;

class AhoCorasick {
	private:
		struct Node {
			std::unordered_map<char, int> children;
			int link;
			int value;

			Node() : link(-1), value(-1) {}
		};

		std::vector<Node> trie;

	public:
		int sum;
		AhoCorasick();
		void insert(const std::string& key, int value);
		void build();
		void query(const std::string& text);
};

AhoCorasick::AhoCorasick() {
	trie.emplace_back(); // Root node
	sum = 0;
}

void AhoCorasick::insert(const std::string& key, int value) {
	int current = 0; // Start from the root

	for (char ch : key) {
		if (trie[current].children.find(ch) == trie[current].children.end()) {
			trie.emplace_back();
			trie[current].children[ch] = trie.size() - 1;
		}
		current = trie[current].children[ch];
	}

	trie[current].value = value;
}

void AhoCorasick::build() {
	std::queue<int> bfsQueue;

	for (const auto& child : trie[0].children) {
		int next = child.second;
		trie[next].link = 0;
		bfsQueue.push(next);
	}

	while (!bfsQueue.empty()) {
		int current = bfsQueue.front();
		bfsQueue.pop();

		for (const auto& child : trie[current].children) {
			char ch = child.first;
			int next = child.second;
			bfsQueue.push(next);

			int link = trie[current].link;
			while (link != -1 && trie[link].children.find(ch) == trie[link].children.end()) {
				link = trie[link].link;
			}

			trie[next].link = (link == -1) ? 0 : trie[link].children[ch];
		}
	}
}

void AhoCorasick::query(const std::string& text) {
	int current = 0;
	int first = -1;
	int last = -1;

	for (char ch : text) {
		while (current != 0 && trie[current].children.find(ch) == trie[current].children.end()) {
			current = trie[current].link;
		}

		if (trie[current].children.find(ch) != trie[current].children.end()) {
			current = trie[current].children[ch];
		}

		int match = current;

		while (match != 0) {
			if (trie[match].value != -1) {
				// Found a match, add the associated value to the result
				int result = trie[match].value;
				if (first == -1) first = result;
				last = result;
			}
			match = trie[match].link;
		}
	}
	sum += first * 10 + last;
	// return result;
}

int main() {
	AhoCorasick ac;

	// Insert keys and values
	ac.insert("1", 1);
	ac.insert("2", 2);
	ac.insert("3", 3);
	ac.insert("4", 4);
	ac.insert("5", 5);
	ac.insert("6", 6);
	ac.insert("7", 7);
	ac.insert("8", 8);
	ac.insert("9", 9);

	bool part_2 = true;
	if (part_2){
		ac.insert("one", 1);
		ac.insert("two", 2);
		ac.insert("three", 3);
		ac.insert("four", 4);
		ac.insert("five", 5);
		ac.insert("six", 6);
		ac.insert("seven", 7);
		ac.insert("eight", 8);
		ac.insert("nine", 9);
	}

	// Build the Aho-Corasick trie
	ac.build();

	// Query text and print the result
	std::string text;
	while(getline(cin, text)){
		ac.query(text);
	}
	cout << ac.sum;
	return 0;
}
