# Practice of binary trees

This is a repository containing some of the Binary tree problems I met. 

` PyBT ` is a library that can be imported to facilitate debugging of binary tree problems.

You can use `PyBT` by the following command after placing the PyBT.py file in work directory: 

```python
import PyBT
```

The following are several functions in ~PyBT~

1. `TreeNode=PyBT.genBT(List)`

    Generate a binary tree from a list (pre-order).

2. `List=PyBT.printBT(TreeNode)`

   Generate a list (pre-order) reflecting the binary tree.

   For instance, List `[2,1,'#','#',4,3,'#','#','#']` means the binary tree:
   ```
       2
      / \
     1   4
        /
       3
    ```
