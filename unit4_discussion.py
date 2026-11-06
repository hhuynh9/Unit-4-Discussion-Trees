"""
====================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
====================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student): Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student): Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on whether
          a value is smaller or larger than the current node.
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        if node is None:
            return Node(value)

        # Smaller values go on the left side.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Larger values go on the right side.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Duplicate values are ignored.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Explain why BST search is often more efficient
          than linear search.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        if node is None:
            return False

        if node.value == value:
            return True

        # Only search the side where the value could exist.
        # This avoids checking every node in a balanced tree.
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Explain why this produces sorted output.
        """
        if node is None:
            return

        # Left, root, right produces sorted values in a BST.
        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ========================================
    # TODO (Student): BUILD A TREE
    # ========================================
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values in both subtrees.
    # 4. Display the inserted values.
    # 5. Explain how BSTs reduce search space.

    print("\n=== TREE CONSTRUCTION ===")

    tree = BST()
    employee_ids = [1050, 1025, 1075, 1010, 1035, 1060, 1090, 1005, 1040]

    for employee_id in employee_ids:
        tree.insert(employee_id)

    print("Inserted employee IDs:", employee_ids)
    print("Root ID:", tree.root.value)

    # In a balanced tree, each comparison can eliminate
    # an entire subtree instead of checking every ID.

    # ========================================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ========================================
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Explain why the values are sorted.

    print("\n=== IN-ORDER TRAVERSAL ===")

    sorted_ids = tree.inorder()
    print("Sorted employee IDs:", sorted_ids)

    # In-order traversal visits left, root, and right.
    # This returns the employee IDs in ascending order.

    # ========================================
    # TODO (Student): SEARCH TESTS
    # ========================================
    # Requirements:
    # 1. Search for at least two existing values.
    # 2. Search for at least two missing values.
    # 3. Explain the results.

    print("\n=== SEARCH TESTS ===")

    for employee_id in [1025, 1090, 999, 1085]:
        print(f"ID {employee_id} found? {tree.search(employee_id)}")

    # Existing IDs return True.
    # Missing IDs return False when the search reaches None.

    # ========================================
    # TODO (Student): EDGE CASES
    # ========================================
    # Demonstrate at least one edge case.
    # Examples:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node

    print("\n=== EDGE CASES ===")

    empty_tree = BST()

    print("Search empty tree for 1050:", empty_tree.search(1050))
    print("Traverse empty tree:", empty_tree.inorder())

    # Duplicate values are ignored by our insertion method.
    before = tree.inorder()
    tree.insert(1050)

    print("Duplicate 1050 ignored:", tree.inorder() == before)

    single_node_tree = BST()
    single_node_tree.insert(42)

    print("One-node tree:", single_node_tree.inorder())

    # Basic checks to make sure the program works.
    assert sorted_ids == sorted(set(employee_ids))
    assert tree.search(1025)
    assert tree.search(1090)
    assert not tree.search(999)
    assert not tree.search(1085)
    assert empty_tree.inorder() == []
    assert not empty_tree.search(1050)
    assert tree.inorder() == before

    print("All example checks passed.")


if __name__ == "__main__":
    main()
