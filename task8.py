def brackets_evaluation(s):
    open_brackets = 0
    closed_brackets = 0
    # цикл в котором перебираются скобки, и добавляются в свои переменные
    for char in s:
        if char == '(':
            open_brackets += 1
        elif char == ')':
            closed_brackets += 1

    score = min(open_brackets, closed_brackets)
    return score


print(brackets_evaluation("()"))
print(brackets_evaluation("(())"))
print(brackets_evaluation("()))"))