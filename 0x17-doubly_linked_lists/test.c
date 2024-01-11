#include <stdio.h>
#include <stdlib.h>

struct Node
{
	int data;
	char chr;
	struct Node *next;
};
struct Node* create_node(int data, char chr)
{
	struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));
        newNode->data = data;
        newNode->chr = chr;
        newNode->next = NULL;
	return newNode;
}
void add_node_at_end(struct Node **head, int data, char c)
{
	struct Node *newNode = create_node(data, c);
	if (*head == NULL)
	{
		*head = newNode;
	}
	else
	{
		struct Node *current = *head;
		while(current->next != NULL)
		{
			current = current->next;
		}
		current->next = newNode;
	}
}
void display_list(struct Node *head)
{
	struct Node * current = head;
	while(current != NULL)
	{
		printf("%d - %c\n", current->data, current->chr);
		current= current->next;
	}
}
void reverse(struct Node *rev)
{
	if (rev == NULL)
	{
		display_list(struct Node *head);
		reverse(
	}
	else
	{
		return;
	}
}
int main(void)
{
	struct Node * head = create_node(1, 'c');
	//struct Node * newNode = create_node(2, 'v');
	//head->next = newNode;
	//printf("%d", head->next->data);
	//printf("%d", newNode->data);
	add_node_at_end(&head, 2, 'x');
	add_node_at_end(&head, 3, 'y');
	add_node_at_end(&head, 4, 'v');
	add_node_at_end(&head, 5, 'z');
	display_list(head);
	return 0;
}
