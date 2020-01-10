from print_tree import pretty_print


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        # 0表示黑 1表示红
        self.color = 1


def left_rotate(node: Node):
    # 左旋
    a = node
    c = node.right
    f = c.left
    c.left = a
    c.parent = a.parent
    a.parent = c
    a.right = f
    if f:
        f.parent = a
    if c.parent:
        if c.parent.left == a:
            c.parent.left = c
        else:
            c.parent.right = c
    else:
        # 若左旋后c为头节点则返回新的头节点
        return c


def right_rotate(node: Node):
    # 右旋
    a = node
    b = node.left
    e = b.right
    b.parent = a.parent
    b.right = a
    a.parent = b
    a.left = e
    if e:
        e.parent = a
    if b.parent:
        if b.parent.left == a:
            b.parent.left = b
        else:
            b.parent.right = b
    else:
        # 若右旋后b为头节点则返回新的头节点
        return b


def get_uncle(node: Node):
    # 获取叔叔节点
    if node.parent.parent.left == node.parent:
        uncle = node.parent.parent.right
    else:
        uncle = node.parent.parent.left
    return uncle


def is_left_node(node: Node):
    # 判断是否为父节点的左子节点
    return node.parent.left == node


def find_rule(node: Node):
    # 判断规则
    if not node.parent:
        return rule1
    if node.parent.color == 0:
        return rule2
    uncle = get_uncle(node)
    if uncle and uncle.color == 1:
        return rule3
    if is_left_node(node.parent):
        if not is_left_node(node):
            return rule4
        else:
            return rule5
    else:
        if is_left_node(node):
            return rule4
        else:
            return rule5


def rule1(node: Node, head: Node):
    node.color = 0
    return head


def rule2(node: Node, head: Node):
    return head


def rule3(node: Node, head: Node):
    uncle = get_uncle(node)
    node.parent.color = 0
    uncle.color = 0
    node.parent.parent.color = 1
    return adjust(node.parent.parent, head)


def rule4(node: Node, head: Node):
    if not is_left_node(node):
        left_rotate(node.parent)
        return rule5(node.left, head)
    else:
        right_rotate(node.parent)
        return rule5(node.right, head)


def rule5(node: Node, head: Node):
    node.parent.color = 0
    node.parent.parent.color = 1
    if is_left_node(node):
        temp = right_rotate(node.parent.parent)
    else:
        temp = left_rotate(node.parent.parent)
    if temp:
        return temp
    return head


def adjust(node: Node, head: Node):
    # 调整红黑树
    rule = find_rule(node)
    return rule(node, head)


def insert_red_color_node(head: Node, node: Node):
    # 先以红色插入节点
    front = head
    temp = head
    while temp:
        front = temp
        if node.val > temp.val:
            temp = temp.right
        elif node.val < temp.val:
            temp = temp.left
        else:
            raise ValueError('you have insert repeat value node')
    if node.val > front.val:
        front.right = node
    else:
        front.left = node
    node.parent = front
    return node


def insert(head: Node, val):
    # 红黑树插入
    node = Node(val)
    if not head:
        head = node
        return adjust(node, head)
    else:
        node = insert_red_color_node(head, node)
    return adjust(node, head)


if __name__ == '__main__':
    head = None
    nums = [2, 8, 12, 5, 4, 6, 1, 7, 15, 13]
    for num in nums:
        head = insert(head, num)
    pretty_print(head)

