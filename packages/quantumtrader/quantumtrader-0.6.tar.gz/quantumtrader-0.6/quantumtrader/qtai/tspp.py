from typing import Optional, Tuple, Any
import pandas as pd
from prophet import Prophet
from prophet.plot import *
from prophet.diagnostics import cross_validation, performance_metrics
from prophet.serialize import model_to_json, model_from_json

from quantumtrader.utils.basics import convert_date_format

# warnings
import warnings
warnings.filterwarnings('ignore')


class TSPP(Prophet):

    def __init__(self, o, verbose: bool = False) -> None:
        self.verbose = verbose
        self.o = self._transform(o, vb=self.verbose)

    def _transform(
        self,
        o: pd.DataFrame,
        ds: str = "date",
        y: str = "close",
        vb: bool = False,
        regressors=None,
    ):
        o = convert_date_format(o)

        o['ds'] = o[ds].values
        o['y'] = o[y].values
        # regressors添加解释变量
        if regressors is not None:
            for regressor in regressors:
                o[regressor] = df[regressor].values

        return o

    def fit_prophet_model(self, o, **kwargs) -> Prophet:
        """fit prophet model

        Args:
          - growth (str, optional): 'linear'、'logistic' 或 'flat'，用于指定线性、逻辑或平坦趋势. Defaults to 'linear'.
          - changepoints (Any, optional): 变化点,通过速率改变确认变化点，默认指定 25 个潜在变化点，这些变化点统一放置在时间序列的前 80% 中，如需手动指定，即`changepoints=['2014-01-01']`,写入日期列表。如果没有指定，将自动选择潜在变化点. Defaults to None.
          - n_changepoints (int, optional):要包含的潜在变化点的数量。如果提供了 `changepoints` 输入，则不使用. Defaults to 25.
          - changepoint_range (float, optional): 变化点范围,在历史数据中估计趋势变化点的比例。默认为0.8，即前80%. Defaults to 0.8.
          - yearly_seasonality (str, optional): 年度季节性,拟合年度季节性，`"auto"`， `True`, `False，或提供的傅里叶分量数(int数值型)，Defaults to 'auto'.
          - weekly_seasonality (str, optional): 周季节性，拟合周季节性。可以是 `'auto'`、`True`、`False`，或者生成傅里叶项的数量(int数值型)，Defaults to 'auto'.
          - daily_seasonality (str, optional): 日季节性，拟合日季节性。可以是 `'auto'`、`True`、`False`，或者生成傅里叶项的数量(int数值型)，Defaults to 'auto'.
          - holidays (Any, optional): 具有列 holiday（字符串）、ds（日期类型）的pd.DataFrame，并且可选地具有列 lower_window 和 upper_window，这些列指定了将被包括为节假日的日期周围的范围。lower_window=-2 将包括日期前两天作为节假日。还可以有列 prior_scale，指定该节假日的先验比例，Defaults to None.
          - seasonality_mode (str, optional): 季节性模式，`'additive'`（默认）或 `'multiplicative'`， Defaults to 'additive'.
          - seasonality_prior_scale (float, optional): 季节性先验比例,调节季节性模型强度的参数。较大的值允许模型拟合更大的季节性波动，较小的值减弱季节性。可以使用 `add_seasonality` 为个别季节性指定. Defaults to 10.
          - holidays_prior_scale (float, optional): 节假日先验比例,调节节假日组成部分模型强度的参数，除非在节假日输入中被覆盖。 Defaults to 10.
          - changepoint_prior_scale (float, optional): 变化点先验比例,调节自动变化点选择的灵活性的参数。较大的值将允许许多变化点，较小的值将允许较少的变化点，Defaults to 0.05.
          - mcmc_samples (int, optional): 整数，如果大于0，将进行完整的贝叶斯推断，使用指定数量的MCMC样本。如果为0，将进行MAP估计，Defaults to 0.
          - interval_width (float, optional): 区间宽度，浮点数，提供的预测不确定性区间的宽度。如果` mcmc_samples=0`，这将只是使用MAP估计的趋势的不确定性. Defaults to 0.8.
          - uncertainty_samples (int, optional): 不确定性样本,用于估计不确定性区间的模拟抽样数量。将此值设置为`0`或`False`将禁用不确定性估计并加快计算. Defaults to 1000.
          - stan_backend (Any, optional): 定义在 `StanBackendEnum`中的字符串，默认：`None` - 将尝试迭代所有可用的后端并找到可行的一个. Defaults to None.
          - scaling (str, optional): [description]. Defaults to 'absmax'.
          - holidays_mode (Any, optional): 节假日模式,`'additive'` 或 `'multiplicative'`。默认为 `seasonality_mode`. Defaults to None.
        """
        model = Prophet(**kwargs)
        model.fit(o)
        return model

    # 饱和预测
    def saturating_forecasts(self,
                             o: Optional[pd.DataFrame] = None,
                             cap: Optional[float] = None,
                             floor: Optional[float] = None,
                             train_size:Optional[float]=None,
                             periods: int = 30,
                             show_plot: bool = False,
                             **kwargs) -> Tuple[pd.DataFrame, Prophet, Any]:
        """生成具有可选上限和下限的预测

        Args:
            cap (float, optional): 上限值. Defaults to None.
            floor (float, optional): 下限值. Defaults to None.
            periods (int, optional): 周期. Defaults to 30.
            show_plot (bool, optional): 显示绘图. Defaults to False.
        
        model_kwargs:
            - growth (str, optional): 'linear'、'logistic' 或 'flat'，用于指定线性、逻辑或平坦趋势. Defaults to 'linear'.
            - changepoints (Any, optional): 趋势变化点,通过速率改变确认变化点，默认指定 25 个潜在变化点，这些变化点统一放置在时间序列的前 80% 中，如需手动指定，即`changepoints=['2014-01-01']`,写入日期列表。如果没有指定，将自动选择潜在变化点. Defaults to None.
            - n_changepoints (int, optional):要包含的潜在趋势变化点的数量。如果提供了 `changepoints` 输入，则不使用. Defaults to 25.
            - changepoint_range (float, optional): 趋势变化点范围,在历史数据中估计趋势变化点的比例。默认为0.8，即前80%. Defaults to 0.8.
            - yearly_seasonality (str, optional): 年度季节性,拟合年度季节性，`"auto"`， `True`, `False，或提供的傅里叶分量数(int数值型)，Defaults to 'auto'.
            - weekly_seasonality (str, optional): 周季节性，拟合周季节性。可以是 `'auto'`、`True`、`False`，或者生成傅里叶项的数量(int数值型)，Defaults to 'auto'.
            - daily_seasonality (str, optional): 日季节性，拟合日季节性。可以是 `'auto'`、`True`、`False`，或者生成傅里叶项的数量(int数值型)，Defaults to 'auto'.
            - holidays (Any, optional): 具有列 holiday（字符串）、ds（日期类型）的pd.DataFrame，并且可选地具有列 lower_window 和 upper_window，这些列指定了将被包括为节假日的日期周围的范围。lower_window=-2 将包括日期前两天作为节假日。还可以有列 prior_scale，指定该节假日的先验比例，Defaults to None.
            - seasonality_mode (str, optional): 季节性模式，`'additive'`（默认）或 `'multiplicative'`， Defaults to 'additive'.
            - seasonality_prior_scale (float, optional): 季节性先验比例,调节季节性模型强度的参数。较大的值允许模型拟合更大的季节性波动，较小的值减弱季节性。可以使用 `add_seasonality` 为个别季节性指定. Defaults to 10.
            - holidays_prior_scale (float, optional): 节假日先验比例,调节节假日组成部分模型强度的参数，除非在节假日输入中被覆盖。 Defaults to 10.
            - changepoint_prior_scale (float, optional): 变化点先验比例,调节自动变化点选择的灵活性的参数。较大的值将允许许多变化点，较小的值将允许较少的变化点，Defaults to 0.05.
            - mcmc_samples (int, optional): 整数，如果大于0，将进行完整的贝叶斯推断，使用指定数量的MCMC样本。如果为0，将进行MAP估计，Defaults to 0.
            - interval_width (float, optional): 区间宽度，浮点数，提供的预测不确定性区间的宽度。如果` mcmc_samples=0`，这将只是使用MAP估计的趋势的不确定性. Defaults to 0.8.
            - uncertainty_samples (int, optional): 不确定性样本,用于估计不确定性区间的模拟抽样数量。将此值设置为`0`或`False`将禁用不确定性估计并加快计算. Defaults to 1000.
            - stan_backend (Any, optional): 定义在 `StanBackendEnum`中的字符串，默认：`None` - 将尝试迭代所有可用的后端并找到可行的一个. Defaults to None.
            - scaling (str, optional): [description]. Defaults to 'absmax'.
            - holidays_mode (Any, optional): 节假日模式,`'additive'` 或 `'multiplicative'`。默认为 `seasonality_mode`. Defaults to None.

        pe_kwargs:
           - model (Any): Prophet类对象。拟合后的Prophet模型
           - horizon (Any): 是指预测的一个时间范围、时间长度,当只定义`horizon`，`initial`值是`horizon`的三倍，`period`则是`horizon`的一半，`horizon` 例如：
                
                '1 day'：1天
                '2 hours'：2小时
                '30 minutes'：30分钟
                '5 seconds'：5秒
                '45 milliseconds'：45毫秒
                '100 microseconds'：100微秒
                '200 nanoseconds'：200纳秒

           - period (Any, optional): 意味着每增加一个模型，`period`的值将被添加到训练数据集. Defaults to None.
           - initial (Any, optional): 第一个训练周期将至少包含这么多数据，如果没有提供，将使用`3 * horizon`. Defaults to None.
           - parallel (Any, optional):如何并行化预测计算。默认情况下不使用并行，注意，一些操作目前持有Python的全局解释器锁，因此使用线程进行并行化可能比顺序训练慢。Defaults to None.

                None : 不使用并行
                'processes':使用`concurrent.futures.ProcessPoolExectuor`进行并行化
                'threads':使用`concurrent.futures.ThreadPoolExecutor`进行并行化
                'dask'：使用Dask进行并行化，这需要创建一个dask.distributed客户端。
                `object` : 任何具有 `.map` 方法的实例。这个方法将被调用，使用 

                    :func:single_cutoff_forecast 和一个可迭代序列，其中每个元素是要传递给 
                    :func:single_cutoff_forecast 的参数元组的序列

           - cutoffs (Any, optional): 指定在交叉验证期间使用的截断点. Defaults to None.
           - disable_tqdm (bool, optional): 如果为True，则禁用在parallel=None时显示的进度条. Defaults to False.
           - extra_output_columns (Any, optional): 返回字符串或字符串列表，例如 'trend' 或 ['trend']。在输出中返回的附加列，除了'yhat'和'ds'. Defaults to None.

        Returns:
            [type]: [description]
        """
        if o is None:
            o = self.o
        model_params = {
            "growth": "linear",
            "changepoints": None,
            "n_changepoints": 25,
            "changepoint_range": 0.8,
            "yearly_seasonality": "auto",
            "weekly_seasonality": "auto",
            "daily_seasonality": "auto",
            "holidays": None,
            "seasonality_mode": "additive",
            "seasonality_prior_scale": 10,
            "holidays_prior_scale": 10,
            "changepoint_prior_scale": 0.05,
            "mcmc_samples": 0,
            "interval_width": 0.8,
            "uncertainty_samples": 1000,
            "stan_backend": None,
            "scaling": "absmax",
            "holidays_mode": None
        }
        model_params.update({
            k: v
            for k, v in kwargs.items() if k in model_params
        })
        o["cap"] = cap
        o["floor"] = floor
        if train_size is not None:
            train_size = int(len(o) * 0.8)
            train = o.iloc[:train_size].copy()
            test = o.iloc[train_size:].copy()
            model = self.fit_prophet_model(train, **model_params)
        else:
            model = self.fit_prophet_model(o, **model_params)
        future = model.make_future_dataframe(periods=periods)
        future['cap'] = cap
        future['floor'] = floor
        forecast = model.predict(future)

        pe_kwargs = {
            "horizon": "10 minutes",
            "period": None,
            "initial": None,
            "parallel": "processes",
            "cutoffs": None,
            "disable_tqdm": True,
            "extra_output_columns": None
        }
        pe_kwargs.update({k: v for k, v in kwargs.items() if k in pe_kwargs})
        pe, cv = self.performance_evaluation(model, **pe_kwargs)
        if show_plot:

            if train_size is not None:
                fig = model.plot(forecast)
                ax = fig.gca()  #获取坐标轴
                add_changepoints_to_plot(ax, model, forecast,cp_color="g")
                ax.plot(test["ds"], test["y"], "r")  # 将真实值显示红色
                forecast

            else:
                fig = model.plot(forecast)
                add_changepoints_to_plot(fig.gca(), model, forecast,cp_color="g")
            fig = plot_cross_validation_metric(cv, metric="mape")

        return forecast, model, pe


    def performance_evaluation(self, o, **kwargs):
        """时间序列的交叉验证
        """

        cv = cross_validation(model=o, **kwargs)
        return performance_metrics(cv), cv


    def save(self,m):
        with open(r'prophet_data\models\prophet_baseline_model.json', 'w') as fout:
            fout.write(model_to_json(m))  # Save model

        with open(r'prophet_data\models\prophet_baseline_model.json', 'r') as fin:
            m = model_from_json(fin.read())  # Load model 


TSPP.__doc__="""time_series_prophet


"""
