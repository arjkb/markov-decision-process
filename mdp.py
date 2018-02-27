import copy

# def get_TP(state, action):
#     if state == 'TERMINAL_STATE':
#         return [((None, 0))]
#     elif (state, action) == ('a', 'go'):
#         # print("ha!")
#         return [('b', 0.5), ('c', 0.5)]
#     elif (state, action) == ('b', 'go'):
#         return [('d', 1)]
#     elif (state, action) == ('c', 'go'):
#         return [('a', 0.5), ('e', 0.5)]
#     elif (state, action) == ('d', 'go'):
#         return [('f', 1)]
#     elif (state, action) == ('e', 'go'):
#         return [('d', 0.5), ('f', 0.5)]
#     elif (state, action) == ('f', 'go'):
#         return [('TERMINAL_STATE', 1)]
#
#
# def rewards(state, action, ns):
#     return 1

def get_TP(state, action):
    if state == 'TERMINAL_STATE':
        return (None, 0)
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

# def foo(st, ac):
#     if (st, ac) == ('hi', 100):
#         return ('bye', 404)

def main():
    old_values = dict()
    values = dict()
    # discount = 0.9
    # actions = ['go', 'exit']
    # states = ['TERMINAL_STATE', 'a', 'b', 'c', 'd', 'e', 'f']
    #
    # possible_actions = {
    #     'TERMINAL_STATE': [],
    #     'a': ['go'],
    #     'b': ['go'],
    #     'c': ['go'],
    #     'd': ['go'],
    #     'e': ['go'],
    #     'f': ['go']
    # }

    discount = 1
    actions = ['east', 'west', 'exit']
    states = ['TERMINAL_STATE', 'a', 'b', 'c', 'd', 'e']

    possible_actions = {
        'TERMINAL_STATE': [],
        'a': ['exit'],
        'b': ['east', 'west'],
        'c': ['east', 'west'],
        'd': ['east', 'west'],
        'e': ['exit']
    }

    for state in states:
        if state not in old_values:
            old_values[state] = 0

    values = copy.deepcopy(old_values)

    for i in range(5):
        # print("iteration #{}".format(i))
        for state in states:
            s = 0
            q = list()
            for action in possible_actions[state]:
                # print(" st={}, ac={}".format(state, action))
                ns, p = get_TP(state, action)
                # print(get_TP(state, action))
                # print(" {} -{}-> {}, p = {}".format(state, action, ns, p))
                s = p * (rewards(state, action, ns) + discount * old_values[ns])
                # s = sum(map(lambda ns, p: p * (rewards(state, action, ns) + discount*old_values[ns]), get_TP(state, action)))
                # print(s)
                q.append(s)
            # print(q)
            values[state] = max(q) if (len(q) > 0) else 0
        print(" iter {}, values = {}".format(i, values))
        old_values = copy.deepcopy(values)

    print(values)


if __name__ == '__main__':
    main()
