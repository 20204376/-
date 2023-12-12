# 이진 탐색 트리의 노드를 나타내는 클래스
class Node:
    def __init__(self, value):
        self.value = value  # 노드의 값 (우선순위)
        self.left = None     # 왼쪽 자식 노드
        self.right = None    # 오른쪽 자식 노드

# 우선순위 큐를 구현하는 클래스
class PriorityQueue:
    def __init__(self):
        self.root = None  # 이진 탐색 트리의 루트 노드

    # 우선순위 큐에 새로운 값을 삽입하는 메서드
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    # 재귀적으로 노드를 삽입하는 내부 메서드
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    # 우선순위 큐에서 가장 작은 값을 추출하는 메서드
    def pop(self):
        if not self.root:
            return None

        min_node = self._find_min(self.root)
        self.root = self._remove_recursive(self.root, min_node.value)
        return min_node.value

    # 트리에서 가장 작은 값을 찾는 내부 메서드
    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    # 트리에서 특정 값을 삭제하는 내부 메서드 (재귀적으로 구현)
    def _remove_recursive(self, node, value):
        if not node:
            return None

        if value < node.value:
            node.left = self._remove_recursive(node.left, value)
        elif value > node.value:
            node.right = self._remove_recursive(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # 두 자식 노드가 있는 경우, 오른쪽 서브트리에서 가장 작은 값을 찾아 대체
            min_node = self._find_min(node.right)
            node.value = min_node.value
            node.right = self._remove_recursive(node.right, min_node.value)

        return node

# 우선순위 큐 사용 예시
priority_queue = PriorityQueue()
priority_queue.insert(5)
priority_queue.insert(3)
priority_queue.insert(7)
priority_queue.insert(1)

print(priority_queue.pop())  # 출력: 1
print(priority_queue.pop())  # 출력: 3
