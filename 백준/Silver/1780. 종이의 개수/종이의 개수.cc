#include <iostream>
#include <vector>

using namespace std;

int m = 0, z = 0, o = 0;

void d_q(const vector<vector<int>>& matrix, int row, int col, int size) {
    int target = matrix[row][col]; // 비교할 기준 숫자
    bool ok = true;

    for (int i = row; i < row + size; ++i) {
        for (int j = col; j < col + size; ++j) {
            // 값이 다르면 ok를 false로 바꾸고 break
            if (matrix[i][j] != target) {
                ok = false;
                break;
            }
        }
        if (!ok) break;
    }

    if (ok) {
        if (target == -1) {
            m++;
        } else if (target == 0) {
            z++;
        } else {
            o++;
        }
    } else {
        int new_size = size / 3;
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) {
                d_q(matrix, row + i * new_size, col + j * new_size, new_size);
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

    d_q(matrix, 0, 0, n);

    cout << m << endl;
    cout << z << endl;
    cout << o << endl;

    return 0;
}
