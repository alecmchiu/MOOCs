/**
 * Resizes a bitmap
 */
       
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "bmp.h"

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 4)
    {
        fprintf(stderr, "Usage: ./resize n infile outfile\n");
        return 1;
    }
    
    //parse n as f through strtof
    double f = strtof(argv[1],NULL);
    if (f <= 0.0 || f > 100.0){
        fprintf(stderr, "n must be in (0.0,100.0]\n");
        return 1;
    }

    // remember filenames
    char *infile = argv[2];
    char *outfile = argv[3];

    // open input file 
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    // open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 3;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 || 
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }
    
    //store old dimensions
    LONG biWidth_old = bi.biWidth;
    LONG biHeight_old = bi.biHeight;
    
    //scale dimensions by f
    bi.biWidth = floor(bi.biWidth * f);
    bi.biHeight = floor(bi.biHeight * f);
    
    // determine padding in new image
    int padding_new = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    
    // new image size is number of pixels * 3 + number of pads
    bi.biSizeImage = ((bi.biWidth * abs(bi.biHeight) * 3) + (padding_new * abs(bi.biHeight)));
    
    // new bitmap file size is image size + size of headers
    bf.bfSize = bi.biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);

    // write outfile's BITMAPFILEHEADER
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);

    // determine padding for scanlines
    int padding = (4 - (biWidth_old * sizeof(RGBTRIPLE)) % 4) % 4;
    
    // counter for vertical resizing
    int height_new = 0;

    // iterate over infile's scanlines
    for (int i = 0, biHeight = abs(biHeight_old); i < biHeight; i++)
    {
        //store row
        RGBTRIPLE *row_old = malloc(sizeof(RGBTRIPLE)*biWidth_old);
        
        // iterate over pixels in scanline
        for (int j = 0; j < biWidth_old; j++)
        {

            // read RGB triple from infile and write into array
            fread(&row_old[j], sizeof(RGBTRIPLE), 1, inptr);

        }
        
        // copy row as many times as necessary
        while ((int)(height_new/f) == i){
            
            //write the new row
            for (int j = 0; j< bi.biWidth; j++){
                fwrite(&row_old[(int)(j/f)],sizeof(RGBTRIPLE),1,outptr);
            }
            
            // write the padding if necessary
            for (int k = 0; k < padding_new; k++){
                fputc(0x00, outptr);
            }
            
            height_new++;
        }
        
        free(row_old);

        // skip over padding, if any
        fseek(inptr, padding, SEEK_CUR);
        
    }

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}
