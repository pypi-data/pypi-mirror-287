# -*- coding: utf-8 -*-
from pandas_ta import dema
from pandas_ta import ema
from pandas_ta import fwma
from pandas_ta import hilo
from pandas_ta import hl2
from pandas_ta import hlc3
from pandas_ta import hwma
from pandas_ta import ichimoku
from pandas_ta import jma
from pandas_ta import kama
from pandas_ta import linreg
from pandas_ta import ma
from pandas_ta import mcgd
from pandas_ta import midpoint
from pandas_ta import midprice
from pandas_ta import ohlc4
from pandas_ta import pwma
from pandas_ta import rma
from pandas_ta import sinwma
from pandas_ta import sma
from pandas_ta import ssf
from pandas_ta import supertrend
from pandas_ta import swma
from pandas_ta import t3
from pandas_ta import trima
from pandas_ta import vidya
from pandas_ta import vwap
from pandas_ta import vwma
from pandas_ta import wcp
from pandas_ta import wma
from pandas_ta import zlma

import pandas as pd
import numpy as np
import talib as ta


def alma(src: pd.Series,
         window_size: int = 9,
         offset: float = 0.85,
         sigma: float = 6.0) -> pd.Series:
    """Arnaud Legoux 移动平均线（ALMA）

        使用高斯分布来加权价格数据，以解决传统移动平均线如简单移动平均线（SMA）或指数移动平均线（EMA）所面临的滞后和平滑问

    Args:
        src (pd.Series):  数据源（e.g. data["close"]）
        window_size (int, optional):  窗口数量（ K线数量）. Defaults to 9.
        offset (float, optional):偏移量（向右或向左调整平均值的因子），控制平滑度(更接近1)和响应性(更接近0)之间的权衡. Defaults to 0.85.
        sigma (float, optional): 均线平滑度。Sigma越大，ALMA越平滑. Defaults to 6.0.

    Raises:
        ValueError: 源数据长度必须至少与窗口数（ K线数量）大小一样长

    Returns:
        pd.Series: alma
    """
    if len(src) < window_size:
        raise ValueError("源数据长度必须至少与窗口大小一样长")

    # 计算便宜了m和标准差s，调整 s 以匹配高斯函数中的指数项
    m = np.floor(offset * (window_size - 1)).astype(int)
    s = window_size / (2 * sigma**2)

    # 计算权重及归一化权重
    weights = np.exp(-0.5 * ((np.arange(window_size) - m)**2) / s)
    weights /= weights.sum()  # Normalize the weights

    # 使用卷积将权重应用于序列（这对于大型数组是高效的）
    result = np.convolve(src, weights, mode='valid')

    # 卷积操作会使结果缩短 'window_size - 1' 个元素
    # 因此，我们需要在结果前面添加 NaN 值以匹配原始序列的长度
    result = np.concatenate((np.full(window_size - 1, np.nan), result))

    return result.astype(np.float32)

def dema(src: pd.Series, length: int = 15) -> pd.Series:
    """双重指数移动平均线-DEMA（Double Exponential Moving Average）

        DEMA旨在减少传统移动平均线产生的滞后性，并减少可能扭曲价格图表走势的“噪音”数量
        
        通过结合单一EMA和双层EMA来改善传统平均线的时间落后问题，从而更早地显示出价格反转的可能性

    Args:
        src (pd.Series): 数据源（e.g. data["close"]）
        length (int, optional): 周期长度. Defaults to 15.

    Returns:
        pd.Series: dema
    """
    e = ta.EMA(src, length)
    d = ta.EMA(e, length)
    return (2 * e - d).astype("float32")

def hma(src: pd.Series, length: int = 9) -> pd.Series:
    """赫尔移动平均线-hma(Hull Moving Average)

    Args:
        src (pd.Series): 数据源（e.g. data["close"]）
        length (int, optional): 周期长度. Defaults to 9.

    Returns:
        pd.Series: hma
    """
    wma1 = 2 * ta.WMA(src, int(length / 2))
    wma2 = ta.WMA(src, length)
    diff = wma1 - wma2
    sqrtLength = round(np.sqrt(length))
    return ta.WMA(diff, sqrtLength)

def tema(src: pd.Series, length: int = 15) -> pd.Series:
    """三重指数移动平均线-TEMA（Triple Exponential Moving Average）

        通过平滑价格数据并识别趋势，三次平滑价格数据减少价格波动的影响

    Args:
        src (pd.Series):数据源（e.g. data["close"]）
        length (int, optional): 周期长度. Defaults to 15.

    Returns:
        pd.Series: tema
    """
    e = ta.EMA(src, length)
    ema_ema = ta.EMA(e, length)
    ema_ema_ema = ta.EMA(ema_ema, length)
    return (3 * (e - ema_ema) + ema_ema_ema).astype("float32")

def vwrma(src: pd.Series, volume: pd.Series, length: int = 14) -> pd.Series:
    """成交量加权移动均线-VWMA(Volume Weighted Moving Average)

    Args:
        src (pd.Series): 加权数据系列（e.g. 收盘价差值-data["close"].diff()）
        volume (pd.Series): 成交量
        length (int, optional): 周期长度. Defaults to 14.

    Returns:
        pd.Series: vwrma
    """
    result = rma(src * volume, length) / rma(volume, length)
    return result.astype(np.float32)
