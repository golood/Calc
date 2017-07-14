import math          

def arifm(s):
    """Метод для реализации грамматики арифметических выражений

    Реализована следующая грамматика:
                    -> expr  : term | (term) | expr + term |  expr + term
                       term  : -(expr) | number | term * number | term / number
                       number: [0-9] | expr

    """
    return expr(s)

def expr(s):
    i = 0
    if s[0] in '(' and s[len(s)-1] == ')':
        return term(s[1:len(s)-1])
    for ch in index(len(s)):
        if s[ch] in ')':
            i += 1
        if s[ch] in '(':
            i -= 1
        if s[ch] in ['-', '+']:
            if i == 0:
                if s[ch] in '-':
                    if len(s[:ch]) != 0:
                        return expr(s[:ch]) - term(s[ch+1:])
                if s[ch] in '+':
                    return expr(s[:ch]) + term(s[ch+1:])
    return term(s)
          
def term(s):
    i = 0

    if s[0] in '-':
        if s[1] in '(' and s[len(s)-1] == ')':
            return -expr(s[2:len(s)-1])
    
    for ch in index(len(s)):
        if s[ch] in ')':
            i += 1
        if s[ch] in '(':
            i -= 1
        if s[ch] in ['*', '/']:
            if i == 0:
                if s[ch] in '*':
                    return term(s[:ch]) * number(s[ch+1:])
                if s[ch] in '/':
                    try: 
                        ans =  term(s[:ch]) / number(s[ch+1:])
                    except ZeroDivisionError:
                        return 0
                    else:
                        return ans          
    return number(s)

def number(s):
    if s[0] == '-':
        if s[1:].isdigit():
            return float(s)
    if s.isdigit():
        return float(s)
    else:
        return expr(s)

def index(n):
    """Итератор для обхода строки с права на лево"""
    i = n - 1
    while i >= 0:
        yield i
        i -= 1
            
def hello():
    s = '''Калькулятор.
        Команды:
            help [команда]- выдает справку о команде, если аргумент пустой,
                            то выводит список всех комманд.
            q             - выход
        '''
    return s

def help_(s):
    """Метод обработки комманды help"""
    if s == 'help':
        print(hello())
        return True
    if s == 'help q':
        print('q - Выход из приложения')
        return True
    
def inputStr():
    """Чтение ввода пользователя """
    s = input("Введите выражение: ")
    return s

def main():
    """Управляющий метод"""
    print(hello())
    while True:
        s = inputStr()
        if help_(s):
            continue
        if s == 'q':
            print('Пока!')
            break
        print(arifm(s))
    
        


if __name__ == "__main__":
    main()
