# Theoretical Basis

## Binary tree species

1. Full binary tree

   all nodes exist

   2^k-1

2. Complete binary tree

   Except the last layer, other levels are all full, and the bottom layer is continuous from left to right

3. Binary search tree: 布局没有要求，只要元素和左右节点的顺序正确即可

4. Balanced Binary search Tree：任意左右子树高度差不能大于1（元素有序）

   Map-set-multimap-multiset

## Storage mode

### Linked store

构造一个链表，用两个指针分别表示左右子孩

### Line storage（少用）

a b c d e f g

0 1 2 3 4 5 6

给定某一个节点的下表，求它的左右孩子，2*i+1  2*i+2

## Traversal of binary trees

### DFS - recursion

前 中 后序遍历都是dfs 

实现方式：stack，recursion，Iterative（非recursion）

### BFS

Sequence traversal：一层一层去遍历













