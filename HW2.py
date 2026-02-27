
import csv



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class HomeWork2:

    # Problem 1: Construct an expression tree from a postfix expression
    def constructBinaryTree(self, input) -> TreeNode:
        if not input:
            return None
        stack = []
        operators = {'+', '-', '*', '/'}

        for token in input:
            if token not in operators:

                # The numbers will go into nodes and then will go onto the stack

                stack.append(TreeNode(token))
            else:

                # poping the children, first right and then left

                rightNode = stack.pop()
                leftNode = stack.pop()

                # Creating an operator node and pushing back

                newNode = TreeNode(token, leftNode, rightNode)
                stack.append(newNode)

        return stack[0] if stack else None

    # Problem 2.1: Pre-order traversal (root, left, right)

    def prefixNotationPrint(self, head: TreeNode) -> list:
        if not head:
            return []
        result = [head.val]
        result += self.prefixNotationPrint(head.left)
        result += self.prefixNotationPrint(head.right)

        return result


    # Problem 2.2: In-order traversal (left, root, right)

    def infixNotationPrint(self, head: TreeNode) -> list:
        if not head:
            return []
        if head.left is None and head.right is None:
            return [head.val]

        leftPart = self.infixNotationPrint(head.left)
        rightPart = self.infixNotationPrint(head.right)

        return ['('] + leftPart + [head.val] + rightPart + [')']



    # Problem 2.3: Post-order traversal (left, right, root)

    def postfixNotationPrint(self, head: TreeNode) -> list:
        if not head:
            return []
        result = []
        result += self.postfixNotationPrint(head.left)
        result += self.postfixNotationPrint(head.right)
        result.append(head.val)

        return result

class Stack:



    def __init__(self):
        pass

    def evaluatePostfix(self, exp: str) -> int:
        pass

# Main Function.
if __name__ == "__main__":
    homework2 = HomeWork2()

    print("\nRUNNING TEST CASES FOR PROBLEM 1")
    testcases = []
    try:
        with open('p1_construct_tree.csv', 'r') as f:
            testcases = list(csv.reader(f))
    except FileNotFoundError:
        print("p1_construct_tree.csv not found")

    for i, (postfix_input,) in enumerate(testcases, 1):
        postfix = postfix_input.split(",")
        root = homework2.constructBinaryTree(postfix)
        output = homework2.postfixNotationPrint(root)
        assert output == postfix, f"P1 Test {i} failed"
        print(f"P1 Test {i} passed")

    print("\nRUNNING TEST CASES FOR PROBLEM 2")
    testcases = []
    try:
        with open('p2_traversals.csv', 'r') as f:
            testcases = list(csv.reader(f))
    except FileNotFoundError:
        print("p2_traversals.csv not found")

    for i, row in enumerate(testcases, 1):
        postfix_input, exp_pre, exp_in, exp_post = row
        postfix = postfix_input.split(",")
        root = homework2.constructBinaryTree(postfix)
        assert homework2.prefixNotationPrint(root) == exp_pre.split(","), f"P2-{i} prefix failed"
        assert homework2.infixNotationPrint(root) == exp_in.split(","), f"P2-{i} infix failed"
        assert homework2.postfixNotationPrint(root) == exp_post.split(","), f"P2-{i} postfix failed"
        print(f"P2 Test {i} passed")