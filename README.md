# computer-security
Three computer security specific python programs to perform invasive and security driven functions
All three programs are writen in Python 3.  

## Program 1

The aim of the first program is to modify another.  
  
It performs the following actions:  
Opens a file named 'sfs.py' in the current directory  
Navigate to line 52 of the file and add the text "Virus"  
Save the file under it's original name.  
  
Note that the number of lnes in the programs code does not change, this is one method to evade detection. By ensuring that the number of lines of the program stays the same makes it harder for detection methods to detect this change in the programs code.  


## Program 2
The aim of the second program is to read the data stored within an image file and extract a secret message which is encoded within.

The image is first converted to bits and is read. After reading the bits I then provide the specified values of p and q to locate the secret message hidden within the image.
  
  
## Program 3  
  
The third program decodes a message which is encoded using a baby block cipher AES. 

