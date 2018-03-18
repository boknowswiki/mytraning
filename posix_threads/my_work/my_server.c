#include <pthread.h>
#include "errors.h"

#define CLIENT_NUM  3

#define REQ_READ    0
#define REQ_WRITE   1
#define REQ_QUIT    2

typedef struct request_s {
    pthread_cond_t          request_done;
    int                     operation;
    char                    prompt[64];
    char                    text[128];
    int                     request_done_flag;
    int                     sync;
    struct request_s        *next;
} request_t;

typedef struct server_s {
    request_t   *first;
    request_t   *last;
    int         running;
    pthread_mutex_t server_mutex;
    pthread_cond_t  server_request;
    pthread_t   thread_id;
} server_t;

typedef struct client_s {
    pthread_mutex_t client_mutex;
    pthread_cond_t  client_done;
    int             index[CLIENT_NUM];
    server_t        server;
    pthread_t       thread_id[CLIENT_NUM];
} client_t;

int client_running;
client_t    my_client;
server_t    my_server;

void *server_routine(void *arg)
{
    request_t *request;
    int operation, len;
    int status = 0;

    while (1) {
        status = pthread_mutex_lock (&my_server.server_mutex);
        if (status != 0)
            err_abort (status, "Lock server mutex");

        /*
         * Wait for data
         */
        while (my_server.first == NULL) {
            status = pthread_cond_wait (
                &my_server.server_request, &my_server.server_mutex);
            if (status != 0)
                err_abort (status, "Wait for request");
        }
        request = my_server.first;
        my_server.first = request->next;
        if (my_server.first == NULL)
            my_server.last = NULL;
        status = pthread_mutex_unlock (&my_server.server_mutex);
        if (status != 0)
            err_abort (status, "Unlock server mutex");

        /*
         * Process the data
         */
        operation = request->operation;
        switch (operation) {
            case REQ_QUIT:
                break;
            case REQ_READ:
                if (strlen (request->prompt) > 0)
                    printf (request->prompt);
                if (fgets (request->text, 128, stdin) == NULL)
                    request->text[0] = '\0';
                /*
                 * Because fgets returns the newline, and we don't want it,
                 * we look for it, and turn it into a null (truncating the
                 * input) if found. It should be the last character, if it is
                 * there.
                 */
                len = strlen (request->text);
                if (len > 0 && request->text[len-1] == '\n')
                    request->text[len-1] = '\0';
                break;
            case REQ_WRITE:
                puts (request->text);
                break;
            default:
                break;
        }
        if (request->sync) {
            status = pthread_mutex_lock (&my_server.server_mutex);
            if (status != 0)
                err_abort (status, "Lock server mutex");
            request->request_done_flag = 1;
            status = pthread_cond_signal (&request->request_done);
            if (status != 0)
                err_abort (status, "Signal server condition");
            status = pthread_mutex_unlock (&my_server.server_mutex);
            if (status != 0)
                err_abort (status, "Unlock server mutex");
        } else
            free (request);
        if (operation == REQ_QUIT)
            break;
    }
    return NULL;

}

void server_request (int operation, int sync, char *prompt, char *text)
{
    request_t *request;
    int status;

    status = pthread_mutex_lock(&my_server.server_mutex);
    if (status)
        err_abort(status, "pthread_mutex_lock failed.\n");

    request = (request_t*)malloc(sizeof(request_t));
    if (request == NULL)
        errno_abort("request malloc failed.\n");

    request->next = NULL;
    request->operation = operation;
    request->sync = sync;

    if (request->sync) {
        request->request_done_flag = 0;
        status = pthread_cond_init(&request->request_done, NULL);
        if (status)
            err_abort(status, "pthread_cond_init request_done failed.\n");
    }

    if (prompt != NULL)
        strncpy(request->prompt, prompt, 64);
    else
        request->prompt[0] = '\0';
    if (operation == REQ_WRITE && text != NULL)
        strncpy(request->text, text, 128);
    else
        request->text[0] = '\0';

    //printf("request->prompt %s, request->text %s\n", request->prompt, request->text);

    if (my_server.first == NULL) {                   
        my_server.first = request;                   
        my_server.last = request;                    
    } else {                                          
        (my_server.last)->next = request;            
        my_server.last = request;                    
    } 

    status = pthread_cond_signal(&my_server.server_request);
    if (status)
        err_abort(status, "pthread_cond_signal failed.\n");

    if (sync) {
        while (!request->request_done_flag) {
            status = pthread_cond_wait(&request->request_done,
                    &my_server.server_mutex);
            if (status)
                err_abort(status, "pthread_cond_wait failed.\n");
        }

        if (operation == REQ_READ) {
            if(strlen(request->text) > 0)
                strcpy(text, request->text);
            else
                text[0] = '\0';
        }

        status = pthread_cond_destroy(&request->request_done);
        if (status)
            err_abort(status, "pthread_cond_desctroy failed.\n");
        free(request);
    }

    status = pthread_mutex_unlock(&my_server.server_mutex);
    if (status)
        err_abort(status, "pthread_mutex_unlock failed.\n");
}

void *client_routine(void *arg)
{
    int index = (int)arg;
    int loops = 0;
    char prompt[64];
    char text[128];
    char formatted[128];
    int status = 0;

    sprintf(prompt, "Client %d> ", index);
    //printf("prompt %s\n", prompt);

    while (1) {
        server_request(REQ_READ, 1, prompt, text);

        if (strlen(text) == 0)
            break;

        for (loops = 0; loops < 4; loops++) {
            sprintf(formatted, "(client %d loops %d write %s)", 
                    index, loops, formatted); 
            server_request(REQ_WRITE, 0, NULL, formatted);
            sleep(1);
        }
    }

    status = pthread_mutex_lock(&my_client.client_mutex);
    if (status)
        err_abort(status, "pthread_mutex_lock failed.\n");

    client_running--;

    if (client_running == 0) {
        status = pthread_cond_signal(&my_client.client_done);
        if (status)
            err_abort(status, "pthread_cond_signal failed.\n");
    }

    status = pthread_mutex_unlock(&my_client.client_mutex);
    if (status)
        err_abort(status, "pthread_mutex_unlock failed.\n");

    return NULL;
}

int create_client(client_t *c, int count)
{
    int status = 0;
    int index = 0;

    client_running = count;

    status = pthread_mutex_init(&c->client_mutex, NULL);
    if (status)
        err_abort(status, "pthread_mutex_init failed.\n");

    status = pthread_cond_init(&c->client_done, NULL);
    if (status)
        err_abort(status, "pthread_cond_init failed.\n");

    for (; index < count; index++) {
        c->index[index] = index;

        status = pthread_create(&c->thread_id[index], NULL,
                client_routine, c->index[index]);
        if (status)
            err_abort(status, "pthread_create failed.\n");
    }

    return 0;
}

int create_server(server_t *s)
{
    int status = 0;
    pthread_attr_t  detached_attr;

    status = pthread_attr_init(&detached_attr);
    if (status)
        err_abort(status, "pthread_attr_init failed.\n");

    status = pthread_attr_setdetachstate(&detached_attr,
                PTHREAD_CREATE_DETACHED);
    if (status)
        err_abort(status, "pthread_attr_setdetachstate failed.\n");

    status = pthread_mutex_init(&s->server_mutex, NULL);
    if (status)
        err_abort(status, "pthread_mutex_init failed.\n");

    status = pthread_cond_init(&s->server_request, NULL);
    if (status)
        err_abort(status, "pthread_cond_init failed.\n");

    s->first = s->last = NULL;

    status = pthread_create(&my_server.thread_id, &detached_attr,
                server_routine, NULL);
    if (status)
        err_abort(status, "pthread_create failed.\n");

    pthread_attr_destroy(&detached_attr);

    return 0;
}

int main (int argc, char argv[])
{
    int status = 0;

    status = create_server(&my_server);
    if (status)
        err_abort(status, "create server failed.\n");

    status = create_client(&my_client, CLIENT_NUM);
    if (status)
        err_abort(status, "create client failed.\n");

    status = pthread_mutex_lock(&my_client.client_mutex);
    if (status)
        err_abort(status, "pthread_mutex_lock failed.\n");
    
    while (client_running > 0) {
        status = pthread_cond_wait(&my_client.client_done,
                &my_client.client_mutex);
        if (status)
            err_abort(status, "pthread_cond_wait failed.\n");
    }

    status = pthread_mutex_unlock(&my_client.client_mutex);
    if (status)
        err_abort(status, "pthread_mutex_unlock failed.\n");

    printf("All done.\n");

    server_request(REQ_QUIT, 1, NULL, NULL);

    return 0;
}
