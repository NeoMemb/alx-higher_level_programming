#include "lists.h"

/**
 * check_cycle - Function that checks if a singly linked list
 * has a cycle in it.
 * @list_head: head of linked list
 *
 * Return: return 1 if cycle detected, 0 otherwise
 */

int check_cycle(listint_t *list_head)
{
	listint_t *first_ptr, *secnd_ptr;

	if (!list_head)
		return (0);

	first_ptr = list_head;
	secnd_ptr = list_head->next;
	while (secnd_ptr && first_ptr && secnd_ptr->next)
	{
		if (first_ptr == secnd_ptr)
			return (1);

		first_ptr = first_ptr->next;
		secnd_ptr = secnd_ptr->next->next;
	}

	return (0);
}
