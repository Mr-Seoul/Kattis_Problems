#include<iostream>
#include<array>
#include<vector>
#include<cmath>
#include<bitset>

using namespace std;

long long int findIndex(long long int val) {
    if (val == 2) {
        return 1;
    } else if (val % 2 == 0 || val == 1) {
        return 0;
    } else {
        return ((val+1)/2);
    }
}

vector<long long int> twoVal(long long int val, vector<char> list) {
    long long int i = 2;

    while (i < list.size()) {
        if (list[findIndex(i)] == '1' && list[findIndex(val-i)] == '1') {
            return vector<long long int>{i,val-i};
        } else {
            if (i == 2) {
                i += 1;
            } else {
                i += 2;
            }
        }
    }
    return vector<long long int>{'0','0'};
}

int main() {
    //Parse inputs
    long long int n;
    cin >> n;

    //Init values
    vector<char> possiblePrime(floor(n/2)+1,'1');
    possiblePrime[0] = false;

    //Sieve the primes
    for (long long int i = 3; i < ceil(sqrt(n+1)); i += 2) {
        if (possiblePrime[findIndex(i)] == '1') {
            for (long long int j = i*i; j < n+1; j += i) {
                possiblePrime[findIndex(j)] = '0';
            }
        }
    }

    if (n < 7) {
        cout << "Neibb";
        return 0;
    }

    long long int first = (n % 2 == 0 ? 2 : 3);
    long long int target = n - first;

    vector<long long int> result = twoVal(target,possiblePrime);

    cout << first << " " << result[0] << " " << result[1];
    return 0;
}