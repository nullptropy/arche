# coding: utf-8

from .state import State
from dataclasses import dataclass

@dataclass
class POP:
    pass

@dataclass
class SET:
    state: State

@dataclass
class PUSH:
    state: State

# use this for static checking
Transition = POP | SET | PUSH | None
