class MyClass:
    def used_method(self):
        return 42

    def never_called_method(self):
        return "I am dead code"

    def another_dead_method(self):
        return "also dead"


obj = MyClass()
result = obj.used_method()
print(result)
