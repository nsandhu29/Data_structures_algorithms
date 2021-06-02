import stack_class as sc

string = "gninrael nIdekniL htiw tol a nrael"
reversed_string = ''
s = sc.Stack()

for char in string:
    s.push(char)

while not s.is_empty():
    reversed_string += s.pop()

print(reversed_string)