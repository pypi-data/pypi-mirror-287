/**
    This is a dummy file for libc functions. 
    It is an aproximation of the function with everything removed except for function calls and local variables

 */

// Simplified printf implementation
int printf( char *format, ...) {
    va_list args;
    //remove va_start and va_end
    int result = vprintf(format, args);
    return result;
}

// Simplified scanf implementation
int scanf( char *format, ...) {
    va_list args;
    //remove va_start and va_end
    int result = vfscanf(stdin, format, args);
    return result;
}

// Simplified fopen implementation
FILE *fopen( char *filename,  char *mode) {
    FILE *file = fopen(filename, mode);
    return file;
}

// Simplified fclose implementation
int fclose(FILE *stream) {
    int result = fclose(stream);
    return result;
}

// Simplified fread implementation
size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream) {
    size_t result = fread(ptr, size, nmemb, stream);
    return result;
}

// Simplified fwrite implementation
size_t fwrite( void *ptr, size_t size, size_t nmemb, FILE *stream) {
    size_t result = fwrite(ptr, size, nmemb, stream);
    return result;
}

// Simplified malloc implementation
void *malloc(size_t size) {
    void *ptr = malloc(size);
    return ptr;
}

// Simplified free implementation
void free(void *ptr) {
    free(ptr);
}

// Simplified memcpy implementation
void *memcpy(void *dest,  void *src, size_t n) {
    void *result = memcpy(dest, src, n);
    return result;
}

// Simplified memset implementation
void *memset(void *s, int c, size_t n) {
    void *result = memset(s, c, n);
    return result;
}

// Simplified strcpy implementation
char *strcpy(char *dest,  char *src) {
    char *result = strcpy(dest, src);
    return result;
}

// Simplified strlen implementation
size_t strlen( char *s) {
    size_t length = strlen(s);
    return length;
}

// Simplified strcmp implementation
int strcmp( char *s1,  char *s2) {
    int result = strcmp(s1, s2);
    return result;
}

// Simplified strcat implementation
char *strcat(char *dest,  char *src) {
    char *result = strcat(dest, src);
    return result;
}

// Simplified atoi implementation
int atoi( char *str) {
    int number = atoi(str);
    return number;
}

// Simplified exit implementation
void exit(int status) {
    exit(status);
}

// qsort comparison function
int compare_ints( void *a,  void *b) {
    int arg1 = *( int*)a;
    int arg2 = *( int*)b;
    return (arg1 - arg2);
}

// Simplified qsort implementation
void qsort(void *base, size_t nmemb, size_t size, int (*compar)( void *,  void *)) {
    qsort(base, nmemb, size, compar);
}

// Simplified bsearch implementation
void *bsearch( void *key,  void *base, size_t nmemb, size_t size, int (*compar)( void *,  void *)) {
    void *result = bsearch(key, base, nmemb, size, compar);
    return result;
}

// Main function
int main(int argc, char* argv[]) {
    return 0;
}
