#include "lists.h"
/**
* insert_node - function to insert node in sorted list
* @head: double pointer of listint_t type
* @number: int
* Return: adress of new node or NULL
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	temp = *head;
	while (temp->next != NULL)
	{
		if (number < temp->n)
		{
			new->next = temp;
			*head = new;
			return (new);
		}
		if (number <= temp->next->n)
		{
			new->next = temp->next;
			temp->next = new;
			return (new);
		}
		temp = temp->next;
	}
	new->next = NULL;
	temp->next = new;
	return (new);
}
