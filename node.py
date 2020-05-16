import uuid
from semantic import split_actions, modify_actions, post_modify_actions, post_modify_actions_2


def get_node_uuid():
    _NODE_UUID = str(uuid.uuid4())[:8]

    return _NODE_UUID

ANSI_RESET = "\u001B[0m"
ANSI_RED = "\u001B[31m"
ANSI_GREEN = "\u001B[32m"
ANSI_YELLOW = "\u001B[33m"
ANSI_BLUE = "\u001B[34m"
ANSI_PURPLE = "\u001B[35m"
ANSI_ORANGE_BG = "\033[48;2;255;165;0m"
ANSI_DARK_CYAN = "\033[96m"

# it shall be 65 
unique_id = 129300
G_identifiers = {}
grammar_dict = {}
grammar_dict_sym = {}
start_symbol = ''


def print_dark_cyan(msg):
    print(f"{ANSI_DARK_CYAN}{msg}{ANSI_RESET}")


def print_yellow(msg):
    print(f"{ANSI_YELLOW}{msg}{ANSI_RESET}")

def print_purple(msg):
    print(f"{ANSI_PURPLE}{msg}{ANSI_RESET}")

def print_blue(msg):
    print(f"{ANSI_BLUE}{msg}{ANSI_RESET}")


def print_red(msg):
    print(f"{ANSI_RED}{msg}{ANSI_RESET}")


def print_green(msg):
    print(f"{ANSI_GREEN}{msg}{ANSI_RESET}")



class Node():
    # state is list of list. Each list is a row
    def __init__(self, name, parent, depth=0):
        self.name = name
        self.parent = parent
        self.children = []
        self.left = None
        self.right = None
        self.depth = depth
        self.id = get_node_uuid()
        self.leaves = []
    
    def __del__(self):
        #print('Destructor called, vehicle deleted.')
        pass

    def build_tree(self, action_list):
        '''
        stack.append(Root node)

        while stack is not empty:
            pop node n
            x = check_action_list:
                if  x is match or consume:
                    do nothing
                else:
                    insert x into n.children
                    push x into stack (reverse order)     
        '''
        actions = action_list.copy()
        nodes_list = [self]
        current_node = self

        while nodes_list:
            current_node = nodes_list.pop(-1)
            print_green(f"current Node| id:{current_node.id}, Name:{current_node.name}")

            pack = split_actions(actions.pop(0))
            print_blue(f"package is: {pack}")

            if len(pack) == 2:
                # create nodes:
                n = []
                for i in pack[1]:
                    temp = Node(i, current_node,current_node.depth + 1)
                    n.insert(0, temp)
                    current_node.children.append(temp)

                for j in n:
                    nodes_list.append(j)
            else:
                # it's match or consume
                self.leaves.append(current_node)
    
    def show_tree(self):

        nodes_list = [self]
        current_node = self

        
        while nodes_list:
            current_node = nodes_list.pop(0)
            print("---"*current_node.depth, end='-' )
            print_dark_cyan(f"Name: {current_node.name}, Id: {current_node.id}")
            

            
            for n in current_node.children:
                nodes_list.append(n)
                print("---"*n.depth, end='-' )
                print_yellow(f"Child Name: {n.name}, Id: {n.id}")

    def show_tree_2(self):

        nodes_list = [self]
        current_node = self

        
        while nodes_list:
            current_node = nodes_list.pop(-1)
            print("---"*(current_node.depth), end='' )
            print_dark_cyan(f"Node Name: {current_node.name}")

            #print_dark_cyan(f"Name: {current_node.name}, Id: {current_node.id}")
            
            l = []
            for n in current_node.children:
                l.insert(0,n)
                #print("_"*n.depth, end='-' )
                #print_yellow(f"Child Name: {n.name}, Id: {n.id}")
                #print_yellow(f"Child Name: {n.name}")

            for j in l:
                nodes_list.append(j)
            





'''
dfs(initial_state, goal):
            # returns Success or Failure

            frontier = stack.new(initial_state)
            explored = set.new()

            while not frontier.isEmpty():
                state = frontier.pop()
                explored.add(state)

                if goal(state):
                    return Success(state)
                
                # note: in a tree the neighbors of a state
                # are (parent, children)
                # neighbors are left,right,up,down
                for neighbor in state.neighbors():
                    if neighbor not in frontier U explored:
                        frontier.push(neighbor)
                    
            return Failure
 '''

print(get_node_uuid())
print(get_node_uuid())

actions = ["E   ⟶   ['T', 'R']", "T   ⟶   ['F', 'S']", "F   ⟶   ['n']", 'Match : n', "S   ⟶   ['𝛆']", 'Consume 𝛆', "R   ⟶   ['+', 'E']", 'Match : +', "E   ⟶   ['T', 'R']", "T   ⟶   ['F', 'S']", "F   ⟶   ['n']", 'Match : n', "S   ⟶   ['*', 'T']", 'Match : *', "T   ⟶   ['F', 'S']", "F   ⟶   ['n']", 'Match : n', "S   ⟶   ['𝛆']", 'Consume 𝛆', "R   ⟶   ['𝛆']", 'Consume 𝛆', 'Match : $', 'Success']
act = modify_actions(actions)
act = post_modify_actions(act)
act = post_modify_actions_2(act)
print_dark_cyan(act)
root = Node("E", None)
root.build_tree(act)
x = root.children[1].children[1].children[0].children[1].children[1].children[0].children[0].name
x = root.children[1].children[1].children[0].children[0].depth
y = root.children[0].children[0]
z = y.children[0]
#del y
print(x)
print(z.name)
print(root.leaves)


#root.show_tree()
root.show_tree_2()
#print(y.name)
#print(y.name)
        