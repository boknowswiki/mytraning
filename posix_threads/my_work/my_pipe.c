#include <stdio.h>
#include <string.h>
#include <pthread.h>
#include <stdlib.h>

#define MAX_STAGES  2
#define MAGIC       0xBEEF

typedef struct stage_s {
    pthread_mutex_t stage_mutex;
    pthread_cond_t  stage_avail;
    pthread_cond_t  stage_ready;
    int             data_ready;
    int             data;
    pthread_t       thread_id;
    struct stage_s  *next;
} stage_t;

typedef struct pipe_s {
    pthread_mutex_t pipe_mutex;
    stage_t         *head;
    stage_t         *tail;
    int             stages;
    int             active;
    int             magic;
} pipe_t;

void pipe_send (stage_t *stage, int data)
{
    pthread_mutex_lock(&stage->stage_mutex);

    while (stage->data_ready) {
        pthread_cond_wait(&stage->stage_ready, &stage->stage_mutex);
    }

    stage->data = data;
    stage->data_ready = 1;
    pthread_cond_signal(&stage->stage_avail);
    pthread_mutex_unlock(&stage->stage_mutex);
}

void *pipe_stage (void *arg)
{
    stage_t *stage = (stage_t *)arg;
    stage_t *next = stage->next;

    printf("%s: stage->thread_id %ld.\n", __func__, stage->thread_id);
    pthread_mutex_lock(&stage->stage_mutex);

    while (1) {
        while (!stage->data_ready) {
            pthread_cond_wait(&stage->stage_avail, &stage->stage_mutex);
        }

        pipe_send(next, stage->data+1);
        stage->data_ready = 0;
        pthread_cond_signal(&stage->stage_ready);
    }

}

void create_pipe (pipe_t *p, int stages)
{
    int i = 0, status = 0;
    stage_t **head = &p->head, *new_stage, *stage;
    pthread_mutex_init(&p->pipe_mutex, NULL);

    p->stages = stages;
    p->active = 0;
    p->magic = MAGIC;

    printf("%s: stages %d.\n", __func__, stages);
    for (i = 0; i < stages; i++) {
        new_stage = (stage_t *)malloc(sizeof(stage_t));
        if (new_stage == NULL) {
            printf("malloc failed.\n");
            return;
        }

        printf("new_stage address %p.\n", new_stage);

        pthread_mutex_init(&new_stage->stage_mutex, NULL);
        pthread_cond_init(&new_stage->stage_avail, NULL);
        pthread_cond_init(&new_stage->stage_ready, NULL);

        *head = new_stage;
        head = &new_stage->next;
    }

    *head = NULL;
    p->tail = new_stage;

    for (stage = p->head; stage != NULL; stage = stage->next) {
        printf("stage address %p\n", stage);
    }

    printf("creating threads.\n");
    for (stage = p->head; stage->next != NULL; stage = stage->next) {
        status = pthread_create(&stage->thread_id, NULL, pipe_stage, (void*)stage);
        if (status)
            printf("%s, pthread create failed %d.\n", __func__, status);
    }

    return;
}

void pipe_start(pipe_t *p, int data)
{
    if (p->magic != MAGIC) {
        printf("pipe not created yet.\n");
        return;
    }
    pthread_mutex_lock(&p->pipe_mutex);

    p->active++;

    pthread_mutex_unlock(&p->pipe_mutex);

    pipe_send(p->head, data);
}

void pipe_result(pipe_t *p, int *result)
{
    int empty = 0;
    stage_t *tail = p->tail;

    pthread_mutex_lock(&p->pipe_mutex);

    if(p->active <= 0)
        empty = 1;
    else
        p->active--;

    pthread_mutex_unlock(&p->pipe_mutex);

    if (empty) {
        printf("it's empty, return result 0\n");
        *result = 0;
        return;
    }

    pthread_mutex_lock(&tail->stage_mutex);

    while (!tail->data_ready) {
        pthread_cond_wait(&tail->stage_avail, &tail->stage_mutex);
    }
    *result = tail->data;
    tail->data_ready = 0;
    pthread_cond_signal(&tail->stage_ready);
    pthread_mutex_unlock(&tail->stage_mutex);
}

void main(int argc, char *argv[])
{
    pipe_t  my_pipe;
    int     data, result;
    char    cmd[128];

    create_pipe(&my_pipe, MAX_STAGES);

    while (1) {
        printf("cmd > ");
        if (fgets(cmd, sizeof(cmd), stdin) == NULL) exit(0);

        printf("cmd is %s\n", cmd);
        if (strlen(cmd) <= 1) {
            printf("cmd len <= 1.\n");
            continue;
        }
        if (strlen(cmd) <= 2 && cmd[0] == '=') {
            pipe_result(&my_pipe, &result);
            printf("result is %d\n", result);
        }
        else {
            sscanf(cmd, "%d", &data);
            printf("got data %d.\n", data);
            pipe_start(&my_pipe, data);
        }
    }
}
