"""
Lab: Rooted & Compressed - Tree Traversal and Huffman Coding
COSC 2436 - Chapter 7

This starter code scaffolds three parts:
  Part 1: BFS vs DFS directory traversal
  Part 2: DFS vs BFS shortest-path counterexample (mango-seller style)
  Part 3: Mini Huffman coding (build tree, encode, decode)

Fill in every function marked with a TODO. Do not change function
signatures - the entry point at the bottom calls them exactly as written.
All input data below is hardcoded (no file I/O, no randomness) so the
lab runs the same way every time.
"""

from collections import deque
import heapq


# ---------------------------------------------------------------------------
# PART 1: File directory traversal (BFS vs DFS)
# ---------------------------------------------------------------------------

class DirNode:
    """A simple directory/file node used to build a tree (no real filesystem
    access is used here - this is a hardcoded tree so the lab is portable)."""

    def __init__(self, name, children=None):
        self.name = name
        # children is a list of DirNode objects (an empty list means a 'file')
        self.children = children if children is not None else []


def build_sample_directory():
    # Leaf 'files'
    file1 = DirNode("notes.txt")
    file2 = DirNode("todo.txt")
    file3 = DirNode("photo.png")
    file4 = DirNode("song.mp3")
    file5 = DirNode("draft.docx")
    file6 = DirNode("index.html")
    file7 = DirNode("style.css")

    # Sub-folders
    docs = DirNode("docs", [file1, file2, file5])
    media = DirNode("media", [file3, file4])
    web = DirNode("web", [file6, file7])

    # Root (11 nodes total)
    root = DirNode("root", [docs, media, web])
    return root


def print_names_bfs(start_dir):
    queue = deque([start_dir])  # starter queue - build the loop below
    while queue:
        current = queue.popleft()
        print(current.name)
        for child in current.children:
            queue.append(child)


def print_names_dfs(start_dir):
    """
    Print every node name in the tree using DEPTH-FIRST traversal.
    This should be RECURSIVE and needs no queue.
    """
    print(start_dir.name)
    for child in start_dir.children:
        print_names_dfs(child)
    pass


# ---------------------------------------------------------------------------
# PART 2: DFS fails at shortest path - counterexample
# ---------------------------------------------------------------------------

class TreeNode:
    """A binary tree node used for the mango-seller style counterexample."""

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def build_mango_tree():
    # Left branch: root -> left -> left -> left = target (depth 3)
    left_leaf = TreeNode("target")
    left_level2 = TreeNode("L2", left=left_leaf)
    left_level1 = TreeNode("L1", left=left_level2)

    # Right branch: root -> right = target (depth 1)
    right_leaf = TreeNode("target")

    root = TreeNode("root", left=left_level1, right=right_leaf)
    return root


def dfs_search(root, target):
    if root is None:
        return None
    if root.value == target:
        return root

    left_result = dfs_search(root.left, target)
    if left_result is not None:
        return left_result
    
    return dfs_search(root.right, target)


def bfs_search(root, target):
    queue = deque([root]) if root is not None else deque()  # starter queue
    queue = deque([root]) if root is not None else deque()

    while queue:
        current = queue.popleft()
        if current.value == target:
            return current
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

    return None


# ---------------------------------------------------------------------------
# PART 3: Mini Huffman coding
# ---------------------------------------------------------------------------

class HuffmanNode:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):
        # Needed so heapq can order HuffmanNode objects by frequency.
        return self.freq < other.freq


def count_frequencies(text):
    freq_dict = {}
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq


def build_huffman_tree(freq_dict):
    heap = []
    for char, freq in freq_dict.items():
        heapq.heappush(heap, HuffmanNode(freq, char))

    if len(heap) == 1:
        only = heapq.heappop(heap)
        return HuffmanNode(only.freq, left=only)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)

    return heap[0]


def generate_codes(node, prefix='', code_map=None):
    if code_map is None:
        code_map = {}
    if node is None:
        return code_map
    if node.char is not None:
        code_map[node.char] = prefix if prefix else "0"
        return code_map
    generate_codes(node.left, prefix + "0", code_map)
    generate_codes(node.right, prefix + "1", code_map)
    return code_map


def huffman_encode(text, codes):
    """
    Encode text into a single bitstring using the code table produced by
    generate_codes.
    """
    encoded = ""
    return "".join(codes[char] for char in text)


def huffman_decode(encoded, root):
    decoded = []
    current = root
    for bit in encoded:
        current = current.left if bit == "0" else current.right
        if current.char is not None:
            decoded.append(current.char)
            current = root
    return "".join(decoded)


# ---------------------------------------------------------------------------
# Entry point - deterministic, hardcoded scaffolding (no file I/O, no random)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=== Part 1: Directory Traversal ===")
    root_dir = build_sample_directory()
    print("BFS order:")
    print_names_bfs(root_dir)
    print("\nDFS order:")
    print_names_dfs(root_dir)

    print("\n=== Part 2: DFS vs BFS Shortest Path ===")
    mango_root = build_mango_tree()
    dfs_result = dfs_search(mango_root, "target")
    bfs_result = bfs_search(mango_root, "target")
    print(f"DFS found target: {dfs_result.value} (took the FAR path)")
    print(f"BFS found target: {bfs_result.value} (took the CLOSE path)")

    print("\n=== Part 3: Huffman Coding ===")
    sample_text = "abracadabra"
    freqs = count_frequencies(sample_text)
    print("Frequencies:", freqs)

    huffman_tree = build_huffman_tree(freqs)
    codes = generate_codes(huffman_tree)
    print("Codes:", codes)

    encoded = huffman_encode(sample_text, codes)
    print("Encoded bitstring:", encoded)

    decoded = huffman_decode(encoded, huffman_tree)
    print("Decoded text:", decoded)
    assert decoded == sample_text, "Round-trip failed!"

    fixed_width_bits = 8 * len(sample_text)
    print(f"Huffman bits: {len(encoded)}  vs  fixed-width bits: {fixed_width_bits}")
