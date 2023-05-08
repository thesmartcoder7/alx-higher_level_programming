#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - this checks if singly linked list is a cycle
 * Return: 0 if no cycle, 1 is yes
 * @list: list head
*/
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow = list;

	if (!list)
		return (0);

	while (1)
	{
		if (fast->next != NULL && fast->next->next != NULL)
		{
			fast = fast->next->next;
			slow = slow->next;

			if (fast == slow)
				return (1);
		}
		else
			return (0);
	}
}
