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
def delete(r,n):
    if r is None:
        return r
    if n < r.val:
        r.left=delete(r.left,n)
    elif n > r.val:
        r.right=delete(r.right,n)
    else:
        if r.left is None:
            t=r.right
            r=None
            return t
        elif r.right is None:
            t=r.left
            r=None
            return t
        t=minval(r.right)
        r.val=t.val
        r.right= delete(r.right,t.val)
    return r 
def minval(n):
    c=n
    while(c.left is not None):
        c=c.left
    return c
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
del a
a=[]
delete(r,10)
inorder(r)
print("The inorder traversal of the tree after deleting 10 is",a)
