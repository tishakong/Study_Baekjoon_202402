#include <iostream>
#include <vector>
#include <string>
//근데 string은 너무 길어지면 비효율적이라고 함. 대신 ostringstream?을 쓰라는 얘기 있었음

using namespace std;

int w = 0, b = 0;

void quad_tree(const vector<vector<int>>& matrix, int x, int y, int size) {
    bool ok = true;
    int target = matrix[x][y];

    for (int i = x; i < x + size; ++i) {
        for (int j = y; j < y + size; ++j) {
            if (matrix[i][j] != target) {
                ok = false;
                break;
            }
        }
        if (!ok) break;
    }

    if (ok) {
        if (target == 0) {
            w++;
        } else {
            b++;
        }    } 
    else {
        int new_size = size / 2;
        for (int i = 0; i < 2; ++i) {
            for (int j = 0; j < 2; ++j) {
                quad_tree(matrix, x + i * new_size, y + j * new_size, new_size);
            }
        }
    }
}

int main() {
    int n;
    cin >> n;

    vector<vector<int>> matrix(n, vector<int>(n));

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> matrix[i][j];
        }
    }

    quad_tree(matrix, 0, 0, n);

    cout << w << endl;
    cout << b << endl;
    
    return 0;
}
