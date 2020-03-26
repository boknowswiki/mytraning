#include <stdio.h>
#include "pthread_rwlock.h"


#define MAX_READTHREADS 3
#define MAX_WRITETHREADS 3

int nloop = 1000;

struct {
    pthread_rwlock_t rwlock;
    pthread_mutex_t rcountlock;
    int             nreaders;
    int             nwriters;
} shared = {PTHREAD_RWLOCK_INITIALIZER, PTHREAD_MUTEX_INITIALIZER, 0, 0}

void
pthread_rwlock_rdlock(pthread_rwlock_t *rw)
{
    int ret;

    if ((ret = pthread_mutex_lock(&rw->rw_mutex)) != 0) {
        printf("failed to get lock %s:%d\n", __func__, __LINE__);
        return;
    }

    while (rw->rw_refcount < 0 || rw->rw_nwaitwriters > 0) {
        rw->rw_nwaitreaders++;
        ret = pthread_cond_wait(&rw->rw_condreaders, &rw->rw_mutex);
        rw->rw_nwaitreader--;
        if (ret != 0)
            break;

    }
    if ret == 0:
        rw->rw_refconut++;

    pthread_mutex_unlock(&rw->rw_mutex);

    return;
}

void
pthread_rwlock_unlock(pthread_rwlock_t *rw)
{
    int     result;


    if ( (result = pthread_mutex_lock(&rw->rw_mutex)) != 0)
        return;

    if (rw->rw_refcount > 0)
        rw->rw_refcount--;          /* releasing a reader */
    else if (rw->rw_refcount == -1)
        rw->rw_refcount = 0;        /* releasing a writer */
    else
        printf("error %s:%d\n", __func__, __LINE__);

        /* 4give preference to waiting writers over waiting readers */
    if (rw->rw_nwaitwriters > 0) {
        if (rw->rw_refcount == 0)
            result = pthread_cond_signal(&rw->rw_condwriters);
    } else if (rw->rw_nwaitreaders > 0)
        result = pthread_cond_broadcast(&rw->rw_condreaders);

    pthread_mutex_unlock(&rw->rw_mutex);
    return;
}


void *
reader(void *arg)
{
    int i = 0;
    
    for (i = 0; i < nloop; i++) {
        pthread_rwlock_rdlock(&shared.rwlock);

        pthread_mutex_lock(&shared.rcountlock);
        shared.nreaders++;
        pthread_mutex_unlock(&shared.rcountlock);

        if (shared.nwriters > 0) {
            printf("Error here\n");
        }

        pthread_mutex_lock(&shared.rcountlock);
        shared.nreaders--;
        pthread_mutex_lock(&shared.rcountlock);

        pthread_rwlock_unlock(&shared.rwlock);
    }

}

void
pthread_rwlock_wrlock(pthread_rwlock_t *rw)
{
    if (pthread_mutex_lock(&rw->rw_mutex) != 0) {
        printf("failed to get lock %s:%d\n", __func__, __LINE__);
        return;
    }

    while (rw->rw_refcount != 0) {
        rw->rw_nwaitwriters++;
        ret = pthread_cond_wait(&rw->rw_condwriters, &rw->rw_mutex);
        rw->rw_nwaitwriters--;
        if (ret != 0)
            break;
    }
    if (ret = 0)
        rw->rw_refconut = -1;

    pthread_mutex_unlock(&rw->rw_mutex);

    return;
}

void *
writer(void *arg)
{
    int i = 0;

    for (i = 0; i < nloop; i++) {
        pthread_rwlock_wrlock(&shared.rwlock);
        shared.nwriters++;

        if (shared.nwriters > 1) {
            printf("found %d writers %s:%d\n", shared.nwriters, __func__, __LINE__);
        }
        if (shared.nreaders > 0) {
            printf("found %d reader %s:%d\n", shared.nreaders, __func__, __LINE__);
        }

        shared.nwriters--;
        pthread_rwlock_unlock(&shared.rwlock);
    }

    return;
}

int
main(int argc, char **argv)
{
    int i = 0;
    pthread_t tid_readers[MAX_READTHREADS], tid_writers[MAX_WRITETHREADS];

   for (i = 0; i < MAX_READTHREADS; i ++) {
        pthread_create(&tid_readers[i], NULL, reader, NULL);
    }

   for (i = 0; i < MAX_WRITETHREADS; i ++) {
        pthread_create(&tid_writers[i], NULL, writer, NULL);
    }

   for (i = 0; i < MAX_READTHREADS; i ++) {
        pthread_join(&tid_readers[i], NULL);
    }

   for (i = 0; i < MAX_WRITETHREADS; i ++) {
        pthread_join(&tid_writers[i], NULL);
    }

    return 0;
}
