/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

// 剛好還有半小時，再寫一題
// Runtime: 4 ms (49.07%), Memory Usage: 6.1 MB (0%)
// 相當懷舊，原本最熟的是 C，但大學時期還需要別人救場
struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    
    struct ListNode * origin = head, * reg = head;
    
    int count = 1, i;
    while(head->next != NULL){
        ++count;
        head = head->next;
    }
    
    // 刪完列表為空的特例
    if(count == 1){
        free(origin);
        return NULL;
    }
    
    head = origin;
    
    // 目標前一個
    for(i = 0; i < count-n-1; ++i)
        head = head->next;
    
    if(count == n){
        origin = origin->next;
        free(head);
    } // 目標是第一個時會有問題，優先處理
    else if(head->next->next == NULL){
        free(head->next);
        head->next = NULL;
    } // 目標是最後一個時也會有問題，基於判斷式邏輯放第二個
    else{
        head = head->next;
        reg = head->next;
        head->val = head->next->val;
        head->next = head->next->next;
        free(reg);
    } // 一般狀況
    return origin;
}
