# Python Codes Repertory

![Python Version][pyversion-badge]
![Dependencies][depd-badge]

## Bayes func

In bayee file, there is a module from the book thinkbayes. However, some deprecated codes in Python 3.5 have been fixed.
For example:
```python
#original
pmf = Pmf()
print pmf.Prob()
#fixed
print(pmf.Prob())

#original
class example():
  def __init__(self,some_dict):
    self.dict = some_dict
  def some_method(self):
    reuturn sum(self.dict.itervalues())
    
#fixed
class example():
  def __init__(self,some_dict):
    self.dict = some_dict
  def some_method(self):
    reuturn sum(self.dict.values())

```

## Some work file

### HtmlPrint Module

If you want to collect the python outputs in a html page, the htmlprint module would help you.
For instance:

```python
from htmlprint import p
import numpy as np
import pandas as pd

x=pd.DataFrame(np.rand(10,10))
p.print(x)

y = np.array([1,2,3])
p.print(y)

```


## Some classifier tools basing on tensorflow

### 1.Linear Regression

```python
#Use the LinearRegressor
lr = LinearRegressor(x,y)
lr.train()

#get the coefs
lr.pred()

#get the loss function curve
lr.loss_curve
```

### 2.Multi-Layer Neuro Network



## Financial Stats

### Adding a tool for ploting candlesticks for stock ohlc price



[pyversion-badge]: https://img.shields.io/badge/Python-v3.5-orange.svg
[depd-badge]: https://img.shields.io/badge/Dependencies-Tensorflow-blue.svg

