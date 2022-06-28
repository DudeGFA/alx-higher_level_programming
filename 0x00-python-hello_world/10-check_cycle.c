#include "lists.h"
/**
 * check_cycle - checks for a cycle in
 * a singly linked list
 * @list: singly linked list
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *z = list;
	listint_t *p = list;

	if (!list)
	{
		return (0);
	}
	while (p && z && z->next)
	{
		p = p->next;
		z = z->next->next;
		if (p == z)
		{
			return (1);
		}
	}
	return (0);
}
