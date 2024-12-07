#ifndef TEMPLATE_H
#define TEMPLATE_H

#include<vector>
#include<iostream>
#include<utility>
#include<tuple>

void helloWorld(void);

class Point {
public:
    int y, x;

		Point();
    Point(int y, int x);
    Point rotateClockwise90();
    Point rotateAnticlockwise90();
    Point operator+(Point other);
    Point operator-(Point other);
		bool operator==(const Point &other) const;

    friend std::ostream &operator<<(std::ostream &os, const Point &m);
};

// Define custom hash structs
struct PointHash {
    std::size_t operator()(const Point& p) const;
};

struct PairOfPointsHash {
    std::size_t operator()(const std::pair<Point, Point>& p) const;
};

template<class T>
bool same(std::vector<T> question, std::vector<T> answer){
	int question_size = question.size(), answer_size = answer.size();
	bool same = question_size == answer_size;
	for (int i = 0; i < std::min(question_size, answer_size); i++)
	{
		same &= question[i] == answer[i];
	}
	if (!same){
		std::cout << "Q: ";
		for (int i = 0; i < question_size; i++)
		{
			std::cout << question[i] << ' ';
		}
		std::cout << "\nA: ";
		for (int i = 0; i < answer_size; i++)
		{
			std::cout << answer[i] << ' ';
		}
		std::cout << std::endl;
	}
	return same;
}



template<class T>
bool same(std::vector<std::vector<T>> question, std::vector<std::vector<T>> answer){
	int question_size = question.size(), answer_size = answer.size();
	bool is_same = question_size == answer_size;
	for (int i = 0; i < std::min(question_size, answer_size); i++)
	{
		is_same &= same(question[i], answer[i]);
		if (!is_same) std::cout << "←i " << i << std::endl;
	}
	return is_same;
}


template<class T>
void print(std::vector<T> array){
	for (const auto & character: array){
		std::cout << character << " ";
	}
	std::cout << std::endl;
}

template<class T>
void print(std::vector<std::vector<T>> matrix){
	for (const auto & array: matrix){
		for (const auto & character: array){
			std::cout << character << " ";
		}
		std::cout << std::endl;
	}
}

// Custom hash for std::pair
struct pair_hash {
    template <typename T1, typename T2>
    std::size_t operator()(const std::pair<T1, T2>& p) const {
        auto h1 = std::hash<T1>{}(p.first);
        auto h2 = std::hash<T2>{}(p.second);
        return h1 ^ (h2 << 1); // Combine the hashes
    }
};

// Custom hash for a tuple with three elements
struct tuple_hash {
    template <typename T1, typename T2, typename T3>
    std::size_t operator()(const std::tuple<T1, T2, T3>& t) const {
        auto h1 = std::hash<T1>{}(std::get<0>(t));
        auto h2 = std::hash<T2>{}(std::get<1>(t));
        auto h3 = std::hash<T3>{}(std::get<2>(t));
        return h1 ^ (h2 << 1) ^ (h3 << 2); // Combine the hashes
    }
};
#endif
