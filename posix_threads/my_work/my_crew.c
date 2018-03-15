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

void *worker_routine(void *arg)
{
    worker_t *worker = (worker_t*)arg;
    crew_t *c = worker->crew;
    int status = 0;
    work_t *work, *new;
    struct stat filestat;
    struct dirent *entry;

    entry = (struct dirent*)malloc(sizeof(struct dirent) + name_max+1);
    if (entry == NULL)
        errno_abort("malloc entry failed.\n");

    status = pthread_mutex_lock(&c->crew_mutex);
    if (status)
        err_abort(status, "lock failed.\n");

    while (c->work_count == 0) {
        status = pthread_cond_wait(&c->crew_ready, &c->crew_mutex);
        if (status)
            err_abort(status, "wait for ready");
    }

    status = pthread_mutex_unlock(&c->crew_mutex);
    if (status)
        err_abort(status, "unlock mutex failed.\n");

    printf("worker %d starting.\n", worker->index);
    while (1) {
        status = pthread_mutex_lock(&c->crew_mutex);
        if (status)
            err_abort(status, "lock failed.\n");

        printf("worker %d: first %p, work_count %d.\n",
            worker->index, (void*)c->head, c->work_count);

        while (c->head == NULL) {
            status = pthread_cond_wait(&c->crew_ready, &c->crew_mutex);
            if (status)
                err_abort(status, "wait ready failed.\n");
        }

        printf("worker %d gets work: %lx, work_count %d.\n",
            worker->index, c->head, c->work_count);

        work = c->head;
        c->head = c->head->next;
        if (c->head == NULL)
            c->tail == NULL;

        status = pthread_mutex_unlock(&c->crew_mutex);
        if (status)
            err_abort(status, "unlock mutex failed.\n");

        status = lstat(work->path, &filestat);

        if (S_ISLNK(filestat.st_mode))
            printf("worker %d, %s is a link, skipping.\n",
                worker->index, work->path);
        else if (S_ISDIR(filestat.st_mode)) {
            DIR *dir;
            struct dirent *result;

            dir = opendir(work->path);
            if (dir == NULL) {
                printf("unable to open dir %s\n", work->path);
                continue;
            }

            while (1) {
                status = readdir_r(dir, entry, &result);
                if (status) {
                    printf("unable to read dir %s\n", work->path);
                    break;
                }

                if (result == NULL)
                    break;

                if (strcmp(entry->d_name, ".") == 0)
                    continue;
                if (strcmp(entry->d_name, "..") == 0)
                    continue;

                new = (work_t*)malloc(sizeof(work_t));
                if (new == NULL)
                    errno_abort("unable malloc new work.\n");

                new->path = (char*)malloc(path_max);
                if (new->path == NULL)
                    errno_abort("unable malloc new->path.\n");

                strcpy(new->path, work->path);
                strcat(new->path, "/");
                strcat(new->path, entry->d_name);
                new->string = work->string;
                new->next = NULL;
                status = pthread_mutex_lock(&c->crew_mutex);
                if (status)
                    err_abort(status, "failed to lock\n");

                if (c->head == NULL) {
                    c->head = new;
                    c->tail = new;
                } else {
                    c->tail->next = new;
                    c->tail = new;
                }

                c->work_count++;
                printf("worker %d, add work %lx, head %lx, \
                    tail %lx, work_count %d\n", worker->index, 
                    new, c->head, c->tail, c->work_count);
                status = pthread_cond_signal(&c->crew_ready);
                status = pthread_mutex_unlock(&c->crew_mutex);
                if (status)
                    err_abort(status, "failed to unlock\n");
            }

            closedir(dir);
        } else if (S_ISREG(filestat.st_mode)) {
            FILE *search;
            char buf[256], *buf_ptr, *search_ptr;

            search = fopen(work->path, "r");
            if (search == NULL)
                printf("unable to open file %s.\n", work->path);
            else {
                while (1) {
                    buf_ptr = fgets(buf, sizeof(buf), search);
                    if (buf_ptr == NULL) {
                        printf("end of the file or fgets fialed.\n");
                        break;
                    }
                    search_ptr = strstr(buf, work->string);
                    if (search_ptr != NULL) {
                        flockfile(stdout);
                        printf("worker %d found %s in %s\n",
                            worker->index, work->string, work->path);
                        funlockfile(stdout);
                        break;
                    }
                }
                fclose(search);
            }
        } else {
            printf("other types.\n");
        }

        free(work->path);
        free(work);

        status = pthread_mutex_lock(&c->crew_mutex);
        if (status)
            err_abort(status, "unlock failed\n");

        c->work_count--;
        printf("worker %d, decremented work to %d\n", 
            worker->index, c->work_count);

        if (c->work_count <= 0) {
            printf("crew work done %d\n", worker->index);
            status = pthread_cond_broadcast(&c->crew_done);
            if (status)
                err_abort(status, "broadcast failed\n");
            status = pthread_mutex_unlock(&c->crew_mutex);
            if (status)
                err_abort(status, "unlock failed\n");
            break;
        }

        status = pthread_mutex_unlock(&c->crew_mutex);
        if (status)
           err_abort(status, "unlock failed\n");
    }

    free(entry);

    return NULL;
}

int start_crew (crew_t *c, char *path, char *string)
{
    work_t  *r;
    int status;

    status = pthread_mutex_lock(&c->crew_mutex);
    if (status)
        return status;

    while (c->work_count > 0) {
        status = pthread_cond_wait(&c->crew_done, &c->crew_mutex);
        if (status) {
            pthread_mutex_unlock(&c->crew_mutex);
            return status;
        }
    }

    errno = 0;
    path_max = pathconf(path, _PC_PATH_MAX);
    printf("path_max %d.\n", path_max);
    if (path_max == -1) {
        if (errno != 0)
            errno_abort("unable to get path_max\n");
    }
    
    errno = 0;
    name_max = pathconf(path, _PC_NAME_MAX);
    printf("name_max %d.\n", name_max);
    if (name_max == -1) {
        if (errno != 0)
            errno_abort("unable to get name_max\n");
    }

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

    printf("path %s, string %s.\n", path, string);
    strcpy(r->path, path);
    //strcpy(r->string, string);
    r->string = string;
    r->next = NULL;

    if (c->head == NULL) {
        c->head = r;
        c->tail = r;
    } else {
        c->tail->next = r;
        c->tail = r;
    }

    c->work_count++;

    status = pthread_cond_signal(&c->crew_ready);
    if (status) {
        free(r->path);
        free(r);
        c->head = NULL;
        c->work_count = 0;
        pthread_mutex_unlock(&c->crew_mutex);
        return status;
    }

    while (c->work_count > 0) {
        status = pthread_cond_wait(&c->crew_done, &c->crew_mutex);
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

    status = pthread_cond_init(&c->crew_done, NULL);
    if (status)
        return status;

    status = pthread_cond_init(&c->crew_ready, NULL);
    if (status)
        return status;

    for (c_index = 0; c_index < c_size; c_index++) {
        c->crew[c_index].index = c_index;
        c->crew[c_index].crew = c;
        status = pthread_create(&(c->crew[c_index].thread_id), 
                    NULL, worker_routine, (void*)&c->crew[c_index]);
        if (status)
            err_abort(status, "pthread_create failed.\n");
    }

    return 0;
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
        err_abort(status, "create_crew failed.\n");

    status = start_crew(&my_crew, argv[2], argv[1]);

    if (status)
        err_abort(status, "start_crew failed.n\n");

    return 0;
}

