#include "lists.h"
/**
 * insert_node - insert a number inside a sorted linked list
 * @head: pointer to the head of the l list
 * @number: the integer to insert
 * Return: a pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *pointer1, *pointer2, *tempo;

	tempo = malloc(sizeof(listint_t));
	if (tempo == NULL)
		return (NULL);
	tempo->n = number;
	if (*head == NULL)
	{
		*head = tempo;
		tempo->next = NULL;
		return (tempo);
	}
	pointer1 = *head;
	pointer2 = pointer1->next;
	while (pointer2 != NULL)
	{
		if (pointer1->n > number)
		{
			*head = tempo;
			tempo->next = pointer1;
			return (tempo);
		}
		if (pointer1->n < number && pointer2->n > number)
		{
			pointer1->next = tempo;
			tempo->next = pointer2;
			return (tempo);
		}
		pointer1 = pointer1->next;
		pointer2 = pointer2->next;
	}
	pointer1->next = tempo;
	tempo->next = NULL;
	return (tempo);
}
