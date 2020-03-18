'''Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3

'''
board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']]

#Can you hear me?

def wordExists(board,word):
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == word[0] and dfs_search(i,j,board,word,0):
        return True
  return False
      
      

def dfs_search(i,j,board,word,count):
  if count == len(word):
    return True

  if i<0 or i>= len(board) or j<0 or j>=len(board[i]) or board[i][j] != word[count]:
    return False
  
  temp_letter = board[i][j]
  board[i][j]=' '

  found = dfs_search(i+1,j,board,word,count+1) or dfs_search(i-1,j,board,word,count+1) or dfs_search(i,j-1,board,word,count+1) or dfs_search(i,j+1,board,word,count+1)

  board[i][j] = temp_letter


  return found
print(wordExists(board,'ABCCEDC'))

      

