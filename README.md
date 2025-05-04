# TOC_Project
# Syntax Analysis of Arithmetic Expressions using Context-Free Grammar

## Overview

This project demonstrates the application of the Theory of Computation (TOC), specifically Context-Free Grammars (CFGs), to build a syntax analyzer for arithmetic expressions. A Python-based program is developed to parse and validate expressions involving basic arithmetic operations (addition, subtraction, multiplication, division, exponentiation, modulus) and trigonometric functions. This project illustrates how CFGs can be used to define the syntax of a language and how a simple parser can be implemented based on these grammars.

## Table of Contents

* [Introduction](#introduction)
* [Characteristics of TOC in Syntax Analysis](#characteristics-of-toc-in-syntax-analysis)
* [TOC and Syntax Analysis](#toc-and-syntax-analysis)
* [CFG for Arithmetic Expressions](#cfg-for-arithmetic-expressions)
* [Implementation](#implementation)
* [Output](#output)
* [Conclusion](#conclusion)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Running the Code](#running-the-code)
* [Usage](#usage)
* [Further Enhancements](#further-enhancements)

## Introduction

This project explores the fundamental role of the Theory of Computation (TOC), particularly Context-Free Grammars (CFGs), in the design and implementation of syntax analyzers. TOC provides a formal framework for describing the syntax of languages, ranging from programming languages to, as demonstrated here, arithmetic and trigonometric expressions using CFGs. A syntax analyzer, or parser, is a crucial component of compilers and interpreters responsible for verifying the structural correctness of the input.

## Characteristics of TOC in Syntax Analysis

(Refer to the project report for detailed information)

## TOC and Syntax Analysis

(Refer to the project report for detailed information)

## CFG for Arithmetic Expressions

(Refer to the project report for the detailed Context-Free Grammar used in this project)

## Implementation

The syntax analyzer is implemented in Python using a recursive descent parsing technique. The production rules of the defined Context-Free Grammar are directly translated into recursive functions within the `MathSyntaxAnalyzer` class. This class includes methods for parsing different components of the arithmetic expressions, such as terms, factors, and handling parentheses and functions. Error handling is incorporated to identify and report syntax errors in the input expressions.

The core of the implementation resides in the `parse()` method, which initiates the parsing process, and the individual methods corresponding to the non-terminal symbols of the grammar (e.g., `E` for expression, `T` for term, `F` for factor). The `lexer()` method (implicitly used through string manipulation and indexing) helps in tokenizing the input expression.

## Output

(Refer to the project report for example output showcasing successful parsing and error detection.)

## Conclusion

This project successfully demonstrated the application of Context-Free Grammars (CFGs) from the Theory of Computation (TOC) in building a basic syntax analyzer for arithmetic expressions. The Python-based recursive descent parser effectively validates the syntactic correctness of input expressions based on the defined grammar. This exercise highlights the fundamental role of TOC in the design and implementation of language processing tools like compilers and interpreters, where ensuring the syntactic validity of the input is a crucial initial step.

## Getting Started

### Prerequisites

* Python 3.x installed on your system.

### Running the Code

1.  Save the provided Python code (from the `Implementation` section of the report) as a `.py` file (e.g., `math_parser.py`).
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the script using the command: `python math_parser.py`
5.  The program will prompt you to "Enter a mathematical expression:". Enter the expression you want to analyze and press Enter.

## Usage

Upon running the script, you will be prompted to enter a mathematical expression. The analyzer will then attempt to parse the expression based on the defined grammar.

* If the expression is syntactically correct according to the grammar, the program will output "Result: [evaluation of the expression]". Note that this basic syntax analyzer might not fully evaluate the expression but rather confirm its syntactic structure.
* If the expression contains syntax errors, the program will output an "Error:" message indicating the type of error encountered.

**Example Valid Inputs:**

* `2 + 3 * 4`
* `(5 - 1) / 2`
* `sin(30) + 10`
* `2 ^ 3`
* `15 % 4`

**Example Invalid Inputs:**

* `2 ++ 3`
* `(5 - 1`
* `cos 45)`
* `3 * (2 +)`

## Further Enhancements

The project can be further enhanced in the following ways:

* **Expanding the Grammar:** Support for more operators (e.g., unary minus), functions, and variables.
* **More Comprehensive Parsing Algorithm:** Implementing a more advanced parsing algorithm (e.g., LR parsing) to handle a wider range of grammars and provide more informative error messages, including the location of the error.
* **Abstract Syntax Tree (AST) Generation:** Building an Abstract Syntax Tree (AST) during parsing. The AST can then be used for subsequent processing, such as semantic analysis and evaluation.
* **Symbol Table Management:** Incorporating a symbol table to handle variables and their values.
* **Evaluation of Expressions:** Extending the parser to not only check the syntax but also evaluate the valid arithmetic expressions.
