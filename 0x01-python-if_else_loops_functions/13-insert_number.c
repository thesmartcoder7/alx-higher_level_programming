#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - this inserts a number into a sorted
 *               singly linked list.
 *
 * @head: list head
 * @num: what to store in the new node
 *
 * Return: pointer to the new node
 */
listint_t *insert_node(listint_t **head, int num)
{
	listint_t *main_n;
	listint_t *new_n;

	main_n = *head;

	new_n = malloc(sizeof(listint_t));
	if (new_n == NULL)
		return (NULL);
	new_n->n = num;

	if (*head == NULL || (*head)->n > num)
	{
		new_n->next = *head;
		*head = new_n;
		return (new_n);
	}

	while (main_n->next != NULL)
	{
		if ((main_n->next)->n >= num)
		{
			new_n->next = main_n->next;
			main_n->next = new_n;
			return (new_n);
		}
		main_n = main_n->next;
	}

	new_n->next = NULL;
	main_n->next = new_n;
	return (new_n);
}

