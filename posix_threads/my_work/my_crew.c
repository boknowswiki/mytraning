#include <sys/types.h>
#include <pthread.h>
#include <sys/stat.h>
#include <dirent.h>
#include "errors.h"

#define CREW_SIZE   2

typedef struct work_s {
    struct work_s   *next;
    char            *path;
    char            *string;
} work_t;

typedef struct worker_s {
    pthread_t   thread_id;
    struct  crew_s  *crew;
    int         index;
    
} worker_t;

typedef struct crew_s {
    pthread_mutex_t crew_mutex;
    pthread_cond_t  crew_done;
    pthread_cond_t  crew_ready;
    int             crew_size;
    int             work_count;
    work_t          *head, *tail;
    worker_t        crew[CREW_SIZE];
} crew_t;

size_t  path_max;
size_t  name_max;


int start_crew (crew_t *c, char *path, char *string)
{
    work_t  *r;
    int status;

    status = pthread_mutex_lock(&c->crew_mutex);
    if (status)
        return status;

    while (c->crew_count > 0) {
        status = pthread_cond_wait(&c->crew_done, &c->crew_mutex);
        if (status) {
            pthread_mutex_unlock(&c->crew_mutex);
            return status;
        }
    }

    errno = 0;
    path_max = pathconf(path, __PC_PATH_MAX);
    
    errno = 0;
    name_max = pathconf(path, __PC_NAME_MAX);

    r = (work_t*)malloc(sizeof(work_t));
    if (r == NULL) {
        printf("malloc r failed.\n");
        pthread_mutex_unlock(&c->crew_mutex);
        abort();
    }

    r->path = (char*)malloc(sizeof(path_max));
    if (r->path == NULL) {
        printf("malloc r->path failed.\n");
        pthread_mutex_unlock(&c->crew_mutex);
        abort();
    }

    strcpy(c->path, path);
    strcpy(c->string, string);
    r->next = NULL;

    if (c->head == NULL) {
        c->head = r;
        c->tail = r;
    } else {
        c->tail->next = r;
        c->tail = r;
    }

    c->work_count++;

    status = pthread_cond_signal(&c->ready);
    if (status) {
        free(r->path);
        free(r);
        c->head = NULL;
        c->work_count = 0;
        pthread_mutex_unlock(&c->crew_mutex);
        return status;
    }

    while (c->work_count > 0) {
        status = pthread_signal_wait(&c->crew_done, &c->crew_mutex);
        if (status)
            err_abort(status, "waiting for crew to finish failed.\n");
    }

    status = pthread_mutex_unlock(&c->crew_mutex);
    if (status)
        err_abort(status, "unlock failed.\n");

    return 0;
}

int create_crew (crew_t *c, int c_size)
{
    int c_index = 0;
    int status = 0;

    if (c_size > CREW_SIZE)
        return EINVAL;

    c->crew_size = c_size;
    c->work_count = 0;
    c->head = c->tail = NULL;

    status = pthread_mutex_init(&c->crew_mutex, NULL);
    if (status)
        return status;

    status = pthread_cond_init(&c->done, NULL);
    if (status)
        return status;

    status = pthread_cond_init(&c->ready, NULL);
    if (status)
        return status;

    for (c_index = 0; c_index < c_size; c_index++) {
        status = pthread_create(&(c->[c_index].thread_id), NULL,
                        worker_routine, (void*)c->[c_index]);
        if (status)
            err_abort(status, "pthread_create failed".\n);
    }

    return 0
}

int main (int argc, char *argv[])
{
    crew_t my_crew;
    int status = 0;

    if (argc < 3) {
        printf("Usages: %s string path\n", argv[0]);
        return -1;
    }

    status = create_crew(&my_crew, CREW_SIZE);

    if (status)
        err_abort(status, "create_crew failed".\n);

    status = start_crew(&my_crew, argv[2], argv[1]);

    if (status)
        err_abort(status, "start_crew failed.n\n");

    return 0;
}

