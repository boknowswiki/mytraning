#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>


typedef struct alarm_s {
	char message[128];
	int sleep_time;
} alarm_t;

void *thread_alarm_work(void *arg)
{
	alarm_t *new = (alarm_t*)arg;
	int status;

	status = pthread_detach(pthread_self());
	if (status != 0) {
		printf("Thread detached failed.\n");
		abort();
	}

	sleep(new->sleep_time);
	printf("%s\n", new->message);
	free(new);

	return NULL;
}

int main (int argc, char *argv[])
{
	char cmd[128] = "\0";
	int status = 0;
	char prompt[64] = "Enter alarm > ";
	char message[128] = "\0";
	int val = 0;
	pid_t pid = 0;
	pthread_t tid;
	alarm_t *new_alarm;

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
			new_alarm = (alarm_t*)malloc(sizeof(alarm_t));
			new_alarm->sleep_time = val;
			strcpy(new_alarm->message, message);
			status = pthread_create(&tid, NULL, thread_alarm_work, new_alarm);
			if (status != 0) {
				printf("pthread create failed.\n");
				abort();
			}
		}
		fprintf(stdout, "%s", prompt);
	}

	return 0;
}
