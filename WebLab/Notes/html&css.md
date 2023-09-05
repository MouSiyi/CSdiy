### HTML

Hypertext Markup Language  
The language that your browser uses in order to describe the **contents and structure** of web pages.  
HTML = Nested Boxes(The page and also the code)

<!DOCTYPE html>
<html>
    <head>
        <title>Title!</title>
    </head>
    <body>
        <h1>Heading!</h1>
        <p>Paragragh!</p>
    </body>
</html>

#### Normal Tags:

<html>:root of html document         
<head>:info about document       
<body>:document body       
<h1>,<h2>...:header tag     
<p>:paragragh tag    
<div>:generic block section     
<span>:generic inline section

#### Attributes(to modify a tag):

<tagname abc="xyz">
opening tag;attribute                 
</tagname>
closing tag

Inserting Links:  
<a href="https://github.com/Bmanksy/CSdiy"></a>

Inserting Images:
<img src="">
(self-closed)

NOTE:Semantics MATTER!  
Dont just use <div>!

### CSS

Cascading Style Sheets  
The rules that tell your web browser how stuff looks like.  
CSS = A list of **descriptions**

#### id vs class:

An element can have only 1 id;  
An element can have multiple classes and multiple elements can have the same class

<div id="anid">       
<div class="class1 class2 class3">    
And in css:      
.class     
#id

多 class 便于模块化

**utility classes**: classes that just apply one css attribute

**css variables**: can be defined and used throughout
:root{
--variable1:xxxx;
--variable2:xxx;
}

**box model**

**8pt grid system**

### Useful Tools:

google fonts
color picker

### Combining html&css:

<link rel="stylesheet" href="style.css" />
