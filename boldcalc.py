import re


def bold_calc(expression_string):
    if expression_string[0] == '#':
        return None

    *variable, expression = expression_string.split("=")

    if len(variable) > 1:
        return "Syntax error"

    if variable and not variable[0].isidentifier():
        return "Assignment error"

    if re.search(r"(?://)|(?:\*\*)|(?:\w\()|(?:\b\d+[_A-Za-z])", expression):
        return "Syntax error"

    try:
        ans = eval(re.sub(r"([A-Za-z_]\w*)", r"_\1", expression).replace("/", "//"), bold_calc.variables)
    except NameError:
        return "Name error"
    except BaseException:
        return "Runtime error"

    if not isinstance(ans, int):
        return "Syntax error"

    if variable:
        bold_calc.variables["_" + variable[0]] = ans
        return None

    return ans


bold_calc.variables = {}
while s := input().replace(' ', ''):
    if (res := bold_calc(s)) is not None:
        print(res)