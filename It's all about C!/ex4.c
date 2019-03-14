#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>

void die(const char *message)
{
	if(errno)
		perror(message);
	else
		printf("ERROR: %s\n", message);

	exit(EXIT_FAILURE);
}

typedef int (*compare_cb) (int a, int b);

int *bubble_sort(int *numbers, int count, compare_cb cmp)
{
	int temp = 0, i, j;
	int *target = malloc(count *sizeof(int));

	if(!target)
		die("Memory error.\n");

	memcpy(target, numbers, count * sizeof(int));

	for(i = 0; i < count; i++)
	{
		for(j = 0; j < count - 1; j++)
		{
			if(cmp(target[j], target[j + 1]) > 0)
			{
				temp = target[j + 1];
				target[j + 1] = target[j];
				target[j] = temp;
			}
		}
	}

	return target;
}

int sorted_order(int a, int b)
{
	return a - b;
}

int reverse_order(int a, int b)
{
	return b - a;
}

int strange_order(int a, int b)
{
	if(a == 0 || b == 0)
		return 0;
	else
		return a % b;
}

void test_sorting(int *numbers, int count, compare_cb cmp)
{
	int i;
	int *sorted = bubble_sort(numbers, count, cmp);

	if(!sorted)
		die("Failed to sort as requested..");

	for (i = 0; i < count; i++){
		printf("%d", sorted[i]);
	}
	printf("\n");

	free(sorted);
	
	// this tiny little insignificant part of code
	// prints out raw assembly bytecode of cmp function *-*
	unsigned char *data = (unsigned char *)cmp;

	for (i = 0; i < 25; i++) {
		printf("%02x:", data[i]);
	}
	printf("\n");
}

int main(int argc, char *argv[])
{
	if (argc < 2) die("USAGE: ex4 4 3 1 5 6");

	int count = argc - 1;
	int i;
	char **inputs = argv + 1;

	int *numbers = malloc(count * sizeof(int));
	if (!numbers) die("Memory error.\n");

	for (i = 0; i < count; i++)
		numbers[i] = atoi(inputs[i]);

	test_sorting(numbers, count, sorted_order);
	test_sorting(numbers, count, reverse_order);
	test_sorting(numbers, count, strange_order);
	
	free(numbers);

	return 0;
}
