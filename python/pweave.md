


Install pweave with Atom:

    apm install language-weave Hydrogen
    apm install language-markdown atom-html-preview pdf-view
    apm install hydrogen-launcher platformio-ide-terminal




Sample report goes here:

% Sample Pweave HTML report
% Paul Teehan
% 2017-08-29

# Introduction

First you need to install [Pweave](http://mpastell.com/pweave/index.html)

This document is an example of a Pweave report.  The source file
is a mixture of Markdown text and Python code.  When you run Pweave,
it will execute the source file and produce an HTML file.  In this
example, the source file lives in the `src/` folder.  There is a
script `generate.sh` that runs Pweave.  Generally you can execute like this:

`pweave -f md2html *.pmd`

If you are frequently editing text, you can add the `-d` tag and the code
chunks will be cached, so you don't have to re-run over and over.  Note that
if you change the code it won't re-execute, you need to run the whole thing
over again.

`pweave -d -f md2html *.pmd`

If you're using the Atom text editor, install the `language-weave` plugin
and you'll get syntax highlighting support.  Also, the `Spyder` IDE
has native support.

Below is a Python code block - this will print a dataframe.  Experiment
with [dataframe styling](https://pandas.pydata.org/pandas-docs/stable/style.html)
to change the way it displays.  You can make the code inivisible
by adding `echo=False` to the source; we'll do that in the next code block.

```python
import pandas as pd
df = pd.DataFrame({'a':[1,2,3], 'b':[4,5,6]})
df.style
```

## Subsection

The following code block will display a graph, and will hide the source code.

```python, echo=False, fig=True, caption='Figure 1: Test plot', results='hidden'
from plotnine import *
from plotnine.data import *
result = 123*457
ggplot(mtcars, aes('wt', 'mpg')) + geom_point()
```

# Final section

In this case I am including some Python code to display the
result: <%=result%>, which was calculated in a previous code block.
