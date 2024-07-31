import asyncio
from abc import ABCMeta, ABC, abstractmethod
from typing import Type, Any
from typing_extensions import Self
from spy_tool.project import camel_to_snake
from spy_tool.misc import async_gen_func
from spy_tool.logger import logger
from spy_tool.mixins.cp_mixin import CpMixin


class SpiderMeta(ABCMeta):

    def __new__(mcs, name, bases, attrs):
        if attrs.get('name') is None:
            attrs['name'] = camel_to_snake(name)
        if attrs.get('Item') is None:
            attrs['Item'] = dict
        return super().__new__(mcs, name, bases, attrs)

    def __subclasscheck__(self, subclass) -> bool:
        require_props = ('name', 'Item')
        require_props_check = all(hasattr(subclass, p) for p in require_props)

        required_methods = ('create_instance', 'start_requests', 'save_item')
        required_methods_check = all(hasattr(subclass, m) and callable(getattr(subclass, m)) for m in required_methods)

        return all([require_props_check, required_methods_check])


class Spider(ABC, metaclass=SpiderMeta):
    name: str
    Item: dict

    def __repr__(self) -> str:
        return f'<Spider name: {self.name}>'

    __str__ = __repr__

    def __init__(self, *args: Any, **kwargs: Any):
        self.args = args
        self.kwargs = kwargs
        super().__init__(*args, **kwargs)

    @classmethod
    def create_instance(cls, *args: Any, **kwargs: Any) -> Self:
        return cls(*args, **kwargs)

    @abstractmethod
    def start_requests(self):
        pass

    @abstractmethod
    def save_item(self, item: dict) -> None:
        pass


CpObject = type('CpObject', (CpMixin,), {'logger': logger})
CpSpider = type('CpSpider', (Spider, CpMixin), {'logger': logger})


def crawl(spider_cls: Type[Spider], *init_args: Any, **init_kwargs: Any) -> None:
    async def _crawl():
        if not issubclass(spider_cls, Spider):
            raise TypeError(f'Spider_cls: {spider_cls} does not fully implemented required interface!')
        spider_ins = spider_cls.create_instance(*init_args, **init_kwargs)
        start_requests = spider_ins.start_requests
        async for item in async_gen_func(start_requests):
            spider_ins.save_item(item)

    asyncio.run(_crawl())
