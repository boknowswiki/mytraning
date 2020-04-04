#include <pthread.h>

typedef struct {
    pthread_mutex_t rw_mutex;
    pthread_cond_t  rw_condreader;
    pthread_cond_t  rw_condwriters;
    int             rw_nwaitreaders;
    int             rw_nwaitwriters;
    int             rw_refcount;
} pthread_rwlock_t;

#define PTHREAD_RWLOCK_INITIALIZER  { PTHREAD_MUTEX_INITIALIZER, \
            PTHREAD_COND_INITIALIZER, PTHREAD_COND_INITIALIZER, \
            0, 0, 0 }
