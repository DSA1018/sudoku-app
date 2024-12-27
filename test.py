from flask import Flask, render_template

app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
#learn more about json configurations
#does not even work rn

@app.route("/")
#to tell flask what url should trigger the function


def make_board():
    board = [[]]
    for i in range(9):
        board.append([])
        for j in range(9):
            board[i].append(j + 1)
    board_text = print_board(board)
    board_text = board_text.replace("\n", "<br>")  # Replace newlines with <br> tags
    return render_template('index.html', board_text=board_text)

def print_board(board: list[list[int]]):
    text = ""
    for i in range (len(board)-1):
        row = board[i]
        for elt in row:
            text += f"| {elt}"
        text += " | \n"
    return text

if __name__ == '__main__':
    app.run()