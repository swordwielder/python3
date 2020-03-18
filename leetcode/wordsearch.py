def exist(self, board: List[List[str]], word: str) -> bool:
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == word[0] and self.dfs_search(i,j,board,word,0):
                return True




def dfs_search(self,i,j, board, word, count):
    if count == len(word):
        return True

    if i< 0 or i >=len(board) or j<0 or j>=len(board[i]) or board[i][j] != word[count]:
        return False

    temp_letter= board[i][j]
    board[i][j]=' '

    found = self.dfs_search(i+1,j, board, word, count+1) or self.dfs_search(i-1,j, board, word, count+1) or self.dfs_search(i,j+1, board, word, count+1) or self.dfs_search(i,j-1, board, word, count+1)

    board[i][j] = temp_letter

    return found
