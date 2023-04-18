---
layout: default
---




## QT基本介绍

<!-- <div  align="center">    
 <img src="image/intro-1.jpg" width = "180" height = "200" align=center />
</div> -->

![官网](image/intro-1.jpg)

### 1.1 背景信息
- 官网：https://www.qt.io/
- 下载：https://download.qt.io/
- 跨平台可视化开发工具(Winows/Mac/Linux/Android/IOS)

- 有收费版和免费的开源版(Opensource distribution under an LGPL or GPL license)
- 免费版开发的桌面应用,发布时不要求开源,须带一些动态链接库,无法静态绑定到一个.exe文件
- Qt是核心库,类比Python
- QtCreator是IDE,用于开发桌面应用(如WPSoffice),类比Pycharm
- QtQuick可用于开发移动应用




### 1.2 用Qt创建桌面工程

1. 运行Qt Creator
![运行Qt Creator](image/intro-3.png)
2. 新建Qt Widgets项目（即带窗口界面的项目）
![新建Qt Widgets项目](image/intro-4.png)
3. 指定文件夹和项目名称
![指定文件夹和项目名称](image/intro-5.png)
4. 指定一个源文件中的类名以及其基类(QMainWindow或QDialog...)
![指定一个源文件中的类名以及其基类](image/intro-6.png)
5. 工程创建完成



### 1.3 Qt项目文件组成

- helloworld.pro 项目文件
- hellodialog.h用户自定义类的头文件
- hellodialog.cpp 用户自定义类的源文件
- main.cpp 程序的入口文件, 包括main函数
- hellodialog.ui程序的界面文件 (XML格式, 只能可视化编辑)

**hellodialog.h 用户自定义类的头文件**
```c++
#ifndef HELLODIALOG_H
#define HELLODIALOG_H
namespace Ui {// 界面的名字空间
    class HelloDialog;
}
class HelloDialog : public QDialog {
    Q_OBJECT; //宏定义
public:
    explicit HelloDialog(QWiget * parent = 0);
    ~HelloDialog();
private:
    Ui:: HelloDialog * ui;
};

#endif // HELLODIALOG_H
```

### 1.4 发布Qt编写的可执行程序

1. 在左下角选择release版并编译,在release版文件夹下面得到.exe文件
2. 将以下.dll文件和.exe文件放在同一文件夹下一起发布
    - libgcc_s_dw2-1.dll
    - libstdc++-6.dll
    - libwinpthread-1.dll (也可能不要)
    - Qt5Core.dll
    - Qt5Gui.dll
    - Qt5Widgets.dll
