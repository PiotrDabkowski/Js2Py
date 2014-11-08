
class BracketParser:
    def __init__(self, source):
        self.source = source
        
    def bracket_iter(self, brackets=('()','{}','[]')):
        starts = [e[0] for e in brackets]
        in_bracket = 0
        n = 0
        while n<len(self.source):
            e = self.source[n]
            if not in_bracket and e in starts:
                in_bracket = 1
                start = n
                b_start, b_end = brackets[starts.index(e)]
            elif in_bracket:
                if e==b_start:
                    in_bracket += 1
                elif e==b_end:
                    in_bracket -= 1
                    if not in_bracket:
                        yield self.source[start:n+1]
            n+=1
            
    
    
