class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def buildTree(arr):
    root = TreeNode(None)
    for i in range(len(arr)):
        child = TreeNode(arr[i])
        root.children.append(child)
        buildSubtree(arr, i + 1, arr[i], child)
    return root

def buildSubtree(arr, index, lastValue, parent):
    for i in range(index, len(arr)):
        if arr[i] > lastValue:
            child = TreeNode(arr[i])
            parent.children.append(child)
            buildSubtree(arr, i + 1, arr[i], child)

def dfs(node, path, allPaths):
    if node.value is not None:
        path.append(node.value)
    if not node.children:
        if len(path) > 0:
            allPaths.append(path.copy())
    else:
        for child in node.children:
            dfs(child, path, allPaths)
    if node.value is not None:
        path.pop()

arr = list(map(int, input().split()))

root = buildTree(arr)
allPath = []
dfs(root, [], allPath)
longest = max(allPath, key=len)

print(longest)