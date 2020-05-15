

todos = [['$', 'E'], ['$', 'R', 'T'], ['$', 'R', 'S', 'F'], ['$', 'R', 'S', 'n'], ['$', 'R', 'S'], ['$', 'R', '𝛆'], ['$', 'R'], ['$', 'E', '+'], ['$', 'E'], ['$', 'R', 'T'], ['$', 'R', 'S', 'F'], ['$', 'R', 'S', 'n'], ['$', 'R', 'S'], ['$', 'R', 'T', '*'], ['$', 'R', 'T'], ['$', 'R', 'S', 'F'], ['$', 'R', 'S', 'n'], ['$', 'R', 'S'], ['$', 'R', '𝛆'], ['$', 'R'], ['$', '𝛆'], ['$'], []]
inputs = ['n', 'n', 'n', '+', '+', '+', '+', 'n', 'n', 'n', 'n', '*', '*', 'n', 'n', 'n', '$', '$', '$', '$', '$', '$', ' ']
action = ["E   ⟶   ['T', 'R']", "T   ⟶   ['F', 'S']", "F   ⟶   ['n']", 'Match : n', "S   ⟶   ['𝛆']", 'Consume 𝛆', "R   ⟶   ['+', 'E']", 'Match : +', "E   ⟶   ['T', 'R']", "T   ⟶   ['F', 'S']", "F   ⟶   ['n']", 'Match : n', "S   ⟶   ['*', 'T']", 'Match : *', "T   ⟶   ['F', 'S']", "F   ⟶   ['n']", 'Match : n', "S   ⟶   ['𝛆']", 'Consume 𝛆', "R   ⟶   ['𝛆']", 'Consume 𝛆', 'Match : $', 'Success']

print(len(todos))
print(len(action))

print(action[0].split("⟶"))

x = action[0].split("⟶")
for i in x:
    i.strip()
    print(i)

print(x)


["METHOD_BODY   ⟶   ['STATEMENT_LIST']", "STATEMENT_LIST   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['DECLARATION']", 'DECLARATION   ⟶   [\'PRIMITIVE_TYPE\', "\'id\'", "\';\'"]', 'PRIMITIVE_TYPE   ⟶   ["\'int\'"]', "Match : 'int'", "Match : 'id'", "Match : ';'", "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['ASSIGNMENT']", 'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]', "Match : 'id'", "Match : 'assign'", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found', 'EXPRESSION_2   ⟶   not found', "Match : ';'", "STATEMENT_LIST_2   ⟶   ['STATEMENT', 'STATEMENT_LIST_2']", "STATEMENT   ⟶   ['IF']", 'IF   ⟶   ["\'if\'", "\'(\'", \'EXPRESSION\', "\')\'", "\'{\'", \'STATEMENT\', "\'}\'", "\'else\'", "\'{\'", \'STATEMENT\', "\'}\'"]', "Match : 'if'", "Match : '('", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'id\'"]', "Match : 'id'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found', 'EXPRESSION_2   ⟶   ["\'relop\'", \'SIMPLE_EXPRESSION\']', "Match : 'relop'", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found', "Match : ')'", "Match : '{'", "STATEMENT   ⟶   ['ASSIGNMENT']", 'ASSIGNMENT   ⟶   ["\'id\'", "\'assign\'", \'EXPRESSION\', "\';\'"]', "Match : 'id'", "Match : 'assign'", "EXPRESSION   ⟶   ['SIMPLE_EXPRESSION', 'EXPRESSION_2']", "SIMPLE_EXPRESSION   ⟶   ['TERM', 'SIMPLE_EXPRESSION_2']", "TERM   ⟶   ['FACTOR', 'TERM_2']", 'FACTOR   ⟶   ["\'num\'"]', "Match : 'num'", 'TERM_2   ⟶   not found', 'SIMPLE_EXPRESSION_2   ⟶   not found', 'EXPRESSION_2   ⟶   not found', 'Consume 𝛆', "Match : '}'", 'Consume 𝛆', 'Consume 𝛆', 'STATEMENT   ⟶   not found', 'Consume 𝛆', 'STATEMENT_LIST_2   ⟶   not found', 'Match : $', 'Success']