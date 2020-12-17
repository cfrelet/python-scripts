def new_decorator(func):
    def wrap_func():
        print("some code before exe func")
        func()
        print("some code after exe func")
    return wrap_func

@new_decorator
def func_need_deco():
    print("please decorate me!")

func_need_deco()


