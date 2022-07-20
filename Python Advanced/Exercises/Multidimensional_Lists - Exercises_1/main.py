rows, cols = [3, 3]
matrix = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
          ]

for row in range(rows - 1):
    for col in range(cols - 1):

        if matrix[row][col] == "5":

            print(matrix[row - 1][col - 1])  # 1 ↖
            print(matrix[row - 1][col])  # 2 ↑
            print(matrix[row - 1][col + 1])  # 3 ↗
            print(matrix[row][col - 1])  # 4 ←
            print(matrix[row][col])  # 5 ⑤ ⒌ ⑸ ⚒ ☕ ↻ 🔃
            print(matrix[row][col + 1])  # 6 →
            print(matrix[row + 1][col - 1])  # 7 ↙
            print(matrix[row + 1][col])  # 8 ↓
            print(matrix[row + 1][col + 1])  # 9 ↘