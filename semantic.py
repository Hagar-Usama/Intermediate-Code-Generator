from parser_genrator import show_parser_table


def modify_actions(actions):
    '''
    prepares the list to parsing tree
    '''
    action_list = []

    for action in actions:
        x = action.split("⟶")
        y = []
        for i in x:
            print(y)
            y.append(i.strip())
        if len(y) > 0:
            action_list.append(y)

    #print(action_list)
    return action_list


def post_modify_actions(actions):
    action_list = []

    actions.remove(['Success'])

    for action in actions:
        #print(f"action is: {action}")
        if action[0].startswith("Match"):
            action_list.append(["Match"])
        elif action[0].startswith("Consume"):
            action_list.append(["Consume"])
        elif action[1].startswith("not found"):
            action_list.append(["epsilon"])
        else:
             action_list.append(action)
            
    #list_them(action_list)

    return action_list
      

def post_modify_actions_2(actions):
    action_list = []
    for action in actions:
        if len(action)==2:
            x = []
            x.append(action[0].split())
            x.append(list_it(action[1]))
            action_list.append(x)
        else:
            action_list.append(action)
    #print(action_list)
    return action_list


def list_it(str_list):
    x = str_list
    x = x.replace(']','') 
    x = x.replace('[','') 
    x = x.replace("'",'')  
    x = x.split(',')

    y = []
    for i in x:
        y.append(i.strip())

    return y

def list_them(actions):
    action_list = []

    for action in actions:
        if isinstance(action, list):
            action_list.append(list_it(action_list))
    print(action_list)

def split_actions(action):
    
    if len(action) == 2:
        return action[0],action[1]
    else:
        return action[0]




def main():
    actions = ["E   ⟶   ['T', 'R']", "T   ⟶   ['F', 'S']", "F   ⟶   ['n']", 'Match : n', "S   ⟶   ['𝛆']", 'Consume 𝛆', "R   ⟶   ['+', 'E']", 'Match : +', "E   ⟶   ['T', 'R']", "T   ⟶   ['F', 'S']", "F   ⟶   ['n']", 'Match : n', "S   ⟶   ['*', 'T']", 'Match : *', "T   ⟶   ['F', 'S']", "F   ⟶   ['n']", 'Match : n', "S   ⟶   ['𝛆']", 'Consume 𝛆', "R   ⟶   ['𝛆']", 'Consume 𝛆', 'Match : $', 'Success']
    act = modify_actions(actions)
    act = post_modify_actions(act)
    post_modify_actions_2(act)


   

    pass

if __name__ == '__main__':
    main()