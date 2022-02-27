from dataclasses import dataclass

@dataclass
class Link(object):    
    def __init__(self, value: any, name: str, id: str):
        self.id = id
        self.name = name
        self.value = value

    # def __repr__(self):
    #     self_var_names = ','.join(list(self.__dict__.keys()))
    #     return self.__class__.__name__+'(' + self_var_names + ')'    

    def get_value(self, var_name: str = 'value'):        
        if var_name not in self.__dict__:
            raise ValueError(f'`{var_name}` not present in Link.')
        return self.__dict__.get(var_name)
    
    def set_value(self, value: any, var_name: str = 'value') -> None: 
        if var_name not in self.__dict__:
            raise ValueError(f'Field `{var_name}` is not not present in Link.')
        self.__dict__[var_name] = value

if __name__ == '__main__':
    a = Link('adi')
    print(a)
    print('a.get_value() is:', a.get_value())
    b = Link('krish')
    c = Link('krish')
    print('b.get_value() is:', b.get_value(), 'at id: ', id(b))
    print('c.get_value() is:', c.get_value(), 'at id: ', id(c))
    print('is b == c ?', b == c)
    a.set_value('cia')
    print('a.set_value("cia")', a.get_value())

    class IntLink(Link):
        def __init__(self, data: int):
            self.data = data

    # @dataclass
    # class IntLink(Link):        
    #     data: int