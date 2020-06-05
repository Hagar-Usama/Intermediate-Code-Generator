class Symbol:
    def __init__(self, lex, stype, value=None):
        self.lex = lex
        self.type = stype
        self.value = value


class SymTable:
    def __init__(self):
        self.table = {}
        self.coolTable = {}
        self.locals = {}
    
    def add_symbol(self, sym):
        #check if already exists (duplicate declaration)
        self.table[sym.lex] = sym
        self.coolTable[sym.lex] = [sym.type, sym.value]
        #print_yellow(f"add symbol: {sym.lex}, val: {sym.value}")
        self.locals[sym.lex] = len(self.locals)


    def lookup_table(self,key):
        if key in self.coolTable:
            return self.coolTable[key]
        else:
            return False

    def update_symbol_val(self,key,val):

        x = self.lookup_table(key)
        if x:
            x[1] = val
            self.coolTable[key] = x

    def get_index(self, key):
        if key in self.locals:
            return self.locals[key]
        else:
            return 0



        


