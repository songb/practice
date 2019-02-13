class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ParentTreeNode(object):
    def __init__(self, current, parent):
        self.current = current
        self.parent = parent


def lowestCommonAncestor(root, p, q):
    qu = [ParentTreeNode(root, None)]
    pp = ParentTreeNode(root, None)
    qp = ParentTreeNode(root, None)
    find_p = False
    find_q = False
    while qu and (not find_p or not find_q):
        t = qu.pop(0)
        left_node = t.current.left
        if left_node:
            lnp = ParentTreeNode(left_node, t)
            qu.append(lnp)

            if left_node.val == p.val:
                pp = lnp
                find_p = True

            if left_node.val == q.val:
                qp = lnp
                find_q = True

        right_node = t.current.right
        if right_node:
            rnp = ParentTreeNode(right_node, t)
            qu.append(rnp)

            if right_node.val == p.val:
                pp = rnp
                find_p = True

            if right_node.val == q.val:
                qp = rnp
                find_q = True

    parents = {p.val, q.val}
    pp = pp.parent
    qp = qp.parent

    while pp or qp:
        if pp:
            if pp.current.val in parents:
                return pp.current.val
            parents.add(pp.current.val)
            pp = pp.parent
        if qp:
            if qp.current.val in parents:
                return qp.current.val
            parents.add(qp.current.val)
            qp = qp.parent


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


r = stringToTreeNode("[3,5,1,6,2,0,8,null,null,7,4]")

p = stringToTreeNode("[5]")
q = stringToTreeNode("[1]")
k = lowestCommonAncestor(r, p, q)
print(k)
