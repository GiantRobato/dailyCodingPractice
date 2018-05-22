#include <iostream>
#include <map>
#include <ctype.h>
#include <vector>
#include <algorithm>

using namespace std;

const char* input1 = "abcde";
const char* input2 = "dbbaCEDbdAacCEAadcB";
const char* input3 = "EbAAdbBEaBaaBBdAccbeebaec";

typedef pair<char,int> score;

void tally(const char* input){
	cout << "input was: " << input << endl;
	string s(input);
	map<char,int> counts;
	vector<score> v;		//for sorting

	for(auto c : s) counts[tolower(c)] += (islower(c)) ? 1 : -1;

	//copy k-v pairs from map to iterator
	copy(counts.begin(),counts.end(), back_inserter<vector<score>>(v));

	//sort by letter order if not counts are equal
	sort(v.begin(), v.end(),
		[](const score& l, const score& r){
			if(l.second != r.second) return l.second > r.second;
			return l.first < r.first;
		});

	cout << "output: " << endl;
	for(auto it : v){
		cout << it.first << ":" << it.second;
		if(it != v.back()) cout << ", ";
	}
	cout << endl << endl;

}

int main(int argc, char* argv[]){
	tally(input1);
	tally(input2);
	tally(input3);
}





