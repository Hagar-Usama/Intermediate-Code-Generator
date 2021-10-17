# Intermediate Code Generator

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://forthebadge.com)



Voila, we have reached the last phase 🪄 ✨. ICG is the third phase of my compiler (Genepiler). It's planned to join my _'Oh My Compiler'_ project!

> The name of this phase is a little bit misleading. The phase compacted the last three phases of a typical compiler (Intermediate Code Generator - Code Optimizer - Target Code Generation).

This phase takes the _lexemes_ from the [first phase](https://github.com/Hagar-Usama/Lexical) along with the _actions_ from the [second phase](https://github.com/Hagar-Usama/parser-generator) and produces _java code_ 🙌

---

### Easy Steps: 
* [x] Step one : Token
* [x] Step two : Parse tree
* [x] Step three: AST
* [x] Step Four: IC

---


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
* [x] remove print logs
* [x] consider module file to add your modules in
* [x] optimize backpatching
* [x] add arguments (argparse)
* [x] consider add directory for input and directory for output

* [x] report

### New Tasks:
* [ ] fix bugs
* [ ] consider generalizing the last phase

---

## Bugs 🐞:

>  🤔 I believe I've fixed most of the bugs (maybe all of the them).


* [ ] check_type is not working properly in some cases
> added a couple of lines to fix it temporarily

* [ ] get_val_2 & get_virtual shall be combined. Yet, some functions are not working then
>  * try to add flag <br>
>  * let it return a list of virtual nodes to work with separately

* [ ] do not declare multiple (seems to get something wrong) - check logic [not informative]

* [ ] backpatching not working when no labels

---

## Notes
* what if num is neg (is that handled?)
* handle range to be general (check phase 1)

---

## Running Jasmin

1. put your code in .j file
2. run the folowing command
bash `` java -jar jasmin.jar file.j ``
3. now a class file is generated, to run: `` java file ``

## [Memory] Plan (schedule)
* Today: 14 May
* Actual Deadline: ~~30 May~~ 6 Jun
* Phase Deadline: 20 May

> 3 days to just implement this<br>
> 1 day for the report


### Schedule:
* 14 May Getting to know what's going on
* 15 - 20 May : Build the program >>

