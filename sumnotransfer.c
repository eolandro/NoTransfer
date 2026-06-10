#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>

//char secreto[] = {78, 111, 104, 97, 99, 107, 80, 87, 0};
int main(int argc, char **argv){
	if (argc <= 1){
		printf("Usage:\nsumnotransfer archivont");
		return 1;
	}
	srand(time(NULL));

	FILE *fnt;
	fnt = fopen(argv[1],"rb");
	int btdata = 0;
        uint8_t	tmp = 0;
	int na = 0;

	if (fnt == NULL){
		printf("No se puede abrir el archivont\n");
		return 1;
	}
	do{
		btdata = fgetc(fnt);
		if ( btdata != EOF ) {
			na = rand() % 256;
			if (na > btdata){
				printf("%d-%d\n",na,(na - btdata));
			}
			if (na < btdata){
				printf("%d+%d\n",(btdata - na),na);
			}
			if (btdata == 0){
				printf("1-1\n");
			}
			if (na == btdata){
				printf("%d+1\n",(btdata - 1));
			}
		}
	}while ( btdata != EOF );

	fclose(fnt);

	return 0;
}

