import itertools
import time
# test cases
# https://www.gatevidyalay.com/first-and-follow-compiler-design/
ANSI_RESET = "\u001B[0m"
ANSI_RED = "\u001B[31m"
ANSI_GREEN = "\u001B[32m"
ANSI_YELLOW = "\u001B[33m"
ANSI_BLUE = "\u001B[34m"
ANSI_PURPLE = "\u001B[35m"
ANSI_ORANGE_BG = "\033[48;2;255;165;0m"
ANSI_DARK_CYAN = "\033[96m"

'''
sync is reserved now

'''

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


gram = {


    'A' : [['B','X','b','c'] , ['d','e','f'] , ['g','h','i'] , ['𝛆']],
    'X' : [['q']],
    'B' : ['s','𝛆']
}

gram2 = {
    'S': [['A','B','C','D']],
    'A': [['a'], ['𝛆']],
    'B': [['C','D'], ['b']],
    'C': [['c'],['𝛆']],
    'D': [['A','a'], ['d'],['𝛆']]

}

pr1 = {
    'S': [['A']],
    'A': [['a','B',"A'"]],
    "A'": [['d',"A'"],['𝛆']],
    'B': [['b']],
    "A'": [['d',"A'"],['𝛆']],
    'C': [['g']]

}

pr3 = {
    'S': [['(','L',')'],['a']],
    'L': [['S',"L'"]],
    "L'": [[',','S'],['𝛆']],
}
non_terminal_list = ['A','X','B']
non_terminal_list2 = ['S','A','B','C','D']
termial_pr1 = ["S", "A" , "A'", "B", "C"]
termial_pr3 = ["S", "L", "L'"]

G_follow = {}

def get_terminal_list(grammar , option=0):
    nt = get_non_terminal_list(grammar)
    #nt_list = list(nt)
    ternmial_list = set()

    for p in grammar:
        for i in grammar[p]:
            for t in i:
                if t not in nt:
                    ternmial_list.add(t)

    # ternmial_list.update(ternmial_list.difference(nt))
    
    if has_epsilon(ternmial_list):
        ternmial_list.remove('𝛆')

    #print_red(ternmial_list)
    if option:
        ternmial_list.add('$')

    #print_yellow(ternmial_list)
    #print_blue(nt)
    return ternmial_list


def get_non_terminal_list(grammar):
    non_terminal_list = set()

    for nt in grammar:
        non_terminal_list.add(nt)
        
   
    #print_blue(non_terminal_list)
    return non_terminal_list
    
def hash_it(keys):
    keys = list(keys)
    index_list = [*range(0, len(keys), 1)] 
    dictionary = dict(zip(keys,index_list))
    #print_dark_cyan(dictionary)
    return dictionary

def initialize_parsing_tree(non_terminal_list, terminal_list):

    #row_dict = hash_it(non_terminal_list)
    #col_dict = hash_it(terminal_list)

    #row = ['sync'] * len(non_terminal_list)
    col = ['sync'] * len(terminal_list)

    parsing_table = []

    for i in non_terminal_list:
        parsing_table.append(col)

    #print(row)
    #print(col)
    #print_purple(parsing_table)
    return parsing_table
    
   
   
def is_non_terminal(A, non_terminal_list):
    if A in non_terminal_list:
        return True
    return False

def has_epsilon(my_list):
    if '𝛆' in my_list:
        return True
    return False

def get_first(grammar, non_terminal, non_terminal_list):
    first_i = set()

    # scanning each list in non_terminal
    for j in grammar[non_terminal]:
        #print(f'{j[0]}')
        if is_non_terminal(j[0], non_terminal_list):
            # scanning each element in list
            for element in j:
                flag = False
                if is_non_terminal(element, non_terminal_list):
                    x = get_first(grammar, element, non_terminal_list)

                    f = has_epsilon(x)

                    """
                    if has_epsilon(x):
                        x.remove('𝛆')
                        flag = True
                    else:
                        break

                    """
                    
                    if f:
                        x.remove('𝛆')
                        first_i.update(x)
                        flag = True
                    else:
                        first_i.update(x)
                        break
                    
                else:
                    if element == '𝛆':
                        flag = True 
                    else:
                        first_i.add(element)
                #print(flag)
                    #break
            if flag:
                #print('flag is true')
                first_i.add('𝛆')       
        else:
            first_i.add(j[0])
    return first_i


    

def get_first_1(grammar, non_terminal, non_terminal_list):
    '''
    https://www.gatevidyalay.com/first-and-follow-compiler-design/

    rules applied: 

        1) For a production rule X → ∈,
            First(X) = { ∈ }

        2) For any terminal symbol ‘a’,
            First(a) = { a }

        3) For a production rule X → Y1Y2Y3,
            calculate first(Y1):
                If ∈ ∉ First(Y1), then First(X) = First(Y1)
                If ∈ ∈ First(Y1), then First(X) = { First(Y1) – ∈ } ∪ First(Y2Y3)
            else repeat 3) for Y(n+1)

        assumption for recursion and factoring:
            left recursion and left factoring are eliminated

    '''
    first_i = set()

    # scanning each list in non_terminal
    for j in grammar[non_terminal]:
        ##print(j[0])

        # if terminal add it directly
        if not is_non_terminal(j[0], non_terminal_list):
            first_i.add(j[0])
            
        else:
            # if a non-terminal,walk through
            for k in j:
                if is_non_terminal(k, non_terminal_list):
                    temp = get_first(grammar, k, non_terminal_list)
                    first_i.update(temp)
                    if not has_epsilon(temp):
                        break
                else:
                    ##print(k)
                    first_i.add[k]
                    break
                    

    return first_i

def get_follows(grammar, first_set, start_symbol, non_terminal_list):
    follows = {}
    for non_terminal in non_terminal_list:
        follow = get_follow(grammar, non_terminal, first_set, start_symbol, non_terminal_list)
        follows[non_terminal] = follow

    return follows

def get_follow(grammar, non_terminal, first_set, start_symbol, non_terminal_list):
    '''
        1) for starting symbol place $ in the follow set
        2) if the is a production A → 𝞪B𝝱:
            Follow(B) = First(𝝱)
            if First(𝝱) has 𝝴 :
                Follow(B) = Follow(A)
        3) if the is a production A → 𝞪B:
            Follow(B) = Follow(A)

        find_first_sole → returns firsts and follows NT

    '''
    follow_i = set()
    if non_terminal is start_symbol:
        follow_i.add('$')
        ##print("follow first")

    # step one get the follows based on firsts
    productions = parse_production(get_rhs(grammar, non_terminal))
    print(f'productions for {non_terminal} : {productions}')

    #first_follow = find_first_sole(grammar, non_terminal, productions, non_terminal_list)
    first, follow = find_first_sole(grammar, non_terminal, productions, non_terminal_list)
    first_follow = parse_find_first(first, follow)
    ##print(f'initial follows are {first_follow[0]} : {first_follow[1]}')

    follow_i.update(first_follow[0])
    for i in first_follow[1]:
        follow_i.update(get_follow(grammar, i, first_set, start_symbol, non_terminal_list)) 
    return follow_i



def parse_production(production_list):
    new_production_list = {}
    new_list_out = []
    temp = []
    for i in production_list:
        ##print(production_list[i])
        new_list = []
        for j in production_list[i]:
            ##print(j)
            
            if not j:
                ##print("epsilon")
                temp = ['𝛆']
            else:
                temp = j
            new_list.append(temp)
        new_production_list[i] = new_list    
        #new_list_out.append(new_list)
    ##print(new_production_list)
    return new_production_list


def find_first_sole(grammar, non_terminal, non_terminal_production, non_terminal_list, epsilon=0):
    #non terminal production for one non-terminal
    first = set()
    follow_of_follow = set()
    external_list = []
    
    for i in non_terminal_production:
        count = 0
        for j in non_terminal_production[i]:
            count += 1

            ##print(f'*{j}*')
            ##print(f'len of j : {len(j)}')
            for element in j:
                internal_list = set()
                if is_non_terminal(element, non_terminal_list):
                    first_part = get_first(grammar, element, non_terminal_list)
                    ##print(f'get partial first {first_part} for {element}')
                    first.update(first_part)
                    internal_list.update(first_part)



                    # this part added for parsing table
                    if epsilon == 1:
                        if '𝛆' in first_part:
                            first.add('𝛆')

                    # if a NT has no epsilon then no need to continue
                    if '𝛆' not in first_part:
                        break
                    # if NT has epsilon and it's the last one in list
                    elif count == len(j):
                        follow_of_follow.add(i)

                else:
                    if element == '𝛆':
                        follow_of_follow.add(i)
                        # this part added for parsing table
                        if epsilon == 1:
                                first.add('𝛆')
                    else:
                        first.add(element)
                        internal_list.add(element) 

                    break
            external_list.append(internal_list)
            #print(f'internal list: {internal_list}')

        ##print("*.*"*20)
    if '𝛆' in first:
        if not epsilon:
            first.remove('𝛆')
    if '𝛆'in follow_of_follow:
        follow_of_follow.remove('𝛆')
    if non_terminal in follow_of_follow:
        # ignore it (avoid recursion)
        follow_of_follow.remove(non_terminal)

    return first, follow_of_follow
    

def parse_find_first(first_set , follow_set):
    return [first_set, follow_set]

def find_first(grammar, non_terminal_production, non_terminal_list):
    '''
    
    '''
    first_i = set()
    follow_of_follow = set()

    count = 0

    for i in non_terminal_production:
        ##print(i)
        for j in non_terminal_production[i]:
            break
            #print(j)
    
    ##print(f'terminal production = {terminal_production}')
    """ 
    for i in non_terminal_production:
        #print(f'non-terminal production part: {non_terminal_production[i]}')
        if len(non_terminal_production[i]) == 0:
            #print("just get follow")
            break

        ##print("enteur find")
        # going to each list for a 
        for j in non_terminal_production[i]:
            count += 1
            #print(f'j is : {j}')

            for k in j:
                # first of non-terminal = get_first
                #print(len(non_terminal_production[i]))
                if is_non_terminal(k, non_terminal_list):
                    #print(f"{k} is non-terminal")

                    first_ii = get_first(grammar, k, non_terminal_list)
                    #print(f'first : {first_ii}')
                    first_i.update(first_ii)
                    if '𝛆' not in first_ii:
                        #print("epsilon not found!!")
                        # if last of the list of firsts  &&  is a non-terminal
                        # add follow of j
                        break
                    
                    # if we are in the last element and this element has 𝛆
                    # then get follow of j 
                    if count == len(non_terminal_production[i]):
                        #print(f"followee = {i}")
                        follow_of_follow.add(i)

                else:
                    first_i.add(j)
    first_i.remove('𝛆')
    #print(f'i in find first = {count}') 
    """
    return first_i


def get_index(key, the_list ):

    
    index_list = []

    for i in range(0, len(the_list)):
        print(the_list[i])
        if the_list[i] == key:
            index_list.append(i)
    return index_list

def slice_list(index_list, the_list):

    slices = set()
    for i in range(0, len(index_list)-1):
        begin = index_list[i] + 1
        end = index_list[i+1] - 1
        slices.add(tuple(the_list[begin: end]))
        print(f'{the_list[begin: end]}')
    begin = index_list[i]
    last_element = the_list[begin:]
    
    
    
    return slices


def get_rhs(grammar, non_terminal):
    rhs_dict = {}
    #first = set()
   
    # for each rule
    for i in grammar:
        ##print(grammar[i])
        # for each list in a rule
        first = set()
        second = []
        indx_list = set()
        slices = []

        for j in grammar[i]:
            ##print(f'j is: {j}')
            if non_terminal in j:
                
                # if terminal is found, let slice it
                ##print("guard")
                # temp = j
                the_index = get_index(non_terminal, j)

                # get first occurance of the NT
                indx = j.index(non_terminal)
                temp = j[indx+1:]
                if non_terminal in temp:
                    slices_temp = [list(y) for x, y in itertools.groupby(temp, lambda z: z == non_terminal) if not x]
                    for z in slices_temp:
                        if z not in slices:
                            slices.append(z)
                else:
                    if temp not in slices:
                        slices.append(temp) 

                print(f"*slices are* {slices} **")
                ##print(indx)
                ##print(f"{i} --> *{j[indx+1:]}* ")
                #if j[indx+1:] not in first:
                #first.add(j[indx+1:])
                #first.add('ff')
                tick_list = tuple(slices)
                #first.add(tick_list)

        #slices = list(dict.fromkeys(slices))
        

        if len(slices) != 0:
            rhs_dict[i] = list(slices)
        
        print(slices)
        #first.clear()
    print(rhs_dict)
    return rhs_dict

def separate_production(production_list):
    sep_production = []

    # for each production
    for i in production_list:
        # for each list in a production
        for j in production_list[i]:
            
            sep_production.append({ i: j})
    print(sep_production)
    return sep_production


def build_parsing_table(grammar, non_terminal_list, start_symbol):

    '''
    build a predictive parsing table

    for each production n → 𝞪
        for each a ∈ first(𝞪)
            add n → 𝞪 to T[n,a]
        if 𝛆 ∈ first(𝞪) then
            for each b ∈ follow(n)
                add n → 𝞪 to T[n,a]

    let P be the list of grammar {n → 𝞪} , T the parsing table:

        b = n → 𝞪
        for P in grammar:
            x = first(P.𝞪)
            for i in x:
                if i != 𝛆:
                    T[n,i] = P
            if has_espilon(x):
                y = follow(P.n)
                for j in y:
                    T[n,j] = P 

    '''

    # separate grammar
    # get list of dicts each point to one production
    #sep_production = separate_production(grammar)
    T = {}

    non_terminal_list = get_non_terminal_list(grammar)
    terminal_list = get_terminal_list(grammar,1)

    # list of lists initialized with 'sync'
    parsing_table = initialize_parsing_tree(non_terminal_list,terminal_list)
    terminal_dict = hash_it(terminal_list)
    non_terminal_dict = hash_it(non_terminal_list)

    first_set = get_firsts(grammar, non_terminal_list)
    #print_red(parsing_table)

    for g in grammar:

        ## returns modified production list dict()
        ## alpha shall be a list of production list
        # print("*"*15)
        # print('[start] separate grammar production')
        productions_list = separate_grammar_production(g, grammar[g])
        # need n--> NT ,
        # get_dict_items()
        col_dict = {}
        temp_dict = {}
        temp_dict2 = {}

        for p in productions_list:
            #print(f'i in production  n → 𝞪 : {p}')
            x,_ = find_first_sole(grammar, '𝛄',p,non_terminal_list,1)
            key,val =  get_dict_items(p)
            #index_row = non_terminal_dict[key]
            #print_green(f'{key}, {index_row}')

            #print_yellow(f'firsts : {x}')

            for i in x:
                if i != '𝛆':
                    # print(f'[n,i] → P, [{key},{i}]  → {p}')
                    # print(f"add {i}")
                    temp_dict[i] = p

                   
                    #index_col = terminal_dict[i]
                   # parsing_table[index_row][index_col] = p
            #print_yellow(parsing_table[non_terminal_dict[key]])
                    
                #T[key]= temp_dict  

            
            if has_epsilon(x):
                # print("has 𝛆!")
                y = get_follow(grammar,key, first_set, start_symbol,non_terminal_list)
                # print_green(f"follow: {y}")
                for j in y:
                    temp_dict[j] = p

                    index_col = terminal_dict[j]
                    #parsing_table[index_row][index_col] = p
                # print(f'temp_dict: {temp_dict}')

            T[key]= temp_dict
            # print_red(f'temp_dict: {temp_dict}')
            # print(f"x is {x}***")
            #print('[end] separate grammar production')
            #print("*"*15)
    # print_green(parsing_table)
    #print(T)
    return T
    
def parse_input(parsing_table, input_list, start_symbol, non_terminal_list, terminal_list, delay=0):
    '''
    http://www.cs.ecu.edu/karl/5220/spr16/Notes/Top-down/LL1.html

    stack todo = [$]
    stack matched = []
    t = get_next_input()

    while todo is not empty:
        if TOS(todo) is non terminal:
            x = lookup_table(TOS(todo), t)
            if x:
                todo.push(x)
            else:
                raise_error(panic)
        else if TOS(todo) is terminal:
            if t == TOS(todo):
                t= get_next_input()
            else:
                raise_error(panic)
    
    '''
    input_list.append('$')
    terminal_list.add('𝛆')
    terminal_list.add('$')

    print_blue(f"the input: {input_list}")
    t= input_list.pop(0)
    print_yellow(f"current token: {t}")
    todo = ['$',start_symbol]
    match = []
    action = []
    s = []
    todos = [todo.copy()]
    count = 0

    #temp state
    first_state = ['$',start_symbol]

    # todos
    A = []
    #inputs
    B = []
    #actions
    C = []

    # returns todos , actions, inputs
    inputs = [t]
    if count == 0:
        todos.append(todo.copy())
    while todo:
        c = "Consume 𝛆"

        time.sleep(delay)
        # todos
        todos.append(todo[-1])

        if todo[-1] in non_terminal_list:
            print_yellow(f'todo.TOS : {todo[-1]}, terminal : {t}')
            x = lookup_table(parsing_table, todo[-1], t)

        
            #tos = todo[-1]

            tos =todo.pop(-1)
            #todos.append(tos.copy())

            s.append(tos)

           
            if x:
                action.append({tos:x.copy()})
                c = {tos:x.copy()}

                print_green(f"found in table {x}")
                # x is a list needs some pops
                x.reverse()
                #replace the current terminal with the def
                #todo.pop(-1)
                while(x):
                    todo.append(x.pop(0))
            
            else:
                #print_red("Not found in table")
                action.append({tos:"not found"})

                c = {tos:"not found"}

                pass

        elif todo[-1] in terminal_list:
            # if equal remove it in both sides
            if t == todo[-1]:
                print_green(f"*.*.* Match : {t} *.*.*")
                action.append(f"Match : {t}")

                match.append(t)
                c = f"Match : {t}"

                if input_list:
                    t = input_list.pop(0)
                    inputs.append(t)

                tos = todo.pop(-1)
                s.append(tos)
                
            elif todo[-1] == '𝛆':
                tos = todo.pop(-1)
                s.append(tos)
                action.append({tos:"epsi"})
                
            else:
                print_yellow("Sytanx Error")
                todo.pop(-1)
                

        print_dark_cyan(f"Todo Stack: {todo}")
        print_blue(f"Current Token: {t}")
        print_yellow(f"Matches Stack: {match}")
        A.append(todo.copy())
        B.append(t)
        C.append(pretty_rule(c))
        count +=1

    
    A.insert(0,first_state)

    if not input_list:
        print_green("*.*.* Success! *.*.*")
        B.append(" ")
        C.append("Success")
        return A,B,C
        return True
    else:
        print_purple("Sytanx Error")
        return False

def pretty_rule(rule):
    if isinstance(rule, dict):
        key, val = get_dict_items_2 (rule)
        return str(key+ "   ⟶   " + str(val))
    return rule

def separate_grammar_production(key, value):
    '''
        key is the non-terminal
        value is the list pointed to
    '''
    production_dict = {key: value}
    alpha = []

    for i in value:
        alpha.append({key: [i]})

    #print(alpha)
    return alpha

def get_dict_items(the_dict):
    for i in the_dict:
        return i, the_dict[i][0]

def get_dict_items_2(the_dict):
    for i in the_dict:
        return i, the_dict[i]


def lookup_table(parsing_table, non_terminal, terminal):

    
    if non_terminal in parsing_table:
        x = parsing_table[non_terminal]
        if terminal in x:
            #print_green(parsing_table[non_terminal][terminal])
            _,value = get_dict_items(parsing_table[non_terminal][terminal])
            return value.copy()
    
    return False

def get_next_input(input_list):
    if input_list:
        return input_list.pop(0)
    else:
        return False

        
def get_firsts(grammar , non_terminal_list):
    '''
     collects each firsts in a BIG dictionary   
    
    '''
    firsts = {}
    for i in grammar:
        first_i = get_first(grammar, i, non_terminal_list)
        firsts[i] = first_i
    return firsts


