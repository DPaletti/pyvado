"""
This type stub file was generated by pyright.
"""

from antlr4.RuleContext import RuleContext
from antlr4.atn.ATN import ATN
from antlr4.atn.ATNState import ATNState

class LL1Analyzer(object):
    HIT_PRED = ...
    def __init__(self, atn: ATN) -> None:
        ...
    
    def getDecisionLookahead(self, s: ATNState):
        ...
    
    def LOOK(self, s: ATNState, stopState: ATNState = ..., ctx: RuleContext = ...):
        ...
    

