import re


def js_to_python(js):
    python = js
    # Replace let and const with variable assignments
    python = re.sub(r"let (.*) = (.*);", r"\1 = \2", python)
    python = re.sub(r"const (.*) = (.*);", r"\1 = \2", python)

    # Replace function definition with def
    python = re.sub(r"function (.*)\((.*)\)", r"def \1(\2)", python)

    # Replace return with return
    python = re.sub(r"return (.*);", r"return \1", python)

    python = re.sub(r"prompt", r"input", python)
    python = re.sub(r"parseInt", r"int", python)
    python = re.sub(r"//", r"#", python)
    python = re.sub(r";", r"", python)

    # Replace console.log with print
    python = re.sub(r"console\.log\((.*)\)", r"print(\1)", python)
    # label = False
    lines = python.splitlines()
    counter = 0
    label = False
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        lines[i] = ("    " * counter) + lines[i]
        if "{" in lines[i]:
            lines[i] = re.sub("{", ":", lines[i])
            counter += 1
        if "}" in lines[i]:
            lines[i] = re.sub("}", "", lines[i])
            counter -= 1
        # print(lines[i])

    updatePython = ""
    for i in lines:
        updatePython += i + "\n"

    return updatePython


def indentToNbsp(txt):
    return re.sub(r"\t", r"&nbsp;&nbsp;", txt)
