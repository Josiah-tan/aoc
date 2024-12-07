#include<iostream>
#include"template.h"

using namespace std;

void helloWorld(void){
	cout << "hello world\n";
}

Point::Point() : y(0), x(0) {} // Default constructor

Point::Point(int y, int x) : y(y), x(x) {}

Point Point::rotateClockwise90() {
	return Point(this->x, -this->y);
}

Point Point::rotateAnticlockwise90() {
	return Point(-this->x, this->y);
}

Point Point::operator+(Point other) {
	return Point(this->y + other.y, this->x + other.x);
}

Point Point::operator-(Point other) {
	return Point(this->y - other.y, this->x - other.x);
}

bool Point::operator==(const Point &other) const{
	return this->y == other.y && this->x == other.x;
}

std::ostream &operator<<(std::ostream &os, const Point &m) {
	return os << "(" << m.y << ", " << m.x << ")";
}

// Implement the PointHash struct
std::size_t PointHash::operator()(const Point& p) const {
    auto h1 = std::hash<int>{}(p.y);
    auto h2 = std::hash<int>{}(p.x);
    return h1 ^ (h2 << 1); // Combine the hashes
}

// Implement the PairOfPointsHash struct
std::size_t PairOfPointsHash::operator()(const std::pair<Point, Point>& p) const {
    PointHash pointHash;
    auto h1 = pointHash(p.first);
    auto h2 = pointHash(p.second);
    return h1 ^ (h2 << 1); // Combine the hashes of both Points
}
