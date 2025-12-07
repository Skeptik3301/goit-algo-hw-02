def check_symmetry(expression):
    """
    Перевіряє симетричність дужок у виразі.
    """
    stack = []
    matching_brackets = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        
        if char in "({[":
            stack.append(char)
        
       
        elif char in ")}]":
          
            if not stack or stack.pop() != matching_brackets[char]:
                return "Несиметрично"
    
   
    if not stack:
        return "Симетрично"
    else:
        return "Несиметрично"


if __name__ == "__main__":
    expressions = [
        "( ){[ 1 ]( 1 + 3 )( ){ }}:",
        "( 23 ( 2 - 3);",
        "{ 11 }",
        "123(4  442d)WOW"
    ]

    for expr in expressions:
        print(f"'{expr}': {check_symmetry(expr)}")