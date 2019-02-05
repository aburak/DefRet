# DefRet
Linux Command Line Word Definition Retriever

To install, run install.sh file. It will copy def and practice files into /usr/local/bin folder and create .def folder in the home directory. In .def folder, it also creates words.txt file to store the searched words if the user wants to.

Via def function, the supplied word is looked up in the dictionary and displayed on the terminal. If the user wants to save, it will be saved into words.txt file.

In practice mode, the user is asked the meaning of words which were searched and saved before. There are two options. One of them is test. The second option is free text entry.

- def function usage:  
def <word> <save_flag>:  
  <word>: word to retrieve the definition  
  <save_flag>: 1 to save the word to a text file, default value is 0  

- practice function usage:  
practice  
