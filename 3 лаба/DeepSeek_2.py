#FIXME: Docstring
#FIXME: Очевидные комментарии
#TODO:
class Node:
    """
        Конструктор узла дерева.

        :param val: Значение узла (число или код оператора)
        :param left: Левый потомок
        :param right: Правый потомок
        :return: None
        """
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_from_rpn(expression):
    """
    Строит дерево выражения из строки в обратной польской записи.

    :param expression: Строка с выражением в ОПН (токены через пробел)
    :return: Корень построенного дерева или None, если выражение пустое
    """
    stack = []
    for token in expression.split():
        if token.lstrip('-').isdigit():
            stack.append(Node(int(token)))
        else:
            op_map = {'+': -1, '-': -2, '*': -3, '/': -4, '%': -5}
            op = op_map[token]
            right = stack.pop()
            left = stack.pop()
            stack.append(Node(op, left, right))
    return stack[0]


def evaluate_tree(node):
    """
    Рекурсивно вычисляет значение поддерева.

    :param node: Корень поддерева для вычисления
    :return: Числовое значение выражения в поддереве
    """
    if node.val >= 0:  
        return node.val
    
    left_val = evaluate_tree(node.left)
    right_val = evaluate_tree(node.right)
    
    if node.val == -1:  
        return left_val + right_val
    elif node.val == -2: 
        return left_val - right_val
    elif node.val == -3: 
        return left_val * right_val
    elif node.val == -4:  
        return left_val // right_val
    elif node.val == -5:  
        return left_val % right_val


def simplify_tree(node):
    """
    Упрощает дерево, сворачивая поддеревья умножения в листы.

    :param node: Корень поддерева для упрощения
    :return: Новый корень упрощенного поддерева
    """
    if node is None:
        return None
    
    node.left = simplify_tree(node.left)
    node.right = simplify_tree(node.right)
    
    if node.val == -3:
        val = evaluate_tree(node)
        return Node(val)
    
    return node


def read_expression_from_file(filename):
    """
    Читает выражение из текстового файла.

    :param filename: Путь к файлу с выражением
    :return: Строка с выражением в обратной польской записи
    """
    with open(filename, 'r') as f:
        return f.read().strip()


def main():
    """
    Точка входа в программу. Читает файл, строит и упрощает дерево.

    :return: None
    """
    filename = "expression.txt"
    
    expr = read_expression_from_file(filename)
    root = build_tree_from_rpn(expr)
    new_root = simplify_tree(root)
    
    print("Указатель на корень полученного дерева:", new_root)


if __name__ == "__main__":
    main()