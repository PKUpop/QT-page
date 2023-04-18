---
layout: default
---



## 示例0 创建Qt工程

[讲解视频链接](http://39.96.165.147/Projects/QT-video/sample_0.mp4)

本示例演示如何创建一个简单的Qt工程

- 基类的选择与区别
- Qt工程的文件结构
- 各种文件的代码解读
- 窗口界面的设计与修改

### 1 创建工程类选择

![创建工程类选择](image/0-1.png)



### 2 不同“基类”的差别

![不同“基类”的差别](image/0-2.png)

- <font color=#4e70be>**基类**</font>有QMainWindow, QDialog, QWidget可选
- QWidget是其他两个类的基类, 较为通用
- QMainWindow是有菜单栏的窗口
- QDialog显示一个临时的对话框

### 3 Qt工程文件结构

![Qt工程文件结构](image/0-3.png)

- .pro文件：自动生成的工程文件
- .h文件：存放类定义的头文件
- .cpp文件：存放代码执行逻辑的源代码文件
- .ui文件：控制界面布局的界面文件


### 4 头文件myhellodialog.h解读

![头文件myhellodialog.h解读](image/0-4.png)


### 5 主函数main.cpp解读

![主函数main.cpp解读](image/0-5.png)



### 6 类函数myhellodialog.cpp解读

![类函数myhellodialog.cpp解读](image/0-6.png)


### 7 窗口界面编辑

![窗口界面编辑](image/0-7.png)

界面布局功能提供了两种窗口界面编辑模式：
- 文本化编辑模式
- 可视化编辑模式

#### 7.1 窗口添加新组件

![窗口添加新组件](image/0-8.png)


#### 7.2 修改组件内容(通过代码)

![修改组件内容(通过代码)](image/0-9.png)


#### 7.3 修改组件内容(通过属性栏)

![修改组件内容(通过属性栏)](image/0-10.png)

**属性栏修改组件后myhellodialog.ui内容的变化**
![修改组件内容(通过属性栏)](image/0-11.png)



