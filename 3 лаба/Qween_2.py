import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def get_op_value(op):
    """Кодирует знак операции согласно условию"""
    if op == '+': return -1
    if op == '-': return -2
    if op == '*': return -3
    if op == '/': return -4
    if op == '%': return -5
    return 0

def evaluate(left_val, right_val, op):
    """Вычисляет результат арифметической операции"""
    if op == -1: return left_val + right_val
    if op == -2: return left_val - right_val
    if op == -3: return left_val * right_val
    if op == -4: return left_val // right_val  # Деление нацело
    if op == -5: return left_val % right_val   # Остаток от деления
    return left_val

def simplify(node):
    """Рекурсивно удаляет операции умножения, заменяя их вычисленным значением"""
    if node is None:
        return None
    
    # Постфиксный обход: сначала обрабатываем дочерние поддеревья
    node.left = simplify(node.left)
    node.right = simplify(node.right)
    
    # Если текущий узел представляет собой умножение (-3)
    if node.value == -3:
        # Вычисляем значение этого поддерева
        result = evaluate(node.left.value, node.right.value, -3)
        
        # Превращаем текущий узел в лист с вычисленным значением
        node.value = result
        node.left = None
        node.right = None
        
    return node

def build_and_simplify_tree(filename):
    """Считывает файл, строит дерево и упрощает его"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            # Разбиваем содержимое файла на токены (числа и операции)
            tokens = f.read().split()
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")
        return None

    stack = []
    for token in tokens:
        if token.isdigit():
            # Если токен - число (от 0 до 9), создаем лист
            stack.append(Node(int(token)))
        else:
            # Если токен - операция
            op_val = get_op_value(token)
            if op_val != 0:
                right_child = stack.pop()
                left_child = stack.pop()
                
                node = Node(op_val)
                node.left = left_child
                node.right = right_child
                stack.append(node)
    
    if not stack:
        return None
        
    root = stack[0]
    
    # Преобразуем дерево, избавляясь от умножений
    root = simplify(root)
    
    return root

if __name__ == "__main__":
    # Имя файла строго по условию задачи
    filename = "filename"
    
    root = build_and_simplify_tree(filename)
    
    if root:
        # В Python аналогом указателя на объект является его id (адрес в памяти)
        print(f"Указатель на корень дерева (id): {id(root)}")
        
        # Дополнительный вывод для проверки (значение в корне и структура)
        print(f"Значение в корне после преобразования: {root.value}")
    else:
        print("Не удалось построить дерево.")