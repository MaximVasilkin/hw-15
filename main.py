from Stack import Stack


def brackets_balance(brackets_in):
    stack = Stack()
    bracket_dict = {'(': ')', '[': ']', '{': '}'}
    message = 'Дисбаланс'
    for bracket in brackets_in:
        if bracket in bracket_dict:
            stack.push(bracket)
        elif bracket not in bracket_dict and not stack.IsEmpty():
            deleted_bracket = stack.pop()
            if bracket != bracket_dict[deleted_bracket]:
                print(message)
                break
        elif stack.IsEmpty():
            print(message)
            break
    else:
        print('Сбалансированно')


if __name__ == '__main__':
    data = ('(((([{}]))))',
            '[([])((([[[]]])))]{()}',
            '{{[()]}}',
            '}{}',
            '{{[(])]}}',
            '[[{())}]')
    for item in data:
        brackets_balance(item)
