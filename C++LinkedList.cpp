#include <iostream>

class Node{
    public:
        int data;
        Node* next;
        Node(){
            data = 0;
            next = NULL;
        }
        Node(int data_value){
            data = data_value;
            next = NULL;
        }
};

class LinkedList{
    public:
        Node* head;
        
        LinkedList(){
            head = NULL;
        }
        void appendNode(int data, int pos= -1 ){
            Node* pointer = new Node();
            pointer->data = data;
            //Node new_node(data); doesnt WORK;; It is required new node to be allocated, like above

            Node* cur_pointer = head;

            //WHEN LIST IS EMPTY
            if(cur_pointer == NULL){
                head = pointer;
                std::cout<<"Node with data "<<data<<" is appended."<<std::endl;
                return;
            }

            //WHEN WE INSERT NEW NODE AT THE END OF A LIST
            else if (pos == -1 || pos == length()+1){
                while((*cur_pointer).next != NULL){
                    //std::cout<<"Traversing!"<<std::endl;
                    cur_pointer = (*cur_pointer).next; 
                }
                (*cur_pointer).next = pointer;
                std::cout<<"Node with data "<<data<<" is appended."<<std::endl;
                return;
            }

            //WHEN WE INSERT NODE AT SPECIFIC POSITION IN LIST
            else if(pos != -1){   //-1 is default value
                if(pos > length()+1 || pos < 1){
                    std::cout<<"Position is out of range, "<<pointer->data<<" was NOT appended"<< std::endl;
                }
                else{
                    if(pos ==1){
                        pointer->next = cur_pointer;
                        head = pointer;
                        std::cout<<"Node with data "<<data<<" is appended."<<std::endl;
                    }
                    else{
                        int counter = 1;
                        Node* temp_pointer= head;
                        while(counter != pos){
                            temp_pointer = cur_pointer;
                            cur_pointer = cur_pointer->next;
                            counter++;
                        }
                        pointer->next = cur_pointer;
                        temp_pointer->next = pointer;
                        std::cout<<"Node with data "<<data<<" is appended."<<std::endl;

                    }
                    
                }
            }
        }

        //PRINT OUT LINKED LIST
        void displayLinkedList(){
            Node* cur_pointer= head;
            std::cout<<"\n";
            std::cout<<"There are "<<length()<< " elements in Linked List."<<std::endl;
            
            while( (*cur_pointer).next != NULL){
                std::cout<<(*cur_pointer).data<<" ";
                cur_pointer = (*cur_pointer).next;
                }
            std::cout<<(*cur_pointer).data<<std::endl; // last element, because loop ends earlier
            
            std::cout<<std::endl;
                
        }

        //LENGTH OF THE LINKED LIST
        int length(){
            int counter = 0;
            Node* cur_pointer = head;
            while(cur_pointer != NULL){
                counter++;
                cur_pointer = (*cur_pointer).next;
            }
            /*if(counter == 1){
                std::cout<<"There is "<<counter<<" element in the Linked List!"<<std::endl;
                return counter;
            }
            std::cout<<"There are "<<counter<<" elements in the Linked List!"<<std::endl;*/
            return counter;
        }
        //DELETE NODE AT SPECIFIC POSITION
        void delete_node(int pos = -1054){
            Node* cur_pointer = head;
            Node* temp_pointer = head;


            if(head == NULL){
                std::cout <<"Linked List is empty." <<std::endl;
            }
            else if (pos == 1){
                cur_pointer = cur_pointer->next;
                head = cur_pointer;

            }
            // if no value is passed, pos will be default value -1054 and the last node will be deleted
            else if(pos == -1054){
                while(cur_pointer->next != NULL){
                    temp_pointer = cur_pointer;
                    cur_pointer = cur_pointer->next;
                    }
                temp_pointer->next = NULL;
                
            }
            else if(pos<1 || pos> length()+1){
                std::cout<<"Position of element you want to delete is out of range, "<< std::endl;
            }
            else{
                int counter = 1;
                while(counter != pos){
                    temp_pointer = cur_pointer;
                    cur_pointer = cur_pointer->next;
                    counter++;
                }
                temp_pointer->next = cur_pointer->next;
            }
        }

};

//Testing
int main(){
    std::cout<<"Hello LinkList maker!"<<std::endl;
    LinkedList first;

    first.appendNode(11);
    first.appendNode(517);
    first.appendNode(899);
    first.appendNode(777,1);
    first.appendNode(33);
    first.displayLinkedList();

    first.delete_node(); //deletes last node in Linked List
    first.displayLinkedList();

    first.appendNode(21290, 3);
    first.displayLinkedList();

    first.delete_node(2); //deletes node at position 2 in Linked List
    first.displayLinkedList();

    return 0;
}