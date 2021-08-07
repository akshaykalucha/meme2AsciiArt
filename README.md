# Meme 2 Ascii Art
## Convert your favourite meme to ASCII art with ```opencv``` and spam those 4chan comments.

# Variables Used
- ```image_size```: the square root of the amount of pixels that each character represents (a value of 1 means that 1 character will represent 1^2=1 pixel).
  - Should be a common factor of the dimensions of the input image. By defualt, it is set as the GCD.
  
- ```colTup```: a tuple of the characters used to make the ASCII art, with ```colTup[0]``` being the darkest value and ```colTup[-1]``` being the lightest value.

- ```Light_set```: a set of ascii characters for light bg image
- ```Dark_set```: set for dark bg
# Examples

![ex2](https://github.com/akshaykalucha3/meme2AsciiArt/blob/master/Examples/example2.png)
![ex1](https://github.com/akshaykalucha3/meme2AsciiArt/blob/master/Examples/example1.png)