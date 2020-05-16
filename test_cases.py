import pytest
from node import Node
from semantic import modify_actions, post_modify_actions, post_modify_actions_2

ANSI_RESET = "\u001B[0m"
ANSI_RED = "\u001B[31m"
ANSI_GREEN = "\u001B[32m"
ANSI_YELLOW = "\u001B[33m"
ANSI_BLUE = "\u001B[34m"
ANSI_PURPLE = "\u001B[35m"
#ANSI_YELLOW = "\u001B[36m"



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


def test_node_tree():
    case = 'test node tree [case 1]'
    actions = ["E   ⟶   ['T', 'R']", "T   ⟶   ['F', 'S']", "F   ⟶   ['n']", 'Match : n', "S   ⟶   ['𝛆']", 'Consume 𝛆', "R   ⟶   ['+', 'E']", 'Match : +', "E   ⟶   ['T', 'R']", "T   ⟶   ['F', 'S']", "F   ⟶   ['n']", 'Match : n', "S   ⟶   ['*', 'T']", 'Match : *', "T   ⟶   ['F', 'S']", "F   ⟶   ['n']", 'Match : n', "S   ⟶   ['𝛆']", 'Consume 𝛆', "R   ⟶   ['𝛆']", 'Consume 𝛆', 'Match : $', 'Success']
    act = modify_actions(actions)
    act = post_modify_actions(act)
    act = post_modify_actions_2(act)

    root = Node("E", None)
    root.build_tree(act)
    actual_value = root.children[1].children[1].children[0].children[1].children[1].children[0].children[0].name
    correct_value = 'n'
    assert_it(correct_value, actual_value, case )

    case = 'test node tree [case 2]'
    actual_value = root.children[1].children[1].children[0].children[0].depth
    correct_value = 4
    assert_it(correct_value, actual_value, case)





def assert_it(correct_value, actual_value, case=""):
        assert correct_value == actual_value,\
        f"{ANSI_RED}[failed] {case}"\
        f" Expected ( {correct_value} )\n got\n ( {actual_value} ){ANSI_RESET}"
        print_green(f"[success] {case}")


def main():
    ###################
    # Run tests
    ###################
    # Sorted by checklist order, feel free to comment/un-comment
    # any of those functions.
    try:
        test_node_tree()
        print_blue('*.*.'*15)
        

    except AssertionError as e:
        print("Test case failed:\n", str(e))
        exit(-1)


if __name__ == "__main__":
    main()
""" 

{
    'METHOD_BODY': [['STATEMENT_LIST']],
    'STATEMENT_LIST': [['STATEMENT', ' ', 'STATEMENT_LIST_2']],
    'STATEMENT_LIST_2': [['STATEMENT', ' ', 'STATEMENT_LIST_2'], ['𝛆']],
    'STATEMENT': [['DECLARATION'], ['IF'], ['WHILE'], ['ASSIGNMENT']],
    'DECLARATION': [['PRIMITIVE_TYPE', ' ', "'id'", ' ', "';'"]],
    'PRIMITIVE_TYPE': [["'int'"], ["'float'"]],
    'IF': [["'if'", ' ', "'('", ' ', 'EXPRESSION', ' ', "')'", ' ', "'{'", ' ', 'STATEMENT', ' ', "'}'", ' ', "'else'", ' ', "'{'", ' ', 'STATEMENT', ' ', "'}'"]],
    'WHILE': [["'while'", ' ', "'('", ' ', 'EXPRESSION', ' ', "')'", ' ', "'{'", ' ', 'STATEMENT', ' ', "'}'"]],
    'ASSIGNMENT': [["'id'", ' ', "'assign'", ' ', 'EXPRESSION', ' ', "';'"]],
    'EXPRESSION': [['SIMPLE_EXPRESSION', ' ', 'EXPRESSION_2']],
    'EXPRESSION_2': [["'relop'", ' ', 'SIMPLE_EXPRESSION'], ['𝛆']],
    'SIMPLE_EXPRESSION': [['TERM', ' ', 'SIMPLE_EXPRESSION_2'], ['SIGN', ' ', 'TERM', ' ', 'SIMPLE_EXPRESSION_2']],
    'SIMPLE_EXPRESSION_2': [["'addop'", ' ', 'TERM', ' ', 'SIMPLE_EXPRESSION_2'], ['𝛆']],
    'TERM': [['FACTOR', ' ', 'TERM_2']],
    'TERM_2': [["'mulop'", ' ', 'FACTOR', ' ', 'TERM_2'], ['𝛆']],
    'FACTOR': [["'id'"], ["'num'"], ["'('", ' ', 'EXPRESSION', ' ', "')'"]],
    'SIGN': [["'addop'"]]
    
}
 """