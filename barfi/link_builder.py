class Link(object):
    def __init__(self, name: str):
        self._type = name
        self._name = name
        self._id = ''
        self._value = None

    def __repr__(self) -> str:
        return f'<barfi.Link of type `{self._type}` at {hex(id(self))}>'

    def get_value(self):  
        if self._value != None:      
            return self._value
        else:
            raise ValueError(f'Value not set for Link(`{self._type}`) at {hex(id(self))}')

    def set_value(self, value: any) -> None:        
        self._value = value

if __name__ == '__main__':
    link1 = Link(name='int')
    print(link1)
    link2 = Link(name='int')
    print(link2)
    link3 = link1
    print(link3)
    link4 = link1
    print(link4)
    