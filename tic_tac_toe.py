tic_tac_toe = (
    ('X', 'O', 'X'),
    (' ', 'X', ' '),
    ('O', ' ', 'O')
)

def count_empty(board:tuple)-> int:
    count = 0
    for row in board:
        for cell in row:
            if cell == ' ':
                count += 1
    return count

if __name__ == "__main__":
    assert count_empty(tic_tac_toe) == 3
