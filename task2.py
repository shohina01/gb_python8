class MyException(Exception):
    def __init__(self, text):
        self.text = text


try:
    a = int(input('a:'))
    b = int(input('b:'))
    if b == 0:
        raise MyException('division to zero is not allowed')
    c = a / b
    print(c)

except MyException as e:
    print(e)
