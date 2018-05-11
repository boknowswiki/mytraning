#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

void client(int wr_p, int rd_p)
{
    char buf[128];
    int len;
    int n;

    fgets(buf, 128, stdin);
    len = strlen(buf);
    if (buf[len-1] == '\n')
        len--;

    write(wr_p, buf, len);

    while(n = read(rd_p, buf, 128) > 0)
        write(stdout, buf, n);
}

void server(int rd_p, int wr_p)
{
    char buf[128];
    int len;
    int n;
    int fd;

    if((n = read(rd_p, buf, 128)) == 0) {
        printf("read 0 byte\n");
    }

    buf[n] = '\0';

    if ((fd = open(buf, O_RDONLY)) < 0) {
        snprintf(buf+n, sizeof(buf) - n, "can not open.\n");
        n = sizeof(buf);
        write(wr_p, buf, n);
    }
    else {
        while(n = read(rd_p, buf, 128) >0)
            write(wr_p, buf, n);
        close(fd);
    }

}

int main(int argc, char *argv[])
{
    int i = 0;
    int p1[2], p2[2];
    pid_t pid;

    for(i = 0; i < argc; i++)
        printf("%d, %s\n", i, argv[i]);

    if(pipe(p1) != 0) {
        printf("create p1 failed.\n");
        exit(-1);
    }


    if(pipe(p2) != 0) {
        printf("create p2 failed.\n");
        exit(-1);
    }

    pid = fork();

    if(pid == 0) {
    //server
        close(p1[1]);
        close(p2[0]);
        server(p1[0], p2[1]);
        exit(0);
    }
    else {
    //client
        close(p1[0]);
        close(p2[1]);
        client(p1[1], p2[0]);
        waitpid(pid, NULL, 0);
        exit(0);
    }

    //return 0;
}
