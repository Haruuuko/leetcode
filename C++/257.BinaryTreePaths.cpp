/*
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
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
#include <iostream>
#include <vector>
using namespace std;

struct TreeNode {
	int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
	vector<string> TreePaths;
	void DFS(TreeNode* node, string answer){
		answer += "->" + to_string(node->val);
		if(!node->left && !node->right){
			TreePaths.push_back(answer);
		}else{
			if(node->left) DFS(node->left, answer);
			if(node->right) DFS(node->right, answer);
		}
	}
    vector<string> binaryTreePaths(TreeNode* root) {
        if(root){
			DFS(root, "");
			for(int i = 0; i < TreePaths.size(); i++)
                TreePaths[i].erase(TreePaths[i].begin(), TreePaths[i].begin() + 2);
		}
		return TreePaths;
    }
};

int main(){
	Solution test;
	TreeNode a(1);
	TreeNode b(2);
	TreeNode c(3);
	TreeNode d(5);
	a.left = &b;
	a.right = &c;
	b.right = &d;
	cout<<test.binaryTreePaths(&a)[0]<<endl;
	return 0;
}
