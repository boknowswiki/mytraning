#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/wait.h>

#define MAXLEN  128
#define FIFO_SERV   "/tmp/fifo.serv"
#define FILE_MODE   (S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH)

int main(int argc, char *argv[])
{
    int i = 0;
    pid_t pid;
    int rd_fifo, wr_fifo;
    char fifo_client[MAXLEN];
    char buf[MAXLEN];
    int len, n, minus_one = 0;
    char *ptr;

    for(i = 0; i < argc; i++)
        printf("%d, %s\n", i, argv[i]);

    pid = getpid();

    printf("%s pid %d.\n", __func__, pid);
    snprintf(fifo_client, sizeof(fifo_client), "/tmp/fifo.%d", pid);
    snprintf(buf, sizeof(buf), "%d ", pid);
    len = strlen(buf);
    printf("len %d\n", len);
    ptr = buf + len;

    if(mkfifo(fifo_client, FILE_MODE) != 0) {
        printf("create fifo1 failed.\n");
        exit(-1);
    }

    printf("entry file name: ");
    fgets(ptr, MAXLEN - len, stdin);
    printf("ptr is %s\n", ptr);
    len = strlen(ptr);
#if 0
    if (ptr[len-1] == '\n')
        minus_one = 1;
#endif
    len = strlen(buf);
    printf("len %d\n", len);
    len = len - minus_one;

    wr_fifo = open(FIFO_SERV, O_WRONLY);

    printf("write to server %s\n", buf);
    write(wr_fifo, buf, len);

    rd_fifo = open(fifo_client, O_RDONLY);
    while((n = read(rd_fifo, buf, MAXLEN)) > 0) {
        //printf("buf is %s\n", buf);
        //write(STDOUT_FILENO, buf, n);
        write(1, buf, n);
        //write(stdout, buf, n);
        //puts(buf);
        //fprintf(stdout, "%s", buf);
    }

    close(wr_fifo);
    close(rd_fifo);

    unlink(fifo_client);
    exit(0);
}
