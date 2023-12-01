# =====================================================
#
# File Name: markdown.py
# Date of Creation: Thu 27 May 2021 11:19:53
# Author: user Tan
# Description: stuff for the Jupyter QTConsole, should be executed with @q
#
# =====================================================
# =====================================================


import matplotlib.pyplot as plt
from rich.console import Console
from rich.markdown import Markdown

#console = Console(force_jupyter=False)
console = Console(force_interactive = True)

def markdown(string):
    # prints in markdown, should be a multilined string
    console.print(Markdown(string)); 

def latex(string, sz = 15):
    # prints only one line of latex
    ax = plt.axes([0,0,0,0]) #left,bottom,width,height
    ax.set_xticks([])
    ax.set_yticks([])
    ax.axis('off')
    plt.text(0,0,'$%s$' %string,size=sz, color="lime") 
