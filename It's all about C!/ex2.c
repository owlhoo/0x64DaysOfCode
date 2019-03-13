#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <string.h>

typedef struct person {
	char *name;
	int age;
	int height;
	int weight;
} Person;

Person * Person_create(char *name, int age, int height, int weight)
{
	Person *who = malloc(sizeof(Person));
	assert(who != NULL);

	who->name = strdup(name);
	who->age = age;
	who->height = height;
	who->weight = weight;

	return who;
}

void Person_destroy(Person * who)
{
	assert(who != NULL);
	
	free(who->name);
	free(who);
}

void Person_print(Person *who)
{
	printf("Hello, I am %s, age %d, tall %d and heavy %d kilos. xd\n", who->name, who->age, who->height, who->weight);
}

int main(int argc, char *argv[])
{
	Person *joe = Person_create("Joe Jo", 32, 64, 140);
	Person *anne = Person_create("Anne Reiner", 20, 72, 180);

	printf("Joe is at memory location %p:\n", joe);
	Person_print(joe);

	printf("Anne is at memory location %p:\n", joe);
	Person_print(anne);

	Person_destroy(joe);
	Person_destroy(anne);
	
	return 0;
}
