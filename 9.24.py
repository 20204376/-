class TreeNode:  # 이진 트리의 노들들 나타내는 클래스 .
    def __init__(self, priority, data):
        self.priority = priority  # Parameters:
        self.data = data          # priority : 우선순위 값
        self.left = None          # data : 노드에 저장된 데이터
        self.right = None

class PriorityQueue:         # 우선순위 큐를 나타내는 클래스
    def __init__(self):
        self.root = None     # Attributes :
                             # root : 이진 트리의 루트 노드

    def insert(self, priority, data):    # 우선순위 큐에 노드를 삽입하는 메서드 
        # Parameters:#
        # priority: 우선순위 값 
        # data: 삽입할 데이터
        self.root = self._insert(self.root, priority, data)

    def _insert(self, node, priority, data):    # 삽입 연산의 내부 구현 메서드
        # Parameters:
        # node: 현재 노드
        # priority: 우선순위 값
        # data: 삽입할 데이터
        if not node:
            return TreeNode(priority, data)
        # Returns : 현재 노드를 갱신한 후의 루트 노드

        if priority < node.priority:
            node.left = self._insert(node.left, priority, data)
        else:
            node.right = self._insert(node.right, priority, data)

        return node

    def _find_max(self, node):
        # 가장 오른쪽에 있는 노드까지 이동
        while node.right:
            node = node.right
        return node

    def _delete_max(self, node):
        # 오른쪽 끝에 있는 노드를 삭제하면서 새로운 노드를 반환
        if not node.right:
            return node.left
        node.right = self._delete_max(node.right)
        return node

    def find_max(self):
        if not self.root:
            return None

        # 가장 큰 우선순위 노드 찾기
        return self._find_max(self.root).data

    def print_priority_order(self):
        # 우선순위에 따라 내림차순으로 출력
        self._print_priority_order(self.root)

    def _print_priority_order(self, node):
        if node:
            # 오른쪽 노드부터 출력하여 우선순위에 따라 내림차순
            self._print_priority_order(node.right)
            print(f"Priority: {node.priority}, Data: {node.data}")
            self._print_priority_order(node.left)

# 우선순위 큐 생성
priority_queue = PriorityQueue()

# 노드 삽입
priority_queue.insert(3, 'C')
priority_queue.insert(1, 'A')
priority_queue.insert(53, 'B')
priority_queue.insert(21, 'F')
priority_queue.insert(18, 'D')
priority_queue.insert(37, 'E')

# 우선순위에 따라 출력
print("큐의 우선순위 순서:")
priority_queue.print_priority_order()
