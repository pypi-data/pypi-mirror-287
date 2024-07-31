__all__ = ['Expression','Suffix_expression','Se','E']
class Expression(object):
    def __init__(self,expression:str):
        self.expression = expression
    def __str__(self):
        return self.expression
class Suffix_expression(object):
    @staticmethod
    def generate_postfix(affix_expression):
        """
        generate postfix expression str
        :param affix_expression: infix expression str, like '2x3+8/3'
        :return: postfix expression str, like '23x83/+'
        """
        if type(affix_expression) is bytes:affix_expression.decode()
        if type(affix_expression) is Expression:affix_expression = str(affix_expression)
        op_rank = {'x': 2, '/': 2, '+': 1, '-': 1}  # 定义加减乘除的优先级
        stack = []  # 用list模拟栈的后进先出
        post_list = []
        for s in affix_expression:
            if s in '+-x/':  # operator
                # 栈不为空，且栈顶运算符的优先级高于当前运算符
                while stack and op_rank.get(stack[-1]) >= op_rank.get(s):  # priority
                    post_list.append(stack.pop())
                stack.append(s)
            else:  # operand
                post_list.append(s)
        while stack:
            post_list.append(stack.pop())
        return Expression(''.join(post_list))
    @staticmethod
    def calculate_postfix(postfix,divide_to_int:bool=False):
        """
        calculate postfix expression
        :param postfix: postfix expression str, like '23x83/+'
        :return: int result, like 2x3+8/3=6+2=8
        """
        if type(postfix) is bytes:postfix.decode()
        if type(postfix) is Expression:postfix = str(postfix)
        stack = []  # 用list模拟栈的后进先出
        for p in postfix:
            if p in '+-x/':  # operator
                value_2 = int(stack.pop())  # 第二个操作数
                value_1 = int(stack.pop())  # 第一个操作数
                if p == '+':
                    result = value_1 + value_2
                elif p == '-':
                    result = value_1 - value_2
                elif p == 'x':
                    result = value_1 * value_2
                else:   # 整除
                    if divide_to_int:
                        result = value_1 // value_2
                    else:
                        result = value_1 / value_2
                stack.append(result)
            else:
                stack.append(p)
        return stack.pop()
Se = Suffix_expression
E = Expression
