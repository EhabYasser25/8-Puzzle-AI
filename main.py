from rich import print
from rich.table import Table
from solvers import Solver

def print_puzzle(state, prev_state, title):
    table = Table(title=title)
    table.add_column("Parent", justify="center", style="cyan", no_wrap=True)
    table.add_column("Child", justify="center", style="magenta", no_wrap=True)
    for i in range(3):
        table.add_row(' '.join([str(x) for x in state[i]]), ' '.join([str(x) for x in prev_state[i]]))
    print(table)

if __name__ == '__main__':
    # Stage 1: Algorithm Selection
    print('.:[ 8-Puzzle Solver ]:.')
    print('[ ] Please select an algorithm:')
    print('     [-] Uninformed Search Methods:')
    print('         [1] Depth-First Search')
    print('         [2] Breadth-First Search')
    print('     [-] Informed Search Methods:')
    print('         [3] A* Search - Manhattan Distance')
    print('         [4] A* Search - Euclidean Distance')

    while True:
        user_choice_algorithm = input('Your Choice: ')
        if user_choice_algorithm in ['1', '2', '3', '4']: break
        print('[!] Invalid choice.')
    
    # Stage 2: Initial State
    initial_state = ''
    print('[ ] Enter 8-Puzzle Initial State:')
    for i in range(3):
        row = input().replace(' ', '')

        # Invalid Input - Error Handler
        if len(row) != 3:
            print("I can't solve puzzles larger than 3x3.")
            exit()
        elif not all([x.isnumeric() for x in row]):
            print("I can't solve puzzles containing non-numeric values.")
            exit()
        
        initial_state += row
    initial_state += str(initial_state.index('0'))
    # initial_state example: 1234567808

    # Stage 3: Solvers
    goal_state = '0123456780'
    solver = Solver()
    # solution, steps, cost_of_path, nodes_expanded, search_depth, running_time = solver.solve(user_choice_algorithm, initial_state, goal_state)
    solution, running_time = solver.solve(user_choice_algorithm, initial_state, goal_state)
    print('Solution:', solution)
    print('Time:', running_time)

    # Stage 4: Results
    # print()
    # for i in range(len(steps)):
    #     if len(steps) - 1 != i:
    #         print_puzzle(steps[i], steps[i+1], f'Step #{i+1}')
    # print()
    # print('.:[ SOLUTION STATS ]:.')
    # print('[ ] [bold]Cost of Path[/bold]:', cost_of_path)
    # print('[ ] [bold]Nodes Expanded[/bold]:', str(set(nodes_expanded)))
    # print('[ ] [bold]Search Depth[/bold]:', search_depth)
    # print('[ ] [bold]Running Time[/bold]:', running_time)