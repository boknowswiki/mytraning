#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>


int main (int argc, char *argv[])
{
	char cmd[128] = "\0";
	int status = 0;
	char prompt[64] = "Enter alarm > ";
	char message[128] = "\0";
	int val = 0;

	if (argc >= 2) {
		printf("Usage: %s <alarm_in_seconds> <message>\n", argv[0]);
		return -1;
	}

	fprintf(stdout, "%s", prompt);

	while (fgets(cmd, sizeof(cmd), stdin) != NULL) {
		//printf("gets %s\n", cmd);
		//val = atoi(cmd);
		if (sscanf(cmd, "%d %128s", &val, message) < 2) {
			printf("bad arguments.\n");
		} else {
			sleep(val);
			printf("slept %d, %s.\n", val, message);
		}
		fprintf(stdout, "%s", prompt);
	}

	return 0;
}
