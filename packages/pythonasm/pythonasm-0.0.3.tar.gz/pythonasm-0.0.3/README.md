# pythonasm Library
I. Overview

This is a Python library that contains a series of functions related to data processing and operations. It can simulate the input and output of an assembler. The author is Lin Honghan, a Chinese sixth-grade primary school student. The pypi account is linhhanpy, and the gitee account is linhhpy. It was made during the summer vacation when being bored.
More functions will be updated in the future, adding an assembler virtual machine and using real assembler instructions.

II. Main Functions
- Defined basic mathematical operation functions: add (addition), sub (subtraction), mul (multiplication), div (division, handling the case where the divisor is 0).
- Handles instructions such as db, mov, etc.
- operation function: Matches and performs corresponding operation operations according to specific instruction patterns.
- check function: Used for checking specific conditions.
- asm function: Can read the specified file, parse the instructions in it, and perform corresponding processing.

III. Usage Method

After importing the relevant modules, you can call the functions within for usage.
IV. Dependent Libraries
 - `re`: Used for regular expression operations.
 - `os`: Used for file and directory-related operations.
 - `keystone`：用于编译
 - `capstone`：用于编译

V. Sample Code
```python
import pythonasm.main
from pythonasm.asm import*

mov("ax", 1)
add("ax", 2)
inc("ax")
db(0x90)  # NOP
int_(0x80)
jmp(0x90)
display()
pythonasm.main.asm('pyasm.asm')
```
```asm
#pyasm.asm
msg db "abc"
mov ax,3
mov bx,0
mov cx,msg
mov dx,3
int 80h
mov ax,4
mov bx,1
mov dx,3
int 80h
```
```input
#command_input
123
```
```command
#command_out
mov ax,1            ;0x66B80100
add ax, 2           ;0x6683C002
inc ax              ;0x66FFC0
db 144              ;0x90
int 128             ;0xCD80
jmp 144             ;0xE98B000000
123
```
VI. Copyright Statement

This library is open source, but the author and source must be indicated. The final interpretation right belongs to Lin Honghan.
# pythonasm 库

 一、概述
这是一个包含了一系列与数据处理和操作相关功能的 Python 库，能模拟汇编器的输入输出，转换机器码，作者为中国六年级小学生林泓翰pypi账号linhhanpy，gitee账号linhhpy，暑假无聊做的。
以后会更新更多功能，增加汇编虚拟机和使用真正的汇编指令。

 二、主要功能（main）
 - 定义了基本的数学运算函数：`add`（加法）、`sub`（减法）、`mul`（乘法）、`div`（除法，处理除数为 0 的情况）。
 - 处理`db`，`mov`等指令。
 - `operation` 函数：根据特定的指令模式匹配并执行相应的运算操作。
 - `check` 函数：用于进行特定条件的检查。
 - `asm` 函数：能够读取指定文件，解析其中的指令并进行相应处理。
 - `display`函数：显示汇编和机器码

 三、使用方法
导入相关模块后，即可调用其中的函数进行使用。

 四、依赖库
 - `re` ：用于正则表达式操作。
 - `os` ：用于文件和目录相关操作。
 - `keystone`：用于编译
 - `capstone`：用于编译

 五、示例代码
```python
import pythonasm.main
from pythonasm.asm import*

mov("ax", 1)
add("ax", 2)
inc("ax")
db(0x90)  # NOP
int_(0x80)
jmp(0x90)
display()
pythonasm.main.asm('pyasm.asm')
```
```asm
#pyasm.asm
msg db "abc"
mov ax,3
mov bx,0
mov cx,msg
mov dx,3
int 80h
mov ax,4
mov bx,1
mov dx,3
int 80h
```
```input
#command_input
123
```
```command
#command_out
mov ax,1            ;0x66B80100
add ax, 2           ;0x6683C002
inc ax              ;0x66FFC0
db 144              ;0x90
int 128             ;0xCD80
jmp 144             ;0xE98B000000
123
```
六、版权声明
本库开源，但需标明作者和出处，最终解释权归林泓翰所有。

