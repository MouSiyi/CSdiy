Program language serves as a framework within which we organize our ideas about computational processes.   

Every powerful language has 3 such mechanisms:    
1. **primitive expressions and statements**(simplest building blocks)
2. **means of combination**,simpler->compound elements
3. **means of abstraction**,by which compound elements can be named and manipulted as units

We deal with 2 kinds of elements: data and function

## Expressions
An *expression* describes a computation and evaluates to a value   

All expressions can use *function call notation*

**Types of Expressions**   
primitive expressions: number,string,name  
conpound expressions: call expression   
...

**Anatomy of a Call Expression**:
e.x. add(2,3)  
operators and operands are also expressions(subexpression in call wxpression)  
**Evaluation procedure for call expression**:  
1. Evaluate the operator and then the operand   
2. Apply the *function* that is the value of the operator subexpression to the *arguments* that are the values of the operand subexpression   

## Names,Assignment and User-Defined Functions   
*assignment*   
`radius = 10`    
evaluates the right side expression and bind the value with the name    
**Assignment Statements**    
The = symbol is the assignment operator   
Assignment is our simplest means of abstraction   
Change the bindings between names and values


## Envionment Diagrams 
The possibility of binding names to values and later retrieving those values by names means the interpreter must maintain some *memory that keeps track of the names,values and bindings*(ENVIRONMENT).       
E.D. visualize the interpreter's process 

Each name is bound to a value
within a frame, a name cannot be repeated

**Assignment Procedure** 
1. evaluate all expressions to the right of = from left to right
2. bind all the names to the left of = to the resulting values in the current frame      
```python
#swapping
x,y=2,3
x,y=y,x
#x=3, y=2,for the left side expressions are valued first from left to right 
```

## Defining Functions

**abstraction**: give sth complex a name, treat it as a whole    
Assignment is a simple means of *abstraction*: binds names to values    
**Functions** encapsulate logic that manipulates data
Function definition is a more powerful means of *abstraction*:binds name to expressions
**aspects of a function abstraction**:domain,range,intent   


```python
def <name>(<formal parameters>):
    return <return expression>

```
Function signature`<name>(<formal parameters>)`: how many arguments a func takes/has all the information needed to create a local frame(thus important!!)   
Function body: defines the computational process 

**def statement execution procedure**
1. Create a func with signature `<name>(<formal parameters>)`
2. Set the body of that func to be everything indented after the first line(not executed until the function is called;scrolls away the body of the func)
3. Bind *<name>* to that func in the *current* frame

**calling user-defined functions procedure**
1. Add a *local* frame, forming a *new* environment
2. Bind the formal parameters to the argument values
3. Execute the body of the func in the *new* environment

Every expression is evaluated in the context of an environment.

So far, the current environment:     
The global frame alone      
A local frame, followed by the global frame   

**An environment is a sequence of frames.**   
**A frame is the box of bindings between names and values**

**A name evaluates to the value bound to that name in the earliest frame of the current environment in which that name is found**

## The Non-Pure Function
**pure functions**:Functions have some input and return some ouput    
**non-pure functions** make some change to the state of the interpreter or computer

## operators
mathematical operators provide a method of *combination*    
each have their own evaluation procedures;can be thought of as short-hand for call expressions    
e.g 5//4 == floordiv(5,4)

## debugging
incremental testing;modular design;precise assumption;
teamwork


哇塞 好酷
吗的 发现太晚了
太好笑了
哪个 是不是点了右上角喇叭 就是右下角跳出提示
可能是让我关注你在干啥 啊啊啊啊啊啊啊 有表情
乡巴佬很兴奋
就打开了
你那边打开个文件试试
欸 滚动也同步吗 同步！没啊qwq 好像是这样或者我先关掉？
我滚一下hhhh 666666 这也太细了
不过你看到我的md了吗
是默认发起者是host？
🉑️
啊啊啊有道理，可能是直接跳转
如果一个大的project可能文件很多
😊
表情能同步诶
哈哈哈哈哈哈
coooooooool
哈哈哈哈哈哈哈是诶
好玩
这花花的世界
说来
你是怎么把这个md广播的

刚刚是你在上下滚动吗？

有个unfollow 右上角喇叭旁边
哦哦哦 右键似乎还有一个follow on the side
这样就可以一边看对面操作一遍看自己的调整
ok了爽欸 太好笑了我要把这对话存下来 ddddd
所以更好笑了 
我再来试试连你那边

哈哈哈哈哈哈
sufer 早期驯化vscode share 实录
hhh 不在对话框交流的问题就就是没有时间戳
时空混乱
哈哈哈哈哈对
行文顺序：乱序
意识流 👌

哈哈哈哈好嘞
我的md见hhhh


爽了爽了 

CS61A
第一节课
的
第一个工具
已经爽了
👌
👍

诶在哪里
哦哦 我是右键

哎呀我好像没得
我试试

qwqwqwq
cca残！！1!!
Can you hear me>?

hhhhhhhh

ohhhhhhhhhh

适合 考试哈哈哈哈哈哈
笑死了
这不比 腾讯文稿 帅多了毫无痕迹
好帅 好帅
苍蝇搓手
我这个操作
有什么特殊的效果吗？

xs对对
有一个小喇叭

所以