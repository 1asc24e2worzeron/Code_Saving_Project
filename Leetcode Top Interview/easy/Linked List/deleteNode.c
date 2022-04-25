/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
// 聽說某面試要考 C, C++ 就練一下
// 沒什麼營養的基本題
// Runtime: 3 ms (94.81%), Memory Usage: 6.3 MB (64.31%)
void deleteNode(struct ListNode* node) {
    struct ListNode* target = node->next;
    node->val = node->next->val;
    node->next = node->next->next;
    free(target);
}
