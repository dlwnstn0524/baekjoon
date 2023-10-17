/**********************************************************************
 * Copyright (c) 2021-2023
 *  Sang-Hoon Kim <sanghoonkim@ajou.ac.kr>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 2 as
 * published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTIABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 **********************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <errno.h>

/* To avoid security error on Visual Studio */
#define _CRT_SECURE_NO_WARNINGS
#pragma warning(disable : 4996)

/*====================================================================*/
/*          ****** DO NOT MODIFY ANYTHING FROM THIS LINE ******       */
#define MAX_NR_TOKENS	16	/* Maximum length of tokens in a command */
#define MAX_TOKEN_LEN	32	/* Maximum length of single token */
#define MAX_ASSEMBLY	128 /* Maximum length of assembly string */

typedef unsigned char bool;
#define true	1
#define false	0
/*          ****** DO NOT MODIFY ANYTHING UP TO THIS LINE ******      */
/*====================================================================*/


/***********************************************************************
 * translate()
 *
 * DESCRIPTION
 *   Translate assembly represented in @tokens[] into a MIPS instruction.
 *   This translate should support following 13 assembly commands
 *
 *    - add
 *    - addi
 *    - sub
 *    - and
 *    - andi
 *    - or
 *    - ori
 *    - nor
 *    - lw
 *    - sw
 *    - sll
 *    - srl
 *    - sra
 *    - beq
 *    - bne
 *
 * RETURN VALUE
 *   Return a 32-bit MIPS instruction
 *
 */

// R: opcode(6) + rs(5) + rt(5) + rd(5) + shamt(5) + funct(6)
// I: opcode(6) + rs(5) + rt(5) + constant|address(16)
// J: opcode(6) + address(26)
static unsigned int translate(int nr_tokens, char *tokens[])
{
	/* TODO:
	 */
	int reg = 0x00000000; // 16진수 하나는 4비트임, 4비트 X 8 = 32비트 = 1 word
	typedef struct inst_struct{ // 원래 그냥 이차원 배열로 하려고 했는데 문자열 원소들 길이가 달라서 오류남
		char *name; // 원소가 다 문자열이니까 시작 주소를 저장한 것, 근데 원소들의 길이가 다 다르니까 차지하는 공간도 다르니까 주소를 저장!! 그 집에 누가 사는지는 중요하지 않음 집 주소가 중요
		char *op;
		char *funct;
		char type;
	} inst_t;

	typedef struct regi_struct{
		char *name;
		int num;
	}regi_t;

	// 명령어이름, opcode, funct, format
	// 
	inst_t assemblyArray[15] = {
		{"add", "0", "0x20", 'R'},
		{"addi", "0x08", "0", 'I'},
		{"sub", "0", "0x22", 'R'},
		{"and", "0", "0x24", 'R'},
		{"andi","0x0c", "0", 'I'},
		{"or", "0", "0x25", 'R'},
		{"ori", "0x0d", "0", 'I'},
		{"nor", "0", "0x27", 'R'},
		{"sll", "0", "0x00", 'R'},
		{"srl", "0", "0x02", 'R'},
		{"sra", "0", "0x03", 'R'},
		{"lw", "0x23", "0", 'I'},
		{"sw", "0x2b", "0", 'I'},
		{"beq", "0x04", "0", 'I'},
		{"bne", "0x05", "0", 'I'}
	};

	regi_t registerArray[32] = {
		{"zero", 0},
		{"at", 1},
		{"v0", 2},
		{"v1", 3},
		{"a0", 4},
		{"a1", 5},
		{"a2", 6},
		{"a3", 7},
		{"t0", 8},
		{"t1", 9},
		{"t2", 10},
		{"t3", 11},
		{"t4", 12},
		{"t5", 13},
		{"t6", 14},
		{"t7", 15},
		{"s0", 16},
		{"s1", 17},
		{"s2", 18},
		{"s3", 19},
		{"s4", 20},
		{"s5", 21},
		{"s6", 22},
		{"s7", 23},
		{"t8", 24},
		{"t9", 25},		
		{"k1", 26},
		{"k2", 27},
		{"gp", 28},
		{"sp", 29},
		{"fp", 30},
		{"ra", 31}
	};
	

	// *opcode 변환* x
	for (int i=0; i<15; i++) { // 명령어 개수만큼 반복 -> 전체를 탐색
		if(strcmp(tokens[0], assemblyArray[i].name) == 0){ // tokens 배열에 있는 명령어와 구조체에 들어있는 명령어의 이름이 같다면 
			int opcode = 0;
			int funct = 0;
			int rs = 0;
			int rt = 0;
			int rd = 0;
			int constant = 0;
			// int shamt = 0;
			char* end; // strtol
			
			switch(assemblyArray[i].type){
				case 'R':
					// 예외적인 shift 연산은 따로 분류
					if(strcmp(tokens[0], "sll") == 0 || strcmp(tokens[0], "srl") == 0 || strcmp(tokens[0], "sra") == 0){
						int shamt = 0;
						shamt = strtol(tokens[3], &end, 16);
						reg = reg | shamt << 6;
					}
					opcode = strtol(assemblyArray[i].op, &end, 16); // 16진수로 반환하는 이유: assemblyarray에 16진수 형태의 문자열이 저장되어있기 때문에
					funct = strtol(assemblyArray[i].funct, &end, 16);
					reg = reg | funct; // bit mask, reg에 funct 값 저장
					reg = reg | opcode << 26; // 레지스터는 32비트이므로 이를 맞춰주기 위해 다른 변수들도 (필요에 따라 앞이 0으로 채워진) 32 비트로 본다

					//(regi_t를 처음부터 끝까지 돌면서 rs, rt, rd 찾기, 가운데 5-5-5-5 채우기)
					for (int j=0; j<32; j++) {
						//rs
						if (strcmp(tokens[2], registerArray[j].name) == 0){ 
							rs = registerArray[j].num;
							reg = reg | rs << 21; 
						} 
						// rt
						if (strcmp(tokens[3], registerArray[j].name) == 0){
							rt = registerArray[j].num;
							reg = reg | rt << 16;
						}
						// rd
						if (strcmp(tokens[1], registerArray[j].name) == 0){
							rd = registerArray[j].num;
							reg = reg | rd << 11;
						}
					}
					break;

				case 'I':
					// op
					opcode = strtol(assemblyArray[i].op, &end, 16);
					reg = reg | opcode << 26;
					// lw, sw
					if (assemblyArray[i].name == "lw"){
						
					}
					//(regi_t를 처음부터 끝까지 돌면서 rs, rt, rd 찾기, 가운데 5-5 채우기)
					for (int j=0; j<32; j++){
						// rs
						if (strcmp(tokens[1], registerArray[j].name) == 0){
							// .name은 이미 정수니까 strtol 안 해도 됨
							rs = registerArray[j].num;
							reg = reg | rs << 21;
						}
						// rt
						if (strcmp(tokens[2], registerArray[j].name) == 0){
							rt = registerArray[j].num;
							reg = reg | rt << 16;
						}
						// constant&address
						constant = strtol(tokens[3], &end, 16);
						reg = reg | constant; 
						
					}
					break;
				default:
					break;
			}

			break;
		}
	} 

	
	return reg;
	// return 0x02324020;
}



/***********************************************************************
 * parse_command()
 *
 * DESCRIPTION
 *   Parse @assembly, and put each assembly token into @tokens[] and the number
 *   of tokes into @nr_tokens. You may use this implemention or your own
 *   from PA0.
 *
 *   A assembly token is defined as a string without any whitespace (i.e., space
 *   and tab in this programming assignment). For exmaple,
 *     command = "  add t1   t2 s0 "
 *
 *   then, nr_tokens = 4, and tokens is
 *     tokens[0] = "add"
 *     tokens[1] = "t0"
 *     tokens[2] = "t1"
 *     tokens[3] = "s0"
 *
 *   You can assume that the characters in the input string are all lowercase
 *   for testing.
 *
 *
 * RETURN VALUE
 *   Return 0 after filling in @nr_tokens and @tokens[] properly
 *
 */
static int parse_command(char *assembly, int *nr_tokens, char *tokens[])
{
	char *curr = assembly;
	int token_started = false;
	*nr_tokens = 0;

	while (*curr != '\0') {  
		if (isspace(*curr)) {
			*curr = '\0';
			token_started = false;
		} else {
			if (!token_started) {
				tokens[*nr_tokens] = curr;
				*nr_tokens += 1;
				token_started = true;
			}
		}
		curr++;
	}

	return 0;
}


/*====================================================================*/
/*          ****** DO NOT MODIFY ANYTHING BELOW THIS LINE ******      */

/***********************************************************************
 * The main function of this program.
 */
int main(int argc, char * const argv[])
{
	char assembly[MAX_ASSEMBLY] = { '\0' };
	FILE *input = stdin;

	if (argc > 1) {
		input = fopen(argv[1], "r");
		if (!input) {
			fprintf(stderr, "No input file %s\n", argv[0]);
			return EXIT_FAILURE;
		}
	}

	if (input == stdin) {
		printf("*********************************************************\n");
		printf("*          >> SCE212 MIPS translator  v0.10 <<          *\n");
		printf("*                                                       *\n");
		printf("*                                       .---.           *\n");
		printf("*                           .--------.  |___|           *\n");
		printf("*                           |.------.|  |=. |           *\n");
		printf("*                           || >>_  ||  |-- |           *\n");
		printf("*                           |'------'|  |   |           *\n");
		printf("*                           ')______('~~|___|           *\n");
		printf("*                                                       *\n");
		printf("*                                   Fall 2023           *\n");
		printf("*********************************************************\n\n");
		printf(">> ");
	}

	while (fgets(assembly, sizeof(assembly), input)) {
		char *tokens[MAX_NR_TOKENS] = { NULL };
		int nr_tokens = 0;
		unsigned int instruction;

		for (size_t i = 0; i < strlen(assembly); i++) {
			assembly[i] = tolower(assembly[i]);
		}

		if (parse_command(assembly, &nr_tokens, tokens) < 0)
			continue;

		instruction = translate(nr_tokens, tokens);

		fprintf(stderr, "0x%08x\n", instruction);

		if (input == stdin) printf(">> ");
	}

	if (input != stdin) fclose(input);

	return EXIT_SUCCESS;
}