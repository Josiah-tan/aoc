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
    AhoCorasick();
    void insert(const std::string& key, int value);
    void build();
    int query(const std::string& text);
};

AhoCorasick::AhoCorasick() {
    trie.emplace_back(); // Root node
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

int AhoCorasick::query(const std::string& text) {
    int current = 0;
    int result = 0;

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
                result += trie[match].value;
            }
            match = trie[match].link;
        }
    }

    return result;
}

int main() {
    AhoCorasick ac;

    // Insert keys and values
    ac.insert("abc", 5);
    ac.insert("123", 2);
    ac.insert("def", 3);

    // Build the Aho-Corasick trie
    ac.build();

    // Query text and print the result
    std::string text = "abc123def";
    int result = ac.query(text);

    std::cout << "Result: " << result << std::endl;

    return 0;
}
