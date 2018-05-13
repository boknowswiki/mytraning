#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/wait.h>
#include <errno.h>

#define MAXLEN  128
#define FIFO_SERV   "/tmp/fifo.serv"
#define FILE_MODE   (S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH)

static int
my_read(int fd, char *ptr)                                        
{
    static int  read_cnt = 0;
    static char *read_ptr;
    static char read_buf[MAXLEN];
 
    if (read_cnt <= 0) {
again:
        if ( (read_cnt = read(fd, read_buf, sizeof(read_buf))) < 0    ) {
            if (errno == EINTR)
                goto again;
            return(-1);
        } else if (read_cnt == 0)
            return(0);
        read_ptr = read_buf;
    }    
   
    read_cnt--;
    *ptr = *read_ptr++;
    return(1);
} 

int
readline(int fd, void *vptr, size_t maxlen)
{  
    int     n, rc;
    char    c, *ptr;
   
    ptr = vptr;
    for (n = 1; n < maxlen; n++) {
        if ( (rc = my_read(fd, &c)) == 1) {
            *ptr++ = c;
            if (c == '\n')
                break;  /* newline is stored, like fgets() */
        } else if (rc == 0) {
            if (n == 1)
                return(0);  /* EOF, no data read */
            else
                break;      /* EOF, some data was read */
        } else
            return(-1);     /* error, errno set by read() */
    }
   
    *ptr = 0;   /* null terminate like fgets() */
    return(n);
}
/* end readline */


int main(int argc, char *argv[])
{
    int i = 0;
    pid_t pid;
    int rd_fifo, wr_fifo, dummy_fifo;
    char buf[MAXLEN+1];
    int n, len;
    int fd;
    char *ptr, fifo_client[MAXLEN];
    char name[MAXLEN];

    for(i = 0; i < argc; i++)
        printf("%d, %s\n", i, argv[i]);

    if(mkfifo(FIFO_SERV, FILE_MODE) != 0) {
        printf("create fifo1 failed.\n");
        exit(-1);
    }

    rd_fifo = open(FIFO_SERV, O_RDONLY);
    dummy_fifo = open(FIFO_SERV, O_WRONLY);

    while((n = readline(rd_fifo, buf, MAXLEN)) > 0) {
        printf("get %s, len %d.\n", buf, n);
    
        if (buf[n-1] == '\n')
            n--;
        buf[n] = '\0';
    
        if ((ptr = strchr(buf, ' ')) == NULL) {
            printf("wrong command\n");
            continue;
        }
    
        *ptr++ = 0;
    
        pid = atoi(buf);
    
        snprintf(fifo_client, sizeof(fifo_client), "/tmp/fifo.%d", pid);
    
        printf("fifo_client is %s\n", fifo_client);
        if ((wr_fifo = open(fifo_client, O_WRONLY)) < 0) {
            printf("wr_fifo open failed\n");
            continue;
        }
    
        //printf("ptr is %s, len %d\n", ptr, strlen(ptr));
        //snprintf(name, len-1, "%s", ptr);
        if ((fd = open(ptr, O_RDONLY)) < 0) {
            snprintf(buf+n, sizeof(buf) - n, "can not open.\n");
            n = sizeof(buf);
            write(wr_fifo, buf, n);
        }
        else {
            //printf("buf is %s\n", buf);
            while((n = read(fd, buf, MAXLEN)) > 0) {
                //printf("buf is %s\n", buf);
                write(wr_fifo, buf, n);
                //printf("%s write buf %s\n", __func__, buf);
            }
            close(fd);
            close(wr_fifo);
        }
    }
}
