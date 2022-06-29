#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *p = *head;
	listint_t *t;
	listint_t *newnode;

	newnode = malloc(sizeof(listint_t));
	if (p == NULL || newnode == NULL)
		return (NULL);
	while(p->n < number && p != NULL)
	{
		if (n == p->n)
			return (p);
		t = p;
		p = p->next;
	}
	t->next = newnode;
	newnode->next = p;
	return (newnode);
}
