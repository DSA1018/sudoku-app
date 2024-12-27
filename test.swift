func make_board () -> [[Int]] {
    var board:[[Int]] = []
    var row_count = 1
    while row_count < 10 {
        var col_count = 1
        var row: [Int] = []
        while col_count < 10 {
            row.append(col_count)
            col_count = col_count + 1
        }
        board.append(row)
        row_count = row_count + 1
    }
    return board
}

func print_board(board: [[Int]]) {
    print("----------------------------------------")
    for row in board{
        for cell in row {
            print ("| " + String(cell), terminator: " ")
        }
        print("|")
        print("----------------------------------------")
    }
}

let board: [[Int]] = make_board()

print_board(board: board)