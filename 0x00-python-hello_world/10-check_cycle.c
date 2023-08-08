#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

/**
 * check_cycle - check speed
 * @list: list
 * Return: 1 if detected, otherwise 0
 */
int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	slow = list;
	fast = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
