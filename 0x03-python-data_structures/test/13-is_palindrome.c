#include "lists.h"
#include <stdlib.h>
int is_palindrome(listint_t **head)
{
    listint_t *child = *head;
    int i, k, j;
    int *arr_of_n;

    if (!head || (*head) == NULL)
        return (1);
    for(j = 0; child != NULL; j++)
        child = child->next;
    arr_of_n = malloc(j * sizeof(int));
    if (arr_of_n == NULL)
        return (1);
    child = *head;
    for(i = 0; child != NULL; i++)
    {
        arr_of_n[i] = child->n;
        child = child->next;
    }
    for(k = 0, i--; k < (j / 2); k++, i--)
    {
        if (arr_of_n[k] != arr_of_n[i])
            return (0);
    }
    return (1);
}
