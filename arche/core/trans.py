# coding: utf-8

class Transition:
    def __init__(self, trans, state=None):
        self.state = state
        self.trans = trans

    def __eq__(self, other):
        return self.trans == other.__name__

class POP(Transition):
    def __init__(self):
        super().__init__(self.__class__.__name__)

class SET(Transition):
    def __init__(self, state):
        super().__init__(self.__class__.__name__, state)

class PUSH(Transition):
    def __init__(self, state):
        super().__init__(self.__class__.__name__, state)

class NONE(Transition):
    def __init__(self):
        super().__init__(self.__class__.__name__)