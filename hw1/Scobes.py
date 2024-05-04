def is_correct_brackets_seq(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

print(is_correct_brackets_seq('())(()'))