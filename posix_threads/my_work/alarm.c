#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>

typedef struct alarm_s {
	char message[128];
	int seconds;
	int sleep_time;
	struct alarm_s * next;
} alarm_t;

pthread_mutex_t alarm_mutex = PTHREAD_MUTEX_INITIALIZER;
alarm_t	alarm_list = NULL;

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
	pthread_t tid;
	alarm_t *new_alarm;

	if (argc >= 2) {
		printf("Usage: %s <alarm_in_seconds> <message>\n", argv[0]);
		return -1;
	}

	status = pthread_create(&tid, NULL, thread_alarm_work, NULL);
	if (status != 0) {
		printf("pthread create failed.\n");
		abort();
	}

	fprintf(stdout, "%s", prompt);

	while (fgets(cmd, sizeof(cmd), stdin) != NULL) {
		new_alarm = (alarm_t*)malloc(sizeof(alarm_t));
		if (sscanf(cmd, "%d %128s", &new_alarm->seconds,
				new_alarm->message) < 2) {
			printf("bad arguments.\n");
			free(new_alarm);
		} else {
			pthread_mutex_lock(&alarm_mutex);
			new_alarm->sleep_time = time(NULL) + new_alarm->seconds;

			
		}
		fprintf(stdout, "%s", prompt);
	}

	return 0;
}
