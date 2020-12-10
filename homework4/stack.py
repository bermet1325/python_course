def create_stack(s):
    s.items = []

def push(s, item):
    s.items.append(item)

def pop(s):
    return s.items.pop

def isEmpty(s):
    if s == 0:
        print("True")
    else:
        print("False")
    return s



