/*
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int treeHeight(TreeNode* root){
        if(root==NULL) return 0;
        int left = treeHeight(root->left);
        if(left==-1) return -1;
        int right = treeHeight(root->right);
        if(right==-1) return -1;
        return abs(left-right)>1 ? -1: max(left, right)+1;
    }
    bool isBalanced(TreeNode* root) {
        return treeHeight(root)==-1 ? false: true;
    }
};
