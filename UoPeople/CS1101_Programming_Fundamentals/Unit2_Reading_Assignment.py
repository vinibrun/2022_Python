
print (8**(-1))

def right_justify(s):
    print((70-len(s))*' '+s)

right_justify('yohohooooooooooooooooooo')
right_justify('yohohoooooo')

def do_twice(f,a):
    f(a)
    f(a)

def do_twice_no_args(f):
    f()
    f()

def print_spam(spam):
    print(spam)

do_twice(print_spam,"Spam")

def do_four(func,arg):
    do_twice(func,arg)
    do_twice(func,arg)

def do_four_no_args(func):
    do_twice_no_args(func)
    do_twice_no_args(func)

do_four(print_spam,'batata')


def print_head_unit():
    print('+ - - - - ', end="")

def print_head_finisher():
    print('+')

def print_body_unit():
    print('|         ', end="")

def print_body_finisher():
    print('|')

def print_head_4():
    do_four_no_args(print_head_unit)
    print_head_finisher()

def print_body_4():
    do_four_no_args(print_body_unit)
    print_body_finisher()

def print_row_4():
    print_head_4()
    do_four_no_args(print_body_4)

def print_foot_4():
    print_head_4()

def print_grid_4x4():
    do_four_no_args(print_row_4)
    print_foot_4()

print_grid_4x4()
