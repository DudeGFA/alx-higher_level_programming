#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *P = *head;
	listint_t *t;
	listint_t *newnode;

	newnode = malloc(sizeof(listint_t))
	if (p == NULL || newnode == NULL)
		return (NULL);
	while(p.n < number && p != NULL)
	{
		t = p;
		p = p->next;
	}
	t->next = newnode;
	newnode.next = p;
	return (newnode);
)
