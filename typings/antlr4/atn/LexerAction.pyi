"""
This type stub file was generated by pyright.
"""

from enum import IntEnum

Lexer = None
class LexerActionType(IntEnum):
    CHANNEL = ...
    CUSTOM = ...
    MODE = ...
    MORE = ...
    POP_MODE = ...
    PUSH_MODE = ...
    SKIP = ...
    TYPE = ...


class LexerAction(object):
    def __init__(self, action: LexerActionType) -> None:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    


class LexerSkipAction(LexerAction):
    INSTANCE = ...
    def __init__(self) -> None:
        ...
    
    def execute(self, lexer: Lexer):
        ...
    
    def __str__(self) -> str:
        ...
    


class LexerTypeAction(LexerAction):
    def __init__(self, type: int) -> None:
        ...
    
    def execute(self, lexer: Lexer):
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __str__(self) -> str:
        ...
    


class LexerPushModeAction(LexerAction):
    def __init__(self, mode: int) -> None:
        ...
    
    def execute(self, lexer: Lexer):
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __str__(self) -> str:
        ...
    


class LexerPopModeAction(LexerAction):
    INSTANCE = ...
    def __init__(self) -> None:
        ...
    
    def execute(self, lexer: Lexer):
        ...
    
    def __str__(self) -> str:
        ...
    


class LexerMoreAction(LexerAction):
    INSTANCE = ...
    def __init__(self) -> None:
        ...
    
    def execute(self, lexer: Lexer):
        ...
    
    def __str__(self) -> str:
        ...
    


class LexerModeAction(LexerAction):
    def __init__(self, mode: int) -> None:
        ...
    
    def execute(self, lexer: Lexer):
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __str__(self) -> str:
        ...
    


class LexerCustomAction(LexerAction):
    def __init__(self, ruleIndex: int, actionIndex: int) -> None:
        ...
    
    def execute(self, lexer: Lexer):
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    


class LexerChannelAction(LexerAction):
    def __init__(self, channel: int) -> None:
        ...
    
    def execute(self, lexer: Lexer):
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __str__(self) -> str:
        ...
    


class LexerIndexedCustomAction(LexerAction):
    def __init__(self, offset: int, action: LexerAction) -> None:
        ...
    
    def execute(self, lexer: Lexer):
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    


