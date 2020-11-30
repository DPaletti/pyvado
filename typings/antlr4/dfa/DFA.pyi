"""
This type stub file was generated by pyright.
"""

from antlr4.atn.ATNState import DecisionState
from antlr4.dfa.DFAState import DFAState

class DFA(object):
    def __init__(self, atnStartState: DecisionState, decision: int = ...) -> None:
        ...
    
    def getPrecedenceStartState(self, precedence: int):
        ...
    
    def setPrecedenceStartState(self, precedence: int, startState: DFAState):
        ...
    
    def setPrecedenceDfa(self, precedenceDfa: bool):
        ...
    
    @property
    def states(self):
        ...
    
    def sortedStates(self):
        ...
    
    def __str__(self) -> str:
        ...
    
    def toString(self, literalNames: list = ..., symbolicNames: list = ...):
        ...
    
    def toLexerString(self):
        ...
    

