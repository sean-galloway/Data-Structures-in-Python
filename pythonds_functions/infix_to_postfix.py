from pythonds.basic import Stack
import string

def infix_to_postfix(infix_expr):
    '''
    ###############################################################################\n
    # Infix to Postfix Converter\n
    ###############################################################################\n
    '''
    # set up the precedent dictionary
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    # define the stack and the token list
    op_stack = Stack()
    postfix_list = []

    token_list = infix_expr.split()

    # Loop thru the tokens and convert to postfix
    for token in token_list:
        if token in string.ascii_uppercase:
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    return " ".join(postfix_list)
