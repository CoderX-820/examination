def check_brackets(strings):
    outputs = []  

    for s in strings:
        stack = []  
        marks = [" "] * len(s)  
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i) 
            elif char == ')':
                if stack:
                    stack.pop()  
                else:
                    marks[i] = '?' 

        for idx in stack:
            marks[idx] = 'x'
        
        marked_string = "\n".join([s, "".join(marks)])
        outputs.append(marked_string)

    return outputs


test_strings = [
    "bge)))))))))",
    "((IIII))))))",
    "()()()()(uuu",
    "))))UUUU((()"
]

for output in check_brackets(test_strings):
    print(output)
    print()  