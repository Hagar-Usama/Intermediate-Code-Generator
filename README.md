# parser-generator

---

## Plan (schedule)
* Today: 14 May
* Actual Deadline: 30 May
* Phase Deadline: 20 May

> 3 days to just implement this<br>
> 1 day for the report

### Schedule:
* 14 May Getting to know what's going on
* 15 - 20 May : Build the program >>


### Unclear Requirements: 🙆
* Requirements seems Unclear for me. However, that is what I got:
Step one : Token
Step two : Parse tree
Step three: AST
Step Four: IC

### Tasks
* [x] build parsing tree
* [x] show tree
* [x] simplify tree
* [x] add lexemes
* [ ] make sure to delete nodes (free/del)
* [x] lift operands up
* [x] build AST
* [x] swap relop with 2 conditions (>=) --> !(<)
* [x] IC
* [x] backpatching
* [x] remove duplicate labels (at most 2)
* [ ] report

## Bugs:
* [ ] check_type not working properly in some cases
> added a couple of lines to fixed temporarily

* [ ] get_val_2 & get_virtual shall be combined. Yet, some functions not working then
>  * try to add flag <br>
>  * make it return list of virtual nodes to work with separately

~ $ java -version
openjdk version "1.8.0_232"
OpenJDK Runtime Environment (build 1.8.0_232-8u232-b09-0ubuntu1~16.04.1-b09)
OpenJDK 64-Bit Server VM (build 25.232-b09, mixed mode)

~ $ javac -version
javac 1.8.0_232

---

## Run Jasmin

1. put your code in text file.j
2. run the command
bash`` java -jar jasmin.jar file.j ``
3. now a class file is generated, to run: `` java file ``
