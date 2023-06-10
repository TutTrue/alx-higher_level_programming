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
 * is_palindrome -  checks if a singly linked list is a palindrome
 * @head: head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int i, j, len, flag = 1;
	listint_t *temp = *head;
	int *arr;

	if (!*head)
		return (flag);
	len = listint_len(*head);
	arr = malloc(sizeof(int) * len);
	if (!arr)
		return (2);
	for (i = 0; i < len; i++)
	{
		arr[i] = temp->n;
		temp = temp->next;
	}
	for (i = 0, j = len - 1; i < len && j > i; i++)
	{
		if (arr[i] != arr[j--])
			flag = 0;
	}
	free(arr);
	return (flag);
}
