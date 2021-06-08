class Node:
    def __init__(self,k):
        self.left=None
        self.right=None
        self.val=k
def insert(r,n):
    if r is None:
        r=n
    else:
        if r.val < n.val :
            if r.right is None:
                r.right=n
                print("Right node of",r.val, "is",n.val) 
            else:
                insert(r.right,n)
        else:
            if r.left is None:
                r.left=n
                print("Left node of",r.val, "is",n.val)
            else:
                insert(r.left,n)
a=[]
def inorder(r):
    if r:
        inorder(r.left)
        a.append(r.val)
        inorder(r.right)
r = Node(13)
print("Root node is ",r.val)
insert(r,Node(12))
insert(r,Node(10))
insert(r,Node(8))
insert(r,Node(15))
insert(r,Node(16))
insert(r,Node(17))
insert(r,Node(18))
inorder(r)
print("The inorder traversal of the tree is",a)

