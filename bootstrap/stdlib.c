#define SYSCALL_WRITE 1

int __print(unsigned fd, const char *buf, unsigned count) {
    unsigned ret;

    asm volatile
    (
    "syscall"
    : "=a"(ret)
    : "a"(SYSCALL_WRITE), "D"(fd), "S"(buf), "d"(count)
    : "rcx", "r11", "memory"
    );

    return ret;
}

int __stringlength(const char *p) {
    const char *start = p;
    while (*p) p++;
    return (p - start);
}

int __reverse(char s[]) {
    int i, j;
    char c;

    for (i = 0, j = __stringlength(s) - 1; i < j; i++, j--) {
        c = s[i];
        s[i] = s[j];
        s[j] = c;
    }

    return 0;
}

int __itoa(int n, char s[]) {
    int i, sign;

    if ((sign = n) < 0)
        n = -n;
    i = 0;
    do {
        s[i++] = n % 10 + '0';
    } while ((n /= 10) > 0);
    if (sign < 0)
        s[i++] = '-';
    s[i] = '\0';
    __reverse(s);

    return 0;
}

int printint(int i) {
    char str[20];
    __itoa(i, str);
    __print(1, str, __stringlength(str));
    return 0;
}