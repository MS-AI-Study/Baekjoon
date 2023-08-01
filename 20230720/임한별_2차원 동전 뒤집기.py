import numpy as np
target = [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
arr = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
nparr = np.array(arr)
column = nparr.shape[0]
Row = nparr.shape[1]

def fliprow(arr, index):
    row_index = index
    flipped_row = arr[row_index, ::-1]
def flipcol(arr, index):
    col_index = index
    flipped_col = arr[:, col_index][::-1]


for i in len(column):
    fliprow(arr, index)
    
print(len(nparr))