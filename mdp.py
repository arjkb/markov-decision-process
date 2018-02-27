import copy

old_values = dict()
values = dict()
discount = 1
actions = ['east', 'west', 'exit']
states = ['TERMINAL_STATE', 'a', 'b', 'c', 'd', 'e']

possible_actions = {
    'a': ['exit'],
    'b': ['east', 'west'],
    'c': ['east', 'west'],
    'd': ['east', 'west'],
    'e': ['exit']
}

def get_TP(state, action):
    if state == 'TERMINAL_STATE':
        return ()
    elif (state, action) == ('a', 'exit'):
        return ('TERMINAL_STATE', 1)
    elif (state, action) == ('b', 'west'):
        return ('a', 1)
    elif (state, action) == ('b', 'east'):
        return ('c', 1)
    elif (state, action) == ('c', 'west'):
        return ('b', 1)
    elif (state, action) == ('c', 'east'):
        return ('d', 1)
    elif (state, action) == ('d', 'west'):
        return ('c', 1)
    elif (state, action) == ('d', 'east'):
        return ('e', 1)
    elif (state, action) == ('e', 'exit'):
        return ('TERMINAL_STATE', 1)

def rewards(state, action, ns):
    if (state, action, ns) == ('a', 'exit', 'TERMINAL_STATE'):
        return 20
    elif (state, action, ns) == ('e', 'exit', 'TERMINAL_STATE'):
        return 1
    else:
        return 0


def main():
    for i in range(5):
        print("iteration #{}".format(i))

if __name__ == '__main__':
    main()
