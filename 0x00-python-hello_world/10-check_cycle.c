#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
 /**
  * check_cycle checks if the list is invloved into cycles
  * @list: pointer to list to check
  * Return: 1 if there are Cycles, 0 otherwise
 */
int check_cycle(listint_t *list)
(
    listint_t *gentle = list, *swift = list;
    /**
     * *gentle - is used to express taht is slow
     * *Swift - is used to express that is fast  
    */
    while (swift && swift->next)
    {
        gentle = gentle->next;
        swift = swift->next->next;
        if (gentle == swift)
        return (1);
        
    }
    return(0);
)
