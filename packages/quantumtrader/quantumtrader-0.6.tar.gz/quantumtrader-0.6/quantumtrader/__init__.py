from importlib.util import find_spec
from pathlib import Path
from pkg_resources import get_distribution, DistributionNotFound
import logging
from importlib import import_module

import os
import sys




lib_name = "quantumtrader"

_dist = get_distribution(lib_name)
try:
    here = Path(_dist.location) / __file__
    if not here.exists():
        raise DistributionNotFound
except DistributionNotFound:
    __version__ = "请使用setup.py安装，或使用 'pip install quantumtrader'进行安装"

version = __version__ = _dist.version

Imports = {
    "alphaVantage-api": find_spec("alphaVantageAPI") is not None,
    "matplotlib": find_spec("matplotlib") is not None,
    "mplfinance": find_spec("mplfinance") is not None,
    "scipy": find_spec("scipy") is not None,
    "sklearn": find_spec("sklearn") is not None,
    "statsmodels": find_spec("statsmodels") is not None,
    "stochastic": find_spec("stochastic") is not None,
    "talib": find_spec("talib") is not None,
    "tqdm": find_spec("tqdm") is not None,
    "vectorbt": find_spec("vectorbt") is not None,
    "pandas_ta": find_spec("pandas_ta") is not None
}



# 动态导入所有子模块

__all__ = []

def import_submodules(package_name):
    root_dir = os.path.dirname(__file__)

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.py') and not filename.startswith('_'):

                module_name = filename[:-3]
                module_path = os.path.join(dirpath, filename)

                module_relative_path = os.path.relpath(module_path, root_dir)
                # 构建导入路径
                import_path = os.path.dirname(module_relative_path).replace(os.sep, '.')

                # 完整的模块名
                full_module_name = f"{package_name}.{import_path}.{module_name}"

                # 检查模块是否已经被导入
                if full_module_name not in sys.modules:
                    # logger.info(f"加载 {full_module_name}")
                    module = import_module(full_module_name)
                    globals()[module_name] = module

                    # 将模块中的所有公共名称添加到 __all__
                    for attribute_name in dir(module):
                        
                        if not attribute_name.startswith('_'):
                            __all__.append(attribute_name)
                            globals()[attribute_name] = getattr(module, attribute_name)

import_submodules(lib_name)

from quantumtrader.qtai import *
from quantumtrader.qtta import *
from quantumtrader.utils import *
