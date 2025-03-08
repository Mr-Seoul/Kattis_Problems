#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <sstream>


using namespace std;

int main() {
    long long int n;
    string instructions = "";

    string line;
    getline(cin, line);  

    istringstream iss(line);
    iss >> n;
    if (!iss.eof()) {
        iss >> instructions;
    };
    long long int curval = pow(2,n+1)-1;
    long long int curNode = 0;
    
    if (instructions.size() > 0) {
        for (int i = 0; i < instructions.size()-1; i++) {
            curval -= pow(2,i+1);
        }
        for (int i = 0; i < instructions.size();i++) {
            if (instructions[i] == 'R') {
            curNode += pow(2,instructions.size()-1-i);
            }
        }      
        curNode += 1;
    }

    curval -= curNode;
    
    cout << curval;
    return 0;
}