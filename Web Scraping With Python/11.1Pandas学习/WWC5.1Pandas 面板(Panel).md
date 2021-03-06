# Pandas 面板(Panel)

**Pandas 面板**(**Panel**)是3维数据的存储结构，面板数据一词来源于计量经济学，部分源于名称：`Pandas` – `pan(el)-da(ta)-s`。
`Panel` 相当于一个存储 `DataFrame` 的字典，3个轴（`axis`）分别代表意义如下:

| `axis 0` | **items**      | item 对应一个内部的数据帧(DataFrame) |
| -------- | -------------- | ------------------------------------ |
| `axis 1` | **major_axis** | 每个数据帧(DataFrame)的索引行        |
| `axis 2` | **minor_axis** | 每个数据帧(DataFrame)的索引列        |

![模型](https://img.geek-docs.com/pandas/201908292303.png)

## 一、Panel的构造函数

```python
pandas.Panel(data, items, major_axis, minor_axis, dtype, copy)
```

参数说明：

|     参数     |                             说明                             |
| :----------: | :----------------------------------------------------------: |
|    `data`    | 支持多种数据类型，如：`ndarray`，`series`，`map`，`lists`，`dict`，`constant`和其他数据帧(`DataFrame`) |
|   `items`    |                           `axis=0`                           |
| `major_axis` |                           `axis=1`                           |
| `minor_axis` |                           `axis=2`                           |
|   `dtype`    |                        每列的数据类型                        |
|    `copy`    |                 是否复制数据，默认为`false`                  |

## 二、创建 Panel

### (一)创建一个空 Panel

```python
#!/usr/bin/env python3
#-*-coding:utf-8-*-

import pandas as pd

d=pd.Panel()
print(d)

'''
# output:
vel namespace will also be removed in the next version
  d=pd.Panel()
<pandas.__getattr__.<locals>.Panel object at 0x000001D488FA3D48>
'''


```

### (二)从3D ndarray创建 Panel

```python
# creating an empty panel
import pandas as pd
import numpy as np

data = np.random.rand(2, 4, 5)
p = pd.Panel(data)
print (p)

'''
# output:
<class 'pandas.core.panel.Panel'>
Dimensions: 2 (items) x 4 (major_axis) x 5 (minor_axis)
Items axis: 0 to 1
Major_axis axis: 0 to 3
Minor_axis axis: 0 to 4
'''
```

### (三)从 DataFrame 字典创建 Panel

```python
#!/usr/bin/env python3
#-*-coding:utf-8-*-

#creating an empty panel
import pandas as pd
import numpy as np

data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print (p)


'''
# output:
<class 'pandas.core.panel.Panel'>
Dimensions: 2 (items) x 4 (major_axis) x 3 (minor_axis)
Items axis: Item1 to Item2
Major_axis axis: 0 to 3
Minor_axis axis: 0 to 2
'''
```

## 三、从panel中读取数据

要从 Panel 中读取数据，可以使用以下方式：  
* Items  
* Major_axis  
* Minor_axis  


### (一)使用Items

```python
#!/usr/bin/env python3
#-*-coding:utf-8-*-

#creating an empty panel
import pandas as pd
import numpy as np

data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print (p)

'''
# output:
<class 'pandas.core.panel.Panel'>
Dimensions: 2 (items) x 4 (major_axis) x 3 (minor_axis)
Items axis: Item1 to Item2
Major_axis axis: 0 to 3
Minor_axis axis: 0 to 2

'''

```


### (二)Major_axis  
```python

#!/usr/bin/env python3
#-*-coding:utf-8-*-

# creating an empty panel
import pandas as pd
import numpy as np
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print (p.major_xs(1))



'''
# output:
      Item1     Item2
0  1.152541  0.581985
1  1.139998 -0.253684
2  0.637131       NaN

'''
```



### (三)Minor_axis



```python
# creating an empty panel
import pandas as pd
import numpy as np
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print (p.minor_xs(1))

'''
# output:
      Item1     Item2
0 -0.854895  0.904276
1 -0.492248 -0.386763
2  0.487797 -1.398289
3  1.224335 -0.300087

'''
```


