# -*- coding: utf-8 -*-

def extract_args(string):
    """ Функция для анализа строки, содержащей аргументы: (10,U[2,2](1,1),5) """

    proc_str = string[1:-1]
    num_parenthesis = 0
    num_brackets = 0
    start = 0
    args = list()
    for ch_num, ch in enumerate(proc_str):
        if ch == u'(':
            num_parenthesis += 1
        elif ch == u')':
            num_parenthesis -= 1
        elif ch == u'[':
            num_brackets += 1
        elif ch == u']':
            num_brackets -= 1
        elif ch == u',' and num_parenthesis == 0 and num_brackets == 0:
            args.append(proc_str[start : ch_num])
            start = ch_num + 1
    
    args.append(proc_str[start :])
    
    return [global_parse_string(arg) for arg in args]


def args_to_unicode(args):
    """ Утилитарная функция для преобразования списка аргументов в строку. """

    return u','.join([unicode(arg) for arg in args])

            
def global_eval(obj):
    """ Функция для вычисления значения объекта. """
 
    print unicode(obj)
    if type(obj) is int:
	    # Если объект - это число, то просто возвращаем его
        return obj
    else:
	    # Если объект - это функция, то вычисляем ее
        return obj.eval_obj()

    
class FunctionU(object):
    """ 
	Объект-функция проекции, например, U[2,1](1,2) == 1 
	U[<кол-во аргументов>,<номер возвращаемого аргумента>](<аргумент1>,<аргумент2>)
	"""

    def __init__(self, string):
        super(FunctionU, self).__init__()
        self.num_args = -1
        self.targ_arg = -1
        self.args = list()
        
        self._parse_string(string)
        
    def _parse_string(self, string):
	    """ Функция для анализа строки. """
        start = string.find(u'[')
        end = string.find(u']', start)
        self.num_args, self.targ_arg = string[start + 1 : end].split(u',')
        self.num_args = int(self.num_args.strip())
        self.targ_arg = int(self.targ_arg.strip())
        
        self.args = extract_args(string[end + 1 : ])
        
    def eval_obj(self):
	    """ Вычисляем функцию U: возвращаем заданный аргумент. """
        return global_eval(self.args[self.targ_arg - 1])
    
    def __unicode__(self):
        return u'U[{},{}]({})'.format(self.num_args, 
                                      self.targ_arg, 
                                      args_to_unicode(self.args))
        
        
class FunctionS(object):
    """ Функция следования. S(x) = x + 1. Вам необходимо ее реализовать. """
    def __init__(self,string):
        pass # Your code here.
        
    def eval_obj(self):
        pass # Your code here.
    
    def __unicode__(self):
        pass # Your code here.
    
    
def global_parse_string(string):
    """ Функция для анализа входной строки. """
    proc_str = string.strip()
    
    tp = proc_str[0]
    if tp == u'U':
        return FunctionU(proc_str[1:])
    elif tp == u'S':
        return FunctionS(proc_str[1:])
    elif tp.isdigit():
        return int(proc_str)
    else:
        raise ValueError()
        
syntax_tree = global_parse_string(u'S(S(S(U[3,2](U[1,1](1),S(U[2,2](1,6)),3))))')
global_eval(syntax_tree)
