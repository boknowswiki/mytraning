#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <time.h>

typedef struct alarm_s {
	char message[128];
	int seconds;
	int sleep_time;
	struct alarm_s * next;
} alarm_t;

pthread_mutex_t alarm_mutex = PTHREAD_MUTEX_INITIALIZER;
alarm_t	*alarm_list = NULL;

void *thread_alarm_work(void *arg)
{
	alarm_t *new;
	int status;
    time_t now;
    int sleep_time;

//printf("%s:%d\n", __func__, __LINE__);
    while(1) {
        pthread_mutex_lock(&alarm_mutex);

//printf("%s:%d\n", __func__, __LINE__);
        new = alarm_list;

        if (new == NULL)
            sleep_time = 1;
        else {
            alarm_list = new->next;
            now = time(NULL);
            if (new->sleep_time <= now)
                sleep_time = 0;
            else
                sleep_time = new->sleep_time - now;
        }

//printf("%s:%d\n", __func__, __LINE__);
        pthread_mutex_unlock(&alarm_mutex);

        if (sleep_time > 0)
            sleep(sleep_time);
        else
            sched_yield();

        if (new != NULL) {
	        printf("%d, %s\n", new->seconds, new->message);
            free(new);
        }
//printf("%s:%d\n", __func__, __LINE__);
    }
}

int main (int argc, char *argv[])
{
	char cmd[128] = "\0";
	int status = 0;
	char prompt[64] = "Enter alarm > ";
	pthread_t tid;
	alarm_t *new_alarm;
    alarm_t **head, *next;

	if (argc >= 2) {
		printf("Usage: %s <alarm_in_seconds> <message>\n", argv[0]);
		return -1;
	}

//printf("%s:%d\n", __func__, __LINE__);
	status = pthread_create(&tid, NULL, thread_alarm_work, NULL);
	if (status != 0) {
		printf("pthread create failed.\n");
		abort();
	}
//printf("%s:%d\n", __func__, __LINE__);

	fprintf(stdout, "%s", prompt);

	while (fgets(cmd, sizeof(cmd), stdin) != NULL) {
//printf("%s:%d\n", __func__, __LINE__);
		new_alarm = (alarm_t*)malloc(sizeof(alarm_t));
		if (sscanf(cmd, "%d %128s", &new_alarm->seconds,
				new_alarm->message) < 2) {
			printf("bad arguments.\n");
			free(new_alarm);
		} else {
			pthread_mutex_lock(&alarm_mutex);
			new_alarm->sleep_time = time(NULL) + new_alarm->seconds;

            head = &alarm_list;
            next = *head;
            while (next != NULL) {
                if (next->sleep_time < new_alarm->sleep_time) {
                    head = &next;
                    next = next->next;
                }
                else {
                    new_alarm->next = next;
                    *head = new_alarm;
                    break;
                }
            }

            if (next == NULL) {
                *head = new_alarm;
                new_alarm->next = NULL;
            }

#if 0
            for (next = alarm_list; next != NULL; next = next->next) {
                printf("%d(%d) %s\n", next->sleep_time, next->seconds, next->message);
            }
#endif

            pthread_mutex_unlock(&alarm_mutex);
		}
		fprintf(stdout, "%s", prompt);
	}

	return 0;
}
