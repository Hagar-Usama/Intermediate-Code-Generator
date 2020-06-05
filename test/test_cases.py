import pytest
from .modules.Symbol import SymTable, Symbol
from .modules.Node import Node, reduce_tree, get_str_val, get_val_2, get_val_virtual
from .modules.Node import generate_code
from .modules.semantic import modify_actions, post_modify_actions, post_modify_actions_2

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

def test_modify_actions():

    case = 'test modify actions [case 1]'
    actions = ["E   ⟶   ['T', 'R']", "T   ⟶   ['F', 'S']", "F   ⟶   ['n']", 'Match : n', "S   ⟶   ['𝛆']", 'Consume 𝛆', "R   ⟶   ['+', 'E']", 'Match : +', "E   ⟶   ['T', 'R']", "T   ⟶   ['F', 'S']", "F   ⟶   ['n']", 'Match : n', "S   ⟶   ['*', 'T']", 'Match : *', "T   ⟶   ['F', 'S']", "F   ⟶   ['n']", 'Match : n', "S   ⟶   ['𝛆']", 'Consume 𝛆', "R   ⟶   ['𝛆']", 'Consume 𝛆', 'Match : $', 'Success']

    actual_value = modify_actions(actions)
    correct_value = None
    assert_it(correct_value, None, case )
    case = 'test modify actions [case 2]'

    actions = [
     "METHOD_BODY   ⟶   ['STATEMENT_LIST']", "STATEMENT_LIST   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']",
     "STATEMENT   ⟶   ['DECLARATION']", 'DECLARATION   ⟶   [\'PRIMITIVE_TYPE\', "\'id\'", "\';\'"]',
     'PRIMITIVE_TYPE   ⟶   ["\'int\'"]', "Match : 'int'", "Match : 'id'", "Match : ';'",
     "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['ASSIGNMENT']",
     'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]', "Match : 'id'",
      "Match : 'assign'", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']",
      "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']",
      "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'id\'"]', "Match : 'id'",
      'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   ["\'addop\'", \'TERM\', \'SIMPLE_EXPRESSION_2\']',
      "Match : 'addop'", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'id\'"]',
      "Match : 'id'", 'TERM_2   ⟶   ["\'mulop\'", \'FACTOR\', \'TERM_2\']', "Match : 'mulop'",
      'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found',
      'EXPRESSION_2   ⟶   not found', "Match : ';'", 'STATEMENT_LIST_2   ⟶   not found', 'Match : $',
      'Success']

    
    actual_value = modify_actions(actions)
    correct_value = [['METHOD_BODY', "['STATEMENT_LIST']"], ['STATEMENT_LIST', "['STATEMENT', 'STATEMENT_LIST_2']"], ['STATEMENT', "['DECLARATION']"], ['DECLARATION', '[\'PRIMITIVE_TYPE\', "\'id\'", "\';\'"]'], ['PRIMITIVE_TYPE', '["\'int\'"]'], ["Match : 'int'"], ["Match : 'id'"], ["Match : ';'"], ['STATEMENT_LIST_2', "['STATEMENT', 'STATEMENT_LIST_2']"], ['STATEMENT', "['ASSIGNMENT']"], ['ASSIGNMENT', '["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]'], ["Match : 'id'"], ["Match : 'assign'"], ['EXPRESSION', "['SIMPLE_EXPRESSION', 'EXPRESSION_2']"], ['SIMPLE_EXPRESSION', "['TERM', 'SIMPLE_EXPRESSION_2']"], ['TERM', "['FACTOR', 'TERM_2']"], ['FACTOR', '["\'id\'"]'], ["Match : 'id'"], ['TERM_2', "['𝛆']"], 'Consume 𝛆', ['SIMPLE_EXPRESSION_2', '["\'addop\'", \'TERM\', \'SIMPLE_EXPRESSION_2\']'], ["Match : 'addop'"], ['TERM', "['FACTOR', 'TERM_2']"], ['FACTOR', '["\'id\'"]'], ["Match : 'id'"], ['TERM_2', '["\'mulop\'", \'FACTOR\', \'TERM_2\']'], ["Match : 'mulop'"], ['FACTOR', '["\'num\'"]'], ["Match : 'num'"], ['TERM_2', "['𝛆']"], 'Consume 𝛆', ['SIMPLE_EXPRESSION_2', "['𝛆']"], 'Consume 𝛆', ['EXPRESSION_2', "['𝛆']"], 'Consume 𝛆', ["Match : ';'"], ['STATEMENT_LIST_2', "['𝛆']"], 'Consume 𝛆', ['Match : $'], ['Success']]
    assert_it(correct_value, actual_value, case )



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

    case = 'test node tree [case 3]'
    actual_value = root.children[0].children[1].children[0]
    correct_value = '𝛆'
    assert_it(correct_value, actual_value.name, case)

    print(f"first address {actual_value}")
    print(f"first address {id(actual_value)}")
    print(f"second address {root.leaves[0]}")

    
    case = 'test node tree [case 4]'
    actions = [
     "METHOD_BODY   ⟶   ['STATEMENT_LIST']", "STATEMENT_LIST   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']",
     "STATEMENT   ⟶   ['DECLARATION']", 'DECLARATION   ⟶   [\'PRIMITIVE_TYPE\', "\'id\'", "\';\'"]',
     'PRIMITIVE_TYPE   ⟶   ["\'int\'"]', "Match : 'int'", "Match : 'id'", "Match : ';'",
     "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['ASSIGNMENT']",
     'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]', "Match : 'id'",
      "Match : 'assign'", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']",
      "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']",
      "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'id\'"]', "Match : 'id'",
      'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   ["\'addop\'", \'TERM\', \'SIMPLE_EXPRESSION_2\']',
      "Match : 'addop'", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'id\'"]',
      "Match : 'id'", 'TERM_2   ⟶   ["\'mulop\'", \'FACTOR\', \'TERM_2\']', "Match : 'mulop'",
      'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found',
      'EXPRESSION_2   ⟶   not found', "Match : ';'", 'STATEMENT_LIST_2   ⟶   not found', 'Match : $',
      'Success']

    act = modify_actions(actions)
    act = post_modify_actions(act)
    act = post_modify_actions_2(act)

    root = Node("METHOD_BODY", None)
    root.build_tree(act)
    actual_value = root.children[0].children[0].children[0].name
    correct_value = 'DECLARATION'
    assert_it(correct_value, actual_value, case )


    case = 'test node tree [case 4]'
    actual_value = root.children[0].children[1].children[0].children[0].children[2].children[1].name
    correct_value = 'EXPRESSION_2'
    assert_it(correct_value, actual_value, case )

    # int y; y=5; int x; x = y+y*5;
    case = 'test node tree [case 5]'
    actions = ["METHOD_BODY   ⟶   ['STATEMENT_LIST']", "STATEMENT_LIST   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']",
             "STATEMENT   ⟶   ['DECLARATION']", 'DECLARATION   ⟶   [\'PRIMITIVE_TYPE\', "\'id\'", "\';\'"]',
             'PRIMITIVE_TYPE   ⟶   ["\'int\'"]', "Match : 'int'", "Match : 'id'", "Match : ';'",
             "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['ASSIGNMENT']",
             'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]', "Match : 'id'", "Match : 'assign'",
             "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']",
             "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found',
             'SIMPLE_EXPRESSION_2   ⟶   not found', 'EXPRESSION_2   ⟶   not found', "Match : ';'",
             "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['DECLARATION']",
             'DECLARATION   ⟶   [\'PRIMITIVE_TYPE\', "\'id\'", "\';\'"]', 'PRIMITIVE_TYPE   ⟶   ["\'int\'"]',
             "Match : 'int'", "Match : 'id'", "Match : ';'", "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']",
             "STATEMENT   ⟶   ['ASSIGNMENT']", 'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]',
             "Match : 'id'", "Match : 'assign'", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']",
             "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']",
             'FACTOR   ⟶   ["\'id\'"]', "Match : 'id'", 'TERM_2   ⟶   not found',
             'SIMPLE_EXPRESSION_2   ⟶   ["\'addop\'", \'TERM\', \'SIMPLE_EXPRESSION_2\']', "Match : 'addop'",
             "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'id\'"]', "Match : 'id'",
             'TERM_2   ⟶   ["\'mulop\'", \'FACTOR\', \'TERM_2\']', "Match : 'mulop'", 'FACTOR   ⟶   ["\'num\'"]',
             "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found',
             'EXPRESSION_2   ⟶   not found', "Match : ';'", 'STATEMENT_LIST_2   ⟶   not found', 'Match : $', 'Success']

    act = modify_actions(actions)
    act = post_modify_actions(act)
    act = post_modify_actions_2(act)

    root = Node("METHOD_BODY", None)
    root.build_tree(act)
    actual_value = root.children[0].children[1].children[0].children[0].children[2].children[0].children[0].children[0].children[0].name
    correct_value = '"num"'
    root.show_tree_2()
    assert_it(correct_value, actual_value, case )



def test_simplify_tree():

    case = 'test simplify tree [case 1]'
    actions = [
     "METHOD_BODY   ⟶   ['STATEMENT_LIST']", "STATEMENT_LIST   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']",
     "STATEMENT   ⟶   ['DECLARATION']", 'DECLARATION   ⟶   [\'PRIMITIVE_TYPE\', "\'id\'", "\';\'"]',
     'PRIMITIVE_TYPE   ⟶   ["\'int\'"]', "Match : 'int'", "Match : 'id'", "Match : ';'",
     "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['ASSIGNMENT']",
     'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]', "Match : 'id'",
      "Match : 'assign'", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']",
      "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']",
      "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'id\'"]', "Match : 'id'",
      'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   ["\'addop\'", \'TERM\', \'SIMPLE_EXPRESSION_2\']',
      "Match : 'addop'", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'id\'"]',
      "Match : 'id'", 'TERM_2   ⟶   ["\'mulop\'", \'FACTOR\', \'TERM_2\']', "Match : 'mulop'",
      'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found',
      'EXPRESSION_2   ⟶   not found', "Match : ';'", 'STATEMENT_LIST_2   ⟶   not found', 'Match : $',
      'Success']

    act = modify_actions(actions)
    act = post_modify_actions(act)
    act = post_modify_actions_2(act)

    root = Node("METHOD_BODY", None)
    root.build_tree(act)
    root.show_tree_2()
    root.simplify_it(['𝛆', "\";\""])
    #root.simplify_tree()
    root.show_tree_2()

    for leaf in root.leaves:
        print(leaf.name,end="\t")


    actual_value = None
    correct_value = []
    assert_it(correct_value, actual_value, case )

def test_add_lexemes():

    case = 'test add lexemes[case 1]'
    actions = ["METHOD_BODY   ⟶   ['STATEMENT_LIST']", "STATEMENT_LIST   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']",
             "STATEMENT   ⟶   ['DECLARATION']", 'DECLARATION   ⟶   [\'PRIMITIVE_TYPE\', "\'id\'", "\';\'"]',
             'PRIMITIVE_TYPE   ⟶   ["\'int\'"]', "Match : 'int'", "Match : 'id'", "Match : ';'",
             "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['ASSIGNMENT']",
             'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]', "Match : 'id'", "Match : 'assign'",
             "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']",
             "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found',
             'SIMPLE_EXPRESSION_2   ⟶   not found', 'EXPRESSION_2   ⟶   not found', "Match : ';'",
             "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['DECLARATION']",
             'DECLARATION   ⟶   [\'PRIMITIVE_TYPE\', "\'id\'", "\';\'"]', 'PRIMITIVE_TYPE   ⟶   ["\'int\'"]',
             "Match : 'int'", "Match : 'id'", "Match : ';'", "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']",
             "STATEMENT   ⟶   ['ASSIGNMENT']", 'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]',
             "Match : 'id'", "Match : 'assign'", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']",
             "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']",
             'FACTOR   ⟶   ["\'id\'"]', "Match : 'id'", 'TERM_2   ⟶   not found',
             'SIMPLE_EXPRESSION_2   ⟶   ["\'addop\'", \'TERM\', \'SIMPLE_EXPRESSION_2\']', "Match : 'addop'",
             "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'id\'"]', "Match : 'id'",
             'TERM_2   ⟶   ["\'mulop\'", \'FACTOR\', \'TERM_2\']', "Match : 'mulop'", 'FACTOR   ⟶   ["\'num\'"]',
             "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found',
             'EXPRESSION_2   ⟶   not found', "Match : ';'", 'STATEMENT_LIST_2   ⟶   not found', 'Match : $', 'Success']

    act = modify_actions(actions)
    act = post_modify_actions(act)
    act = post_modify_actions_2(act)

    root = Node("METHOD_BODY", None)
    root.build_tree(act)
    root.show_tree_2()
    root.simplify_it(['𝛆'])
    root.show_tree_2()
    root.add_lexemes(["int","y",";","y","=","5",";","int", "x", ";", "x","=","y","+","y","*","5",";"])
    #print(root.leaves)
    for i in root.leaves:
        print(i.name, i.lexeme)

    #root.simplify_tree()
    #root.show_tree_2()




def test_semantic():
    case = 'test semantic [case 1]'
    actions = ["METHOD_BODY   ⟶   ['STATEMENT_LIST']", "STATEMENT_LIST   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']",
             "STATEMENT   ⟶   ['DECLARATION']", 'DECLARATION   ⟶   [\'PRIMITIVE_TYPE\', "\'id\'", "\';\'"]',
             'PRIMITIVE_TYPE   ⟶   ["\'int\'"]', "Match : 'int'", "Match : 'id'", "Match : ';'",
             "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['ASSIGNMENT']",
             'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]', "Match : 'id'", "Match : 'assign'",
             "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']",
             "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found',
             'SIMPLE_EXPRESSION_2   ⟶   not found', 'EXPRESSION_2   ⟶   not found', "Match : ';'",
             "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['DECLARATION']",
             'DECLARATION   ⟶   [\'PRIMITIVE_TYPE\', "\'id\'", "\';\'"]', 'PRIMITIVE_TYPE   ⟶   ["\'int\'"]',
             "Match : 'int'", "Match : 'id'", "Match : ';'", "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']",
             "STATEMENT   ⟶   ['ASSIGNMENT']", 'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]',
             "Match : 'id'", "Match : 'assign'", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']",
             "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']",
             'FACTOR   ⟶   ["\'id\'"]', "Match : 'id'", 'TERM_2   ⟶   not found',
             'SIMPLE_EXPRESSION_2   ⟶   ["\'addop\'", \'TERM\', \'SIMPLE_EXPRESSION_2\']', "Match : 'addop'",
             "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'id\'"]', "Match : 'id'",
             'TERM_2   ⟶   ["\'mulop\'", \'FACTOR\', \'TERM_2\']', "Match : 'mulop'", 'FACTOR   ⟶   ["\'num\'"]',
             "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found',
             'EXPRESSION_2   ⟶   not found', "Match : ';'", 'STATEMENT_LIST_2   ⟶   not found', 'Match : $', 'Success']

    act = modify_actions(actions)
    act = post_modify_actions(act)
    act = post_modify_actions_2(act)

    root = Node("METHOD_BODY", None)
    root.build_tree(act)
    #root.show_tree_2()
    root.simplify_it(['𝛆','";"'])
    root.add_lexemes(["int","y",";","y","=","5",";","int", "x", ";", "x","=","y","+","y","*","5",";"])

    #reduce_tree(root)
    
    root.eliminate_exp({'"addop"', '"mulop"','"relop"', '"assign"'})
    root.show_tree_2()
    #reduce_tree(root)
    root.update_leaves()
    #get_str_val(root)


    root.add_lexemes(["int","y","y","5","int", "x", "x","y","y","7"])
    root.show_tree_2()
    
    
    symtab = SymTable()
    #root.semantic_analysis(symtab)
    #print(symtab.table)
    #print(symtab.coolTable)

    get_val_2(root,symtab)

    root.show_tree_2()


    print(len(root.leaves))

    for i in root.leaves:
        print(i.name,end="\t")

    actual_value = None
    correct_value = None
    assert_it(correct_value, actual_value, case )

    

def test_lexeme():
    case = 'test semantic [case 1]'
    # parse table from phase 2
    actions = ["METHOD_BODY   ⟶   ['STATEMENT_LIST']", "STATEMENT_LIST   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']",
             "STATEMENT   ⟶   ['DECLARATION']", 'DECLARATION   ⟶   [\'PRIMITIVE_TYPE\', "\'id\'", "\';\'"]',
             'PRIMITIVE_TYPE   ⟶   ["\'int\'"]', "Match : 'int'", "Match : 'id'", "Match : ';'",
             "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['ASSIGNMENT']",
             'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]', "Match : 'id'", "Match : 'assign'",
             "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']",
             "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found',
             'SIMPLE_EXPRESSION_2   ⟶   not found', 'EXPRESSION_2   ⟶   not found', "Match : ';'",
             "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['DECLARATION']",
             'DECLARATION   ⟶   [\'PRIMITIVE_TYPE\', "\'id\'", "\';\'"]', 'PRIMITIVE_TYPE   ⟶   ["\'int\'"]',
             "Match : 'int'", "Match : 'id'", "Match : ';'", "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']",
             "STATEMENT   ⟶   ['ASSIGNMENT']", 'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]',
             "Match : 'id'", "Match : 'assign'", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']",
             "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']",
             'FACTOR   ⟶   ["\'id\'"]', "Match : 'id'", 'TERM_2   ⟶   not found',
             'SIMPLE_EXPRESSION_2   ⟶   ["\'addop\'", \'TERM\', \'SIMPLE_EXPRESSION_2\']', "Match : 'addop'",
             "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'id\'"]', "Match : 'id'",
             'TERM_2   ⟶   ["\'mulop\'", \'FACTOR\', \'TERM_2\']', "Match : 'mulop'", 'FACTOR   ⟶   ["\'num\'"]',
             "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found',
             'EXPRESSION_2   ⟶   not found', "Match : ';'", 'STATEMENT_LIST_2   ⟶   not found', 'Match : $', 'Success']

    # modify the parsing table to adapt with this phase
    act = modify_actions(actions)
    act = post_modify_actions(act)
    act = post_modify_actions_2(act)

    root = Node("METHOD_BODY", None)
    root.build_tree(act)

    # remove epsillon nodes
    root.simplify_it(['𝛆'])
    root.add_lexemes(["int","y",";","y","=","5",";","int", "x", ";", "x","=","y","+","y","*","5",";"])
    root.simplify_it(['";"'])
    root.eliminate_exp({'"addop"', '"mulop"', '"assign"'})
    reduce_tree(root)

    symtab = SymTable()
    get_val_2(root,symtab)
    
    root.show_tree_2()

    print_yellow(symtab.coolTable)

def test_full_input():
    case = 'test full input [case 1]'

    actions = ["METHOD_BODY   ⟶   ['STATEMENT_LIST']", "STATEMENT_LIST   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']",
    "STATEMENT   ⟶   ['DECLARATION']", 'DECLARATION   ⟶   [\'PRIMITIVE_TYPE\', "\'id\'", "\';\'"]',
    'PRIMITIVE_TYPE   ⟶   ["\'int\'"]', "Match : 'int'", "Match : 'id'", "Match : ';'",
    "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['ASSIGNMENT']",
    'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]', "Match : 'id'", "Match : 'assign'",
    "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']",
    "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found',
    'SIMPLE_EXPRESSION_2   ⟶   not found', 'EXPRESSION_2   ⟶   not found', "Match : ';'",
    "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']",
    "STATEMENT   ⟶   ['DECLARATION']", 'DECLARATION   ⟶   [\'PRIMITIVE_TYPE\', "\'id\'", "\';\'"]',
    'PRIMITIVE_TYPE   ⟶   ["\'float\'"]', "Match : 'float'", "Match : 'id'", "Match : ';'",
    "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['ASSIGNMENT']",
    'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]', "Match : 'id'", "Match : 'assign'",
    "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']",
    "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'id\'"]', "Match : 'id'", 'TERM_2   ⟶   not found',
    'SIMPLE_EXPRESSION_2   ⟶   ["\'addop\'", \'TERM\', \'SIMPLE_EXPRESSION_2\']', "Match : 'addop'",
    "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'id\'"]', "Match : 'id'",
    'TERM_2   ⟶   ["\'mulop\'", \'FACTOR\', \'TERM_2\']', "Match : 'mulop'", 'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'",
    'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found', 'EXPRESSION_2   ⟶   not found', "Match : ';'",
    "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['IF']",
    'IF   ⟶   ["\'if\'", "\'(\'", \'EXPRESSION\', "\')\'", "\'{\'", \'STATEMENT\', "\'}\'", "\'else\'", "\'{\'", \'STATEMENT\', "\'}\'"]',
    "Match : 'if'", "Match : '('", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']",
    "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']",
    'FACTOR   ⟶   ["\'id\'"]', "Match : 'id'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found',
    'EXPRESSION_2   ⟶   ["\'relop\'", \'SIMPLE_EXPRESSION\']', "Match : 'relop'",
    "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'num\'"]',
    "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found', "Match : ')'", "Match : '{'",
    "STATEMENT   ⟶   ['ASSIGNMENT']", 'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]', "Match : 'id'",
    "Match : 'assign'", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']",
    "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']",
    'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found',
    'EXPRESSION_2   ⟶   not found', "Match : ';'", "Match : '}'", "Match : 'else'", "Match : '{'",
    "STATEMENT   ⟶   ['ASSIGNMENT']", 'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]', "Match : 'id'",
    "Match : 'assign'", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']",
    "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']",
    'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found',
    'EXPRESSION_2   ⟶   not found', "Match : ';'", "Match : '}'", "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']",
    "STATEMENT   ⟶   ['WHILE']",
    'WHILE   ⟶   ["\'while\'", "\'(\'", \'EXPRESSION\', "\')\'", "\'{\'", \'STATEMENT\', "\'}\'"]', "Match : 'while'",
    "Match : '('", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']",
    "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'id\'"]',
    "Match : 'id'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found',
    'EXPRESSION_2   ⟶   ["\'relop\'", \'SIMPLE_EXPRESSION\']', "Match : 'relop'",
    "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']",
    'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found',
    "Match : ')'", "Match : '{'", "STATEMENT   ⟶   ['ASSIGNMENT']",
    'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]', "Match : 'id'", "Match : 'assign'",
    "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']",
    "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'id\'"]', "Match : 'id'", 'TERM_2   ⟶   not found',
    'SIMPLE_EXPRESSION_2   ⟶   ["\'addop\'", \'TERM\', \'SIMPLE_EXPRESSION_2\']', "Match : 'addop'",
    "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found',
    'SIMPLE_EXPRESSION_2   ⟶   not found', 'EXPRESSION_2   ⟶   not found', "Match : ';'", "Match : '}'",
    'STATEMENT_LIST_2   ⟶   not found', 'Match : $', 'Success']

    # modify the parsing table to adapt with this phase
    act = modify_actions(actions)
    act = post_modify_actions(act)
    act = post_modify_actions_2(act)

    root = Node("METHOD_BODY", None)
    root.build_tree(act)

    # remove epsillon nodes
    root.simplify_it(['𝛆'])
    lex = ['int','y',';','y','=','5',';','float','x', ';', 'x', '=', 'y', '+', 'y','*', '2.5', ';',
            'if','(','x','<','3',')','{','y','=','7',';','}','else','{','y','=','3',';','}',
            'while','(','y','<','5',')','{','y','=','y','+','1',';','}'
    ]
    print(f"len(lex)= {len(lex)}")
    
    root.add_lexemes(lex)
    # mind that additional "" is added
    root.simplify_it(['";"', '"{"','"}"', '"("', '")"','"if"','"else"','"while"'])

    root.update_leaves()
    for i in root.leaves:
        print_green(f"leaf update: {i.name}")

    root.eliminate_exp({'"addop"', '"mulop"', '"relop"', '"assign"'})
    reduce_tree(root)

    symtab = SymTable()
    get_val_2(root,symtab)
    root.show_tree_2()
    
    get_val_virtual(root,symtab)
    root.show_tree_2()
    print_yellow(symtab.coolTable)

    actual_value = None
    correct_value = None

    assert_it(correct_value, actual_value, case)

    case = 'test generating code [case 1]'
    generate_code(root, symtab)
    root.show_tree_2(1)

    assert_it(correct_value, actual_value, case)

    case = 'test generating code [case 2]'
    actions = ["METHOD_BODY   ⟶   ['STATEMENT_LIST']", "STATEMENT_LIST   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['DECLARATION']", 'DECLARATION   ⟶   [\'PRIMITIVE_TYPE\', "\'id\'", "\';\'"]', 'PRIMITIVE_TYPE   ⟶   ["\'int\'"]', "Match : 'int'", "Match : 'id'", "Match : ';'", "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['ASSIGNMENT']", 'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]', "Match : 'id'", "Match : 'assign'", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found', 'EXPRESSION_2   ⟶   not found', "Match : ';'", "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['DECLARATION']", 'DECLARATION   ⟶   [\'PRIMITIVE_TYPE\', "\'id\'", "\';\'"]', 'PRIMITIVE_TYPE   ⟶   ["\'int\'"]', "Match : 'int'", "Match : 'id'", "Match : ';'", "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['ASSIGNMENT']", 'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]', "Match : 'id'", "Match : 'assign'", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found', 'EXPRESSION_2   ⟶   not found', "Match : ';'", "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['DECLARATION']", 'DECLARATION   ⟶   [\'PRIMITIVE_TYPE\', "\'id\'", "\';\'"]', 'PRIMITIVE_TYPE   ⟶   ["\'int\'"]', "Match : 'int'", "Match : 'id'", "Match : ';'", "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['ASSIGNMENT']", 'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]', "Match : 'id'", "Match : 'assign'", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found', 'EXPRESSION_2   ⟶   not found', "Match : ';'", "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['ASSIGNMENT']", 'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]', "Match : 'id'", "Match : 'assign'", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'id\'"]', "Match : 'id'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   ["\'addop\'", \'TERM\', \'SIMPLE_EXPRESSION_2\']', "Match : 'addop'", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'id\'"]', "Match : 'id'", 'TERM_2   ⟶   ["\'mulop\'", \'FACTOR\', \'TERM_2\']', "Match : 'mulop'", 'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found', 'EXPRESSION_2   ⟶   not found', "Match : ';'", "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['IF']", 'IF   ⟶   ["\'if\'", "\'(\'", \'EXPRESSION\', "\')\'", "\'{\'", \'STATEMENT\', "\'}\'", "\'else\'", "\'{\'", \'STATEMENT\', "\'}\'"]', "Match : 'if'", "Match : '('", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'id\'"]', "Match : 'id'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found', 'EXPRESSION_2   ⟶   ["\'relop\'", \'SIMPLE_EXPRESSION\']', "Match : 'relop'", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found', "Match : ')'", "Match : '{'", "STATEMENT   ⟶   ['ASSIGNMENT']", 'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]', "Match : 'id'", "Match : 'assign'", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found', 'EXPRESSION_2   ⟶   not found', "Match : ';'", "Match : '}'", "Match : 'else'", "Match : '{'", "STATEMENT   ⟶   ['ASSIGNMENT']", 'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]', "Match : 'id'", "Match : 'assign'", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found', 'EXPRESSION_2   ⟶   not found', "Match : ';'", "Match : '}'", "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['WHILE']", 'WHILE   ⟶   ["\'while\'", "\'(\'", \'EXPRESSION\', "\')\'", "\'{\'", \'STATEMENT\', "\'}\'"]', "Match : 'while'", "Match : '('", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'id\'"]', "Match : 'id'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found', 'EXPRESSION_2   ⟶   ["\'relop\'", \'SIMPLE_EXPRESSION\']', "Match : 'relop'", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found', "Match : ')'", "Match : '{'", "STATEMENT   ⟶   ['ASSIGNMENT']", 'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]', "Match : 'id'", "Match : 'assign'", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'id\'"]', "Match : 'id'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   ["\'addop\'", \'TERM\', \'SIMPLE_EXPRESSION_2\']', "Match : 'addop'", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found', 'EXPRESSION_2   ⟶   not found', "Match : ';'", "Match : '}'", 'STATEMENT_LIST_2   ⟶   not found', 'Match : $', 'Success']
     # modify the parsing table to adapt with this phase
    act = modify_actions(actions)
    act = post_modify_actions(act)
    act = post_modify_actions_2(act)

    root = Node("METHOD_BODY", None)
    root.build_tree(act)


    # remove epsillon nodes
    root.simplify_it(['𝛆'])
    lex = ['int','x',';','x','=','3',';','int','y', ';', 'y', '=', '4',';','int','z', ';', 'z', '=', '5',';',
     'z', '=','x', '+', 'y', '*', '2', ';',
    'if','(','z','==','11',')','{','x','=','2',';','}','else','{','y','=','7',';','}',
            'while','(','y','<','10',')','{','y','=','y','+','2',';','}']
    
    root.add_lexemes(lex)
    # mind that additional "" is added
    root.simplify_it(['";"', '"{"','"}"', '"("', '")"','"if"','"else"','"while"'])

    root.update_leaves()
    for i in root.leaves:
        print_green(f"leaf update: {i.name}")

    root.eliminate_exp({'"addop"', '"mulop"', '"relop"', '"assign"'})
    reduce_tree(root)

    symtab = SymTable()
    get_val_2(root,symtab)
    root.show_tree_2()
    
    get_val_virtual(root,symtab)
    
    generate_code(root, symtab)
    #root.show_tree_2(1)
    code = root.code
    code = root.get_code()

    print_blue("code is")
    print_yellow(code)

    code_list = code.split('\n')
    print_green(code_list)

    root.backpatch()
    print_purple(root.jasmin_in("coode"))

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
        #test_modify_actions()
        print_blue('*.*.'*15)
        #test_node_tree()
        print_blue('*.*.'*15)
        #test_simplify_tree()
        print_blue('*.*.'*15)
        #test_add_lexemes()
        print_blue('*.*.'*15)
        #test_semantic()
        #print_blue('*.*.'*15)
        #test_lexeme()
        print_blue('*.*.'*15)
        test_full_input()


        

    except AssertionError as e:
        print("Test case failed:\n", str(e))
        exit(-1)


if __name__ == "__main__":
    main()
