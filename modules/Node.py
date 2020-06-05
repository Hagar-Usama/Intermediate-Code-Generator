import uuid
from modules.semantic import split_actions, modify_actions, post_modify_actions, post_modify_actions_2
import re
from modules.color_print import print_yellow, print_blue, print_dark_cyan, print_green, print_purple, print_red
from modules.Symbol import Symbol, SymTable

def get_node_uuid():
    _NODE_UUID = str(uuid.uuid4())[:8]

    return _NODE_UUID

 
unique_id = 129300
G_identifiers = {}
grammar_dict = {}
grammar_dict_sym = {}
start_symbol = ''


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
        self.isleaf = False
        self.lexeme = ''
        self.type = None
        self.value = ''
        self.code = ""
        self.comp_code = ""

    
    def __del__(self):
        #print('Destructor called, vehicle deleted.')
        pass

    def get_code(self):
        #p = re.compile('\\n+')
        #x = self.code.split("\n")
        x =  re.sub(r'(\n)+', '\n', self.code)
        x = re.sub(r'(\n    \n)+', '\n',x)
        x = x.strip("\n")
        
        return x

        
    def backpatch(self):
        '''
        gather all labels
        if there is a consecutive labels:
            store them
            replace them with the first one in the list
            delete the duplicates

        '''

        code_list = self.get_code()
        code_list = code_list.split("\n")
        labels = []
        dups = []


        for i, value in enumerate(code_list):
            if value.endswith(":"):
                labels.append((i, value))

        if labels:
                
            temp = labels[0][0]
            for i, value in enumerate(labels):
                
                if value[0] == temp + 1:
                    #print("dup", value)
                    #dups.append((labels[i][1][:-1], labels[i-1][1][:-1]))
                    dups.append((labels[i][1], labels[i-1][1]))

                temp = value[0]
            
            #print("dups",dups)

            

            #print_yellow(self.get_code())
            #print_blue(dups)
            
            for i in dups:
                # replace labels
                self.code = self.code.replace(i[0][:],"not needed")
                self.code = self.code.replace("not needed","")
                self.code = self.code.replace(i[0][:-1],i[1][:-1])
                # remove redundant
                

            #print(self.get_code())

            #print("print labels")
            #print(labels)

        return labels
       
    def jasmin_in(self, name):

        part1 = ".class public " + f"{name}\n"
        part1 += """.super java/lang/Object 
.method public <init>()V 
    aload_0 
    invokespecial java/lang/Object/<init>()V 
    return 
.end method 
.method public static main([Ljava/lang/String;)V
    .limit stack 10 
    .limit locals 100\n"""

        part2 = self.get_code()
        part3 = """\n     return
.end method"""
        
        full_code = part1 + part2 + part3

        return full_code

        #write it into file


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
            #print_green(f"current Node| id:{current_node.id}, Name:{current_node.name}")

            pack = split_actions(actions.pop(0))
            #print_blue(f"package is: {pack}")

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
                #print(f"it is else: {pack}")
                self.leaves.append(current_node)
                current_node.isleaf = True

    def update_leaves(self):
        leaves = []

        nodes_list = [self]
        current_node = self

        
        while nodes_list:
            current_node = nodes_list.pop(-1)
            for n in current_node.children:
                nodes_list.append(n)
                
            if current_node.children == []:
                leaves.insert(0,current_node)
                current_node.isleaf = True

        self.leaves = leaves


        for i in self.leaves:
            #print_purple(i.name)
            pass




    
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

    def show_tree_2(self, option=0):

        nodes_list = [self]
        current_node = self

        
        while nodes_list:
            current_node = nodes_list.pop(-1)
            print(" |"*(current_node.depth), end='\n' )
            #print("|",end='')
            print(" "*(current_node.depth*2), end='--' )

            #print_dark_cyan(f"Node Name: {current_node.name}, Value: {current_node.value}, lex: {current_node.lexeme}, type:{current_node.type}")
            print_node(current_node,option)
            #print_dark_cyan(f"Node Name: {current_node.name}, {current_node}")

            #print_dark_cyan(f"Name: {current_node.name}, Id: {current_node.id}")
            
            l = []
            for n in current_node.children:
                l.insert(0,n)
                #print("_"*n.depth, end='-' )
                #print_yellow(f"Child Name: {n.name}, Id: {n.id}")
                #print_yellow(f"Child Name: {n.name}")

            for j in l:
                nodes_list.append(j)

    def simplify_tree(self):

        # for each leaf that is epsilon 𝛆, remove it, and its parent if it is the only child
        unwanted = []
        x = []
        for leaf in self.leaves:
            print_yellow(leaf.name)
            if leaf.name == '𝛆':
                #print_red("it is eps")
                parent = leaf.parent
                #print_green(parent.children)
                parent.children = parent.children.remove(leaf)
                #self.leaves.remove(leaf)
                x.append(leaf)
                
                

                if not isinstance(parent.children, list):
                    parent.children = []

                del leaf
        for i in x:
            self.leaves.remove(i)       
            #while unwanted:
            #    x = unwanted.pop(-1)
            #    del x
    
    def simplify_tree_2(self, terminal_list):
        '''
        [1] enter list of unwanted terminals
        [2] compare it with leaves and extract nodes

        simplify:
        [1] enqueue first element in removed in queue
        [2] while Q is not empty:
            n = Q.deQ
            if removed not empty:
                n.children.remove(removed.deQ)
            if n has no children:
                Q.enQ(n.parent)
                n.parent.children.remove(n)
        
        '''
        rem = []
        for i in terminal_list:
            for leaf in self.leaves:
                #print(f"leaf name is {leaf.name}")
                if leaf.name == i:
                    rem.append(leaf)


        #print(f"rem is : {rem}")

        for i in rem:
            #print(i.name,end="\t")
            pass
        

        node_list = []
        node_list.append(rem[0].parent)

        for i in node_list:
            print(i.name,end="\t")

        while node_list:
            n = node_list.pop(0)
            if rem:
                #print(f"n.children {n.children}")
                #print(f"rem[0] {rem[0]}")
                n.children.remove(rem.pop(0))
            if not n.children:
                node_list.append(n.parent)
                n.parent.children.remove(n)

            
    def simplify_it(self, terminal_list):

        terminal_list = set(terminal_list)

        q = []
        l = []
        
        for i in self.leaves:
            if i.name in terminal_list:
                l.append(i)

        for i in l:
            #print(f"{i.name}, {i}")
            q.append(i.parent)

        #print(len(l))
        if len(l) > 0 :
            q.append(l[0].parent)
            #print(f"q : {q[0]}")

            while q:
                n = q.pop(0)
                if l:
                    x = l.pop(0)
                    #print(f'list is {x.name}, {x}')
                    #print(f'n children {n.name} -> {n.children}')
                    #if x in n.children:
                    #print("remove child")
                    if x in self.leaves:
                        self.leaves.remove(x)
                    n.children.remove(x)


                if not n.children:
                    #print("node has no children")
                    #print(f"push the node into q {n.parent.name}")
                    q.append(n.parent)
                    # remove n
                    x = n
                    y = n.parent
                    if x in y.children:
                        if x in self.leaves:
                            self.leaves.remove(x)
                        y.children.remove(x)

    def add_lexemes(self, lex_list):
        '''
        search for leaves (tokens)
        attach lexemes as their children
        make lexems the leaves
        '''

        self.simplify_it(['𝛆'])

    

        for i, value in enumerate(self.leaves):
            #print(f"lex: {lex_list[i]}, token: {value.name}")
            value.lexeme = lex_list[i]
            #print(i, value)

    def semantic_analysis(self, symtab):
        nodes_list = [self]
        current_node = self

        
        while nodes_list:
            current_node = nodes_list.pop(-1)
            if current_node.name == "DECLARATION":
                #print_blue(f"Yay! declaration {current_node.children[1].lexeme}")
                current_node.type = current_node.children[0].name
                current_node.value = current_node.children[1].lexeme

                lex =  current_node.children[1].lexeme
                stype = current_node.children[0].name
                new_sym = Symbol(lex, stype)
                symtab.add_symbol(new_sym)
            
            elif current_node.name == "ASSIGNMENT":
                #print_blue(f"Yay! Assignment {current_node.children[0].name}")
                #valuee = []
                get_value(current_node.children[2])
                #print_green(val)
                pass

            else:
                for child in current_node.children:
                    nodes_list.insert(0,child)

    def reduce_tree(self,n):

        n = self

        if n.isleaf:
            return

        for i in n.children:
            self.reduce_tree(i)

        if len(n.children) == 1:
            #print_yellow(f"node is : {n.name}")

            #self.reduce_tree(n.children[0])
            temp1 = n.parent
            
            # if it is not the root
            if temp1 != None:
                #print_yellow(f"temp1 {temp1}")
                temp2 = n
                #print_yellow(f"temp2 {temp2}")
                n = n.children[0]
                n.parent = temp1
                node_index = temp1.children.index(temp2)
                temp1.children[node_index] = n
                n.depth = n.depth - 1 
            else:
                # if parent is root: just remove the child:
                temp1 = n.children[0]       #to be removed
                n.children = temp1.children

                # mind you have to delete in other conditions
                del n
    
    def eliminate_exp(self, op_list):

        '''
        if the node  n is the leftmost child:
            x = n.parent
            x.remove(n)
            while len(x.children)==1:
                x= x.parent

        '''

        for leaf in self.leaves:
            if leaf.name in op_list:
                #print_green(f"leaf is: {leaf.name}")
                # if it is the leftmost
                if leaf.parent.children[0] == leaf:
                    

                    x = leaf.parent
                    x.children.remove(leaf)

                    while len(x.children) == 1:
                        x = x.parent


                    x.name = leaf.name
                    x.lexeme = leaf.lexeme

                    self.leaves.remove(leaf)

                else:
                    # for assign
                    leaf.parent.name = leaf.name
                    leaf.parent.lexeme = leaf.lexeme
                    leaf.parent.children.remove(leaf)
                    self.leaves.remove(leaf)

    

def reduce_tree(n):

        
        if n.isleaf:
            return

        for i in n.children:
            reduce_tree(i)

        if len(n.children) == 1:
            #print_yellow(f"node is : {n.name}")

            #self.reduce_tree(n.children[0])
            temp1 = n.parent
            
            # if it is not the root
            if temp1 != None:
                #print_yellow(f"temp1 {temp1}")
                temp2 = n
                #print_yellow(f"temp2 {temp2}")

                n = n.children[0]
                
                n.parent = temp1
                node_index = temp1.children.index(temp2)
                temp1.children[node_index] = n
                n.depth = n.depth - 1 
            else:
                # if parent is root: just remove the child:
                temp1 = n.children[0]       #to be removed
                n.children = temp1.children

                del n
        
def get_value(n):

    if n.isleaf:
        #val.append(n.lexeme) 
        #print_yellow(n.lexeme)
        #return val
        pass
    
    for i in n.children:
        get_value(i)

def get_str_val(n):
    if n.isleaf:
        val = n.lexeme

    else:
        for i in n.children:
            val = get_str_val(i)
            n.value += val

        #print_yellow(n.value)



def get_val_2(n, symtab):

    #print_yellow(f"name: {n.name}")


    if n.name == "IF" or n.name =="WHILE":
        pass

    elif n.isleaf:
        x = check_cat(n)
        if x == "num":
            #print_purple(n.lexeme)
            n.value,ntype = check_type(n.lexeme)
            #print_green(type(n.value))
            n.type = ntype

        elif x == "id":

            #print_green(n.lexeme)
            y = n.parent
            if n.parent.name != "DECLARATION":
                val = symtab.lookup_table(n.lexeme)
                if val:
                    if val[1] == None:
                        #print_red("variable not assigned")
                        pass
                    else:
                        n.value = val[1]
                        n.type = val[0]
                    #print_blue(f"id type : {n.type}")
                else:
                    #print_red("variable not declared")
                    n.type = "undefined"
            else:
                #declaration:
                new_sym = Symbol(n.lexeme, n.parent.children[0].lexeme)
                symtab.add_symbol(new_sym)
                #print_red(symtab.coolTable)
                
    else:

        if n.lexeme == '*':
            get_val_2(n.children[0], symtab)
            get_val_2(n.children[1], symtab)
            n.value = n.children[0].value * n.children[1].value
            _,n.type = check_type(n.value)

        elif n.lexeme == '/':
            get_val_2(n.children[0], symtab)
            get_val_2(n.children[1], symtab)
            n.value = n.children[0].value / n.children[1].value
            _,n.type = check_type(n.value)

        elif n.lexeme == '+':
            get_val_2(n.children[0], symtab)
            get_val_2(n.children[1], symtab)
            n.value = n.children[0].value + n.children[1].value
            _,n.type = check_type(n.value)
        
        elif n.lexeme == '-':
            get_val_2(n.children[0], symtab)
            get_val_2(n.children[1], symtab)
            n.value = n.children[0].value - n.children[1].value
            _,n.type = check_type(n.value)


        elif n.name == '"assign"':
            get_val_2(n.children[1], symtab) 
            #print_dark_cyan(f"val for assign: {n.children[1].value}")       
            n.value = n.children[1].value
            n.type =  n.children[1].type
            n.children[0].value = n.value
            
            stype,_ = symtab.lookup_table(n.children[0].lexeme)
            #print_red(f"sytpe is : {stype}")
            new_sym = Symbol(n.children[0].lexeme, stype, n.children[0].value)

            symtab.add_symbol(new_sym)
            symtab.update_symbol_val(n.children[0].lexeme, n.children[0].value)
            #shall be got from table
            n.children[0].type = n.type
        
        elif n.lexeme == '<':
            get_val_2(n.children[0], symtab)
            get_val_2(n.children[1], symtab)
            n.value = int(n.children[0].value < n.children[1].value)
            _,n.type = check_type(n.value)
        
        else:
            for i in n.children:
                #if i.name !="DECLARATION":
                get_val_2(i,symtab)

    #print(symtab.coolTable)


def get_val_virtual(n, symtab):

    '''
    For conditional blocks
    
    '''

    #print_yellow(f"name: {n.name}")


    if n.isleaf:
        x = check_cat(n)
        if x == "num":
            #print_purple(n.lexeme)
            n.value,ntype = check_type(n.lexeme)
            #print_green(type(n.value))
            n.type = ntype

        elif x == "id":

            #print_green(n.lexeme)
            y = n.parent
            if n.parent.name != "DECLARATION":
                val = symtab.lookup_table(n.lexeme)
                if val:
                    if val[1] == None:
                        print_red("variable not assigned")
                    else:
                        n.value = val[1]
                        n.type = val[0]
                    #print_blue(f"id type : {n.type}")
                else:
                    print_red("variable not declared")
                    n.type = "undefined"
            else:
                #declaration:
                pass
                
    else:

        if n.lexeme == '*':
            get_val_virtual(n.children[0], symtab)
            get_val_virtual(n.children[1], symtab)
            n.value = n.children[0].value * n.children[1].value
            _,n.type = check_type(n.value)

        elif n.lexeme == '/':
            get_val_virtual(n.children[0], symtab)
            get_val_virtual(n.children[1], symtab)
            n.value = n.children[0].value / n.children[1].value
            _,n.type = check_type(n.value)

        elif n.lexeme == '+':
            get_val_virtual(n.children[0], symtab)
            get_val_virtual(n.children[1], symtab)
            n.value = n.children[0].value + n.children[1].value
            _,n.type = check_type(n.value)
        
        elif n.lexeme == '-':
            get_val_virtual(n.children[0], symtab)
            get_val_virtual(n.children[1], symtab)
            n.value = n.children[0].value - n.children[1].value
            _,n.type = check_type(n.value)


        elif n.name == '"assign"':
            get_val_virtual(n.children[1], symtab) 
            #print_dark_cyan(f"val for assign: {n.children[1].value}")       
            n.value = n.children[1].value
            n.type =  n.children[1].type
            n.children[0].value = n.value
            
            stype,_ = symtab.lookup_table(n.children[0].lexeme)
            #shall be got from table
            n.children[0].type = n.type
        
        elif n.lexeme == '<':
            get_val_virtual(n.children[0], symtab)
            get_val_virtual(n.children[1], symtab)
            n.value = int(n.children[0].value < n.children[1].value)
            _,n.type = check_type(n.value)
        
        else:
            for i in n.children:
                #if i.name !="DECLARATION":
                get_val_virtual(i,symtab)

    #print(symtab.coolTable)


def generate_code(n, symtab):
    #print_yellow(f"name: {n.name}")

    if n.isleaf:
        x = check_cat(n)
        if x == "num":
            
            if n.type == "int":
                if n.value < 6:
                    n.code = "\n    " + n.type[0] + "const_" + str(n.value)
                else:
                    n.code = "\n    " + "bipush " + str(n.value)

            elif n.type == "float":
                n.code = "\n    "  + "ldc " + str(n.value) + "f" 


        elif x == "id":

            #print_green(n.lexeme)
            y = n.parent
            
            if n.parent.name == "DECLARATION":
                # add to stack
                pass
            elif n.parent.name == '"assign"':
                index = symtab.get_index(n.lexeme)

                if index > 6:
                    n.code = "\n    " + n.type[0] + "store " + str(index)
                else:
                    
                    n.code = "\n    " + n.type[0] + "store_" + str(index)
                
                
            else:
                
                index = symtab.get_index(n.lexeme)
                if index < 6:
                    n.code = "\n    " +  n.type[0] + "load_" + str(index)
                else:
                    n.code = "\n    " + n.type[0] + "load " + str(index)

                if n.type == "int" and n.parent.type == "float":
                    n.code += "\n    i2f"
                
    else:

        if n.lexeme == '*':

            generate_code(n.children[0], symtab)
            generate_code(n.children[1], symtab)


            
            r_code = n.children[0].code
            l_code = "\n    " + n.children[1].code
            
            n.code = r_code + l_code + "\n    " +  n.type[0] + 'mul'

        elif n.lexeme == '/':
            generate_code(n.children[0], symtab)
            generate_code(n.children[1], symtab)

            r_code = n.children[0].code
            l_code = "\n    " + n.children[1].code
            n.code = r_code + l_code + "\n    " +  n.type[0] + 'div'
            

            
        elif n.lexeme == '+':
            generate_code(n.children[0], symtab)
            generate_code(n.children[1], symtab)

            if n.children[0].lexeme == "1" and n.children[0].type == "int":
                n.code = n.type[0] + "inc" + " " + str(symtab.get_index(n.children[1].lexeme)) + ",1"
            elif n.children[1].lexeme == "1" and n.children[1].type == "int":
                n.code = n.type[0] + "inc" + " " + str(symtab.get_index(n.children[0].lexeme)) + ",1"
            else:
                r_code = n.children[0].code
                l_code = "\n    " + n.children[1].code
                n.code = r_code + l_code + "\n    " +  n.type[0] + 'add'
                
            
        elif n.lexeme == '-':
            generate_code(n.children[0], symtab)
            generate_code(n.children[1], symtab)

            r_code = n.children[0].code
            l_code = "\n    " + n.children[1].code
            n.code = r_code + l_code + "\n    " +  n.type[0] + 'sub'
            
            

        elif n.name == '"assign"':
            generate_code(n.children[0], symtab)
            generate_code(n.children[1], symtab)
            
            # load store
            n.code = n.children[1].code + '\n    ' +  n.children[0].code

        elif n.name == '"relop"':

            generate_code(n.children[0], symtab)
            generate_code(n.children[1], symtab)

            n.code = n.children[0].code + '\n' + n.children[1].code

            if n.lexeme == '<':
                
                if n.children[0].type == "int":
                    n.code += '\n    ' +  'if_icmpge'
                elif n.children[0].type == "float":
                    n.code += '\n    ' + "fcmpg" + "\n    " + "ifge"

            elif n.lexeme == '>':
                
                if n.children[0].type == "int":
                    n.code += '\n    ' +  'if_icmple'
                elif n.children[0].type == "float":
                    n.code += '\n    ' +  "fcmpl" + "\n    " + "ifle"
            
            elif n.lexeme == '>=':
                
                if n.children[0].type == "int":
                    n.code += '\n    ' +  'if_icmplt'
                elif n.children[0].type == "float":
                    n.code += '\n    ' +  "fcmpl" + "\n    " + "iflt"
            
            elif n.lexeme == '<=':
                
                if n.children[0].type == "int":
                    n.code += '\n    ' +  'if_icmpgt'
                elif n.children[0].type == "float":
                    n.code += '\n    ' +  "fcmpg" + "\n    " + "ifgt"
            
            elif n.lexeme == '==':
                
                if n.children[0].type == "int":
                    n.code += '\n    ' +  'if_icmpne'
                elif n.children[0].type == "float":
                    n.code += '\n    ' + "fcmpl" + "\n    " + "ifne"

            elif n.lexeme == '!=':

                if n.children[0].type == "int":
                    n.code += '\n    ' +  'if_icmpeq'
                elif n.children[0].type == "float":
                    n.code += '\n    ' +  "fcmpl" + "\n    " + "ifeq"

        elif n.name =="IF":

            for i in n.children:
                generate_code(i, symtab)

            label_else = assign_unique_name()
            label_next = assign_unique_name()
            
            n.code = n.children[0].code + " " + label_else
            # then.code            
            n.code += '\n    ' + n.children[1].code
            # goto Next
            n.code += '\n    ' + "goto " + label_next
            # else label
            n.code += '\n' + label_else +  ':' 
            # else.code
            n.code += '\n    ' + n.children[2].code
            # Next label
            n.code += '\n' + label_next + ':'

        elif n.name =="WHILE":

            for i in n.children:
                generate_code(i, symtab)

            label_w = assign_unique_name()
            label_next = assign_unique_name()


            n.code = label_w + ':'
            # !exp.code
            n.code += '\n    ' + n.children[0].code + " " + label_next
            # condition.code
            n.code += '\n    ' + n.children[1].code
            # goto while again
            n.code += '\n    ' + "goto " + label_w
            # Next label
            n.code += '\n' + label_next + ':'
            

            
        else:
            for i in n.children:
                if i.name !="DECLARATION":
                    generate_code(i,symtab)


            
            for i in n.children:
                n.code += "\n" + i.code
               

def print_node(n, option=0):
    block_list = ["METHOD_BODY", "WHILE", "IF","DECLARATION", "STATEMENT_LIST_2","STATEMENT_LIST"]
    if not option:
        if n.name in block_list:
            print_yellow(f"Node Name: {n.name}")
        elif n.name == '"relop"':
            print_dark_cyan(f"Node Name: {n.name}, Value: {n.value}, lex: {n.lexeme}")
        else:
            print_dark_cyan(f"Node Name: {n.name}, Value: {n.value}, lex: {n.lexeme}, type:{n.type}")
    else:
        if n.name == "METHOD_BODY":
             print_yellow(f"Node Name: {n.name}, code: {n.code}")
        elif n.name in block_list:
            print_yellow(f"Node Name: {n.name}")
        elif n.name == '"relop"':
            print_dark_cyan(f"Node Name: {n.name}, Value: {n.value}, lex: {n.lexeme} ")
        else:
            print_dark_cyan(f"Node Name: {n.name}, Value: {n.value}, lex: {n.lexeme}, type:{n.type}")


def assign_unique_name():
    assign_num = get_node_uuid()
    return 'L_'+ assign_num[0] + assign_num[1]  + assign_num[2]
    
def check_diff_types(n1, n2):
    if n1.type != n2.type:
        pass

def check_cat(n):
    
    if n.name == '"id"':
        return "id"
    elif n.name == '"num"':
        return "num"
    else:
        return n.name

def check_type(num):

    if isinstance(num, float):
        return float(num),'float'
    try:
        return int(num),'int'
    except ValueError:
        return float(num),'float'

def read_input_list(file_path):
    with open(file_path) as f:
        lines = [line.rstrip() for line in f]
    return lines

