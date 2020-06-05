#from parser_genrator import show_parser_table
import os


def get_current_directory(): 
    current_path = os.path.dirname(os.path.abspath(__file__))
    return current_path

def modify_actions(actions):
    '''
    prepares the list to parsing tree
    '''
    action_list = []


    for action in actions:
        x = action.split("⟶")
        y = []
        for i in x:
            y.append(i.strip())
        

        if len(y) ==2:
            if y[1] == "not found":
                y[1] = "['𝛆']"
                action_list.append(y)
                action_list.append('Consume 𝛆')
            else:
                action_list.append(y)
        else:
            action_list.append(y)


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
    #print(action_list)

def split_actions(action):
    
    if len(action) == 2:
        if action[1] != ['not found']:
            return action[0],action[1]
    else:
        return action[0]

