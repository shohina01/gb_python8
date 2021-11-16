class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Enter only numbers: '))
                self.my_list.append(val)
                print(f'Current list - {self.my_list} \n ')
            except:
                print(f"Not a number")
                y_or_n = input(f'Try again? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                 elif y_or_n == 'N' or y_or_n == 'n':
                    return 'the end'


try_except = Error(1)
print(try_except.my_input())
