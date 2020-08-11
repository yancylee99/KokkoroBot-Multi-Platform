# 开发者文档
开发者文档分为两部分：基于 service 接口进行上层功能开发；基于 `kokkoro.common_interface` 与 `kokkoro.platform_patch` 进行新平台适配。

## 上层功能开发
接口与 HoshinoBot 几乎保持一致，如果之前有过 HoshinoBot 二次开发经验，相信你一定能快速上手 KokkoroBot 的二次开发。

### 模块管理 (Modules)
KokkoroBot 延用了 HoshinoBot 中的模块管理机制。
1. 在 `kokkoro/modules` 中新建文件夹 `new_module`
2. 在 `kokkoro/config/__bot__.py` 中的 `MODULES_ON` 中添加 `new_module` 模块
3. 在 `new_module` 中编写业务逻辑


### 服务层 (Services)
一个模块中可以有一个或多个服务。每个服务中可以有一个或多个功能。服务可以通过 `lssv`, `enable`, `disable` 等命令进行交互式管理。

```python
#Example
from kokkoro.service import Service
sv = Service('new-service')
```

Service 构造函数如下所示
- `name: str` - 服务名
- `use_priv: int` - 使用所需要的权限
    - 默认为 `priv.NORMAL`
- `manage_priv: int` - 管理所需要的权限
    - 默认为 `priv.ADMIN`
- `enable_on_default: bool` - 是否默认开启
    - 默认为 `True`
- `visible: bool` - 是否对 `lssv` 命令可见
    - 使用 `lssv -a` 命令可以查看不可见服务
    - 默认为 `True`

```python
def __init__(self, name, use_priv=None, manage_priv=None, enable_on_default=None, visible=None):
```

### 装饰器
使用服务层提供的装饰器(decorator)装饰功能函数，装饰器会自动将功能函数注册到 KokkoroBot中，一旦消息触发了装饰器的匹配条件，将会自动触发对应功能函数。

```python
#Example
from kokkoro.service import Service
sv = Service('help')
@sv.on_prefix(('帮助', 'help'), only_to_me=False)
async def help(bot: KokkoroBot, ev: EventInterface):
    await bot.send(ev, '这是帮助信息')
```

#### on_prefix
前缀匹配。
- prefix: Union[str, Tuple[str]] - 前缀
- only_to_me: bool - 是否需要 at bot
```python
def on_prefix(self, prefix, only_to_me=False) -> Callable:
```

#### on_fullmatch
完全匹配。
- word: Union[str, Tuple[str]] - 完全匹配
- only_to_me: bool - 是否需要 at bot
```python
def on_fullmatch(self, word, only_to_me=False) -> Callable:
```

#### on_suffix
前缀匹配。
- suffix: Union[str, Tuple[str]] - 后缀
- only_to_me: bool - 是否需要 at bot
```python
def on_suffix(self, suffix, only_to_me=False) -> Callable:
```

#### on_keyword
关键词匹配。
- keywords: Union[str, Tuple[str]] - 关键词
- only_to_me: bool - 是否需要 at bot
```python
def on_keyword(self, keywords, only_to_me=False) -> Callable:
```

#### on_rex
正则匹配。
- rex: Union[str, re.Pattern] - 正则表达式
- only_to_me: bool - 是否需要 at bot
```python
def on_rex(self, rex: Union[str, re.Pattern], only_to_me=False) -> Callable:
```

### 功能函数


功能函数仅仅接受两个参数 KokkoroBot 对象与 EventInterface 对象




## 新平台适配
目前新平台适配主要涉及两个模块 `kokkoro.common_interface` 与 `kokkoro.platform_patch`。