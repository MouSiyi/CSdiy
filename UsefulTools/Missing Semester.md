## 操作系统(OS)
#### 操作系统核心(Kernel)
操作系统是直接参考硬件规格(Microcomputer, Minicomputer,....)写成的一组程序，管理电脑中所有活动以及驱动系统中的所有硬件。
核心程序非常重要，所放置到内存当中的区块是受保护的，开机之后一直常驻于内存。
##### 核心功能
系统调用接口
程序管理：cpu调度机制，运算资源有效分配
内存管理
文件系统管理
设备驱动
#### 系统调用(System Call)
我们希望开发软件，在这基础上原本需要参考核心相关功能。操作系统提供了一整组的开发接口（系统调用层）避免了这个问题。（比如使用C语言开发，系统调用接口会将其转化为核心可以了解的任务函数）
#### 应用程式

## OS & CLI & Shell
操作系统是一组管理电脑中所有活动以及驱动系统中的所有硬件的一组程序。其 核心(Kernel) 程序非常重要，不能轻易被接触和改动。
我们一般使用者就只能通过 壳(Shell) 来跟核心沟通，以让核心达到我们所想要达到的工作。

我们命令行界面(Command Line Interface, CLI)键入的命令(Command)经由Shell编译与核心进行沟通。所以写命令实际上在进行Shell编程。

Shell is a programming environment. 
If Shell is asked to execute a command that doesn't match one of its programming keywords, it consults an *enviroment variable* called `$PATH` (it lists which directories the shell should search for programs when is is given a command)

## Environment Variables
### 分类
按生命周期分：
永久的：在环境变量脚本文件中配置，用户每次登录时会自动执行这些脚本，相当于永久生效。
临时的：用户利用export命令，在当前终端下声明环境变量，关闭Shell终端失效。
按作用域分：
系统环境变量：公共的，对全部的用户都生效。
用户环境变量：用户私有的、自定义的个性化设置，只对该用户生效。
```
echo $SHELL   查看所用shell
echo $PATH
which echo
/bin/echo $PATH
```

Linux 常用shell为bash



## Shell tools & scripting
#### Command一般格式
```shell
command -options parameter1 parameter2 ...
```
1. 一行命令第一个输入的部分是指令名`command`，比如变换工作目录的`cd`；或者可执行文件，比如`script`
2. 选项设置为`-options`，通常选项前会带 `-` 号，比如`-h`；使用选项完整全名则带 `--`号，比如`--help`
3. `parameter`为`option`或者`command`的参数
4. 以空格区分，不论空几格都视为一格
5. 大小写敏感

#### Help
* manual page: `man command`
* help: `command --help`

#### Apt(Advanced Package Tool)
Apt is a package manager used for managing the installation, updating and removal of sofrware packages.
All the packages we install on the system are referenced from a common database.本地储存了一份软件包信息列表，如软件大小、版本、依赖等。
`sudo apt update` is responsible for updating this database

#### Disc Management(磁盘管理)
* 磁盘使用(disc usage): `du`
想看自己主文件夹所占空间，`cd ~` 后使用如下命令：
```shell
du -sh                  显示总计占用
du -h --max-depth=1     显示子目录具体占用
-s：summarize
-h：human-readable
--max-depth=1: 超过指定层数的目录后，予以忽略

##### Navigating in the shell
##### 目录与路径
```shell
.         此层目录
..        上一层目录
~         “目前使用者身份”的主文件夹
~account  "account"这个账号使用者的主文件夹
/         根目录
```
绝对路径从根目录 `/` 写起；
相对路径指相对于当前工作文件夹。比如`/bin`到`/mnt`，需返回上一层目录 `/` 再进入`mnt`，相对路径为`../mnt`


#### 文件与目录管理
* 查看目前工作文件夹(print working directory): `pwd`
* 列出文件与目录(list):`ls`
```shell
mousy@5900X-3090:/home$ ls
byxin  jieying  ljz  lost+found  mousy  qyx  remote

mousy@5900X-3090:/home$ ls -l （包含文件的属性与权限等）
total 40
drwxr-x---  6 byxin   byxin    4096  7月  3 20:58 byxin
drwxr-x---  6 mousy   mousy    4096  7月  3 17:20 mousy
drwxr-x--- 26 qyx     qyx      4096  7月  3 20:01 qyx
drwxr-x--- 11 remote  remote   4096  4月 20  2022 remote
[1][  2  ]
[1]表示文件类型：d代表目录，-代表文件，l为链接文件...
[2]表示不同主体权限，rwx表示读写执行操作。前三个占位符为文件拥有者权限。
```

* 更改工作文件夹(change directory):`cd`
```shell
cd /      转到根目录
cd ~      转到主文件夹
cd 相对路径
mousy@5900X-3090:/bin$ cd ../mnt
mousy@5900X-3090:/mnt$
cd 绝对路径
mousy@5900X-3090:/mnt$ cd /bin
mousy@5900X-3090:/bin$

```

* 创建新文件: `touch`
* 创建新目录(make directory): `mkdir`
```shell
mkdir 绝对路径或相对路径      利用绝对路径创建新目录
mkdir -p test1/test2/test3  在当前目录下创建新多层目录
```

* 编辑文件: `nano`

* 复制文件(copy): `cp`
```shell
cp file(source) file/directory(destination)
cp source1 source2 source3 ... directory
```

* 删除文件或目录(remove): `rm`
```shell
rm  文件或目录
rm -r 目录    （确认要删掉包含子目录的整个目录）
```

* 移动文件与目录，或更名(move):  `mv`
```shell
mv [-fiu] source destination
mv [options] source1 source2 source3 .... directory
选项与参数：
-f ：force 强制的意思，如果目标文件已经存在，不会询问而直接覆盖；
-i ：若目标文件 （destination） 已经存在时，就会询问是否覆盖！
-u ：若目标文件已经存在，且 source 比较新，才会更新 （update
```

* Finding files : `find`
```bash
find path [-option] [parameter]
```

```bash
# Find directories named src
find . -name src -type d
# Find python files that have a folder named test in their path
find . -path '*/test/*.py' -type f
# Find files modified in the last day
find . -mtime -1
# Find zip files with size in range 500k to 10M
find . -size +500k -size -10M -name '*.tar.gz'
```

* Finding code : `grep`
```bash
grep [options] pattern [files]
```
* 连续打印(concatenate): `cat`  有趣的是倒着打印是`tac`
* 打印头几行(head)：`head`
```bash
head [-n number] 文件
例如：
head -n 5 /etc/man_db.conf
```
#### Command history
```bash
history
history | grep [pattern]
```
#### Connecting programs
A linux shell receives input and sends output as streams of characters.
* Standard  streams：`stdin` , `stdout`, `stderr`
The respective file descripers:
* stdin : `0`
* stdout : `1`
* stderr : `2`
当一个程序启动时会自动开启

想知道标准流和文件的关系？ 如何运作
In the shell, programs have two primary *streams* associated with them: input & output.Normally a program's input and output are both the terminal. But we can rewire those streams.
* Simple redirection `< file`  , `> file` 
Here `cat` not given any arguments, it prints contents from its input stream to its output stream
```bash
echo hello > hello.txt
cat < hello.txt

cat < hello.txt > hello2.txt
```
* Append to a file : `>>`
* The `|` operator lets you “chain” programs such that the output of one is the input of another
ex:  output the 6th row of state of semester into last-modified.txt
```bash
stat semester | head -n 6 | tail -n 1 > ~/last-modified.txt
```

#### Super User
```
$ sudo find -L /sys/class/backlight -maxdepth 2 -name '*brightness*'
/sys/class/backlight/thinkpad_screen/brightness
$ cd /sys/class/backlight/thinkpad_screen
$ sudo echo 3 > brightness
An error occurred while redirecting file 'brightness'
open: Permission denied
```
This error occurs because the _shell_ (which is authenticated just as your user) tries to open the brightness file for writing, before setting that as `sudo echo`’s output.(但其实还是不太懂， 这里的sudo是只授权了echo？但是打开并传进brightness并没有授权？)
```
$ echo 3 | sudo tee brightness
```
Since the `tee` program is the one to open the `/sys` file for writing, and _it_ is running as `root`, the permissions all work out.

#### Shebang(!#)
A shebang is the character sequence consisting of the charaters number sign(#) and exclamation mark(!) at the beginning of a script.
ex: We wirte a script ./semester
/bin/sh as the interpreter directive:
```bash
#! /bin/sh            
curl --head --silent https://missing.csail.mit.edu
```
We either use `bash ./semester`,(强制使用bash interpreter, 无论shebang里是啥)
or  change the mode of the script and directely execute it.
```
chmod u+x ./semester
./semester
```

#### Shell Scripting
Shell scripting is optimized for performing shell-related tasks.
* Assignment Statement
```bash
foo=bar

echo "$foo"
#strings delimited with "" will substitute variable values
#prints bar

echo '$foo'
#strings delimited with '' are literal strings
#print $foo
```
* Variable substitution
* Defining functions
```bash
mcd(){
	mkdir -p "$1"
	cd "$1"
}
```
Bash uses a variety of special variables to refer to arguments, error codes, and other relevant var.
[special variables](https://tldp.org/LDP/abs/html/special-chars.html)
- `$0` - Name of the script
- `$1` to `$9` - Arguments to the script. `$1` is the first argument and so on.
- `$@` - All the arguments
- `$#` - Number of arguments
- `$?` - Return code of the previous command
- `$$` - Process identification number (PID) for the current script
- `!!` - Entire last command, including arguments. A common pattern is to execute a command only for it to fail due to missing permissions; you can quickly re-execute the command with sudo by doing `sudo !!`
- `$_` - Last argument from the last command. If you are in an interactive shell,or by typing `Esc` followed by `.` or `Alt+.`
* Returns:
Commands will often return output using `STDOUT`, errors through `STDERR`, and a *Return Code* to report error which we can use in script. 
A value of 0 usually means everything went ok; anything different from 0 means an error occured.
* Command substitution `$(command)` 
Get the output of the command as a variable.
```bash
for file in $(ls)
```
* Process substitution `<(command)`
Execute command and place the output in a temporary file.(useful when command parameters are files)
```bash
diff <(ls foo) <(ls bar)
```
* Globbing
*wildcards* :use `?` or `*` to match one or any amount of characters respectively
*curly braces* : use `{}` when you have a common substring in a series of commands
```bash
mv *{.py, .sh} folder
# move all *.py and *.sh files to folder
```

## Data Wrangling
Date to wrangle + tools

Get some data from server log(who's trying to log in?)
```bash
ssh myserver journalctl
```
Use a pipe to stream a remote file through `grep` on local computer:
```bash
ssh myserver journalctl | grep sshd
```
Filter on the remote server, and massage the data locally:
```bash
ssh myserver 'journalctl | grep sshd | grep "Disconnected from"' | less
```
`less`  gives a pager that allows us to scroll up and down the long output.
Stick the current filtered logs into a file:
```bash
ssh myserver 'journalctl | grep sshd | grep "Disconnected from"' > ssh.log
less ssh.log
```
Global Regular Expression Print: `grep`

Stream Editer: `sed`
In it, we give short commands for how to modify the file.
```bash
ssh myserver journalctl
 | grep sshd
 | grep "Disconnected from"
 | sed 's/.*Disconnected from //'
```
`sed` substitution command: `s` 
```
s/REGEX/SUBSTITUTION
```
`REGEX` is the regular expression we want to search for.
Other commands like injecting `i` ; explicitly printing `p` ;....
Note:
Although to do in-place substitution is tempting, but the input.txt will be clear before writing in, and thus input.txt has been empty before `sed`.
```bash
sed s/REGEX/SUBSTITUTION/ input.txt > input.txt
sed s/REGEX/SUBSTITUTION/ input.txt 
#只用这个也会覆盖原文件
```
use `-i.bak` to make a backup end with `.bak` in advance
```
sed -i.bak s/REGEX/SUBSTITUTION/ input.txt
```

### Regular expression
**Everything is essentially a character**, regular expressions are **patterns** to match a specific sequence of characters(a string).
* letters, digits`\d`, punctuations, whitespace ... 
* `\W` any non-alphanumeric char, `\D` any non-digit char,  `\S` any non-whitespace char
Regular expressions are usually surrounded by `/`. Most ASCII characters just carry their normal meaning, but some characters have special matching behavior. 
Escape the special meaning of a metacharacter using `\` .

- `.` means "any single character" except newline
- `[abc]` any one character of `a` `b` `c`
- `^` excludes specific characters
- `-` match a character in list of sequential charactersv
examples:
`[0-6]`, `[^n-p]`, and `\w` is equivalent to `[A-Za-z0-9]` often used to match characters in English text.
* `{}` : repetitions
examples:
`a{3}` match the char exactly 3 times ; `a{1,3}` match the char no less than once no more than 3 times ;`a{1,}` ;`[wxy]{5}` ; `.{2,6}` 

- `*` zero or more of the preceding match
examples:
`.*` zero or more of any char
- `+` one or more of the preceding match
- `?` denotes optionality, zero or one of the preceding match

* white space:` ` , tab `\t` , new line `\n` ; and `\s` match any white space.

To write specific regular expression:
- `^` the start of the line
- `$` the end of the line
- `\b` matches the boundary between a word and a non-word char
- `(RX1|RX2)` either somthing that matches `RX1` or `RX2`

Groups: match text and offer entry to information for further processing.
* `()` : any subpattern inside `()` will be **captured** as a **group**
It can also be nested.
* reference the captured groups: `\0`(the full matched text), `\n`(the nth group)

Any text matched by a regex surrounded by parentheses is stored in a numbered *capture group*(available for substitution as `\1` , `\2` , `\3` ...)
Modify the filter:
```bash
ssh myserver journalctl
 | grep sshd
 | grep "Disconnected from"
 | sed -E 's/.*Disconnected from (invalid |authenticating )?user (.*) [^ ]+ port [0-9]+( \[preauth\])?$/\2/'
```
- `sort`  
- `uniq -c`  prefix lines by the number of occurences
```bash
ssh myserver journalctl
 | grep sshd
 | grep "Disconnected from"
 | sed -E 's/.*Disconnected from (invalid |authenticating )?user (.*) [^ ]+ port [0-9]+( \[preauth\])?$/\2/'
 | sort | uniq -c
 | sort -nk1,1 | tail -n10 
 #sort in numeric order; sort only by the first whitespace-separated column
```
Extract only the usernames as a comma-separated list
```bash
ssh myserver journalctl
 | grep sshd
 | grep "Disconnected from"
 | sed -E 's/.*Disconnected from (invalid |authenticating )?user (.*) [^ ]+ port [0-9]+( \[preauth\])?$/\2/'
 | sort | uniq -c
 | sort -nk1,1 | tail -n10
 | awk '{print $2}' | paste -sd,

```
- `paste` : combine lines `-s` by a given single-character delimiter `-d`;`,` here
### awk - another editor
`awk` is a programming language rly good at **processing text streams**. 
`awk` programs take the form of an *optional pattern* plus a *block* saying what to do if the pattern matches a given line. The default pattern matches all lines. 
Inside the block, `$0` is set to the entier line's contents, and `$1` through `$n` are set to the `n`th field of the line(default separator is white space, can be changed with `-F` ).
In fact `awk` can replace `grep` and `sed` .
```bash
BEGIN { rows = 0 }
$1 == 1 && $2 ~ /^c[^ ]*e$/ { rows += $1 }
END { print rows }
```
### Analyzing data
`bc` : a calculator that can read from `STDIN` .
```bash
| paste -sd+ | bc -l

echo "2*($(data | paste -sd+))" | bc -l
```
`R` : a programming language good at **data analysis and plotting**.```
```
ssh myserver journalctl
 | grep sshd
 | grep "Disconnected from"
 | sed -E 's/.*Disconnected from (invalid |authenticating )?user (.*) [^ ]+ port [0-9]+( \[preauth\])?$/\2/'
 | sort | uniq -c
 | awk '{print $1}' | R --no-echo -e 'x <- scan(file="stdin", quiet=TRUE); summary(x)'
```
### Data wrangling to make arguments
Many commands donot support passing arguments from pipes. We can use `xargs` (extended arguments) to transform `stdin` into command parameters. 
Using `xargs`, we can do data wrangling to find things to install or remove based on some longer list.
```
rustup toolchain list | grep nightly | grep -vE "nightly-x86" | sed 's/-x86.*//' | xargs rustup toolchain uninstall
```

## Command-line Environment
`ps` : an external(not shell-internal) command which can tell all the processes running on the system.
`jobs` : a shell command tells about the jobs that the current shell is managing. Jobs are processes started by shell.
### Job Control 
#### Killing a process
Shell uses a UNIX communication mechanism called a *signal* to communicate information to the process.
When a process receives a signal it stops execution, deals with the signal and potentially changes the flow of execution based on the information. Thus, signals are *software interrupts*.

Closing the terminal will send signal `SIGHUP`.
Typing `Ctrl-C` prompts the shell to deliver a `SIGINT` signal to the process. The default behavior is to terminate the process, but it can be caught or ignored.
Typing `Ctrl-\` to deliever a `SIGQUIT` signal, can be captured or ignored.
`SIGINT` and `SIGQUIT` are usually associated with terminal related requests.
`SIGTERM` is a more generic signal for killing a process. We use the  `kill` command : `kill -TERM <PID>`
##### Pausing and backgrounding processes
`SIGSTOP` : typeing `Ctrl-Z` will prompt the shell to send `SIGTSTP`(Terminal stop).
`Ctrl-Z` and `bg` the job : background a running program
`fg` : foreground a backgrounded running program.
Also use `bg` or `fg` to continue the stopped job in the background or foreground. 
Refer to jobs using their `PID` or `%<job number>`
`&` run in the background

Use wrapper `nohup` to ignore `SIGHUP`

### Terminal Multiplexer
- Sessions
  - Windows 
    - Panes 
![[Pasted image 20230719092303.png]]

### Aliases
A shell alias is a short form for another command that your shell will replace automatically.
`alias` is a shell cmd that takes a single argument
```bash
alias alias_name="command_to_alias arg1 arg2"
#no space around =
```
To ignore an alias: `\`
To disable an alias: `unalias ls`

NOTE: aliases do not persist shell sessions by default. To make an alias persistent you need to include it in shell startup files, like `.bashrc`.
And `.bashrc` may tell you can write aliases in `.bash_aliases`

### Dotfiles
Many programs(shell included) are configured using plain-text files, *dotfiles*. On startup, shell will read many files to load its configuration. [Shell startup scripts](https://blog.flowblok.id.au/2013-02/shell-startup-scripts.html)
For `bash` , editing `.bashrc` or `.bash_profile` will work in most systems. 
We can put dotfiles into a file `dotfiles` for management.
Use `ln -s path/to/file path/to/link` to create a symlink.

### Remote Machines
### SSH Basic
 SSH(Secure Shell)是一种协议，此处主要介绍Ubuntu中OpenSSH免费开源实现。Windows则需要使用PuTTY(参照SSH登录)
 OpenSSH分为客户端 openssh-client和服务器openssh-server
 如果只想远程登陆服务器只需要安装openssh-client(ubuntu默认安装)
```
sudo apt-get install openssh-client 
sudo apt-get install openssh-server 
```
- `ssh` into a server
  SSH 服务默认端口为22，可使用`-p`修改端口号
```bash
ssh foo@bar.mit.edu
#server specified with a URL
ssh foo@192.168.1.42
#server specified with an IP
```
- Executing commands
  `ssh user@server`  can run commands directly
- SSH keys
  - Key generation : 
```bash
  ssh-keygen -t rsa
  #类型选择为rsa加密算法
```
  在`~/`中生成`.ssh`文件夹，包含公钥`id_rsa`和私钥`id_rsa`文件
  * Key copy: 
  ```
  ssh-copy-id user@server
  ```
  将公钥写入`server`的`~/.ssh/authorized_key`
### Port Forwarding
待填
### SSH Configuration
`vim ~/.ssh/config`
```
Host 自定义Host名
        User username
        Hostname 192.168.192.38
        Port 22
        IdentityFile ~/.ssh/id_rsa
```
