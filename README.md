# KidsLang Interpreter
###### I created this as something to do in my spare time, and something to teach the children about code. This is definitely NOT Turing Complete. At least, not yet, but I dont plan to make it that way. 
------------
### Syntax
###### This will print hello, notice how quotes are not needed as everything is a string.
```
say hello
```
###### This will print hello, 10 times
```
repeat 10
    say hello
end
```
###### 2 dashes create a single line comment, there are no multiline comments as of writing this.
```
-- hello
```
###### The keyword "make" lets you declare a variable, this makes a variable named foo have the value of 64.
```
make foo 64
```
###### Typing in "wait" and a number will wait that many seconds, this will work with variables as well.
```
wait 5
```
###### This have 5 basic arithmetic operators, using + - * / ^.
###### (You must separate ANY operators with a space or they wont work. This is *definitely* a feature and not a fundamental design flaw or anything.)
```
say 1 + 1
say 5 - 3
say 6 * 2
say 9 / 3
say 2 ^ 8
```
###### You can also concatenate with the ".." operator
```
make baz kids
make foo Lang
say baz .. foo
```
###### Whitespaces are usually removed from the end (and beginning) of lines when being processed, so if you want to concatenate with a space use "__"
```
say goodbye __ camelCase standardization
```
###### There are 4 boolean operators, these will be turned into the strings "True" or "False". They are =, !=, <, >
```
make foo 18
make baz 16
say foo > baz
```
###### You can use the above boolean operators to activate if loops
```
make foo 15
make baz 10
if foo > baz
    say foo is greater than baz
end
-- You can also just use the words "True" or "False" and even "Yes" or "No"
-- eg: if yes, if true, if no, if false
```
###### If you want to print an operator by itself, add a "/" behind it
```
say What is 1 /+ 1?
```
###### If you want to print the name of a variable, add a "/" to the beginning of it.
```
make baz 15
say /baz
```
###### You can use user inputs with the "ask" command, the answer will be recorded to a variable named "answer".
```
ask What is your name?
say Hi, __ answer .. !
```
------------
###### As of now, the only way to open a file is to name it myCode.kl, and opening the .py file in the same directory. I plan to make it just a double click, to make it easier.
