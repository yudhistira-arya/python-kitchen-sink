# global
global_variable = "this is global"
print(f"global variable: {global_variable}")

if True:
    # still global
    global_variable = "still global"

print(f"after if: {global_variable}")


def my_function(c):
    # local scope
    global_variable = c
    print(f"Inside local function:  {global_variable}")


def my_function2():
    # global_variable is not overidden
    print(f"inside local function: {global_variable}")


def change_global():
    global global_variable  # bad practice
    global_variable = "I modify global"


print(f"global_variable: {global_variable}")
my_function("banana")
my_function2()
change_global()
print(f"global_variable after calling change_global: {global_variable}")


def non_local():
    x = "b"

    def inner():
        nonlocal x
        x = "c"
        print(f"inner: {x}")

    inner()
    print(f"outer: {x}")


non_local()

if __name__ == '__main__':
    pass
