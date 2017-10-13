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
