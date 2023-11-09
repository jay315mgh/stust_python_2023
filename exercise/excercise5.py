#建立外部函數
def outer_fun(a, b):
    #建立加法函數
    def addition(a, b):
        return a + b
    #在原有式子上在加5
    add = addition(a, b)
    return add + 5

result = outer_fun(4, 7)
print(result)   