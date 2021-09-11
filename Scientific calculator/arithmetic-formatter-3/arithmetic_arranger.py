import re


def arithmetic_arranger(problems, solve=False):
    # check problem list
    first = ""
    second = ""
    sumx = ""
    lines = ""
    arranged_problems=""
    # maximal problems is 5
    if len(problems) > 5:
      return "Error: Too many problems."
    # split problem to separate components
    for prob in problems:
      if(re.search("[^\s0-9.+-]", prob)):
        if(re.search("[/]", prob) or re.search("[*]", prob)):
          return "Error: Operator must be '+' or '-'."
        return "Error: Numbers must only contain digits."
      a = prob.split()
      firsts = a[0]
      seconds = a[2]
      operands = a[1]
        # check the length of the number, max 4 digits
      sums=""
      if (len(firsts) > 4 or len(seconds) > 4):
        return "Error: Numbers cannot be more than four digits."
      if (operands == '+'):
        sums = str(int(firsts) + int(seconds))
      if operands == "-":
        sums = str(int(firsts) - int(seconds))
      # set length of sum and top, bottom and line values
      length = max(len(firsts), len(seconds)) + 2
      top = str(firsts).rjust(length)
      bottom = operands + str(seconds).rjust(length - 1)
      line = ""
      res = str(sums).rjust(length)
      for s in range(length):
        line += "-"
       # add to the overall string
      if prob !=problems[-1]:
        first += top + '    '
        second += bottom + '    '
        lines += line + '    '
        sumx += res + '    '
      else:
        first += top
        second += bottom
        lines += line
        sumx += res 
            
          # strip out spaces to the right of the string
    if solve:
      sumx.rstrip()
      arranged_problems = first + '\n' + second + '\n' + lines + '\n' + sumx
    else:
      arranged_problems = first + '\n' + second + '\n' + lines
    return arranged_problems  