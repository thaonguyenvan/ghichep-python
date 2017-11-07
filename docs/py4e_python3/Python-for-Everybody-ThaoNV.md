# Python for Everybody - Exploring Data Using Python 3

## Mục lục

1. Chapter 1: Why should you learn to write programs?

-------------

## 1. Chapter 1: Why should you learn to write programs?

### 1.1 Kiến trúc phần cứng máy tính

<img src="">

- Central Processing Unit (or CPU) : Được tạo nên nhằm mục đích đưa ra các câu hỏi “what is next?” cho máy tính xử lí. Nếu máy tính của bạn được đánh giá ở mức 3 Gigahertz có nghĩa CPU của bạn có thể thực hiện 3 tỷ phép tính trên một giây
- Main Memory : (RAM) lưu thông tin mà CPU cần để xử lí nhanh
- Secondary Memory : Lưu thông tin chậm hơn nhưng không bị mất khi máy tắt (disk drives or flash memory)
- Input and Output Devices : screen, keyboard, mouse, microphone, speaker, touchpad, etc.
- Network Connection: đảm nhận việc trao đổi thông tin qua internet

### 1.2 Words and sentences

Các từ trong ngôn ngữ giao tiếp được dùng trong python:

``` sh
and   del   global  not   with
as  `elif`  `if`  or  yield
assert  `else`  import  pass
break   except  `in`  raise
class   finally   is  `return`
`continue`  `for`   lambda  try
def   from  nonlocal  `while`
```

Khi đặt tên biến phải tránh những từ khóa này

### 1.3 Conversing with Python

- Trước tiên bạn cần cài đặt python lên máy của mình
- Trong phần terminal, gõ "python":

``` sh
Python 3.5.1 (v3.5.1:37a07cee5969, Dec 6 2015, 01:54:25)
[MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Kí tự `>>>` là cách mà python hỏi về yêu cầu mà bạn muốn làm tiếp theo với nó. Như vậy là bạn đã có thể sử dụng python, việc cần làm chỉ là học cách để "giao tiếp" với nó.

Mỗi khi có lỗi, python sẽ đưa ra thông báo:

``` sh
>>> I come in peace, please take me to your leader
File "<stdin>", line 1
I come in peace, please take me to your leader
^
SyntaxError: invalid syntax
>>>
```

### 1.4 interpreter and compiler

Python là một ngôn ngữ bậc cao. Giống như những ngôn ngữ bậc cao khác, CPU thực chất không hề hiểu chúng. Cái mà CPU hiểu đó là mã máy (machine language) được viết dưới dạng bit nhị phân 0 1.

Vì mã máy không thể chạy được trên tất cả các máy tính nên ta cần phải có một trình thông dịch. Nó được chia làm 2 loại chính là trình biên dịch (compilers) và trình thông dịch (interpreters).

Interpreters không có sự khác biệt lớn đối với Compilers. Chúng cũng làm nhiệm vụ chuyển ngôn ngữ bậc cao thành mã nhị phân mà máy tính có thể đọc được. Điểm khác biệt ở chỗ, trước khi chuyển mã nguồn (source code) thành mã máy, interpreter sẽ chuyển mã nguồn sang một dạng gọi là intermediate code. Mỗi phần của đoạn code sẽ được thông dịch và sau đó sẽ được thực thi một cách riêng biệt theo trình tự. Nếu lỗi được tìm thấy tại phần code đang được thông dịch, nó sẽ đưa ra thông báo và dừng tiến trình.

Python sử dụng interpreter, interpreter của nó được viết bằng "C". Nó có thể lưu một vài giá trị được sử dụng trước đó. Ta hay gọi chúng là biến (variables):

``` sh
>>> x = 6
>>> print(x)
6
>>> y = x * 7
>>> print(y)
42
>>>
```

### 1.5 Writing a program

Chúng ta sử dụng text editor để viết Python instructions (script). Python scripts có tên được kết thúc bằng `.py`

Để chạy script, ta cần khai báo tên vào interpreter

``` sh
csev$ cat hello.py
print('Hello world!')
csev$ python hello.py
Hello world!
csev$
```

### 1.6 What is a program?

Đơn giản nó là một chuỗi các câu lệnh Python được dùng để làm gì đó.

### 1.7 The building blocks of programs

- input : Lấy dữ liệu từ bên ngoài
- output : hiển thị kết quả hoặc lưu chúng,...
- sequential execution : thực hiện câu lệnh theo thứ tự lần lượt
- conditional execution : kiểm tra điều kiện rồi thực thi hoặc bỏ qua
- repeated execution : thực hiện môt số câu lệnh lặp lại nhiều lần
- reuse : viết một số instructions và sử dụng chúng nhiều lần

### 1.8 What could possibly go wrong?

- Syntax errors : Lỗi "grammar" rules
- Logic errors : Lỗi logic, có thể là cách mà câu lệnh này liên kết tới câu lệnh khác
- Semantic errors : Cả chương trình không có lỗi nhưng nó không hoạt động như cách bạn mong muốn.

### 1.9 Glossary

- bug : Lỗi trong chương trình
- central processing unit : cpu
- compile : biên dịch từ ngôn ngữ bậc cao sang mã máy
- high-level language : Python, C, Java,...
- interactive mode : Cách sử dụng python interpreter bằng việc gõ các câu lệnh trên prompt
- interpret : Execute 1 dòng 1 lần
- low-level language : được thiết kế để máy tính dễ execute, thường được biết đến với cái tên “machine code” or “assembly language”
- main memory : lưu các chương trình và dữ liệu tạm thời
- parse : kiểm tra chương trình, phân tích cú pháp
- portability : tính năng của program đó là có thể chạy trên nhiều máy tính

## 2. Chapter 2: Variables, expressions, and statements

### 2.1 Values and types

Giá trị (Values) có nhiều loại (types), ví dụ 2 là integer, “Hello, World!” là string.
Những giá trị được đặt trong dấu nháy đơn ('') được coi là strings

### 2.2 Variables

Biến (Variables) refer cho giá trị (value). Câu lệnh gán (assignment statement) sẽ tạo ra một biến mới và gán cho chúng giá trị:

``` python
>>> message = 'And now for something completely different'
>>> n = 17
>>> pi = 3.1415926535897931
```

### 2.3 Variable names and keywords

Tên biến có thể chứa cả chữ lẫn số nhưng không được bắt đầu bằng số. Có thể chưa dấu gạch dưới ( _ ) và tên biến cũng có thể bắt đầu bằng kí tự này.

Không thể đặt tên biến bằng những keywords của Python (đã đề cập ở phía trên).

### 2.4 Statements

Được chia làm 2 loại:

expression statement và assignment

### 2.5 Operators and operands

Operators là các phép tính, giá trị được gán cho nó được gọi là operands.

Python có các Operators sau: +, -, *, /, and **

### 2.6 Expressions

Là sự kết hợp của values, variables, and operators.

``` python
17
x
x + 17
```

### 2.7 Order of operations

Khi mà có nhiều các operators thì chúng sẽ được thực thi theo rules :

- Trong dấu ngoặc đơn sẽ được thực thi trước
- Nhân chia trước, cộng trừ sau
- Khi có cùng độ ưu tiên, thực thi từ trái sang phải.

### 2.8 Modulus operator

``` python
>>> quotient = 7 // 3
>>> print(quotient)
2
>>> remainder = 7 % 3
>>> print(remainder)
1
```

### 2.9 String operations

concatenation

``` python
>>> first = 10
>>> second = 15
>>> print(first+second)
25
>>> first = '100'
>>> second = '150'
>>> print(first + second)
100150
```

### 2.10 Asking the user for input

Python đã có sẵn một "built-in" function để người dùng nhập dữ liệu vào đó là `input`. Khi function này được gọi đến, chương trình sẽ dừng và đợi để người dùng nhập liệu. Khi người dùng kết thúc và ấn "Enter" thì chường trình sẽ tiếp tục và những gì người dùng nhập sẽ được cho vào string.

``` python
>>> input = input()
Some silly stuff
>>> print(input)
Some silly stuff
```

``` python
>>> name = input('What is your name?\n')
What is your name?
Chuck
>>> print(name)
Chuck
```

Hoặc nếu bạn muốn người dùng nhập số thì hãy convert nó sử dụng function int()

``` sh
>>> prompt = 'What...is the airspeed velocity of an unladen swallow?\n'
>>> speed = input(prompt)
What...is the airspeed velocity of an unladen swallow?
17
>>> int(speed)
17
>>> int(speed) + 5
22
```

### 2.11 Comments

Comment trong python được bắt đầu bằng `#` :

``` python
# compute the percentage of the hour that has elapsed
percentage = (minute * 100) / 60
```

## Chapter 3 Conditional execution

### 3.1 Boolean expressions

`True` và `False` là những giá trị đặc biệt, chúng không phải string

Các comparison operators:

x !=y         # x không bằng y
x > y         # x lớn hơn y
x < y         # x nhỏ hơn y
x >= y        # x lớn hơn hoặc bằng y
x <= y        # x nhỏ hơn hoặc bằng y
x is y        # x bằng y
x is not y    # x không bằng y

### 3.2 Logical operators

`and, or, and not`

`x > 0 and x < 10` là True nếu x > 0 và nhỏ hon 10

`n%2 == 0 or n%3 == 0` là true nếu một trong 2 true

`not (x > y)` là true nếu `x>y` là false

### 3.3 Conditional execution

``` python
if x > 0 :
    print('x is positive')
```

Nếu điều kiện true thì nó sẽ thực hiện câu lệnh phía sau dấu `:`. Số lượng câu lệnh sau dấu `:` là không giơi hạn, trong trường hợp bạn muốn bỏ qua, hãy sử dụng pass:

``` python
if x < 0 :
    pass
```

### 3.4 Alternative execution

``` python
if x%2 == 0 :
    print('x is even')
else :
    print('x is odd')
```

### 3.5 Chained conditionals

``` python
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')
```

### 3.6 Nested conditionals

``` python
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')
```

### 3.7 Catching exceptions using try and except

Ý tưởng của `try / except` đó là nếu bạn nghĩ rằng có một phần nào đó trong code có thể gây lỗi và bạn muốn thêm một vài câu lệnh để thay thế trong trường hợp lỗi xảy ra. Những câu lệnh được thêm vào này sẽ không được thực thi nếu không có lỗi nào xảy ra

``` python
inp = input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')
```

Đầu tiên python sẽ thực thi câu lệnh trong block `try`. Nếu có `exceptions` thì python sẽ thực thi câu lệnh trong block `except`

## 4. Iteration

### 4.1 Updating variables

Bạn phải định nghĩa biến trước rồi mới có thể update biến

``` python
>>> x = 0
>>> x = x + 1
```

### 4.2 The while statement

``` python
n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')
```

Workflow:

1. Kiểm tra điều kiện (True hay False)

2. Nếu điều kiện false, thoát khỏ vòng lặp và thực hiện câu lệnh tiếp theo

3. Nếu điều kiện true, thực thi phần body của vòng lặp và quay lại bước 1

### 4.3 “Infinite loops” and break and continue

``` python
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
```

`continue` sẽ không thực hiện tiếp những câu lệnh trong phần thân của vòng lặp nữa mà sẽ quay lại check lại điều kiện.

`break` sẽ thoát hẳn khỏi vòng lặp.

### 4.4 Definite loops using for

`for` là kiểu vòng lặp thường được dùng cho một set (có thể là list bao gồm các từ hoặc số).

``` python
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')
```

## Chapter 8 Lists

### 8.1 A list is a sequence

Giống string, list là tập hợp một số giá trị tuy nhiên các giá trị này có thể thuộc bất cứ loại nào.

Có một cài cách để khai báo một list, cách đơn giản nhất đó là khai báo các phần tử trong dấu ngoặc vuông, bạn cũng có thể khai báo list lồng nhau và list trống.

``` python
>>> cheeses = ['Cheddar', 'Edam', 'Gouda']
>>> numbers = [17, 123]
>>> empty = []
>>> print(cheeses, numbers, empty)
['Cheddar', 'Edam', 'Gouda'] [17, 123] []
```

Bạn cũng có thể sử dụng `list()` để khai báo một list trống

### 8.2 Lists are mutable

Cách lấy dữ liệu của list giống với string . Tuy nhiên bạn có thể thay đổi thứ tự trong list hoặc thay đổi giá trị củ chúng.

### 8.3 Traversing a list

Cách phổ biến nhất để traverse một list đó là dùng for. Nếu bạn muốn thay đổi phần tử thì bạn cần dùng thêm indices.

``` python
for i in range(len(numbers)):
  numbers[i] = numbers[i] * 2
```

### 8.4 List operations

``` python
>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> c = a + b
>>> print(c)
[1, 2, 3, 4, 5, 6]
```

``` python
>>> [0] * 4
[0, 0, 0, 0]
>>> [1, 2, 3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
```

### 8.5 List slices

``` python
>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> t[1:3]
['b', 'c']
>>> t[:4]
['a', 'b', 'c', 'd']
>>> t[3:]
['d', 'e', 'f']
```

Nếu bạn khai báo phần tử đầu tiên, nó sẽ bắt đầu từ đó, phần tử thứ 2 được khai báo sẽ là điểm trước khi kết thúc (trước đó 1 phần tử)

### 8.6 List methods

`append` để thêm phần tử vào List

``` python
>>> t = ['a', 'b', 'c']
>>> t.append('d')
>>> print(t)
['a', 'b', 'c', 'd']
```

`extends` để thêm list vào list khác

``` python
>>> t1 = ['a', 'b', 'c']
>>> t2 = ['d', 'e']
>>> t1.extend(t2)
>>> print(t1)
['a', 'b', 'c', 'd', 'e']
```

`sort` để sắp xếp các phần tử từ thấp tới cao

``` python
>>> t = ['d', 'c', 'e', 'b', 'a']
>>> t.sort()
>>> print(t)
['a', 'b', 'c', 'd', 'e']
```

### 8.7 Deleting elements

`pop` để xóa phần tử khi bạn biết chính xác index của nó

``` python
>>> t = ['a', 'b', 'c']
>>> x = t.pop(1)
>>> print(t)
['a', 'c']
>>> print(x)
b
```

`pop` sẽ giữ lại phần tử vừa bị loại bỏ. Nếu bạn không cần nó, hãy sử dụng `del`

``` python
>>> t = ['a', 'b', 'c']
>>> del t[1]
>>> print(t)
['a', 'c']
```

Nếu bạn biết giá trị muốn loại bỏ (không cần index), hãy dùng remove

``` python
>>> t = ['a', 'b', 'c']
>>> t.remove('b')
>>> print(t)
['a', 'c']
```

Nếu bạn muốn loại bỏ nhiều hơn 1 phần tử, sử dụng `del` với `slice` index

### 8.8 Lists and functions

Có rất nhiều builr-int functions mà bạn có thể dùng sẵn

``` python
>>> nums = [3, 41, 12, 9, 74, 15]
>>> print(len(nums))
6
>>> print(max(nums))
74
>>> print(min(nums))
3
>>> print(sum(nums))
154
>>> print(sum(nums)/len(nums))
25
```

``` python
total = 0
count = 0
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print('Average:', average)
```

### 8.9 Lists and strings

Chuyển đổi từ string sang list

``` python
>>> s = 'spam'
>>> t = list(s)
>>> print(t)
['s', 'p', 'a', 'm']
```

Nếu bạn muốn bẻ string thành các từ riêng biệt, sử dụng `split`

``` python
>>> s = 'pining for the fjords'
>>> t = s.split()
>>> print(t)
['pining', 'for', 'the', 'fjords']
>>> print(t[2])
the
```

Khi sử dụng `split`, bạn sẽ biến string thành list các từ. Bạn có thể sử dụng nó với `delimiter` để kahi báo kí hiệu được loại bỏ

``` python
>>> s = 'spam-spam-spam'
>>> delimiter = '-'
>>> s.split(delimiter)
['spam', 'spam', 'spam']
```

`join` sẽ có chức năng ngược lại với `split`

``` python
>>> t = ['pining', 'for', 'the', 'fjords']
>>> delimiter = ' '
>>> delimiter.join(t)
'pining for the fjords'
```

### 8.10 Parsing lines

Chương trình tìm kiếm dòng bắt đầu với "From" và in từ thứ 3 ra màn hình

``` python
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[2])
```

### 8.11 Objects and values
