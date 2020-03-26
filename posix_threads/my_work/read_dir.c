#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <time.h>

//Just read current dir and print the file and dir names.

void main (int argc, char *argv[])
{
    int status = 0;
    struct stat filestat;

    status = lstat (argv[1], &filestat);

    switch(filestat.st_mode & S_IFMT) {
        case S_IFBLK:  printf("block device\n");            break;
        case S_IFCHR:  printf("character device\n");        break;
        case S_IFDIR:  printf("directory\n");               break;
        case S_IFIFO:  printf("FIFO/pipe\n");               break;
        case S_IFLNK:  printf("symlink\n");                 break;
        case S_IFREG:  printf("regular file\n");            break;
        case S_IFSOCK: printf("socket\n");                  break;
        default:       printf("unknown?\n");                break;
    }

    printf("I-node number:            %ld\n", (long) filestat.st_ino);

    printf("Mode:                     %lo (octal)\n",
            (unsigned long) filestat.st_mode);

    printf("Link count:               %ld\n", (long) filestat.st_nlink);
    printf("Ownership:                UID=%ld   GID=%ld\n",
            (long) filestat.st_uid, (long) filestat.st_gid);

    printf("Preferred I/O block size: %ld bytes\n",
            (long) filestat.st_blksize);
    printf("File size:                %lld bytes\n",
            (long long) filestat.st_size);
    printf("Blocks allocated:         %lld\n",
            (long long) filestat.st_blocks);

    printf("Last status change:       %s", ctime(&filestat.st_ctime));
    printf("Last file access:         %s", ctime(&filestat.st_atime));
    printf("Last file modification:   %s", ctime(&filestat.st_mtime));


}
