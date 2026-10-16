class Node:
    def __init__(self, value):
        self.value = value  # 0-9 для операндов, -1..-5 для операций
        self.left = None
        self.right = None

def build_tree(postfix_expr):
    stack = []
    for token in postfix_expr:
        if token.isdigit():
            stack.append(Node(int(token)))
        else:
            # Кодируем операторы числами от -1 до -5
            op_map = {'+': -1, '-': -2, '*': -3, '/': -4, '%': -5}
            op = op_map[token]
            right = stack.pop()
            left = stack.pop()
            node = Node(op)
            node.left = left
            node.right = right
            stack.append(node)
    return stack[0] if stack else None

def remove_multiplication(root):
    if root is None:
        return None

    if root.value < 0:  # Оператор
        if root.value == -3:  # Умножение
            left_val = evaluate_node(root.left)
            right_val = evaluate_node(root.right)
            root.value = left_val * right_val
            root.left = None
            root.right = None
        else:
            root.left = remove_multiplication(root.left)
            root.right = remove_multiplication(root.right)
    return root

def evaluate_node(node):
    if node is None:
        return 0
    if node.value >= 0:  # Число
        return node.value
    # Операции кодированы отрицательными числами
    left_val = evaluate_node(node.left)
    right_val = evaluate_node(node.right)
    if node.value == -1:  # +
        return left_val + right_val
    elif node.value == -2:  # -
        return left_val - right_val
    elif node.value == -3:  # *
        return left_val * right_val
    elif node.value == -4:  # /
        return left_val // right_val
    elif node.value == -5:  # %
        return left_val % right_val
    else:
        return 0

def read_postfix_file(filename):
    with open(filename, 'r') as file:
        return file.read().strip().split()

def transform_expression(filename):
    postfix = read_postfix_file(filename)
    root = build_tree(postfix)
    if root:
        remove_multiplication(root)
    return root

# Пример использования
filename = 'example.txt'
root = transform_expression(filename)
print("Корень преобразованного дерева:", root.value if root else None)
