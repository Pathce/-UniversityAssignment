from Scanner import Scanner

# 프로그램 로드
f = open("TestProgram.smt", 'r')
target_file = f.readlines()
terminal_dict = {
            "package": 0,    "is": 1, "begin": 2,  "end": 3,    "write": 4,
            ":=": 5,
            "+": 6,          "-": 7,  "*": 8,     "/": 9,
            "(": 10,          ")": 11,
            ";": 12,
            "ID": 13,
            "INTLIT": 14,
            "$": 15
        }
non_terminal_dict = {
    "<program>": 16, "<block>": 17, "<statement_list>": 18, "<statement_tail>": 19, "<statement>": 20,
    "<assignment>": 21, "<io_statement>": 22, "<expression_prime>": 23, "<expression>": 24, "<term>": 25,
    "<term_prime>": 26, "<factor>": 27, "<add_op>": 28, "<multiply_op>": 29
}

# -1 == acc
parsing_table = [
    #action : 0 ~ 15
    #goto : 16 ~ 29
    #
    #reduce : -2 ~ -23
    #acc : -1
    #
    #        0       1       2       3       4       5       6       7       8       9       10      11      12      13      14      15      16      17      18      19      20      21      22      23      24      25      26      27      28      29
    #        pack    is      begin   end     write   :=      +       -       *       /       (       )       ;       ID      INT     $       <pro>   <b>     <s_l>   <s_t>   <st>    <ass>   <io>    <e_p>   <e>     <t>     <t-p>   <f>     <add>   <mul>
            [2,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      1,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
            [0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,     -1,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
            [0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      3,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
            [0,      4,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
            [0,      0,      6,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      5,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
            [0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,     -2,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
            [0,      0,      0,      0,     12,      0,      0,      0,      0,      0,      0,      0,      0,     11,      0,      0,      0,      0,      7,      0,      8,      9,     10,      0,      0,      0,      0,      0,      0,      0],
            [0,      0,      0,     13,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
            [0,      0,      0,      0,     12,      0,      0,      0,      0,      0,      0,      0,      0,     11,      0,      0,      0,      0,      0,     15,     16,      9,     10,      0,      0,      0,      0,      0,      0,      0],
            [0,      0,      0,      0,     -7,      0,      0,      0,      0,      0,      0,      0,      0,     -7,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
    #        pack    is      begin   end     write   :=      +       -       *       /       (       )       ;       ID      INT     $       <pro>   <b>     <s_l>   <s_t>   <st>    <ass>   <io>    <e_p>   <e>     <t>     <t-p>   <f>     <add>   <mul>'''
            [0,      0,      0,     -8,     -8,      0,      0,      0,      0,      0,      0,      0,      0,     -8,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
            [0,      0,      0,      0,      0,     17,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
            [0,      0,      0,      0,      0,      0,      0,      0,      0,      0,     18,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
            [0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,     14,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
            [0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,     -3,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
            [0,      0,      0,     -4,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
            [0,      0,      0,     -6,     12,      0,      0,      0,      0,      0,      0,      0,      0,     11,      0,      0,      0,      0,      0,     43,     16,      9,     10,      0,      0,      0,      0,      0,      0,      0],
            [0,      0,      0,      0,      0,      0,      0,      0,      0,      0,     25,      0,      0,     22,     23,      0,      0,      0,      0,      0,      0,      0,      0,      0,     19,     24,      0,     21,      0,      0],
            [0,      0,      0,      0,      0,      0,      0,      0,      0,      0,     25,      0,      0,     22,     23,      0,      0,      0,      0,      0,      0,      0,      0,      0,     26,     24,      0,     21,      0,      0],
            [0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,     20,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
    #        pack    is      begin   end     write   :=      +       -       *       /       (       )       ;       ID      INT     $       <pro>   <b>     <s_l>   <s_t>   <st>    <ass>   <io>    <e_p>   <e>     <t>     <t-p>   <f>     <add>   <mul>'''
            [0,      0,      0,      0,     -9,      0,      0,      0,      0,      0,      0,      0,      0,     -9,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
            [0,      0,      0,      0,      0,      0,    -16,    -16,     38,     39,      0,    -16,    -16,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,     37,      0,      0,     40],
            [0,      0,      0,      0,      0,      0,    -17,    -17,    -17,    -17,      0,    -17,    -17,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
            [0,      0,      0,      0,      0,      0,    -18,    -18,    -18,    -18,      0,    -18,    -18,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
            [0,      0,      0,      0,      0,      0,     35,     36,      0,      0,      0,    -13,    -13,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,     31,      0,      0,      0,      0,     32,      0],
            [0,      0,      0,      0,      0,      0,      0,      0,      0,      0,     25,      0,      0,     22,     23,      0,      0,      0,      0,      0,      0,      0,      0,      0,     29,     24,      0,     21,      0,      0],
            [0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,     27,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
            [0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,     28,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
            [0,      0,      0,    -10,    -10,      0,      0,      0,      0,      0,      0,      0,      0,    -10,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
            [0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,     30,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
    #        pack    is      begin   end     write   :=      +       -       *       /       (       )       ;       ID      INT     $       <pro>   <b>     <s_l>   <s_t>   <st>    <ass>   <io>    <e_p>   <e>     <t>     <t-p>   <f>     <add>   <mul>'''
            [0,      0,      0,      0,      0,      0,    -19,    -19,    -19,    -19,      0,    -19,    -19,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
            [0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,    -11,    -11,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
            [0,      0,      0,      0,      0,      0,      0,      0,      0,      0,     25,      0,      0,     22,     23,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,     33,      0,     21,      0,      0],
            [0,      0,      0,      0,      0,      0,     35,     36,      0,      0,      0,    -13,    -13,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,     34,      0,      0,      0,      0,     32,      0],
            [0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,    -12,    -12,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
            [0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,    -20,    -20,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
            [0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,    -21,    -21,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
            [0,      0,      0,      0,      0,      0,    -14,    -14,      0,      0,      0,    -14,    -14,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
            [0,      0,      0,      0,      0,      0,      0,      0,      0,      0,    -22,      0,      0,    -22,    -22,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
            [0,      0,      0,      0,      0,      0,      0,      0,      0,      0,    -23,      0,      0,    -23,    -23,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
    #        pack    is      begin   end     write   :=      +       -       *       /       (       )       ;       ID      INT     $       <pro>   <b>     <s_l>   <s_t>   <st>    <ass>   <io>    <e_p>   <e>     <t>     <t-p>   <f>     <add>   <mul>'''
            [0,      0,      0,      0,      0,      0,      0,      0,      0,      0,     25,      0,      0,     22,     23,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,     41,      0,      0],
            [0,      0,      0,      0,      0,      0,    -16,    -16,     38,     39,      0,    -16,    -16,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,     42,      0,      0,     40],
            [0,      0,      0,      0,      0,      0,    -15,    -15,      0,      0,      0,    -15,    -15,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
            [0,      0,      0,     -5,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0],
]


    #0       1       2       3       4       5       6       7       8       9       10      11      12      13      14      15
    #pack    is      begin   end     write   :=      +       -       *       /       (       )       ;       ID      INT     $
def shiftState(stack, input, cur_action):
    stack.append(input[0][0])
    stack.append(cur_action)
    del input[0]
    return stack, input

def gotoState(stack, p_table):
    stack.append(p_table[stack[-2]][stack[-1]])
    return stack

    #16      17      18      19      20      21      22      23      24      25      26      27      28      29
    #<pro>   <b>     <s_l>   <s_t>   <st>    <ass>   <io>    <e_p>   <e>     <t>     <t-p>   <f>     <add>   <mul>
def reduceToken(stack, cur_action):
    if cur_action == -2:
        del stack[-8:]
        stack.append(16)
        return stack
    if cur_action == -3:
        del stack[-8:]
        stack.append(17)
        return stack
    if cur_action == -4:
        del stack[-4:]
        stack.append(18)
        return stack
    # 16      17      18      19      20      21      22      23      24      25      26      27      28      29
    # <pro>   <b>     <s_l>   <s_t>   <st>    <ass>   <io>    <e_p>   <e>     <t>     <t-p>   <f>     <add>   <mul>
    if cur_action == -5:
        del stack[-4:]
        stack.append(19)
        return stack
    if cur_action == -6:
        stack.append(19)
        return stack
    if cur_action == -7:
        del stack[-2:]
        stack.append(20)
        return stack
    if cur_action == -8:
        del stack[-2:]
        stack.append(20)
        return stack
    # 16      17      18      19      20      21      22      23      24      25      26      27      28      29
    # <pro>   <b>     <s_l>   <s_t>   <st>    <ass>   <io>    <e_p>   <e>     <t>     <t-p>   <f>     <add>   <mul>
    if cur_action == -9:
        del stack[-8:]
        stack.append(21)
        return stack
    if cur_action == -10:
        del stack[-10:]
        stack.append(22)
        return stack
    if cur_action == -11:
        del stack[-4:]
        stack.append(24)
        return stack
    if cur_action == -12:
        del stack[-6:]
        stack.append(23)
        return stack
    # 16      17      18      19      20      21      22      23      24      25      26      27      28      29
    # <pro>   <b>     <s_l>   <s_t>   <st>    <ass>   <io>    <e_p>   <e>     <t>     <t-p>   <f>     <add>   <mul>
    if cur_action == -13:
        stack.append(23)
        return stack
    if cur_action == -14:
        del stack[-4:]
        stack.append(25)
        return stack
    if cur_action == -15:
        del stack[-6:]
        stack.append(26)
        return stack
    if cur_action == -16:
        stack.append(26)
        return stack
    # 16      17      18      19      20      21      22      23      24      25      26      27      28      29
    # <pro>   <b>     <s_l>   <s_t>   <st>    <ass>   <io>    <e_p>   <e>     <t>     <t-p>   <f>     <add>   <mul>
    if cur_action == -17:
        del stack[-2:]
        stack.append(27)
        return stack
    if cur_action == -18:
        del stack[-2:]
        stack.append(27)
        return stack
    if cur_action == -19:
        del stack[-6:]
        stack.append(27)
        return stack
    if cur_action == -20:
        del stack[-2:]
        stack.append(28)
        return stack
    # 16      17      18      19      20      21      22      23      24      25      26      27      28      29
    # <pro>   <b>     <s_l>   <s_t>   <st>    <ass>   <io>    <e_p>   <e>     <t>     <t-p>   <f>     <add>   <mul>
    if cur_action == -21:
        del stack[-2:]
        stack.append(28)
        return stack
    if cur_action == -22:
        del stack[-2:]
        stack.append(29)
        return stack
    if cur_action == -23:
        del stack[-2:]
        stack.append(29)
        return stack

p_stack = [0]
right_parse = []

if __name__ == '__main__':
    sc = Scanner(target_file)
    p_input = sc.scanFile()
    current_action = 0
    cnt = 0
    print(p_input)
    while(current_action != -1):
        cnt += 1
        state = p_stack[-1]
        in_put = p_input[0][0]
        current_action = parsing_table[state][in_put]
        print(f"p_stack : {p_stack}")
        print(f"p_input : {p_input[0][0]}")
        print(f"input : {p_input[0]}")
        if current_action > 0 and p_input[0][0] < 16:
            print(f"shift{current_action}")
            p_stack, p_input = shiftState(p_stack, p_input, current_action)
        elif current_action < 0:
            print(f"reduce{current_action}")
            p_stack = reduceToken(p_stack, current_action)
            if current_action != -1:
                right_parse.append(p_stack[-1])
            if p_stack:
                print(f"goto{parsing_table[p_stack[-2]][p_stack[-1]]}")
                p_stack = gotoState(p_stack, parsing_table)
        else:
            print("ERROR")
            break
        if cnt == 500:
            print("break")
            break

    if current_action == -1:
        print("accept")

    print(f"right_parse : {right_parse}")
