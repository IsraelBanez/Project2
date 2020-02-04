from stack_array import Stack

# You should not change this Exception class
class PostfixFormatException(Exception):
    pass

def postfix_eval(input_str):
    """Evaluates a postfix expression"""

    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed"""
    stack_hold = Stack(30)
    operator = ['+', '-', '/', '*', '>>', '<<', '**']
    tokens = input_str.split()
    if len(input_str) == 0:
        raise PostfixFormatException('Insufficient operands')
    for i in tokens:
        if i in operator:
            if stack_hold.size() < 2:
                raise PostfixFormatException('Insufficient operands')
            num2 = stack_hold.pop()
            num1 = stack_hold.pop()
            if i == '+':
                stack_hold.push(float(num1) + float(num2))
            elif i == '-':
                stack_hold.push(float(num1) - float(num2))
            elif i == '*':
                stack_hold.push(float(num1) * float(num2))
            elif i == '/':
                try:
                    stack_hold.push(float(num1) / float(num2))
                except ValueError:
                    raise ZeroDivisionError
            elif i == '**':
                stack_hold.push(float(num1) ** float(num2))
            elif i == '<<':
                try:
                    stack_hold.push(int(num1) << int(num2))
                except ValueError:
                    raise PostfixFormatException('Illegal bit shift operand')
            elif i == '>>':
                try:
                    stack_hold.push(int(num1) >> int(num2))
                except ValueError:
                    raise PostfixFormatException('Illegal bit shift operand')
        elif i not in operator:
            try:
                stack_hold.push(float(i))
            except ValueError:
                raise PostfixFormatException('Invalid token')
    if stack_hold.size() > 1:
        raise PostfixFormatException('Too many operands')
    return stack_hold.pop()

def infix_to_postfix(input_str):
    """Converts an infix expression to an equivalent postfix expression"""

    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression """
    stack_hold = Stack(30)
    tokens = input_str.split()
    precedence = {
        '(': 5,
        ')': 5,
        '+': 4,
        '-': 4,
        '*': 3,
        '/': 3,
        '**': 2,
        '<<': 1,
        '>>': 1}
    stack = []
    if len(input_str) == 0:
        return ''
    for i in range(len(tokens)):
        if numeric(tokens[i]) is True:
            stack.append(tokens[i])
        elif tokens[i] == '(':
            stack_hold.push(tokens[i])
        elif tokens[i] == ')':
            while stack_hold.peek() != '(':
                stack.append(stack_hold.pop())
            stack_hold.pop()
        elif precedence[tokens[i]] == 2:
            for k in range(stack_hold.size()):
                if precedence[stack_hold.items[k]] < precedence[tokens[i]]:
                    stack.append(stack_hold.pop())
                else:
                    break
            stack_hold.push(tokens[i])
        elif tokens[i] in precedence:
            for j in range(stack_hold.size(), 0, -1):
                if precedence[stack_hold.items[j - 1]] <= precedence[tokens[i]]:
                    stack.append(stack_hold.pop())
                else:
                    break
            stack_hold.push(tokens[i])
    while stack_hold.size() > 0:
        stack.append(stack_hold.pop())
    return ' '.join(stack)

def prefix_to_postfix(input_str):
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression(tokens are space separated)"""
    stack_hold = Stack(30)
    tokens = input_str.split()
    if len(input_str) == 0:
        return ''
    for i in range(len(tokens), 0, -1):
        if numeric(tokens[i - 1]) is False:
            first = stack_hold.pop()
            second = stack_hold.pop()
            ad = first + ' ' + second + ' ' + tokens[i - 1]
            stack_hold.push(ad)
        else:
            stack_hold.push(tokens[i - 1])
    return stack_hold.pop()

def numeric(input):
    '''Checks for real numbers including floats and negatives'''
    try:
        float(input)
        return True
    except ValueError:
        return False

if __name__ == "__main__":

    a = '1 + 1 - 2'
    b = infix_to_postfix(a)
    print(b)

    c = '5.5 5 6.6 * +'
    d = postfix_eval(c)
    print(d)

    e = '- / 30 6 4'
    f = prefix_to_postfix(e)
    print(f)

    g = '-25.6'
    h = numeric(g)
    print(h)

    i = 'abc'
    j = numeric(i)
    print(j)
