#include <iostream>

using namespace std;

class Node
{
public:
    int data;
    Node *next;

    Node(int x,Node *n)
    {
       data=x;
       next=n;
    }
};

class Queue
{
    private:
        Node *head;
        Node *last;
    public:
        int counter=0;
        Queue()
        {
            head = nullptr;
        }
        void enqueu(int data)
        {
            Node *newNode= new Node (data, nullptr);

            if(head == nullptr)
            {
                head = newNode;
                last = newNode;
                counter++;
            }
            else{
                last->next = newNode;
                last=last->next ;
                counter++;

            }
        }

        void dequeue()
        {

            if(head == nullptr)
            {
                cout << "No element in the list.";
                return;
            }

            Node *temp = head;
            if(head->next == nullptr){
                head=nullptr;
                last=nullptr;
                counter--;
            }
            else{
                head = head->next;
                counter--;
            }
            delete temp;

        }

        int top()
        {
           if(head == nullptr){
            return -1;
           }
           return head->data;
        }

        bool isEmpty()
        {
            return head == nullptr;
        }
        int size()
        {
            return counter;
        }

        void print()
        {
            Node *p = head;

            while(p != nullptr)
            {
                cout<< p->data << " ";
                p = p->next;
            }
        }
};
  
