#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

#define NUMBER_OF_STRING 20
#define MAX_STRING_SIZE 100

void getname(char *buf);

int main(int argc, char **argv)
{

	srand(time(NULL));
	char quotes[NUMBER_OF_STRING][MAX_STRING_SIZE] =
	{ "Impossible is for the unwilling.",
	  "Stay foolish to stay sane.",
	  "When nothing goes right, go left.",
	  "Try Again. Fail again. Fail better.",
	  "Take the risk or lose the chance.",
          "It's okay to not be okay as long as you are not giving up.",
          "Everything is going to be okay in the end. If it's not the okay, it's not the end.",
          "Do it. With love.",
	  "It is better to be hated for what you are than to be loved for what you are not.",
          "Happiness lies in perspective.",
	  "The best way to pay for a lovely moment is to enjoy it. ",
	  "The ultimate mystery is one's own self.",
	  "It doesn't matter how slow you go as long as you don't stop.",
	  "A tiger doesn't lose sleep over the opinion of sheep.",
	  "What worries you, masters you.",
	  "There are no regrets in life, just lessons.",
	  "Showing off is the fool's idea of glory. ",
	  "Meowwww meoww.. meoww meow meowww! Meowwww?? Meow! Meow!",
	  "Failure is not fatal, but failure to change might be.",
	  "Find what you love and let it kill you."
	};

	if (argc < 2)
	{
		printf("%s [Your name here] \n",argv[0]);
		exit(0);
	}
	getname(argv[1]);
	printf("%s\n", quotes[rand()%20]);
	return 0;
}

void getname(char *buf)
{
	char buffer[32];
	strcpy(buffer,buf);
	printf("Hi %s,\n");
}
