from enum import Enum, auto

class Solution:
    class Event(Enum):
        SIGN = 0
        DIGIT = 1
        DOT = 2
        E = 3
        OTHERS = 4

    class State(Enum):
        START = 0
        SIGN = 1
        DIGIT = 2
        DOT = 3
        DOT_DIGIT = 4
        DOT_DIGIT_E = 5
        DOT_DIGIT_E_SIGN = 6
        DOT_DIGIT_E_DIGIT = 7
        INVALID = 8
    
    def get_event(self, s: str) -> State:
        if s == '+' or s == '-':
            return Solution.Event.SIGN
        if s >= '0' and s <= '9':
            return Solution.Event.DIGIT
        if s == '.':
            return Solution.Event.DOT
        if s == 'e' or s == 'E':
            return Solution.Event.E
        
        return Solution.Event.OTHERS

    
    def isNumber(self, s: str) -> bool:
        transfer = [
            [Solution.State.SIGN, Solution.State.DIGIT, Solution.State.DOT, Solution.State.INVALID, Solution.State.INVALID], # start
            [Solution.State.INVALID, Solution.State.DIGIT, Solution.State.DOT, Solution.State.INVALID,Solution.State.INVALID], # sign
            [Solution.State.INVALID, Solution.State.DIGIT, Solution.State.DOT_DIGIT, Solution.State.DOT_DIGIT_E, Solution.State.INVALID], # digit
            [Solution.State.INVALID, Solution.State.DOT_DIGIT, Solution.State.INVALID, Solution.State.INVALID, Solution.State.INVALID], # dot
            [Solution.State.INVALID, Solution.State.DOT_DIGIT, Solution.State.INVALID, Solution.State.DOT_DIGIT_E, Solution.State.INVALID], # dot-digit
            [Solution.State.DOT_DIGIT_E_SIGN, Solution.State.DOT_DIGIT_E_DIGIT, Solution.State.INVALID, Solution.State.INVALID, Solution.State.INVALID], # dot-digit-e
            [Solution.State.INVALID, Solution.State.DOT_DIGIT_E_DIGIT, Solution.State.INVALID, Solution.State.INVALID, Solution.State.INVALID], # dot-digit-e-sign
            [Solution.State.INVALID, Solution.State.DOT_DIGIT_E_DIGIT, Solution.State.INVALID, Solution.State.INVALID, Solution.State.INVALID], # dot-digit-e-digit
            [Solution.State.INVALID, Solution.State.INVALID, Solution.State.INVALID, Solution.State.INVALID, Solution.State.INVALID] # invalid
        ]

        INIT = Solution.State.START
        state = INIT
        for ss in s:
            event = self.get_event(ss)
            state = transfer[state.value][event.value]
            if state == Solution.State.INVALID:
                return False
        
        return True if state == Solution.State.DIGIT or \
        state == Solution.State.DOT_DIGIT or \
        state == Solution.State.DOT_DIGIT_E_DIGIT \
        else False

# solu = Solution()
# solu.isNumber("e9")