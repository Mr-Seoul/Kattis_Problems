#include <bits/stdc++.h>

using namespace std;

struct Node {
    char c;
    Node* previous;
    Node* next;
};

typedef Node *LinkedList;

LinkedList answer = NULL;

LinkedList strToLinkedList(string s) {
    LinkedList result = nullptr;
    result = new Node{'!', nullptr, nullptr};
    Node *prev = result;
    Node *current = nullptr;

    for (size_t i = 0; i < s.length(); i++) {
        char c = s[i];
        current = new Node{c, prev, nullptr};
        prev->next = current;
        prev = prev->next;
    }
    Node *last = new Node{'!',prev,nullptr};
    prev->next = last;
    return result;
}

void InsertLinkedList(Node *n, char value) {
    Node *AfterCurser = n;

    if (AfterCurser != nullptr) {
        Node *BeforeCurser = n->previous;
    
        Node *NewNode = new Node{value,BeforeCurser,AfterCurser};
        BeforeCurser->next = NewNode;
        AfterCurser->previous = NewNode;
    } else {
        Node *NewNode = new Node{value,nullptr,AfterCurser};
        AfterCurser->previous = NewNode;
    }
}

void DeleteLinkedList(Node *n) {
    Node *AfterCurser = n;
    Node *BeforeCurser = AfterCurser->previous;
    Node *BeforeBeforeCurser = nullptr;

    if (BeforeCurser->previous != nullptr) {
        BeforeBeforeCurser = BeforeCurser->previous;
    }

    if (BeforeBeforeCurser != nullptr) {
        BeforeBeforeCurser->next = AfterCurser;
        if (AfterCurser != nullptr) {
            AfterCurser->previous = BeforeBeforeCurser;
        }
        delete BeforeCurser;
    } else {
        AfterCurser->previous = nullptr;
        delete BeforeCurser;
        answer = AfterCurser;
    }
    
}

void PrintLinkedList (Node *PrintList) {
    for (Node *n = PrintList; n != nullptr; n = n-> previous) {
        if (n != nullptr) {
            PrintList = n;
        }
    }
    string PrintAnswer = "";
    for (Node *n = PrintList->next; n != nullptr; n = n->next) {
        if (n->next != nullptr) {
        PrintAnswer += n->c;
        }
    }
    std::cout << PrintAnswer << "\n";
}


int main() {
    string input;
    cin >> input;

    answer = strToLinkedList(input);
    Node *curser = answer;
    curser = curser->next;
    for (Node *n = answer->next; n != nullptr; n = n->next) {
        if (n->next != nullptr) {
            //cout << n->c;
            switch(n->c) {
                case 'L':
                    {
                    Node *temp = n->next;
                    n = n->previous;
                    if (curser == n->next) {
                        curser = curser->next;
                        DeleteLinkedList(temp);
                        curser = curser->previous;
                    }
                    else {
                        DeleteLinkedList(temp);
                    }

                    curser = curser->previous;
                    break;
                    }
                case 'R':
                    {

                    Node *temp = n->next;
                    n = n->previous;
                    if (curser == n->next) {
                        curser = curser->next;
                        DeleteLinkedList(temp);
                        curser = curser->previous;
                    }
                    else {
                        DeleteLinkedList(temp);
                    }

                    curser = curser->next;
                    break;
                    }
                case 'B':
                    {
                    Node *temp = n->next;
                    n = n->previous;
                    if (curser == n->next) {
                        curser = curser->next;
                        DeleteLinkedList(temp);
                        curser = curser->previous;
                    }
                    else {
                        DeleteLinkedList(temp);
                    }

                    curser = curser->next;
                    if (n == curser->previous) {
                        n = n->next;
                        DeleteLinkedList(curser);
                        n = n->previous;
                    } else {
                        DeleteLinkedList(curser);
                    }
                    curser = curser->previous;

                    break;
                    }
                default:
                    {
                    if (n != curser) {
                        curser = curser->next;
                        InsertLinkedList(curser,n->c);
                        curser = curser->previous;

                        Node *temp = n->next;
                        n = n->previous;
                        if (curser == n->next) {
                            curser = curser->next;
                            DeleteLinkedList(temp);
                            curser = curser->previous;
                        }
                        else {
                            DeleteLinkedList(temp);
                        }
                    } else {
                        curser = curser->next;
                    }
                }
            } 
            //std::cout << " | " << curser->c << ":\n";
            //PrintLinkedList(answer);
        }
    }
    PrintLinkedList(answer);
    return 0;
}
