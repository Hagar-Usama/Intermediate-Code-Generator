from color_print import print_blue, print_green, print_purple, print_red, print_yellow, ANSI_RED, ANSI_RESET
from semantic import modify_actions, post_modify_actions, post_modify_actions_2
from node import Node, SymTable, Symbol, reduce_tree, get_str_val, get_val_2, get_val_virtual
from node import generate_code
from aux_func import get_current_directory, read_file_list, write_in_file


def main():
    
    cd = get_current_directory()

    ## actions from phase 2
    """ 
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

    # the root of the tree
    root = Node("METHOD_BODY", None)
    root.build_tree(act)

    # remove epsillon nodes
    root.simplify_it(['𝛆'])

    # get the input_list
    lex = ['int','y',';','y','=','5',';','float','x', ';', 'x', '=', 'y', '+', 'y','*', '2.5', ';',
            'if','(','x','<','3',')','{','y','=','7',';','}','else','{','y','=','3',';','}',
            'while','(','y','<','5',')','{','y','=','y','+','1',';','}'
    ]
    
    #print(f"len(lex)= {len(lex)}")
    
    ## add lexemes to the tree
    root.add_lexemes(lex)

    # mind that additional "" is added
    ## simplify tree >> APT
    root.simplify_it(['";"', '"{"','"}"', '"("', '")"','"if"','"else"','"while"'])

    root.update_leaves()

    #for i in root.leaves:
    #    print_green(f"leaf update: {i.name}")

    ## build the AST
    root.eliminate_exp({'"addop"', '"mulop"', '"relop"', '"assign"'})
    reduce_tree(root)

    ## build symbol table
    symtab = SymTable()
    ## eval values for each node
    get_val_2(root,symtab)
    
    #root.show_tree_2()
    
    ## eval values for conditional nodes
    get_val_virtual(root,symtab)

    #root.show_tree_2()
    #print_yellow(symtab.coolTable)

    #actual_value = None
    #correct_value = None

    #assert_it(correct_value, actual_value, case)

    case = 'test generating code [case 1]'
    ## generate the byte code
    generate_code(root, symtab)
    #root.show_tree_2(1)

    #assert_it(correct_value, actual_value, case)

    """
    
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
    
    #for i in root.leaves:
    #    print_green(f"leaf update: {i.name}")

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

    #print_blue("code is")
    #print_yellow(code)

    code_list = code.split('\n')
    print_green(code_list)

    root.backpatch()
    #print_purple(root.jasmin_in("coode"))

    code_path = cd + '/' + 'code.j'
    write_in_file(code_path, root.jasmin_in("code"))






if __name__ == "__main__":
    main()
