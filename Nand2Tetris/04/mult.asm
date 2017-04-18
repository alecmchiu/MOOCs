// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

	@i
	M=1 //initialize counter
	@R2
	M=0 //initialize sum

(LOOP)
	@i
	D=M //get iteration
	@R0
	D=D-M //iteration - number of additions
	@END
	D; JGT // (iterations - num adds) > 0
	@R1
	D=M //get number
	@R2
	M=M+D //add number to sum
	@i
	M=M+1 //increment counter
	@LOOP
	0; JMP //repeat

(END)
	@END
	0; JMP