
import sys

infinity = sys.maxsize

def solve_puzzle(Board,Source,Destination):
    #Board represents the board being used
    #Source is the beginning space
    #Destination is where we want to go


    visited = {}
    path = []
    potential_paths =[]
    x_source = Source[0]
    y_source = Source[1]
    x_dest = Destination[0]
    y_dest = Destination[1]
    board_row_len = len(Board)
    board_col_len = len(Board[0])

    if x_dest <= board_row_len-1 and y_dest <= board_col_len-1 and x_dest >= 0 and y_dest >= 0 \
            and Board[x_dest][y_dest] != '#':
        if x_source == x_dest and y_dest == y_source:
            path.append((x_source,y_source))
            return path
        elif x_source <= board_row_len-1 and y_source <= board_col_len-1 and x_source >= 0 and y_source >= 0 \
            and Board[x_source][y_source] != '#':
            moves_amt = 0
            mincost = ([],'',infinity)
            pathdir = ""
            puzzle_helper(Board,x_source,y_source,x_dest,y_dest,path,visited,moves_amt, potential_paths,board_row_len,
                          board_col_len, pathdir)
            for item in potential_paths:
                if item[2] < mincost[2]:
                    mincost = item
            if mincost[2] == infinity:
                return None
            return (mincost[0],mincost[1])
        else:
            return None
    else:
        return None


def puzzle_helper(Board,x_src, y_src, x_dest, y_dest, path, visted, move_amt, potent_paths, xLen, yLen, path_str):

    path.append((x_src,y_src))
    visted[(x_src, y_src)] = (x_src, y_src)

    if (x_src < 0 or y_src < 0 or x_src >=xLen or y_src >=yLen):
        return None
    if (Board[x_src][y_src] != '-'):
        return None
    if (x_src == x_dest and y_src == y_dest):
        full_path = []
        full_path.extend(path)
        potent_paths.append((full_path, path_str, move_amt))
        return

    left_cost = (x_src, y_src-1)
    if left_cost not in visted:
        move_amt += 1
        path_str += 'L'
        puzzle_helper(Board, x_src, y_src-1, x_dest, y_dest, path, visted, move_amt, potent_paths, xLen, yLen, path_str)
        path.pop()
        del visted[left_cost]
        move_amt -= 1
        path_str = path_str[:-1]
    right_cost = (x_src,y_src+1)
    if right_cost not in visted:
        move_amt += 1
        path_str += 'R'
        puzzle_helper(Board, x_src, y_src+1, x_dest, y_dest, path, visted, move_amt, potent_paths, xLen, yLen, path_str)
        path.pop()
        del visted[right_cost]
        move_amt -= 1
        path_str = path_str[:-1]
    up_cost = (x_src-1,y_src)
    if up_cost not in visted:
        move_amt += 1
        path_str += 'U'
        puzzle_helper(Board, x_src-1, y_src, x_dest, y_dest, path, visted, move_amt, potent_paths, xLen, yLen, path_str)
        path.pop()
        del visted[up_cost]
        move_amt -= 1
        path_str = path_str[:-1]
    down_cost = (x_src+1,y_src)
    if down_cost not in visted:
        move_amt += 1
        path_str += 'D'
        puzzle_helper(Board, x_src+1, y_src, x_dest, y_dest, path, visted, move_amt, potent_paths, xLen, yLen, path_str)
        path.pop()
        del visted[down_cost]
        path_str = path_str[:-1]
        move_amt -= 1



