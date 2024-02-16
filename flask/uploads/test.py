import ast
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

py_code = """
def print_pattern(num_rows):
    for i in range(num_rows):
        for num_cols in range(num_rows-i):
            print("*", end="")
        print()
"""

tree = ast.parse(py_code)

def generate_comment(node):
  if isinstance(node, ast.FunctionDef):
    tokens = word_tokenize(node.name)
    comment = "Function: {}() calculates {}".format(node.name, " ".join(tokens))
    print(comment)
  elif isinstance(node, ast.If):
    tokens = word_tokenize(ast.get_source_segment(py_code, node))
    filtered = [w for w in tokens if w.lower() not in stopwords.words('english')]
    comment = "This checks if {}".format(" ".join(filtered))
    print(comment)

for node in ast.walk(tree):
  generate_comment(node)