<h1 align = "center">:rocket: RestfulApi :facepunch:</h1>

---
> 模型部署

## Install
```bash
pip install iapp -U
```
## Usage
```python
import jieba
from iapp import App

pred1 = lambda **kwargs: kwargs['x'] + kwargs['y']
pred2 = lambda x=1, y=1: x - y
pred3 = lambda text='小米是家不错的公司': jieba.lcut(text)

app = App()
app.add_route("/f1", pred1, version="1")
app.add_route("/f2", pred2, version="2")
app.add_route("/f3", pred3, version="3")

app.run()
```