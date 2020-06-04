from parser_genrator import show_parser_table
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




def main():
    actions = ["E   ⟶   ['T', 'R']", "T   ⟶   ['F', 'S']", "F   ⟶   ['n']", 'Match : n', "S   ⟶   ['𝛆']", 'Consume 𝛆', "R   ⟶   ['+', 'E']", 'Match : +', "E   ⟶   ['T', 'R']", "T   ⟶   ['F', 'S']", "F   ⟶   ['n']", 'Match : n', "S   ⟶   ['*', 'T']", 'Match : *', "T   ⟶   ['F', 'S']", "F   ⟶   ['n']", 'Match : n', "S   ⟶   ['𝛆']", 'Consume 𝛆', "R   ⟶   ['𝛆']", 'Consume 𝛆', 'Match : $', 'Success']
    act = modify_actions(actions)
    act = post_modify_actions(act)
    post_modify_actions_2(act)


    # here gather all or import this to another file
    # code as in test cases
    # comment/remove redundant prints

    generated_code = """.class public name
.super java/lang/Object 
.method public <init>()V 
    aload_0 
    invokespecial java/lang/Object/<init>()V 
    return 
.end method 
.method public static main([Ljava/lang/String;)V
    .limit stack 10 
    .limit locals 100 
        iconst_3
    istore_1
    iconst_4
    istore_2
    iconst_5
    istore_3
    iload_1
    iload_2
    iconst_2
    imul
    iadd
    istore_3
    iload_3
    bipush 11
    if_icmpne L_96e
    iconst_2
    istore_1
    goto L_b37
    L_96e:
    bipush 7
    istore_2
L_b37:
    iload_2
    bipush 10
    if_icmpge L_2ec
    iload_2
    iconst_2
    iadd
    istore_2
    goto L_b37
L_2ec:     return
.end method"""

    # jasmin file
    jf = get_current_directory()
    output_file = 'code.j'
    input_path = jf + '/' +  output_file

    with open(input_path, 'w+') as f:
    
        f.write(generated_code)

if __name__ == '__main__':
    main()