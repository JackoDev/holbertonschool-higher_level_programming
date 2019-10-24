#include "lists.h"
/**
 * check_cycle - check for a loop inside a linked list
 * @list: head of the linked list
 * Return: 0 if no loop 1 for yes
 */
int check_cycle(listint_t *list)
{
	listint_t *pointer1, *pointer2;

	pointer1 = list;
	pointer2 = pointer1->next;
	if (list == NULL)
		return (0);
	if (list->next == NULL)
		return (0);
	while (pointer2 != NULL)
	{
		if (pointer2->next == NULL)
			return (0);
		pointer2 = pointer2->next->next;
		pointer1 = pointer1->next;
		if (pointer1 == pointer2)
			return (1);
	}
	return (0);

}
