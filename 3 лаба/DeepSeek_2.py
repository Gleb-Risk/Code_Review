class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_from_rpn(expression):
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
    if node is None:
        return None
    
    node.left = simplify_tree(node.left)
    node.right = simplify_tree(node.right)
    
    if node.val == -3:
        val = evaluate_tree(node)
        return Node(val)
    
    return node


def read_expression_from_file(filename):
    with open(filename, 'r') as f:
        return f.read().strip()


def main():
    filename = "expression.txt"
    
    expr = read_expression_from_file(filename)
    root = build_tree_from_rpn(expr)
    new_root = simplify_tree(root)
    
    print("Указатель на корень полученного дерева:", new_root)


if __name__ == "__main__":
    main()
