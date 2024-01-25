#include <stdio.h>
#include <stdlib.h>
#include  "lists.h"
size_t print_dlistint(const dlistint_t *h)
{
	unsigned int i = 0;

	if(h == NULL)
		return 1;
	while(h != NULL)
	{
		//dlistint_t *head = (dlistint_t *)malloc(sizeof(dlistint_t));
		h = h->next;
		i++; 
	}
	return i;
}
