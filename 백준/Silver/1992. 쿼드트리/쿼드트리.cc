#include <iostream>
#include <vector>
#include <string>

//근데 string은 너무 길어지면 비효율적이라고 함. 대신 ostringstream?을 쓰라는 얘기 있었음

using namespace std;

string result = ""; // 결과 저장할 변수

void quad_tree(const vector<vector<int>>& matrix, int x, int y, int size) {
    bool ok = true;
    int target = matrix[x][y];

    // 인접한 값들이 모두 같은지 확인
    for (int i = x; i < x + size; ++i) {
        for (int j = y; j < y + size; ++j) {
            if (matrix[i][j] != target) {
                ok = false;
                break;
            }
        }
        if (!ok) break;
    }

    // 압축 가능하면 result에 숫자를 추가
    if (ok) {
        result += to_string(target); 
    } 
    // 압축 불가능하면 4조각으로 나누어 재귀 호출
    else {
        result += '(';
        int new_size = size / 2;
        for (int i = 0; i < 2; ++i) {
            for (int j = 0; j < 2; ++j) {
                quad_tree(matrix, x + i * new_size, y + j * new_size, new_size);
            }
        }
        result += ')';
    }
}

int main() {
    int n;
    cin >> n;

    vector<vector<int>> matrix(n, vector<int>(n));

    // 입력
    for (int i = 0; i < n; ++i) {
        string line;
        cin >> line;
        for (int j = 0; j < n; ++j) {
            matrix[i][j] = line[j] - '0'; // 문자를 숫자로 변환
        }
    }

    quad_tree(matrix, 0, 0, n);

    cout << result << endl;

    return 0;
}
