import re
import math

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f'<{self.type}: {self.value}>'

class MathSyntaxAnalyzer:
    def __init__(self, expression):
        self.expression = expression
        self.input = expression
        self.tokens = self.tokenize()
        self.pos = 0
        self.lookahead = self.next_token()
        self.functions = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan
        }

    def tokenize(self):
        tokens = []
        i = 0
        while i < len(self.input):
            char = self.input[i]

            if char.isspace():
                i += 1
                continue

            if re.match(r'\d', char) or char == '.':
                num_str = ''
                while i < len(self.input) and (re.match(r'\d', self.input[i]) or self.input[i] == '.'):
                    num_str += self.input[i]
                    i += 1
                tokens.append(Token('NUMBER', float(num_str)))
                continue

            if re.match(r'[a-zA-Z]', char):
                func_str = ''
                while i < len(self.input) and re.match(r'[a-zA-Z0-9]', self.input[i]):
                    func_str += self.input[i]
                    i += 1
                tokens.append(Token('IDENTIFIER', func_str))
                continue

            if char in '+-*/%^()':
                tokens.append(Token('OPERATOR', char))
                i += 1
                continue

            if char == ',':
                tokens.append(Token('COMMA', char))
                i += 1
                continue

            self.error(f"Invalid character: {char}")
        tokens.append(Token('EOF', None))
        return tokens

    def next_token(self):
        if self.pos < len(self.tokens):
            token = self.tokens[self.pos]
            self.pos += 1
            return token
        return Token('EOF', None)

    def consume(self, expected_type, expected_value=None):
        if self.lookahead.type == expected_type and (expected_value is None or self.lookahead.value == expected_value):
            token = self.lookahead
            self.lookahead = self.next_token()
            return token
        else:
            self.error(f"Expected {expected_type} {expected_value}, but got {self.lookahead}")

    def error(self, message):
        print(f"Syntax Error: {message} at {self.lookahead}")
        exit(1)

    def E(self):
        result = self.T()
        while self.lookahead.type == 'OPERATOR' and self.lookahead.value in ['+', '-']:
            op = self.consume('OPERATOR').value
            right = self.T()
            if op == '+':
                result += right
            elif op == '-':
                result -= right
        return result

    def T(self):
        result = self.F()
        while self.lookahead.type == 'OPERATOR' and self.lookahead.value in ['*', '/', '%']:
            op = self.consume('OPERATOR').value
            right = self.F()
            if op == '*':
                result *= right
            elif op == '/':
                if right == 0:
                    self.error("Division by zero")
                result /= right
            elif op == '%':
                if right == 0:
                    self.error("Modulus by zero")
                result %= right
        return result

    def F(self):
        result = self.P()
        if self.lookahead.type == 'OPERATOR' and self.lookahead.value == '^':
            self.consume('OPERATOR', '^')
            right = self.F()
            result = result ** right
        return result

    def P(self):
        if self.lookahead.type == 'OPERATOR' and self.lookahead.value == '(':
            self.consume('OPERATOR', '(')
            result = self.E()
            self.consume('OPERATOR', ')')
            return result
        elif self.lookahead.type == 'NUMBER':
            return self.consume('NUMBER').value
        elif self.lookahead.type == 'IDENTIFIER':
            func_name = self.consume('IDENTIFIER').value
            if func_name in self.functions:
                self.consume('OPERATOR', '(')
                arg = self.E()
                self.consume('OPERATOR', ')')
                return self.functions[func_name](arg)
            else:
                self.error(f"Undefined function: {func_name}")
        else:
            self.error("Expected a number, function, or '('")

    def parse(self):
        result = self.E()
        self.consume('EOF')
        return result


if __name__ == "__main__":
    expression = input("Enter a mathematical expression:\n")
    analyzer = MathSyntaxAnalyzer(expression)
    try:
        result = analyzer.parse()
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
