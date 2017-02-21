#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

//define unsigned 8 bit integer as byte
typedef uint8_t BYTE;

int main(int argc, char *argv[]){
    
    // check argc
    if (argc != 2){
        fprintf(stderr, "Usage: ./recover image\n");
        return 1;
    }
    
    //remember input file and allocate output filename
    char *infile = argv[1];
    char *outfile = malloc(sizeof(char)*strlen("%03i.jpg"));

    //open input
    FILE *inptr = fopen(infile, "r");
    
    //check input
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }
    
    //store and create filename and image count
    unsigned int img_number = 0;
    sprintf(outfile,"%03i.jpg",img_number);
    
    //create buffer to store bytes
    BYTE *buffer = malloc(sizeof(BYTE)*512);
    
    //read in first block
    fread(buffer,1,512,inptr);
    
    //while the block does not contain a JPEG header, keep reading
    while (!(buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)){
        fread(buffer,1,512,inptr);
    }
    
    //once block has been found, write it to file
    FILE *outptr = fopen(outfile,"w");
    fwrite(buffer,1,512,outptr);
    
    //keep reading until EOF aka when fread doesn't return 512 bytes
    while (fread(buffer,1,512,inptr) == 512){
        
        //if start of new JPEG, close file and start new file
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0){
            fclose(outptr);
            img_number++;
            sprintf(outfile,"%03i.jpg",img_number);
            outptr = fopen(outfile,"w");
        }
        
        //write the bytes
        fwrite(buffer,1,512,outptr);
    }
    
    //free allocated heap memory
    free(buffer);
    free(outfile);
    
    //close file streams
    fclose(inptr);
    fclose(outptr);
    
    return 0;
}