SYSTEM_PROMPT_REPOK="""You are an expert software engineer with proficiency in the Java programming language. Your task is to analyze a Java class and generate the representation invariant of the class. A representation invariant is a boolean method of the class, called repOk, that returns true when executed over valid instances of the class, and returns false otherwise."""

SYSTEM_PROMPT_PROP_LIST="""You are an expert software engineer with proficiency in the Java programming language. Your task is to analyze a Java class and generate a list of properties in plain text that are a part of the representation invariant of the class. A representation invariant is a boolean method of the class that returns true when executed over valid instances of the class, and returns false otherwise."""

SYSTEM_PROMPT_REPOK_AND_PROP="""You are an expert software engineer with proficiency in the Java programming language. Your task is to analyze a Java class and a property in plain text that is a part of the representation invariant of the class, then generate the code for that property. A representation invariant is a boolean method of the class that returns true when executed over valid instances of the class, and returns false otherwise."""

USER_PROMPT_REPOK="""Generate a representation invariant for the following class:
"""
USER_PROMPT_PROP_LIST="""Generate a list of properties in plain text that the representation invariant of the following class must satisfy:
"""
USER_PROMPT_CHAIN_OF_THOUGT="""Generate a representation invariant that verifies the properties above."""

SYSTEM_PROMPT_SIMPLE="""You are an expert software engineer with proficiency in the Java programming language."""

USER_PROMPT_OPENAI="""### Generate a representation invariant for this class. Make sure to only write properties that the class satisfies and with no explanation.
"""

CLASS_EXAMPLE_1="""[Class]
```java
public class MinHeap {
    private int[] heap;
    private int size;
    private int capacity;
    public MinHeap(int capacity) {
        this.capacity = capacity;
        this.size = 0;
        this.heap = new int[capacity];
    }
    private int parent(int index) {
        return (index - 1) / 2;
    }
    private int leftChild(int index) {
        return 2 * index + 1;
    }
    private int rightChild(int index) {
        return 2 * index + 2;
    }
    public void insert(int value) {
        if (size == capacity) {
            throw new IllegalStateException("Heap is full");
        }
        heap[size] = value;
        int current = size;
        size++;
        while (current != 0 && heap[current] < heap[parent(current)]) {
            swap(current, parent(current));
            current = parent(current);
        }
    }
    public int extractMin() {
        if (size == 0) {
            throw new IllegalStateException("Heap is empty");
        }
        int min = heap[0];
        heap[0] = heap[size - 1];
        size--;
        heapifyDown(0);
        return min;
    }
    private void heapifyDown(int index) {
        int smallest = index;
        int left = leftChild(index);
        int right = rightChild(index);
        if (left < size && heap[left] < heap[smallest]) {
            smallest = left;
        }
        if (right < size && heap[right] < heap[smallest]) {
            smallest = right;
        }
        if (smallest != index) {
            swap(index, smallest);
            heapifyDown(smallest);
        }
    }
    private void swap(int i, int j) {
        int temp = heap[i];
        heap[i] = heap[j];
        heap[j] = temp;
    }
}
```
"""

PARTS_OF_CLASS_1="""[Class signature]
public class MinHeap
[Class attributes]
private int[] heap;
private int size;
private int capacity;
[Class methods]
private int parent(int index) {
    return (index - 1) / 2;
}
private int leftChild(int index) {
    return 2 * index + 1;
}
private int rightChild(int index) {
    return 2 * index + 2;
}
public void insert(int value) {
    if (size == capacity) {
        throw new IllegalStateException("Heap is full");
    }
    heap[size] = value;
    int current = size;
    size++;
    while (current != 0 && heap[current] < heap[parent(current)]) {
        swap(current, parent(current));
        current = parent(current);
    }
}
public int extractMin() {
    if (size == 0) {
        throw new IllegalStateException("Heap is empty");
    }
    int min = heap[0];
    heap[0] = heap[size - 1];
    size--;
    heapifyDown(0);
    return min;
}
private void heapifyDown(int index) {
    int smallest = index;
    int left = leftChild(index);
    int right = rightChild(index);
    if (left < size && heap[left] < heap[smallest]) {
        smallest = left;
    }
    if (right < size && heap[right] < heap[smallest]) {
        smallest = right;
    }
    if (smallest != index) {
        swap(index, smallest);
        heapifyDown(smallest);
    }
}
private void swap(int i, int j) {
    int temp = heap[i];
    heap[i] = heap[j];
    heap[j] = temp;
}
"""

REPOK_EXAMPLE_1="""[repOk]
```java
public boolean repOk() {
    for (int i = 0; i < size; i++) {
        int left = leftChild(i);
        int right = rightChild(i);

        if (left < size && heap[left] < heap[i]) {
            return false;
        }
        if (right < size && heap[right] < heap[i]) {
            return false;
        }
    }
    return true;
}
```
"""

TEXT_PROP_LIST_EXAMPLE_1="""[Properties]
- Array Bounds. The size of the heap should not exceed the capacity.
- Heap Property. For every node, the parent should be smaller than or equal to its children.
- Complete Tree Property. The heap should be a complete binary tree, meaning all levels are fully filled except possibly the last level, which is filled from left to right.
"""

TEXT_SINGLE_PROP_EXAMPLE_1="""[Property]
- Heap Property. For every node, the parent should be smaller than or equal to its children.
"""

CODE_SINGLE_PROP_EXAMPLE_1="""[Property]
```java
public boolean property() {
    for (int i = 0; i < size; i++) {
        int left = leftChild(i);
        int right = rightChild(i);

        if (left < size && heap[left] < heap[i]) {
            return false;
        }
        if (right < size && heap[right] < heap[i]) {
            return false;
        }
    }
    return true;
}
```
"""


CLASS_EXAMPLE_2="""[Class]
```java
public class BinTree {
    private class Node {
        private Node left;  // left child
        private Node right; // right child
        private int info;   // data
        public Node(int info) {
            this.info = info;
        }
    }
    private Node root;      // root node
    private int size = 0;   // number of nodes in the tree
    public void add(int x) {
        if (root == null) {
            root = new Node(x);
            size++;
        } else {
            addRecursive(root, x);
        }
    }
    private void addRecursive(Node current, int x) {
        if (x == current.info) {
            return;     // No duplicates allowed
        } else if (x < current.info) {
            if (current.left == null) {
                current.left = new Node(x);
                size++;
            } else {
                addRecursive(current.left, x);
            }
        } else {
            if (current.right == null) {
                current.right = new Node(x);
                size++;
            } else {
                addRecursive(current.right, x);
            }
        }
    }
    public boolean contains(int x) {
        return containsRecursive(root, x);
    }
    private boolean containsRecursive(Node current, int x) {
        if (current == null) {
            return false;
        }
        if (x == current.info) {
            return true;
        }
        return x < current.info ? containsRecursive(current.left, x) : containsRecursive(current.right, x);
    }
    public int getSize() {
        return size;
    }
}
```
"""

REPOK_EXAMPLE_2="""[repOk]
```java
public boolean repOK() {
    if (root == null)
        return size == 0;

    if (numNodes(root) != size)
        return false;

    if (!isAcyclic())
        return false;

    if (!isOrdered(root))
        return false;

    if (!noDuplicates(root))
        return false;

    return true;
}

private boolean isAcyclic() {
    Set<Node> visited = new HashSet<Node>();
    visited.add(root);
    LinkedList<Node> workList = new LinkedList<Node>();
    workList.add(root);
    while (!workList.isEmpty()) {
        Node current = (Node) workList.removeFirst();
        if (current.left != null) {
            if (!visited.add(current.left))
                return false;
            workList.add(current.left);
        }
        if (current.right != null) {
            if (!visited.add(current.right))
                return false;
            workList.add(current.right);
        }
    }
    return true;
}

private int numNodes(Node n) {
    if (n == null)
        return 0;
    return 1 + numNodes(n.left) + numNodes(n.right);
}

private boolean isOrdered(Node n) {
    return isOrdered(n, -1, -1);
}

private boolean isOrdered(Node n, int min, int max) {
    if (n.info == null)
        return false;
    if ((min != -1 && n.info <= (min)) || (max != -1 && n.info >= (max)))
        return false;
    if (n.left != null)
        if (!isOrdered(n.left, min, n.info))
            return false;
    if (n.right != null)
        if (!isOrdered(n.right, n.info, max))
            return false;
    return true;
}

private boolean noDuplicates(Node root) {
    Set<Integer> seen = new HashSet<>();
    return noDuplicatesHelper(root, seen);
}

private boolean noDuplicatesHelper(Node node, Set<Integer> seen) {
    if (node == null) return true;

    if (!seen.add(node.info)) return false;

    return noDuplicatesHelper(node.left, seen) && noDuplicatesHelper(node.right, seen);
}
```

"""
TEXT_PROP_LIST_EXAMPLE_2="""[Properties]
- Consistent size: The size attribute must be equal to the number of nodes in the tree.
- Acyclic structure: The tree structure must be acyclic, i.e., no node should have a path back to itself.
- Ordered structure: The tree must maintain the binary search tree property, where the left child of a node has a value less than the parent node, and the right child has a value greater than the parent node.
- No duplicate values: No two nodes in the tree should have the same value.
"""

TEXT_SINGLE_PROP_EXAMPLE_2="""[Property]
- Acyclic structure: The tree structure must be acyclic, i.e., no node should have a path back to itself.
"""

CODE_SINGLE_PROP_EXAMPLE_2="""[Property]
```java
public boolean property() {
    Set<Node> visited = new HashSet<Node>();
    visited.add(root);
    LinkedList<Node> workList = new LinkedList<Node>();
    workList.add(root);
    while (!workList.isEmpty()) {
        Node current = (Node) workList.removeFirst();
        if (current.left != null) {
            if (!visited.add(current.left))
                return false;
            workList.add(current.left);
        }
        if (current.right != null) {
            if (!visited.add(current.right))
                return false;
            workList.add(current.right);
        }
    }
    return true;
}
```
"""

PARTS_OF_CLASS_2="""[Class signature]
public class BinTree
[Class attributes]
private Node root    
private int size = 0
[Class methods]
public void add(int x) {
    if (root == null) {
        root = new Node(x);
        size++;
    } else {
        addRecursive(root, x);
    }
}
private void addRecursive(Node current, int x) {
    if (x == current.info) {
        return;     // No duplicates allowed
    } else if (x < current.info) {
        if (current.left == null) {
            current.left = new Node(x);
            size++;
        } else {
            addRecursive(current.left, x);
        }
    } else {
        if (current.right == null) {
            current.right = new Node(x);
            size++;
        } else {
            addRecursive(current.right, x);
        }
    }
}
public boolean contains(int x) {
    return containsRecursive(root, x);
}
private boolean containsRecursive(Node current, int x) {
    if (current == null) {
        return false;
    }
    if (x == current.info) {
        return true;
    }
    return x < current.info ? containsRecursive(current.left, x) : containsRecursive(current.right, x);
}
public int getSize() {
    return size;
}
"""

CLASS_EXAMPLE_3="""[Class]
```java
public class LinkedList {
    private static class Node {
        int data;
        Node next;
        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }
    private Node head;
    private int size;
    public LinkedList() {
        head = null;
        size = 0;
    }
    public void add(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
        } else {
            Node current = head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode;
        }
        size++;
    }
    public int remove() {
        if (head == null) {
            throw new IllegalStateException(\"List is empty\");
        }
        int removedData = head.data;
        head = head.next;
        size--;
        return removedData;
    }
}
```
"""

PARTS_OF_CLASS_3="""[Class signature]
public class LinkedList
[Class attributes]
private Node head
private int size
[Class methods]
public void add(int data) {
    Node newNode = new Node(data);
    if (head == null) {
        head = newNode;
    } else {
        Node current = head;
        while (current.next != null) {
            current = current.next;
        }
        current.next = newNode;
    }
    size++;
}
public int remove() {
    if (head == null) {
        throw new IllegalStateException(\"List is empty\");
    }
    int removedData = head.data;
    head = head.next;
    size--;
    return removedData;
}
"""

REPOK_EXAMPLE_3="""[repOk]
public boolean repOk() {
    if (size < 0) {
        return false;
    }
    
    if (size == 0) {
        return head == null;
    }

    if (head == null) {
        return false;
    }

    int nodeCount = 0;
    Set<Node> visitedNodes = new HashSet<>();
    Node current = head;

    while (current != null) {
        if (!visitedNodes.add(current)) {
            return false;
        }

        nodeCount++;
        current = current.next;
    }

    return nodeCount == size;
}
"""

TEXT_PROP_LIST_EXAMPLE_3="""[Properties]
- No negative size: The size attribute must not be negative.
- Size consistency with head: The size attribute must be consistent with head attribute.
- Consistent size: The size attribute must be equal to the number of nodes in the tree.
- Acyclic structure: The linked list structure must be acyclic, i.e., no node should have a path back to itself.
"""

TEXT_SINGLE_PROP_EXAMPLE_3="""[Property]
- Consistent size: The size attribute must be equal to the number of nodes in the tree.
"""

CODE_SINGLE_PROP_EXAMPLE_3="""[Property]
```java
public boolean property() {
    int nodeCount = 0;
    Node current = head;

    while (current != null) {
        nodeCount++;
        current = current.next;
    }

    return nodeCount == size;
}
```
"""


