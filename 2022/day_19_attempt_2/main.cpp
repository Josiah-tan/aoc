#include "cassert"
#include "queue"
#include "unordered_set"
#include "boost/functional/hash.hpp"
#include"template.h"
#include <bits/c++config.h>
#include<iostream>
#include<vector>
#include<algorithm>
#include<climits>
#include<string>

using namespace std;

using Key = std::tuple<int, int, int, int, int, int, int, int, int>;

struct KeyHash {
	std::size_t operator()(const Key & key) const
	{
		return boost::hash_value(key);
	}
};

using Set = std::unordered_set<Key, KeyHash>;

int solve(int ore_cost_ore, int clay_cost_ore, int obsidian_cost_ore, int obsidian_cost_clay, int geode_cost_ore, int geode_cost_obsidian, int time_left)
{
	int best = 0;
	// state: ore, clay, obsidian, geodes, ore_robot, clay_robot, obsidian_robot, geodes_robot, time
	Key initial_state = {0, 0, 0, 0, 1, 0, 0, 0, time_left};
	std::queue<Key> bfs;
	bfs.push(initial_state);
	Set seen;
	while (!bfs.empty())
	{
		Key state = bfs.front();
		bfs.pop();
		int ore = std::get<0>(state);
		int clay = std::get<1>(state);
		int obsidian = std::get<2>(state);
		int geodes = std::get<3>(state);
		int ore_robot = std::get<4>(state);
		int clay_robot = std::get<5>(state);
		int obsidian_robot = std::get<6>(state);
		int geodes_robot = std::get<7>(state);
		int time = std::get<8>(state);

		best = max(best, geodes);
		if (time == 0) continue;

		int max_ore_cost = max(max(max(ore_cost_ore, clay_cost_ore), obsidian_cost_ore), geode_cost_ore);

		if (ore_robot >= max_ore_cost) ore_robot = max_ore_cost; // assigning is weird, maybe skip instead?
		if (clay_robot >= obsidian_cost_clay) clay_robot = obsidian_cost_clay;
		if (obsidian_robot >= geode_cost_obsidian) obsidian_robot = geode_cost_obsidian;
		if (ore >= time * max_ore_cost - ore_robot * (time - 1)) ore = time * max_ore_cost - ore_robot * (time - 1);
		if (clay >= time * obsidian_cost_clay - clay_robot * (time - 1)) clay = time * obsidian_cost_clay - clay_robot * (time - 1);
		if (obsidian >= time * geode_cost_obsidian - obsidian_robot * (time - 1)) obsidian = time * geode_cost_obsidian - obsidian_robot * (time - 1);
		state = {ore, clay, obsidian, geodes, ore_robot, clay_robot, obsidian_robot, geodes_robot, time};

		if (seen.find(state) != seen.end()) continue;
		seen.insert(state);
		if (seen.size() % 1000000 == 0) cout << time << " " << best << " " << seen.size() << endl;
		assert (ore >= 0 && clay >= 0 && obsidian >= 0 && geodes >= 0);
		bfs.push({ore + ore_robot, clay + clay_robot, obsidian + obsidian_robot, geodes + geodes_robot, ore_robot, clay_robot, obsidian_robot, geodes_robot, time - 1});
		if (ore >= ore_cost_ore) bfs.push({ore + ore_robot - ore_cost_ore, clay + clay_robot, obsidian + obsidian_robot, geodes + geodes_robot, ore_robot + 1, clay_robot, obsidian_robot, geodes_robot, time - 1});
		if (ore >= clay_cost_ore) bfs.push({ore + ore_robot - clay_cost_ore, clay + clay_robot, obsidian + obsidian_robot, geodes + geodes_robot, ore_robot, clay_robot + 1, obsidian_robot, geodes_robot, time - 1});
		if (ore >= obsidian_cost_ore && clay >= obsidian_cost_clay) bfs.push({ore + ore_robot - obsidian_cost_ore, clay + clay_robot - obsidian_cost_clay, obsidian + obsidian_robot, geodes + geodes_robot, ore_robot, clay_robot, obsidian_robot + 1, geodes_robot, time - 1});
		if (ore >= geode_cost_ore && obsidian >= geode_cost_obsidian) bfs.push({ore + ore_robot - geode_cost_ore, clay + clay_robot, obsidian + obsidian_robot - geode_cost_obsidian, geodes + geodes_robot, ore_robot, clay_robot, obsidian_robot, geodes_robot + 1, time - 1});
	}
	return best;

}

int main(void){
	int T;
	cin >> T;
	int solution1 = 0;
	int solution2 = 1;
	for (int t = 0; t < T; t++){
		int id, ore_cost, clay_cost, obsidian_cost_ore, obsidian_cost_clay, geode_cost_ore, geode_cost_obsidian;
		cin >> id >> ore_cost >> clay_cost >> obsidian_cost_ore >> obsidian_cost_clay >> geode_cost_ore >> geode_cost_obsidian;
		solution1 += id * solve(ore_cost, clay_cost, obsidian_cost_ore, obsidian_cost_clay, geode_cost_ore, geode_cost_obsidian, 24);
		if (t < 3) solution2 *= solve(ore_cost, clay_cost, obsidian_cost_ore, obsidian_cost_clay, geode_cost_ore, geode_cost_obsidian, 32);
	}
	std::cout << "solution1 = " << solution1 << std::endl;
	std::cout << "solution2 = " << solution2 << std::endl;
}
