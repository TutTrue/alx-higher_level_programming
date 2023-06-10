#include "lists.h"
/**
 * reverse_listint - reverse a list
 * @head: head of the list
 * Return: pointer to the first node
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *cur, *prev;

	if (!*head)
		return (NULL);
	cur  = (*head)->next;
	prev = NULL;
	while (cur)
	{
		(*head)->next = prev;
		prev = *head;
		*head = cur;
		cur = cur->next;
	}
	(*head)->next = prev;
	return (*head);
}
/**
 * is_palindrome -  checks if a singly linked list is a palindrome
 * @head: head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *forw = *head, *backw = *head, *temp;
	int i, counter = 0, flag = 1;

	if (!head)
	{
		flag = 0;
		goto here;
	}
	while (!backw)
	{
		counter++;
		backw = backw->next;
	}
	backw = forw;
	for (i = 1; i < (counter / 2); i++)
		backw = backw->next;
	temp = backw->next;
	backw->next = NULL;
	backw = temp;
	reverse_listint(&backw);
	while (backw && forw)
	{
		if (backw->n != forw->n)
		{
			flag = 0;
			break;
		}
		backw = backw->next;
		forw = forw->next;
	}
	reverse_listint(&backw);
	while (forw->next != NULL)
		forw = forw->next;
	forw->next = backw;
here:
	return (flag);
}
