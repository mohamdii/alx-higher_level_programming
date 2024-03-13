#include <stdio.h>
#include <stdlib.h>

struct Node 
{
	int data;
	char c;
	struct Node *next;
};
void create_node(int data, char c)
{
	struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
	newNode->data = data;
	newNode->c = c;
	newNode->next = NULL;
	printf("%d, %c\n", newNode->data, newNode->c);
}
void add_end(struct Node **head)
{
	*head = create_node(int data, char c);
	struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
	if (head == NULL)
	{
		*head = *newNode
	}
	else
	{
		struct Node *current = *head;
		while(*head != NULL)
		{
			*current = current->next
		}
	}
}
			

}
int main(void)
{
	/**struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
	newNode->data = 12;
	newNode->c = 'x';
	printf("%c",newNode->c);
	return 0;**/
	create_node(544,'c');
	add_end
	return 0;
}
