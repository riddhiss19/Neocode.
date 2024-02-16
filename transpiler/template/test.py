import ast
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

py_code = """
def factorial(n):
  if n == 0: 
    return 1
  else:
    return n * factorial(n-1)

print(factorial(5))
"""

tree = ast.parse(py_code)

def generate_comment(node):
  if isinstance(node, ast.FunctionDef):
    tokens = word_tokenize(node.name)
    comment = "This function {} calculates {}".format(node.name, " ".join(tokens))
    print(comment)
  elif isinstance(node, ast.If):
    tokens = word_tokenize(ast.get_source_segment(py_code, node))
    filtered = [w for w in tokens if w.lower() not in stopwords.words('english')]
    comment = "This checks if {}".format(" ".join(filtered))
    print(comment)

for node in ast.walk(tree):
  generate_comment(node)