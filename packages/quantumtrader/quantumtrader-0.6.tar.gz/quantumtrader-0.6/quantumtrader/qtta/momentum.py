# -*- coding: utf-8 -*-
from pandas_ta import ao
from pandas_ta import apo
from pandas_ta import bias
from pandas_ta import bop
from pandas_ta import brar
from pandas_ta import cci
from pandas_ta import cfo
from pandas_ta import cg
from pandas_ta import cmo
from pandas_ta import coppock
from pandas_ta import cti
from pandas_ta import dm
from pandas_ta import er
from pandas_ta import eri
from pandas_ta import fisher
from pandas_ta import inertia
from pandas_ta import kdj
from pandas_ta import kst
from pandas_ta import macd
from pandas_ta import mom
from pandas_ta import pgo
from pandas_ta import ppo
from pandas_ta import psl
from pandas_ta import pvo
from pandas_ta import qqe
from pandas_ta import roc
from pandas_ta import rsi
from pandas_ta import rsx
from pandas_ta import rvgi
from pandas_ta import slope
from pandas_ta import smi
from pandas_ta import squeeze
from pandas_ta import squeeze_pro
from pandas_ta import stc
from pandas_ta import stoch
from pandas_ta import stochrsi
from pandas_ta import td_seq
from pandas_ta import trix
from pandas_ta import tsi
from pandas_ta import uo
from pandas_ta import willr

import pandas as pd
import numpy as np
from quantumtrader.qtta.overlap import vwrma


def vwrsi(c: pd.Series, v: pd.Series, length: int = 14) -> pd.Series:
    """成交量加权相对强度指数-VWRSI（Volume Weighted Relative Strength Index）

    Args:
        c (pd.Series): 收盘价
        v (pd.Series): 成交量
        length (int, optional): 周期长度. Defaults to 14.

    Returns:
        pd.Series: vwrsi
    """
    change_c = c.diff()
    up = vwrma(
        np.maximum(change_c, 0),
        v,
        length,
    )
    down = vwrma(np.minimum(change_c, 0) * -1, v, length)  # 注意这里乘以-1来转换负值为正值
    # 计算rsi
    # 替换NaN值（如果rma返回NaN），因为除以零会导致NaN
    up[np.isinf(up)] = np.nan  # 替换无穷大值（如果rma可能返回它们）
    down[np.isinf(down)] = np.nan  # 替换无穷大值（如果rma可能返回它们）
    rsi = 100 - (100 / (1 + np.where(up == 0, 1, up / down)))
    rsi[np.isnan(rsi)] = 50  # 替换NaN值为50

    return rsi