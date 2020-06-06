from modules.color_print import print_blue, print_green, print_purple, print_red, print_dark_cyan
from modules.color_print import  print_yellow, ANSI_RED, ANSI_RESET
from modules.semantic import modify_actions, post_modify_actions, post_modify_actions_2
from modules.Symbol import SymTable, Symbol
from modules.Node import Node, reduce_tree, get_str_val, get_val_2, get_val_virtual
from modules.Node import generate_code
from modules.aux_func import get_current_directory, read_file_list, write_in_file, get_arg



def main():

    ## set default file for args
    actions_file = get_arg(1, "actions.txt")
    lexemes_file = get_arg(2, "lexemes.txt")

    
    cd = get_current_directory()
    # actions = ["METHOD_BODY   ⟶   ['STATEMENT_LIST']", "STATEMENT_LIST   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['DECLARATION']", 'DECLARATION   ⟶   [\'PRIMITIVE_TYPE\', "\'id\'", "\';\'"]', 'PRIMITIVE_TYPE   ⟶   ["\'int\'"]', "Match : 'int'", "Match : 'id'", "Match : ';'", "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['ASSIGNMENT']", 'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]', "Match : 'id'", "Match : 'assign'", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found', 'EXPRESSION_2   ⟶   not found', "Match : ';'", "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['DECLARATION']", 'DECLARATION   ⟶   [\'PRIMITIVE_TYPE\', "\'id\'", "\';\'"]', 'PRIMITIVE_TYPE   ⟶   ["\'int\'"]', "Match : 'int'", "Match : 'id'", "Match : ';'", "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['ASSIGNMENT']", 'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]', "Match : 'id'", "Match : 'assign'", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found', 'EXPRESSION_2   ⟶   not found', "Match : ';'", "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['DECLARATION']", 'DECLARATION   ⟶   [\'PRIMITIVE_TYPE\', "\'id\'", "\';\'"]', 'PRIMITIVE_TYPE   ⟶   ["\'int\'"]', "Match : 'int'", "Match : 'id'", "Match : ';'", "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['ASSIGNMENT']", 'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]', "Match : 'id'", "Match : 'assign'", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found', 'EXPRESSION_2   ⟶   not found', "Match : ';'", "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['ASSIGNMENT']", 'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]', "Match : 'id'", "Match : 'assign'", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'id\'"]', "Match : 'id'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   ["\'addop\'", \'TERM\', \'SIMPLE_EXPRESSION_2\']', "Match : 'addop'", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'id\'"]', "Match : 'id'", 'TERM_2   ⟶   ["\'mulop\'", \'FACTOR\', \'TERM_2\']', "Match : 'mulop'", 'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found', 'EXPRESSION_2   ⟶   not found', "Match : ';'", "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['IF']", 'IF   ⟶   ["\'if\'", "\'(\'", \'EXPRESSION\', "\')\'", "\'{\'", \'STATEMENT\', "\'}\'", "\'else\'", "\'{\'", \'STATEMENT\', "\'}\'"]', "Match : 'if'", "Match : '('", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'id\'"]', "Match : 'id'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found', 'EXPRESSION_2   ⟶   ["\'relop\'", \'SIMPLE_EXPRESSION\']', "Match : 'relop'", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found', "Match : ')'", "Match : '{'", "STATEMENT   ⟶   ['ASSIGNMENT']", 'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]', "Match : 'id'", "Match : 'assign'", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found', 'EXPRESSION_2   ⟶   not found', "Match : ';'", "Match : '}'", "Match : 'else'", "Match : '{'", "STATEMENT   ⟶   ['ASSIGNMENT']", 'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]', "Match : 'id'", "Match : 'assign'", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found', 'EXPRESSION_2   ⟶   not found', "Match : ';'", "Match : '}'", "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['WHILE']", 'WHILE   ⟶   ["\'while\'", "\'(\'", \'EXPRESSION\', "\')\'", "\'{\'", \'STATEMENT\', "\'}\'"]', "Match : 'while'", "Match : '('", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'id\'"]', "Match : 'id'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found', 'EXPRESSION_2   ⟶   ["\'relop\'", \'SIMPLE_EXPRESSION\']', "Match : 'relop'", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found', "Match : ')'", "Match : '{'", "STATEMENT   ⟶   ['ASSIGNMENT']", 'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]', "Match : 'id'", "Match : 'assign'", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'id\'"]', "Match : 'id'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   ["\'addop\'", \'TERM\', \'SIMPLE_EXPRESSION_2\']', "Match : 'addop'", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found', 'EXPRESSION_2   ⟶   not found', "Match : ';'", "Match : '}'", 'STATEMENT_LIST_2   ⟶   not found', 'Match : $', 'Success']
    
    action_path = cd + '/' + actions_file

    actions = read_file_list(action_path)

    ## modify the parsing table to adapt with this phase
    act = modify_actions(actions)
    act = post_modify_actions(act)
    act = post_modify_actions_2(act)

    
    ## make sure the actions list is not empty
    root_name = act[0][0][0]

    ## assign the root node
    root = Node(root_name, None)
    root.build_tree(act)


    ## remove epsillon nodes
    root.simplify_it(['𝛆'])

    lex_path = cd + '/' + lexemes_file
    lex = read_file_list(lex_path)
    
    ## add lexemes to the tree
    root.add_lexemes(lex)

    ## mind that additional "" is added
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
    
    ## generate the byte code
    generate_code(root, symtab)
    #root.show_tree_2(1)
    code = root.code
    code = root.get_code()

    #print_blue("code is")
    #print_yellow(code)

    code_list = code.split('\n')
    #print_green(code_list)
    #for i in code_list:
    #    print_green(i)

    root.backpatch()
    #print_purple(root.jasmin_in("coode"))
    

    code_list = root.get_code()
    print_green(code_list)

    print_yellow(symtab.coolTable)

    # output j file for jasmin
    code_path = cd + '/' + 'code.j'
    write_in_file(code_path, root.jasmin_in("code"))






if __name__ == "__main__":
    main()
