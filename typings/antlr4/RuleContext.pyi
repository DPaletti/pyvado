"""
This type stub file was generated by pyright.
"""

from antlr4.tree.Tree import ParseTreeVisitor, RuleNode

RuleContext = None
Parser = None
class RuleContext(RuleNode):
    EMPTY = ...
    def __init__(self, parent: RuleContext = ..., invokingState: int = ...) -> None:
        ...
    
    def depth(self):
        ...
    
    def isEmpty(self):
        ...
    
    def getSourceInterval(self):
        ...
    
    def getRuleContext(self):
        ...
    
    def getPayload(self):
        ...
    
    def getText(self):
        ...
    
    def getRuleIndex(self):
        ...
    
    def getAltNumber(self):
        ...
    
    def setAltNumber(self, altNumber: int):
        ...
    
    def getChild(self, i: int):
        ...
    
    def getChildCount(self):
        ...
    
    def getChildren(self):
        ...
    
    def accept(self, visitor: ParseTreeVisitor):
        ...
    
    def toStringTree(self, ruleNames: list = ..., recog: Parser = ...):
        ...
    
    def __str__(self) -> str:
        ...
    
    def toString(self, ruleNames: list, stop: RuleContext) -> str:
        ...
    


