---
title: Debug Jupyter Python Notebook via VS Code
date: 2021-09-04 15:59:27
tags:
- python
- vscode
- jupyter
---



# Background

When writing a notebook using Jupyter (Notebook or Lab), it is common to write actual codes as separate modules (.py) and call them from the notebook. In this post, we show how to use VS Code debugger from Jupyter to debug (i) cells within Jupyter and (ii) codes in .py files. Surprisingly, I couldn't find any memos explaining this elsewhere.

# Preparation

* Install [`debugpy`](https://github.com/microsoft/debugpy)
* Add a new config in VS Code
  * click the bug/triangle button on the left. 
  * click the gear button. This will open `launch.json`

    {% asset_img vs_gear.png 250 %}

  * click `Add Configuration` -> `Python` -> `Remote Attach`
  * simply accept the defaults (host = localhost, port = 5678) by pressing enters twice. 
   
    {% asset_img code15.png 250 %}

  * This will create an additional config

# Action
* Here is an example:

|VS Code  |Jupyter   |
| :-------: | :-------: |
|{% asset_img code1.png %}|{% asset_img jupyter1.png %}|
 
* From Jupyter: Execute step 3.
* Go back to VS Code and Select `Python: Remote Attach` and click the green triange
{% asset_img code2.png 250 %} 
* Then, you will be connected and should be able to see the following: 
{% asset_img code3.png 250 %}
* From Jupyter, exceute step 4. The `breakpoint()` command invokes a debug activity. 
* Then, go back to VS Code. The cell is copied into a temperary file in VS Code. You can debug the codes in the usual way. 
