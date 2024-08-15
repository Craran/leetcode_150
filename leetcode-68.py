from typing import List
class Solution:
    def divide_groups(self, words: List[str], maxWidth: int) -> List[List[str]]:
        groups: List[List[str]] = []
        group: List[str] = []
        # lens: List[int] = []
        n, sum_len = 0, 0
        for i in range(len(words) - 1):
            n += 1
            group.append(words[i])
            sum_len = sum_len + len(words[i]) if n == 1 else sum_len + len(words[i]) + 1
            len_next = len(words[i + 1]) + 1
            if sum_len + len_next > maxWidth:
                groups.append(group)
                group = []
                sum_len, n = 0, 0
            
        group.append(words[-1])
        groups.append(group)

        return groups

        
    def transfer_str(self, group: List[str], maxWidth: int):
        length = 0
        for word in group:
            length += len(word)
        margin = (maxWidth - length) // (len(group) - 1)
        extra = (maxWidth - length) % (len(group) - 1)
        words_with_blanks = [group[i] + (margin + 1) * ' ' if i < extra else group[i] + margin * ' ' for i in range(len(group) - 1)]
        words_with_blanks.append(group[-1])
        return ''.join(words_with_blanks)

    
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        groups = self.divide_groups(words, maxWidth)
        result: List[str] = []
        for group in groups[:-1]:
            if len(group) == 1:
                result.append(group[0] + ' ' * (maxWidth - len(group[0])))
            else:
                result.append(self.transfer_str(group, maxWidth))
        
        length, n = 0, 0
        for string in groups[-1]:
            n += 1
            length += len(string) if n == 1 else len(string) + 1
        rest_blanks = maxWidth - length
        last_str = ' '.join(groups[-1]) + rest_blanks * ' '
        result.append(last_str)
        return result
        