projects = []
def sdk(E, F):
    return [X + Y for X in E for Y in F]
rw = 'ABCDEFGHI'
cl = '123456789'
columns_review = cl[::-1]
number_of_boxes = sdk(rw, cl)
total_row_units = [sdk(h, cl) for h in rw]
total_column_units = [sdk(rw, c) for c in cl]
total_square_units = [sdk(twg, cwg) for twg in ('ABC','DEF','GHI') for cwg in ('123','456','789')]
total_D1_units = [[rw[s]+cl[s] for s in range(len(rw))]]
total_D2_units = [[rw[s]+columns_review[s] for s in range(len(rw))]]
unit_list = total_row_units + total_column_units + total_square_units + total_D1_units + total_D2_units
number_of_units = dict((i, [u for u in unit_list if i in u]) for i in number_of_boxes)
store = dict((i, set(sum(number_of_units[i],[]))-set([i])) for i in number_of_boxes)
def assigning_value(total_values, boxes, number):
    if total_values[boxes] == number:
        return total_values
    total_values[boxes] = number
    if len(number) == 1:
        projects.append(total_values.copy())
    return total_values
def naked_twins(total_values):
    twins_value = [boxes for boxes in total_values.keys() if len(total_values[boxes]) == 2]
    same_value = [[box_no_1, box_no_2] for box_no_1 in twins_value for box_no_2 in store[box_no_1] if set(total_values[box_no_1]) == set(total_values[box_no_2])]
    for same in same_value:
        box_no_1 = same[0]
        box_no_2 = same[1]
        store_1 = set(store[box_no_1])
        store_2 = set(store[box_no_2])
        common_store = store_1 & store_2
        for single_store in common_store:
            if len(total_values[single_store]) > 1:
                for discard_number in total_values[box_no_1]:
                    total_values = assigning_value(total_values, single_store, total_values[single_store].replace(discard_number,''))
    return total_values
def grid_numbers(grid):
    total_values = []
    default_number = '123456789'
    for s in grid:
        if s == ".":
            total_values.append(default_number)
        elif s in default_number:
            total_values.append(s)
    assert len(total_values) == 81
    return dict(zip(number_of_boxes, total_values))
def display(total_values):
    width = 1+max(len(total_values[s]) for i in number_of_boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for h in rw:
        print(''.join(total_values[h+c].center(width)+('|' if c in '36' else '')
                      for c in cl))
        if h in 'CF': print(line)
    return
def eliminate(total_values):
    solved_number = [boxes for boxes in total_values.keys() if len(total_values[boxes]) == 1]
    for boxes in solved_number:
        digit = total_values[boxes]
        for stores in store[boxes]:
            total_values[stores] = total_values[stores].replace(digit,'')
    return total_values
def only_choice(total_values):
    for number_of_unit in unit_list:
        for digit in '123456789':
            dplaces = [boxes for boxes in number_of_unit if digit in total_values[boxes]]
            if len(dplaces) == 1:
                total_values = assigning_value(total_values, dplaces[0], digit)
    return total_values
def reduce_puzzle_size(total_values):
    solved_number = [boxes for boxes in total_values.keys() if len(total_values[boxes]) == 1]
    stalled = False
    while not stalled:
        solved_number_before = len([boxes for boxes in total_values.keys() if len(total_values[boxes]) == 1])
        total_values = eliminate(total_values)
        total_values = only_choice(total_values)
        total_values = naked_twins(total_values)
        solved_number_after = len([boxes for boxes in total_values.keys() if len(total_values[boxes]) == 1])
        stalled = solved_number_before == solved_number_after
        if len([boxes for boxes in total_values.keys() if len(total_values[boxes]) == 0]):
            return False
    return total_values
def search_value(total_values):
    total_values = reduce_puzzle_size(total_values)
    if total_values is False:
        return False  
    if all(len(total_values[i]) == 1 for i in number_of_boxes):
        return total_values  
    n, i = min((len(total_values[i]), i) for i in number_of_boxes if len(total_values[i]) > 1)
    for number in total_values[i]:
        sudoku = total_values.copy()
        sudoku[i] = number
        aim = search_value(sudoku)
        if aim:
            return aim
def solve(grid):
    total_values = grid_numbers(grid)
    total_values = search_value(total_values)
    return total_values
if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))
    try:
        from visualize import visualize_assignments
        visualize_assignments(projects)
    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')