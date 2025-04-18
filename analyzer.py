import ast

def analyze_python_code(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    total_lines = len(lines)
    comment_lines = sum(1 for line in lines if line.strip().startswith("#"))

    with open(file_path, 'r') as f:
        tree = ast.parse(f.read())

    functions = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    longest_func = max(functions, key=lambda f: f.end_lineno - f.lineno, default=None)
    longest_name = longest_func.name if longest_func else "N/A"
    longest_len = (longest_func.end_lineno - longest_func.lineno + 1) if longest_func else 0

    print(f"\nAnalyzing: {file_path}")
    print(f"Total lines: {total_lines}")
    print(f"Comment lines: {comment_lines}")
    print(f"Number of functions: {len(functions)}")
    print(f"Code to comment ratio: {round(comment_lines / total_lines * 100, 2)}%")
    print(f"Longest function: {longest_name} ({longest_len} lines)")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python analyzer.py <file.py>")
    else:
        analyze_python_code(sys.argv[1])
