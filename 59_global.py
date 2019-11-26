'''
グローバルとローカル

messsage変数はdef print_message()の中でしか使うことができない。
グローバルで使うには global message と宣言が必要

'''



def print_message():
    # the variable 'message' is local to the function itself

    global message
    # now message has become global function

    message = "Hello I'm going to bangalore"
    return message

print(print_message())

print(message)