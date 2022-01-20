pracdata="""[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

data = [[c for c in l] for l in data.split("\n")]

matchers ={}
matchers['['] = ']'
matchers['('] = ')'
matchers['{'] = '}'
matchers['<'] = '>'
paren_err = 0
brack_err = 0
curly_err = 0
angle_err = 0

my_tot=[]
for l in data:
    err = 0
    stack = []
    for c in l:
        if c in matchers.keys():
            stack.append(c)
        else:
            if matchers[stack[-1]] == c:
                stack.pop()
                continue
            else:
                #print("Expected",matchers[stack[-1]])
                #print("Instead found",c)
                #if c==')':
                #    paren_err+=1
                #if c==']':
                #    brack_err+=1
                #if c=='}':
                #    curly_err+=1
                #if c=='>':
                #    angle_err+=1
                err = 1
                break

    if err==0:
        tot=0
        for e in stack[::-1]:
            tot*=5
            if e=='(': tot +=1
            if e=='[': tot +=2
            if e=='{': tot+=3
            if e=='<': tot+=4
        my_tot.append(tot)

my_tot = sorted(my_tot)
print(my_tot)
print(my_tot[int(len(my_tot)/2)])
        
#tot = (paren_err *3) + (brack_err*57) + (curly_err*1197) + (angle_err*25137)

