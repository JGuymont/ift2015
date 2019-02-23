from stack import ListStack, ArrayStack

class ArithmeticExpression:
    
    def __init__(self, trace):
        self.trace = trace
        self.digit_stack = ArrayStack()
        self.op_stack = ListStack()
    
    def _priority(self, op):
        if op in '*/':
            return 2
        elif op in '+-':
            return 1
        return 0

    def _evaluate(self, x, y, op):
        if op == '+':
            return int(y) + int(x)
        elif op == '-':
            return int(y) - int(x)
        elif op == '*':
            return int(y) * int(x)
        elif op == "/":
            if int(x) is not 0:
                return int(y) / int(x)
            else:
                exit("Division by 0, no result!")

    def doOp(self):
        """Effectue une opération de 2 valeurs et empile le résultat"""
        op = self.op_stack.pop()
        x = self.digit_stack.pop()
        y = self.digit_stack.pop()
        if self.trace: print( " doOp(", x, " ", op, " ", y, " )")
        z = self._evaluate(x, y, op)
        self.digit_stack.push(z)
        if self.trace:
            print(" empile le résultat", self.digit_stack)

    def repeat_ops(self, next_op):
        """effectue les opérations (gauche à droite) de même priority"""
        if self.trace: print( " repeatOps..." )
        while len(self.digit_stack) > 1 and self._priority(next_op) <= self._priority(self.op_stack.top()):
            self.doOp()

    def evaluate_expression(self, expr):
        """Evaluate expression
        V = []
        Op  = []
        For z in expr:
        1) If z is digit, add z at the end of V
        2) If z is an operation, 

        example: 2 * 5

        - 
        
        """
        if self.trace: print(' \nEvaluating expression: {}'.format(expr))
        for z in expr:
            if z.isdigit(): 
                self.digit_stack.push(z)
                if self.trace: print( " Chiffre dans la pile: {}".format(self.digit_stack))
            elif z in "+-*/":
                if self.trace: print(" opération lue: {}".format(z))
                self.repeat_ops(z)
                self.op_stack.push(z)
                if self.trace: print(" opération dans la pile: {}".format(self.op_stack))
        self.repeat_ops('$')
        return self.digit_stack.top()

if __name__ == '__main__':
    arithmetic_expr = ArithmeticExpression(True)
    arithmetic_expr.evaluate_expression('2*5+6/2-4*2')
    
    
    