def lexer(stin,listdelim=',',tokens={'{':'}','(':')','[':']'}): # opentoken:closetoken pairs for convenience in parsing elsewhere
    '''Aggregates and yields a seq of obj strings and single char (recursive) grouping delimiters.
    Stepwise yield: caseZ an open-, close- or listdelim- (comma) token; or caseY a single obj string from a flat string repr
    For example: '1{23(4,5)6}7' goes to (python wo quotes) list [1,{,23,(,4,5),6,},7] 
    An open token implies a leading comma, a close token implies a trailing comma; mostly to avoid doubled/adjacent char tokens
    Lookahead a single character to determine if an obj string is already complete.
    Shows concise simplicity of generator for logic working with a stream of tokens, avoiding multiple passes (ie. works on infinite streams).
    '''
    partial_obj_tok=''
    for ch in stin:
        if ch ==listdelim or ch in tokens or ch in tokens.values():  
            yield partial_obj_tok #caseY yield a just-prior completed obj string tok
            partial_obj_tok=''
            yield ch  #caseZ: pass other token chars through, 
        else: partial_obj_tok+=ch #adding to a partial obj string, dont yield string until complete

def parse(strit,sofar=None,listdelimtok=',',closetok=None,depth=0,tokens={'{':'}','(':')','[':']'}):
    '''Create a list of lists and string terminals in one pass to follow lexer()
    ExmpC de-serialize iterator, strit of obj(s) or grouping-delimiting token chars
    Validate and modify iterator of objects with grammars like:
        O -> O | opentokOclosetok eg. (O) | {O}
        O -> objecttok,O | objecttok #left recursion, literal comma
        
    CaseZ: opentoken, append a new list and then add elems via parse()  
    CaseY: closetoken, return completed list;
    CaseX: comma, append an elem, parse() rest of list
    CaseW: initial obj string append an elem to a new list, parse() rest of list
    '''
    def trace(n):
        return f'n is .{n}. sofar .{sofar}. depth.{depth}. cltok.{closetok}.'
    if not sofar: sofar=[] # setting a default in signature ow is a single shared instance
    try:
        n=next(strit)
        if n in tokens: #caseZ down a level, push a parse() onto stack
            print('down: ',trace(n))
            sofar.append(parse(strit,closetok=tokens[n],depth=depth+1)) # sofar containerish/elem obj
        elif n==closetok: # caseY up a level, pop a parse() call
            print('up: ',trace(n))
            return sofar
        elif n==listdelimtok: # caseX across, because there is a sbsq obj string append it and parse() along.
            sofar.append(next(strit))
            print('next in a seq ',trace(n))
            parse(strit,sofar,closetok,depth=depth) 
        else: #caseW same as caseX but we dont absorb any initial comma in a list
            sofar.append(n) #sofar == []
            print('first across ',trace(n))
            parse(strit,sofar,closetok,depth=depth) 
    except StopIteration: return sofar # the very top-level null/missing/moot closetoken if no corr opentoken like \0 byte
