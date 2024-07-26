import asyncio
from abc import ABCMeta, ABC, abstractmethod
from typing import Type, Any
from typing_extensions import Self
from spy_tool.misc import async_gen_func


class SpiderMeta(ABCMeta):
    def __subclasscheck__(self, subclass) -> bool:
        require_props = ('name', 'Item')
        require_props_check = all(hasattr(subclass, p) for p in require_props)

        required_methods = ('create_instance', 'start_requests', 'save_item')
        required_methods_check = all(hasattr(subclass, m) and callable(getattr(subclass, m)) for m in required_methods)

        is_subclass = all([require_props_check, required_methods_check])
        return is_subclass


class Spider(ABC, metaclass=SpiderMeta):
    name: str
    Item: dict

    def __repr__(self) -> str:
        return f'<Spider name: {self.name}>'

    __str__ = __repr__

    @classmethod
    @abstractmethod
    def create_instance(cls, *args: Any, **kwargs: Any) -> Self:
        pass

    @abstractmethod
    def start_requests(self):
        pass

    @abstractmethod
    def save_item(self, item: dict):
        pass


class Crawler(object):
    def crawl(self, spider_cls: Type[Spider], *args: Any, **kwargs: Any):
        asyncio.run(self._crawl(spider_cls, *args, **kwargs))

    @staticmethod
    async def _crawl(spider_cls: Type[Spider], *args: Any, **kwargs: Any):
        if not issubclass(spider_cls, Spider):
            raise TypeError(f'Spider_cls: {spider_cls} does not fully implemented required interface!')
        spider_ins = spider_cls.create_instance(*args, **kwargs)
        start_requests = spider_ins.start_requests
        async for item in async_gen_func(start_requests):
            spider_ins.save_item(item)
