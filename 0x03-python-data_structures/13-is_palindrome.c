#include "lists.h"
/**
 * listint_len - length of linked list
 * @h: head of the list
 * Return: length of a list
 */
size_t listint_len(const listint_t *h)
{
	const listint_t *p;
	int counter = 0;

	p = h;
	while (p)
	{
		counter++;
		p = p->next;
	}
	return (counter);
}
/**
 * reverse_listint - reverse a list
 * @head: head of the list
 * Return: pointer to the first node
 */
int is_palindrome(listint_t **head)
{
	int i, j, len, flag = 1;
	listint_t *temp = *head;

	if (!*head)
		return (flag);
	len = listint_len(*head);
	int *arr = malloc(sizeof(int) * len);
	for (i = 0; i < len; i++)
	{
		arr[i] = temp->n;
		temp = temp->next;
	}
	for (i = 0, j = len - 1; i < len; i++)
	{
		if (arr[i] != arr[j])
			flag = 0;
	}
	free(arr);
	return (flag);
}
