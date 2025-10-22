#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

int main() {
    long long int n;
    cin >> n;
    long long int cheese = 0;
    long long int glory = 0;
    vector<vector<long long int>> events;
    for (int i = 0; i < n; i++) {
        string event;
        long long int sec;
        long long int curCheese;
        long long int curGlory;
        cin >> event >> sec >> curCheese >> curGlory;
        long long int mult;
        if (event == "CAUGHT") {
            mult = 1;
        } else {
            mult = -1;
        } 
        vector<long long int> curEvent = {mult,sec,curCheese,curGlory};
        events.push_back(curEvent);
    }
    long long int maxS; 
    cin >> maxS;
    for (vector<long long int> i: events) {
        if (i[1] < maxS) {
            cheese += i[0]*i[2];
            glory += i[0]*i[3];
        }
    }
    cout << cheese << " " << glory;
}
