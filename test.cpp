#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
using namespace std;

vector<int> longestIncreasingSubsequence(const vector<int>& arr) {
    if (arr.empty()) {
        return {};
    }

    int n = arr.size();
    
    vector<int> dp(n, 1);
    
    vector<int> predecessor(n, -1);
    
    int max_lis_length = 1;
    int end_index = 0; 

    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (arr[i] > arr[j]) {
                if (1 + dp[j] > dp[i]) {
                    dp[i] = 1 + dp[j];
                    predecessor[i] = j; 
                }
            }
        }
        
        if (dp[i] > max_lis_length) {
            max_lis_length = dp[i];
            end_index = i;
        }
    }

    vector<int> lis_sequence;
    int current_index = end_index;

    stack<int> s;

    while (current_index != -1) {
        s.push(arr[current_index]);
        current_index = predecessor[current_index];
    }

    while (!s.empty()) {
        lis_sequence.push_back(s.top());
        s.pop();
    }

    return lis_sequence;
}

int main() {
    int a; cin>>a;

    vector<int> sequence;
    while(a--){
        int b;cin>>b;
        sequence.push_back(b);
    }

    cout << "Input Sequence: ";
    for (int x : sequence) {
        cout << x << " ";
    }
    cout << endl;

    vector<int> lis = longestIncreasingSubsequence(sequence);

    cout << "-----------------------------------" << endl;
    cout << "Length of the LIS: " << lis.size() << endl;
    cout << "The Largest Monotonically Increasing Subsequence (LIS) is: ";
    
    for (int x : lis) {
        cout << x << " ";
    }
    cout << endl;

    return 0;
}