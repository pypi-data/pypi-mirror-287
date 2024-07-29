# 此文件用于编写数据接口---类方式实现

import datetime
import holidays
import asyncio
import pandas as pd
import dolphindb as ddb

from .dict_data import get_price_frequency_dict, get_price_data_type_dict, get_instruments_type_dict
from .dolphin_db_info import *


class GJDataC:

    def __init__(self):
        """
        用于定义一些不同接口所需的变量以及一些初始化操作
        """

        # 数据库参数
        # self.host = HOST
        # self.port = PORT
        # self.user_id = USER_ID
        # self.password = PASSWORD

        # 连接数据库
        # self.db_session = ddb.session()
        # self.db_session.connect(self.host, self.port, self.user_id, self.password)

        ''' get_price 接口相关属性 '''
        self.get_price_data = None  # 用于存放get_price接口数据

        ''' get_instruments 接口相关属性 '''
        self.get_instruments_data = None  # 用于存放get_instruments接口数据

        ''' get_trading_dates 接口相关属性 '''
        self.get_trading_dates_data = None  # 用于存放get_trading_dates接口数据

        ''' get_margin_ratio 接口相关属性 '''
        self.get_margin_ratio_data = None  # 用于存放get_margin_ratio接口数据

        ''' get_fee 接口相关属性 '''
        self.get_fee_data = None  # 用于存放get_fee接口数据

        ''' get_limit_position 接口相关属性 '''
        self.get_limit_position_data = None  # 用于存放get_limit_position接口数据

        ''' get_activate_contract 接口相关属性 '''
        self.get_active_contract_data = None  # 用于存放get_activate_contract接口数据

    @staticmethod
    def connect_db(table_name, db_path):
        """ 
        此方法用于根据不同的数据表及数据库获取数据，只返回Table对象，对应的数据处理在对应的数据接口处理 
        :param table_name: 数据表路径
        :param db_path: 数据库路径
        :return 根据数据库和表路径获取的数据(Table对象), 会话信息(db_session)
        """

        # 连接数据库
        db_session = ddb.session()
        db_session.connect(COMPANY_HOST, COMPANY_PORT, COMPANY_USER_ID, COMPANY_PASSWORD)

        # 从数据库中获取数据
        data = db_session.loadTable(tableName=table_name, dbPath=db_path)

        return data, db_session

    """ 通用方法 """

    @staticmethod
    def general_validate_params_required(param, param_name):
        """
        校验参数是否必填
        :param param: 参数值
        :param param_name: 参数名称
        :return: None （用于校验数据无需返回值）
        """
        if not param:
            raise ValueError(f"{param_name} is required")

    @staticmethod
    def general_validate_either_or(field_1_name, field_1_value, field_2_name, field_2_value):
        """ 
        此方法用于验证二选一的参数填写情况 
        :param field_1_name: 参数1名称
        :param field_1_value: 参数1值
        :param field_2_name: 参数2名称
        :param field_2_value: 参数2值
        :return: None （用于校验数据无需返回值）
        """
        if not field_1_value and not field_2_value:
            raise ValueError(f"{field_1_name} or {field_2_name} is required")
        if field_1_value and field_2_value:
            raise ValueError(f"{field_1_name} and {field_2_name} cannot be both provided")

    def general_validate_date(self, date_str):
        """
        判断字符串是否为datetime.date, datetime.datetime格式。
        :param date_str: 待判断的字符串。
        
        Returns:
            True: 如果是日期格式，返回 True。
            False: 否则返回 False。
        """
        if not self.general_validate_date_str_is_datetime_type(date_str):
            return self.general_validate_date_str_is_date_type(date_str)
        return True

    @staticmethod
    def general_validate_date_str_is_datetime_type(date_data):
        """
        此方法用于验证日期字段是否为可以转换为datetime的类型
        :param date_data: 日期字符串
        
        :return : 如果可以转换为datetime类型，返回 True, 否则返回 False。
        """

        try:
            datetime.datetime.strptime(date_data, '%Y-%m-%d %H:%M:%S')
            return True
        except ValueError:
            return False

    @staticmethod
    def general_validate_date_str_is_date_type(date_data):
        """
        此方法用于验证日期字段是否为可以转换为date的类型
        :param date_data: 日期字符串
        
        :return : 如果可以转换为date类型，返回 True, 否则返回 False。
        """

        try:
            datetime.datetime.strptime(date_data, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    @staticmethod
    def general_validate_field_str_or_list(field_value, field_name):
        """
        对参数的类型进行校验，判断是否为字符串或字符串列表。
        :param field_value: 待校验的参数值。
        :param field_name: 待校验的参数名称。
        :return: None （用于校验数据无需返回值）
        """

        if field_value and not isinstance(field_value, (str, list)):
            raise ValueError(f"{field_name} should be a string or a list of strings")

    @staticmethod
    def general_validate_param_is_str(param_name, param_value):
        """
        校验参数是否为str类型
        :param param_name: 参数名称
        :param param_value: 参数值
        
        :return: None （用于校验数据无需返回值）
        """

        if not isinstance(param_value, str):
            raise ValueError(f"{param_name} type error, please input str type")

    def __general_validate_asset_type(self, asset_type):
        """
        对asset_type进行校验
        :param asset_type: str, 合约类型
        
        :return: None （用于校验数据无需返回值）
        """
        self.general_validate_params_required(asset_type, "asset_type")  # 校验必填参数
        if not isinstance(asset_type, str):
            raise ValueError("asset_type should be a string")
        if asset_type not in ["future", "option"]:
            raise ValueError("asset_type should be 'future' or 'option'")

    def general_validate_fields(self, data, fields):
        """
        根据用户选择的字段进行字段筛选
        :param fields: 字段列表--用户传入的需要返回的字段
        :param data: 数据
        
        :return data: 根据用户填写的字段筛选后的数据
        """

        ''' 校验fields '''
        # 如果没有传入fields, 则返回所有字段
        if not fields:
            return data
        self.general_validate_field_str_or_list(fields, "fields")

        ''' 根据fields进行处理 '''
        # 如果传入了fields，则根据传入的fields进行处理
        columns_list = data.columns.tolist()

        if isinstance(fields, str):
            self._deal_fields(fields, columns_list)
            data = data[[fields]]
        elif isinstance(fields, list):
            for field in fields:
                self._deal_fields(field, columns_list)
            data = data[fields]

        return data

    @staticmethod
    def _deal_fields(_field, columns_list):
        """
        判断用户选择的字段是否存在
        
        :param columns_list: 数据的所有字段
        
        :return: None （用于校验数据无需返回值）
        """
        if _field not in columns_list:
            raise ValueError(
                f"fields: got invalided value '{_field}', choose any in "
                f"{columns_list}")

    @staticmethod
    def general_filter_data_by_field(data, field_name, field_value):
        """
        根据指定的字段进行数据过滤
        :param data: pandas.DataFrame, 数据
        :param field_name: str, 过滤字段
        :param field_value: str or list, 过滤值
        
        :return 根据字段过滤后的数据
        """

        return data[data[field_name].isin(field_value)] if isinstance(
            field_value, list) else data[data[field_name] == field_value]

    def _general_filter_data_by_field(self, data, field_name, field_value):
        """
        根据自定字段进行类型校验以及数据筛选
        :param data: 需要处理的数据
        :param field_name: 字段名
        :param field_value: 字段值
        
        :return : 根据字段过滤后的数据
        """
        self.general_validate_field_str_or_list(field_value, field_name)
        return self.general_filter_data_by_field(data, field_name, field_value)

    def general_date_str_to_date(self, date_str):
        """ 
        将date类型的str转换成datetime.date类型 
        :param date_str: str, 日期字符串
        """
        if not self.general_validate_date_str_is_date_type(date_str):
            raise ValueError("date_str is not a valid date string, please use the format 'YYYY-MM-DD")

        return datetime.datetime.strptime(date_str, "%Y-%m-%d")

    """ get_price(获取行情数据接口) """

    def get_price(self, order_book_ids=None, asset_type="future", frequency=None, start_date=None, end_date=None,
                  fields=None):
        """
        行情数据接口
        :param order_book_ids: 合约代码--必填
        :param asset_type: 合约类型--必填, 默认为--'future'
        :param frequency: 频率--必填
        :param start_date: 开始日期--选填
        :param end_date: 结束日期--选填
        :param fields: 字段列表--选填
        :return: 行情数据
        """

        # # 从数据库获取的数据是Table类型，需要转换为DataFrame类型, 并按照时间进行排序
        # self.get_price_data = self.get_price_data.sort_values(by='datetime', ascending=True)

        ''' 数据校验 (先对必填参数进行校验)'''
        # 对order_book_ids进行校验
        self.__get_price_validate_order_book_ids(order_book_ids)

        # 对asset_type进行校验
        self.__general_validate_asset_type(asset_type)

        # 对frequency进行校验
        self.__get_price_validate_frequency(frequency)

        # 对 start_date 和 end_date 进行校验
        self.__get_price_validate_start_end_date(start_date, end_date)

        ''' 参数校验完成后，开始根据参数从服务器获取数据 '''
        # 此处获取数据时已经根据order_book_ids筛选过一次数据了，所以后续不需要再对该字段进行筛选
        self.__get_price_data_get_data(order_book_ids, asset_type, frequency)

        ''' 数据处理 '''
        # 根据frequency进行处理
        self.__get_price_by_type_frequency(asset_type, frequency)

        # 根据start_date和end_date筛选数据
        self.__get_price_filter_by_date(start_date, end_date, order_book_ids)

        # 对fields进行处理
        self.__get_price_validate_fields(fields)

        return self.get_price_data

    # @staticmethod
    def __get_price_validate_order_book_ids(self, order_book_ids):
        """
        对order_book_ids 类型 以及 是否必填 进行校验
        :param order_book_ids: 合约类型
        
        :return: None 
        """
        self.general_validate_params_required(order_book_ids, "order_book_ids")  # 校验必填参数
        self.general_validate_field_str_or_list(order_book_ids, "order_book_ids")  # 校验参数类型

    # def get_price_filter_by_order_book_ids(self, order_book_ids):
    #     """
    #     根据order_book_ids筛选数据
    #     """
    #     if isinstance(order_book_ids, str):
    #         self.get_price_data = self.get_price_data[self.get_price_data["order_book_ids"] == order_book_ids]
    #     elif isinstance(order_book_ids, list):
    #         self.get_price_data = self.get_price_data[self.get_price_data["order_book_ids"].isin(order_book_ids)]
    #     return self.get_price_data

    def __get_price_validate_frequency(self, frequency):
        """
        对frequency进行校验
        
        :param frequency: 频率
        :return: None
        """

        self.general_validate_params_required(frequency, "frequency")  # 校验必填参数
        if not isinstance(frequency, str):
            raise ValueError("frequency should be a string")

    def __get_price_validate_start_end_date(self, start_date, end_date):
        """
        对 start_date 和 end_date 进行校验
        校验 start_date 和 end_date 是否同时提供，或者都不提供。
        
        :param start_date: 开始日期
        :param end_date: 结束日期
        :return: None
        """
        if (start_date and not end_date) or (not start_date and end_date):
            raise ValueError("start_date and end_date should be both provided or not provided at all")
        if start_date and end_date:
            # 如果提供了，则进行进一步校验
            is_start_datetime = self._is_convertible_datetime(start_date)
            is_end_datetime = self._is_convertible_datetime(end_date)
            if not is_end_datetime or not is_start_datetime:
                raise ValueError(
                    "start_date and end_date should be datetime.datetime objects or "
                    "convertible to datetime.datetime objects")

            # 如果传入的数据类型符合要求，进行转换
            start_date, end_date = self._get_price_convert_start_end_date(start_date, end_date)
            if start_date > end_date:
                raise ValueError("start_date should be earlier than end_date")

    @staticmethod
    def _get_price_convert_start_end_date(start_date, end_date):
        """
        将 start_date 和 end_date 转换为 datetime 类型。
        
        :param start_date: 开始日期，可以是 datetime.datetime 对象或字符串。
        :param end_date: 结束日期，可以是 datetime.datetime 对象或字符串。
        :return: 转换后的 start_date 和 end_date。
        """

        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S') if isinstance(start_date, str) \
            else start_date
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S') if isinstance(end_date, str) \
            else end_date

        return start_date, end_date

    @staticmethod
    def _is_convertible_datetime(date_data):
        """
        判断 date_data 是否是 datetime 类型或可以转换成 datetime 类型的字符串，并精确到秒。
        param: date_data: 要判断的值。

        Returns:
            True 如果 start_date 是 datetime 类型或可以转换成 datetime 类型的字符串，否则 False。
        """

        if isinstance(date_data, datetime.datetime):
            return True
        elif isinstance(date_data, str):
            try:
                datetime.datetime.strptime(date_data, "%Y-%m-%d %H:%M:%S")
                return True
            except ValueError:
                return False
        else:
            return False

    def __get_price_filter_by_date(self, start_date, end_date, order_book_ids):
        """
        根据start_date和end_date筛选数据
        此处order_book_ids参数用于处理未传递start_date和end_date的情况(根据order_book_ids返回距离当前时间最近的一条数据)
        
        :param start_date: 开始时间
        :param end_date: 结束时间
        :param order_book_ids: 合约代码
        :return: None
        """
        # 将'date_time'列转换为datetime类型
        try:
            if self.get_price_data['datetime'].dtype != 'datetime64[ns]':
                self.get_price_data['datetime'] = pd.to_datetime(self.get_price_data['datetime'])
        except ValueError:
            raise ValueError("source data's datetime format is not correct")

        # 如果传递了start_date 和 end_date, 则返回时间段内的数据
        if start_date and end_date:
            self.get_price_data = self.get_price_data[
                (self.get_price_data['datetime'] >= start_date) & (self.get_price_data['datetime'] <= end_date)]

        # 如果没有传递start_date 和 end_date, 则根据传入的order_book_ids返回每个合约距离当前时间最近的一条数据
        elif not start_date and not end_date:
            date_time = datetime.datetime.now()
            self.get_price_data = self.get_price_data[
                self.get_price_data["datetime"] <= date_time]

            # 根据传入的order_book_ids进行处理
            if isinstance(order_book_ids, str):
                self.get_price_data = self.get_price_data.tail(1)
            else:
                # 将order_book_id作为分组键，并找到每个分组中距离当前时间最近的数据
                nearest_data = self.get_price_data.groupby('order_book_ids')
                # 使用 tail(1) 获取每个组的最后一条数据
                self.get_price_data = nearest_data.apply(lambda x: x.tail(1)).reset_index(drop=True)

    def __get_price_validate_fields(self, fields):
        """
        根据用户选择的字段返回数据
        :param fields: 字段列表 -- 用户传入的需要返回的字段
        
        :return : None

        """
        self.get_price_data = self.general_validate_fields(self.get_price_data, fields)

    def __get_price_by_type_frequency(self, asset_type, frequency):
        """
        根据合约类型和frequency筛选数据
        
        :param asset_type: 合约类型
        :param frequency: 频率
        :return: None
        """
        # 判断asset_type是否存在
        if not get_price_frequency_dict.get(asset_type, None):
            raise ValueError(
                f"asset_type: got invalided value {asset_type}, choose any in {list(get_price_frequency_dict.keys())}")

        # frequency是否存在
        exists, suffix = self._ends_with(frequency, list(get_price_frequency_dict[asset_type].keys()))
        if not exists:
            raise ValueError(f"{frequency} is not a valid frequency for {asset_type} contract")
        # frequency存在再根据频率对数据做进一步处理
        else:
            bar_or_tick = get_price_frequency_dict[asset_type][suffix]  # 获取数据类型是bar还是tick，根据值处理字段
            self.__get_price_data_rename_columns(bar_or_tick)  # 重命名字段

    @staticmethod
    def _ends_with(variable, suffixes):
        """判断变量是否以列表中的元素结尾。
        :param variable: 待判断的变量
        :param suffixes: 列表，元素为字符串，表示后缀
        :return: True or False
        """
        for suffix in suffixes:
            if variable.endswith(suffix):
                return True, suffix
        return False, ""

    def __get_price_data_rename_columns(self, bar_or_tick):
        """
        将从数据库中获取的数据列名重命名
        
        :param bar_or_tick: 是bar类型数据还是tick类型(不同类型字段不同)
        :return: None
        """

        new_columns = get_price_data_type_dict.get(bar_or_tick)
        self.get_price_data = self.get_price_data.rename(columns=new_columns)

    def _get_price_get_data(self, order_book_ids, table_name, db_path):
        """
        用于接收数据表以及数据库，获取数据
        : params order_book_ids: 合约代码 
        : params table_name: 数据表路径 
        : params db_path: 数据库路径
        
        : return filtered_data: 从数据库获取并根据合约代码筛选后的数据
        """
        get_price_data, db_session = self.connect_db(table_name, db_path)

        # 使用 DolphinDB 的 where 子句筛选数据
        if isinstance(order_book_ids, str):
            limit_data = get_price_data.where(f"instrument_id='{order_book_ids}'")
        else:
            limit_data = get_price_data.where(f"instrument_id in {order_book_ids}")

        # 分批处理
        filtered_data = self._get_price_get_data_todf(limit_data)

        # 关闭数据库连接
        db_session.close()

        return filtered_data

    @staticmethod
    def _get_price_get_data_todf(data):
        """
        用于接收从数据库获取的数据，并分批处理，将其转换成dataframe格式的数据返回
        : params data: 从数据库获取的数据
        : return : 转换成dataframe格式后的数据
        """

        result = pd.DataFrame()
        if data.rows > 1000000:
            chunk_size, start = 1000000, 0
            while start < data.rows:
                limit_data = data.limit([start, chunk_size]).toDF()
                result = limit_data if result.empty else pd.concat([result, limit_data], ignore_index=True)
                start += chunk_size

            return result
        return data.toDF()

    # @staticmethod
    # def _get_price_get_data_todf_in_batches(self, data, order_book_ids):
    #     """
    #     用于接收从数据库获取的数据，并分批处理，将其转换成dataframe格式的数据返回
    #     : params data: 从数据库获取的数据
    #     : params order_book_ids: 合约代码
    #     : return : 转换成dataframe格式后的数据
    #     """

    #     result = pd.DataFrame()
    #     if isinstance(order_book_ids, str):
    #         if data.rows > 1000000:
    #             chunk_size, start = 1000000, 0
    #             while start < data.rows:
    #                 limit_data = data.limit([start, chunk_size]).toDF()
    #                 result = limit_data if result.empty else pd.concat([result, limit_data], ignore_index=True)
    #                 start += chunk_size

    #             return result
    #         return data.toDF()
    #     elif isinstance(order_book_ids, list):
    #         for order_book_id in order_book_ids:
    #             instrument_id_df = self._get_price_get_data_todf_by_instrument_id(data, order_book_id, result)
    #             result = instrument_id_df if result.empty else pd.concat([result, instrument_id_df], ignore_index=True)
    #         return result
    # def _get_price_get_data_todf_by_instrument_id(self, data, order_book_id, result_df):
    #     """
    #     此方法用于批量获取数据(数据量过大)
    #     :param data: 从dolphindb查询到的数据
    #     :param order_book_ids: 合约代码列表
    #     :param result_df: 处理后的dataframe结果集
    #     """

    #     data.where(f"instrument_id='{order_book_id}'")

    #     if data.rows > 1000000:
    #         chunk_size, start = 1000000, 0
    #         while start < data.rows:
    #             limit_data = data.limit([start, chunk_size]).toDF()
    #             result_df = limit_data if result_df.empty else pd.concat([result_df, limit_data], ignore_index=True)
    #             start += chunk_size

    #         return result_df
    #     return data.toDF()

    def __get_price_data_get_data(self, order_book_ids, asset_type, frequency):
        """ 
        根据参数获取数据库和表名，调用接口获取数据 
        
        :param order_book_ids: 合约代码列表
        :param asset_type: 合约类型
        :param frequency: 频率
        :return: None
        """

        ''' 期货行情数据 '''
        if asset_type == "future":
            if frequency == "tick_l1":  # 期货l1级别tick行情数据
                self.get_price_data = self._get_price_get_data(order_book_ids, history_future_tick_db_table_name,
                                                               history_future_tick_db_path)
            elif frequency == "1d":  # 期货日bar行情数据
                self.get_price_data = self._get_price_get_data(order_book_ids, history_future_day_db_table_name,
                                                               history_future_day_db_path)
            elif frequency == "1min":  # 期货分钟bar行情数据
                self.get_price_data = self._get_price_get_data(order_book_ids, history_future_min_db_table_name,
                                                               history_future_min_db_path)
            # 数据库暂无数据
            # elif frequency == "1min_gtja":  # 公司合成的分钟bar行情数据
            #     self.get_price_data = self._get_price_get_data(order_book_ids, history_future_min_gtja_db_table_name,
            #                                                    history_future_min_gtja_db_path)
            # elif frequency == "tick_l2":  # 期货l2级别tick行情数据
            #     self.get_price_data = self._get_price_get_data(order_book_ids, history_future_tick_l2_db_table_name,
            #                                                      history_future_tick_l2_db_path)
            # else:
            #     raise Exception("frequency is not valid for future contract")
        elif asset_type == "option":
            if frequency == "1d":  # 期权日bar行情数据
                self.get_price_data = self._get_price_get_data(order_book_ids, history_option_day_db_table_name,
                                                               history_option_day_db_path)
            elif frequency == "1min":  # 期权分钟bar行情数据
                self.get_price_data = self._get_price_get_data(order_book_ids, history_option_min_db_table_name,
                                                               history_option_min_db_path)
            elif frequency == "tick":  # 期权tick行情数据
                self.get_price_data = self._get_price_get_data(order_book_ids, history_option_tick_db_table_name,
                                                               history_option_tick_db_path)
            else:
                raise Exception("frequency is not valid for option contract")
        else:
            raise Exception("asset_type is not valid")

    """ get_instruments(合约基础信息) """

    def get_instruments(self, order_book_ids=None, commodity=None, asset_type=None, fields=None):
        """
        获取合约基础信息接口
        :param order_book_ids: str or list,合约代码 和 commodity_type 必填 二选一
        :param commodity: str or list, 合约品种  和 commodity_type 必填 二选一  若填写品种参数，则返回该品种所有合约基础信息
        :param asset_type: str, 合约类型--必填
        :param fields: str or list, 字段列表--选填，默认为全部字段
        :return: 合约基础信息
        """

        ''' 数据校验 '''
        # 对order_book_ids和commodity是否必填进行校验
        self.__get_instruments_validate_order_book_ids_commodity(order_book_ids, commodity)

        # 对asset_type进行校验
        self.__general_validate_asset_type(asset_type)

        ''' 根据传入的asset_type以及order_book_ids获取数据 '''
        self.__get_instruments_data_get_data(asset_type=asset_type, order_book_ids=order_book_ids, commodity=commodity)

        # 重命名字段
        self.__get_instruments_data_rename_columns(asset_type)

        # 从交易参数中填充commodity和trading_hour的值
        # self.get_instruments_deal_commodity_trading_hour()

        ''' 按照文档筛选需要返回的字段 '''
        self.__get_instruments_data_filter_return_fileds(asset_type)

        # 对fields进行校验并根据fields返回对应的字段
        self.__get_instruments_validate_fields(fields)

        return self.get_instruments_data

    def __get_instruments_validate_order_book_ids_commodity(self, order_book_ids, commodity):
        """
        对order_book_ids和commodity_type进行校验
        order_book_ids和commodity_type二选一，且只能二选一
        :param order_book_ids: str or list,合约代码
        :param commodity: str or list, 合约品种
        :return: None
        """

        ''' 对order_book_ids和commodity_type进行校验 '''
        self.general_validate_either_or("order_book_ids", order_book_ids, "commodity", commodity)

        if order_book_ids:
            self.general_validate_field_str_or_list(order_book_ids, "order_book_ids")
        if commodity:
            self.general_validate_field_str_or_list(commodity, "commodity")

    def get_instruments_filter_order_book_ids(self, order_book_ids):
        """
        根据order_book_ids筛选数据
        :param order_book_ids: str or list,合约代码
        :return: None
        """

        self.get_instruments_data = self.get_instruments_data[
            self.get_instruments_data["order_book_id"].isin(order_book_ids)] if isinstance(
            order_book_ids, list) else self.get_instruments_data[
            self.get_instruments_data["order_book_id"] == order_book_ids]

    def get_instruments_filter_commodity(self, commodity):
        """
        根据commodity筛选数据
        :param commodity: str or list, 合约品种
        :return: None

        """

        self.get_instruments_data = self.get_instruments_data[
            self.get_instruments_data["commodity"].isin(commodity)] if isinstance(
            commodity, list) else self.get_instruments_data[
            self.get_instruments_data["commodity"] == commodity]

    def __get_instruments_data_filter_return_fileds(self, asset_type):
        """
        根据asset_type返回对应的字段(不同合约类型字段不同)
        :param asset_type: 合约类型，"future" or "option"
        :return: None
        """

        if asset_type == "future":
            self.get_instruments_data = self.get_instruments_data[get_instruments_type_dict.get("future_return_fields")]
        elif asset_type == "option":
            self.get_instruments_data = self.get_instruments_data[get_instruments_type_dict.get("option_return_fields")]

    def __get_instruments_validate_fields(self, fields):
        """
        根据用户选择的字段返回数据
        :param fields: str or list, 字段列表
        :return: None
        """

        self.get_instruments_data = self.general_validate_fields(self.get_instruments_data, fields)

    def _get_instruments_data_get_data(self, order_book_ids, table_name, db_path):
        """
        用于接收数据表以及数据库，获取数据
        
        :param order_book_ids: 合约代码
        :param table_name: 数据表路径
        :param db_path: 数据库路径
        :return: 获取的数据
        """
        get_instruments_data, db_session = self.connect_db(table_name, db_path)

        filtered_data = pd.DataFrame()
        # 使用 DolphinDB 的 where 子句筛选数据
        if isinstance(order_book_ids, str):
            filtered_data = get_instruments_data.where(f"instrumentid='{order_book_ids}'").toDF()
        elif isinstance(order_book_ids, list):
            filtered_data = get_instruments_data.where(f"instrumentid in {order_book_ids}").toDF()

        # 关闭数据库连接
        db_session.close()

        return filtered_data

    def __get_instruments_data_get_data(self, asset_type=None, order_book_ids=None, commodity=None):
        """ 
        根据参数获取数据库和表名，调用接口获取数据 
        
        :param asset_type: 合约类型
        :param order_book_ids: 合约代码
        :param commodity: 合约品种
        :return: None
        """

        # 如果传入的是commodity，需要获取参数品种下所有合约代码
        if commodity:
            # 如果传递的是品种信息，根据品种去交易参数表中查找出对对应的数据
            # 获取交易参数
            trading_param_data, db_session = self.connect_db(trading_params_db_table_name, trading_params_db_path)

            if isinstance(commodity, str):
                order_book_ids = list(set(
                    trading_param_data.select("contractcode").where(f"productcode = '{commodity}'").toDF()[
                        "contractcode"].to_list()))
            elif isinstance(commodity, list):
                order_book_ids = list(set(
                    trading_param_data.select("contractcode").where(f"productcode in {commodity}").toDF()[
                        "contractcode"].to_list()))

            # 关闭数据库连接
            db_session.close()

        ''' 期货行情数据 '''
        if asset_type == "future":
            self.get_instruments_data = self._get_instruments_data_get_data(order_book_ids,
                                                                            future_contract_db_table_name,
                                                                            future_contract_db_path)
            self.get_instruments_data["type"] = "future"
        elif asset_type == "option":
            self.get_instruments_data = self._get_instruments_data_get_data(order_book_ids,
                                                                            option_contract_db_table_name,
                                                                            option_contract_db_path)
            self.get_instruments_data["type"] = "option"
            self.get_instruments_data["exercise_type"] = self.get_instruments_data["optionstype"]
        else:
            raise Exception("asset_type is not valid")
        self.get_instruments_data["commodity"] = ""
        self.get_instruments_data["trading_hour"] = ""

    def __get_instruments_data_rename_columns(self, asset_type):
        """
        将从数据库中获取的数据列名重命名为文档要求的名字
        
        :param asset_type: 合约类型
        :return: None
        """

        new_columns = get_instruments_type_dict.get(asset_type)
        self.get_instruments_data = self.get_instruments_data.rename(columns=new_columns)

    def get_instruments_deal_commodity_trading_hour(self):
        """
        用于处理commodity和trading_hour
        """

        try:
            # 获取交易参数
            trading_param_data, db_session = self.connect_db(trading_params_db_table_name, trading_params_db_path)

            for index, row in self.get_instruments_data.iterrows():
                match = trading_param_data.toDF()[trading_param_data.toDF()['contractcode'] == row['order_book_id']]
                if not match.empty:
                    self.get_instruments_data.loc[index, 'commodity'] = match['productcode'].iloc[0]
                    self.get_instruments_data.loc[index, 'trading_hour'] = match['tradesection'].iloc[0]
            db_session.close()
        except ValueError as e:
            print(e)
            pass

    """   get_trading_dates(交易日历)  """

    def get_trading_dates(self, date=datetime.date.today(), n=None, start_date=None, end_date=None):
        """
        获取交易日历接口
        :param date: str--选填, 日期
        :param n: str--必填，根据不同值获取对应的交易日历
        :param start_date: str（datetime.date, datetime.datetime）--选填, 开始日期
        :param end_date: str（datetime.date, datetime.datetime）--选填, 结束日期
        若填写【date、n】为入参，则无法填写【start_date、end_date】，反之依然
        :return: 交易日历
        """

        """ 校验参数 """
        self.get_trading_dates_data = self.__get_trading_dates_validate_date_n_start_end(date, n, start_date, end_date)

        return self.get_trading_dates_data

    def __get_trading_dates_validate_date_n_start_end(self, date, n, start_date, end_date):
        """
        校验date、n和start_date、end_date有效性
        
        :param date: str-- 日期
        :param n: str--根据不同值获取对应的交易日历
        :param start_date: str（datetime.date, datetime.datetime）--开始日期
        :param end_date: str（datetime.date, datetime.datetime）--结束日期
        :return: None
        """

        if (date and n) and (start_date and end_date):
            raise ValueError("date、n and start_date、end_date can only be selected one at a time")
        if n and (start_date or end_date):
            raise ValueError("parameter error: cannot pass date、n and start_date、end_date at the same time")
        elif date and n:  # 根据date和n获取交易日历
            return self.__get_trading_dates_by_date_n(date, n)
        elif start_date and end_date:  # 根据start_date和end_date获取交易日历
            return self.__get_trading_dates_by_start_end(start_date, end_date)
        else:
            raise ValueError("parameter error: please pass date、n or start_date、end_date")

    def __get_trading_dates_by_date_n(self, date, n):
        """
        校验 date 和 n
        :param date: str--选填, 日期
        :param n: str--必填，根据不同值获取对应的交易日历
        :return: 根据date和n筛选后的数据
        """

        if not isinstance(n, str):
            raise ValueError("n parameter error, type should be str")
        if n not in ["0", "1", "2", "3", "4", "5", "6"]:
            raise ValueError("n parameter error, value range should be [0, 1, 2, 3, 4, 5, 6]")
        if not isinstance(date, (str, datetime.date)):
            raise ValueError("date parameter error, type should be str or datetime.date")

        if isinstance(date, str):
            date = datetime.datetime.strptime(date, "%Y-%m-%d").date()

        return self.get_dates_in_n(date, n)

    def __get_trading_dates_by_start_end(self, start_date, end_date):
        """
        根据start_date和end_date获取交易日历
        :param start_date: str（datetime.date, datetime.datetime）--选填, 开始日期
        :param end_date: str（datetime.date, datetime.datetime）--选填, 结束日期
        
        :return: 根据start_date和end_date筛选后的数据
        """

        trading_params_data = self.get_trading_dates_get_data()

        # 校验日期类型
        if self.check_date_type(start_date, end_date):
            # 如果类型校验通过，则将start_date和end_date处理成对应的时间数据类型
            if isinstance(start_date, str):
                start_date = self._get_trading_dates_by_start_end(start_date)
            if isinstance(end_date, str):
                end_date = self._get_trading_dates_by_start_end(end_date)
            # 筛选 tradingday 列在 start_date 和 end_date 之间的数据
            filtered_df = trading_params_data.loc[
                (trading_params_data['tradingday'] >= start_date) & (trading_params_data['tradingday'] <= end_date)]

            # 筛选 tradeflag 列等于 T 的数据（是交易日的数据）
            final_df = filtered_df.loc[filtered_df['tradeflag'] == 'T']
            self.get_trading_dates_data = sorted(final_df["tradingday"].tolist())
        else:
            raise ValueError(
                "start_date or end_date type error, please input str, datetime.date or datetime.datetime type")

        return self.get_trading_dates_data

    @staticmethod
    def _get_trading_dates_by_start_end(time_data):
        """
        将时间str数据处理成对应的时间类型（例如：date类型的str，处理成datetime.date类型）
        
        :param time_data: 时间数据
        :return: 转换后的时间数据类型
        """
        try:
            time_data = datetime.datetime.strptime(time_data, "%Y-%m-%d").date()
            return time_data
        except ValueError:
            try:
                time_data = datetime.datetime.strptime(time_data, "%Y-%m-%d %H:%M:%S").date()
                return time_data
            except ValueError:
                raise ValueError("parameter type error")

    def check_date_type(self, _start_date, _end_date):
        """
        判断start_date和end_date是否为str，datetime.date, datetime.datetime三种类型，
        其中，如果是str类型，还要判断是否是datetime.date, datetime.datetime两种类型的字符串.
        :params _start_date: 开始日期
        :params _end_date: 结束日期
        
        :return: 如果类型正确，返回 True。否则返回 False，并打印错误信息
        """
        if isinstance(_start_date, (str, datetime.date, datetime.datetime)) and \
                isinstance(_end_date, (str, datetime.date, datetime.datetime)):
            if isinstance(_start_date, str) and not self.general_validate_date(_start_date):
                raise ValueError("start_date is not a valid date string format")
            if isinstance(_end_date, str) and not self.general_validate_date(_end_date):
                raise ValueError("end_date is not a valid date string format")
            return True
        else:
            raise ValueError(
                "start_date or end_date type error, please input str, datetime.date or datetime.datetime type")

    def get_trading_dates_get_data(self):
        """
        从dolphindb获取交易日历
        :return: 交易日历数据
        """

        params_data, db_session = self.connect_db(trading_dates_db_table_name, trading_dates_db_path)
        trading_params_data = params_data.toDF()
        trading_params_data["tradingday"] = pd.to_datetime(trading_params_data["tradingday"], format="%Y%m%d").dt.date
        db_session.close()
        return trading_params_data

    @staticmethod
    def get_date_get_week_month_year(data, start_date, end_date):
        """
        用于获取当前日期所在周、月、年的交易日数据
        
        :param data: 交易日历数据
        :param start_date: 开始日期
        :param end_date: 结束日期
        
        :return: 交易日历数据

        """

        # 获取开始日期和结束日期
        start_date = datetime.datetime.strptime(start_date, "%Y%m%d").date()
        end_date = datetime.datetime.strptime(end_date, "%Y%m%d").date()

        # 筛选出时间段内的所有数据
        filtered_df = data.loc[(data['tradingday'] >= start_date) & (data['tradingday'] <= end_date)]
        # 筛选出时间段内的所有交易日
        final_df = filtered_df.loc[filtered_df['tradeflag'] == 'T']

        return sorted(final_df["tradingday"].tolist())

    def get_dates_in_n(self, _date, _n):
        """
        获取选定日期, 根据n值获取对应的交易日历。

        :param _date: 选定的日期，可以是 datetime.date 或 datetime.datetime 对象
        :param _n: 时间段，可以是 'week'、'month' 或 'year'
        :return: 一个包含所有日期的列表
        """

        trading_params_data = self.get_trading_dates_get_data()

        cn_holidays = holidays.CN()  # 创建中国节假日对象

        time_period_mapping_dict = {
            "0": _date in cn_holidays,
            "1": trading_params_data.loc[trading_params_data["tradingday"] == _date]["nexttrdday"].iloc[0],
            "2": trading_params_data.loc[trading_params_data["tradingday"] == _date]["prevtrdday"].iloc[0],
            "3": self.get_date_get_week_month_year(trading_params_data,
                                                   trading_params_data.loc[trading_params_data["tradingday"] == _date][
                                                       "firsttrddayweek"].iloc[0],
                                                   trading_params_data.loc[trading_params_data["tradingday"] == _date][
                                                       "lasttrddayweek"].iloc[0]),
            "4": self.get_date_get_week_month_year(trading_params_data,
                                                   trading_params_data.loc[trading_params_data["tradingday"] == _date][
                                                       "firsttrddaymonth"].iloc[0],
                                                   trading_params_data.loc[trading_params_data["tradingday"] == _date][
                                                       "lasttrddaymonth"].iloc[0]),
            "5": self.get_date_get_week_month_year(trading_params_data,
                                                   trading_params_data.loc[trading_params_data["tradingday"] == _date][
                                                       "firsttrddayyear"].iloc[0],
                                                   trading_params_data.loc[trading_params_data["tradingday"] == _date][
                                                       "lasttrddayyear"].iloc[0]),
            "6": trading_params_data.loc[trading_params_data["tradingday"] == _date]["nightday"].iloc[0],
        }

        if _n not in time_period_mapping_dict:
            raise ValueError("n parameter error, value range should be [0, 1, 2, 3, 4, 5, 6]")

        return time_period_mapping_dict[_n]

    # @staticmethod
    # def get_current_week(date_data):
    #     """
    #     获取选定日期的当周。

    #     Args:
    #         date_data: 选定的日期，可以是 datetime.date 或 datetime.datetime 对象。

    #     Returns:
    #         一个元组，包含当前周的开始日期和结束日期，类型为 datetime.date。
    #     """

    #     # 获取星期几 (0-6, 0代表星期一)
    #     weekday = date_data.weekday()

    #     # 计算当周的开始日期和结束日期
    #     start_date = date_data - datetime.timedelta(days=weekday)
    #     end_date = start_date + datetime.timedelta(days=6)

    #     return start_date, end_date

    """ get_margin_ratio 期货保证金 """

    def get_margin_ratio(self, order_book_id=None, commodity=None, date=datetime.datetime.now(), exchange=None):
        """
        获取期货保证金信息接口
        :param order_book_id: str--选填（和commodity二选一），合约代码
        :param commodity: str--选填（和order_book_id二选一），合约品种,如果入参为品种，则返回该品种条件下所有合约的保证金list
        :param date: datetime--必填（默认今天)，日期
        :param exchange: str--必填，交易所
        :return:
        """

        """ 校验数据 """
        # 校验order_book_id和commodity
        self.get_margin_ratio_validate_order_book_id_commodity(order_book_id, commodity)

        # 校验exchange
        self.get_margin_ratio_validate_exchange(exchange)

        # 校验date
        self.get_margin_ratio_validate_date(date)

        """ 处理数据 """
        # 根据date筛选数据
        self.get_margin_ratio_data_by_date(date)

        # 根据exchange筛选数据
        self.get_margin_ratio_data_by_exchange(exchange)

        return self.get_margin_ratio_data[["order_book_id", "commodity", "date", "exchange"]]

    def get_margin_ratio_validate_exchange(self, exchange):
        """ 校验exchange """

        self.general_validate_params_required(exchange, "exchange")  # 校验必填参数

        if not isinstance(exchange, str):
            raise ValueError("exchange should be str")

    def get_margin_ratio_validate_order_book_id_commodity(self, order_book_id, commodity):
        """ 校验order_book_id和commodity """

        ''' 对order_book_ids和commodity_type进行校验 '''
        self.general_validate_either_or("order_book_id", order_book_id, "commodity", commodity)

        ''' 根据order_book_ids和commodity_type进行筛选 '''
        # 因为前面已经对数据进行校验了，所以直接根据不同的参数进行筛选即可
        if order_book_id:
            self.get_margin_ratio_data = self._general_filter_data_by_field(self.get_margin_ratio_data, "order_book_id",
                                                                            order_book_id)
        if commodity:
            self.get_margin_ratio_data = self._general_filter_data_by_field(self.get_margin_ratio_data, "commodity",
                                                                            commodity)

    def get_margin_ratio_validate_date(self, date):
        """ 校验date """

        if isinstance(date, (str, datetime.date, datetime.datetime)):
            if isinstance(date, str) and not self.general_validate_date(date):
                raise ValueError("date 不是有效的日期字符串格式")
            return True
        else:
            raise ValueError("date 类型错误，请传入 str，datetime.date 或 datetime.datetime 类型")

    def get_margin_ratio_data_by_date(self, date):
        """
        根据date筛选数据
        """

        if isinstance(date, str):
            date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        self.get_margin_ratio_data = self.get_margin_ratio_data[self.get_margin_ratio_data["date"] == date]

    def get_margin_ratio_data_by_exchange(self, exchange):
        """
        根据exchange筛选数据
        """

        self.get_margin_ratio_data = self.get_margin_ratio_data[self.get_margin_ratio_data["exchange"] == exchange]

    """ get_fee 期货交割手续费 """

    def get_fee(self, order_book_id=None, commodity=None, date=datetime.datetime.now(), exchange=None):
        """
        获取期货交割手续费信息接口
        :param order_book_id: str--选填（和commodity二选一），合约代码
        :param commodity: str--选填（和order_book_id二选一），合约品种,如果入参为品种，则返回该品种条件下所有合约的交割手续费list
        :param date: datetime--必填（默认今天)，日期
        :param exchange: str--必填，交易所
        :return:
        """

        """ 校验数据 """
        # 校验order_book_id和commodity
        self.get_fee_validate_order_book_id_commodity(order_book_id, commodity)

        # 校验exchange
        self.get_fee_validate_exchange(exchange)

        # 校验date
        self.get_fee_validate_date(date)

        """ 处理数据 """
        # 根据date筛选数据
        self.get_fee_data_by_date(date)

        # 根据exchange筛选数据
        self.get_fee_data_by_exchange(exchange)

        return self.get_fee_data[["order_book_id", "commodity", "date", "exchange"]]

    def get_fee_validate_exchange(self, exchange):
        """ 校验exchange """
        # 是否必填
        self.general_validate_params_required(exchange, "exchange")

        if not isinstance(exchange, str):
            raise ValueError("exchange should be str")

    def get_fee_validate_order_book_id_commodity(self, order_book_id, commodity):
        """ 校验order_book_id和commodity """

        ''' 对order_book_ids和commodity_type进行校验 '''
        self.general_validate_either_or("order_book_id", order_book_id, "commodity", commodity)

        ''' 根据order_book_ids和commodity_type进行筛选 '''
        # 因为前面已经对数据进行校验了，所以直接根据不同的参数进行筛选即可
        if order_book_id:
            self.get_fee_data = self._general_filter_data_by_field(self.get_fee_data, "order_book_id",
                                                                   order_book_id)
        if commodity:
            self.get_fee_data = self._general_filter_data_by_field(self.get_fee_data, "commodity",
                                                                   commodity)

    def get_fee_validate_date(self, date):
        """ 校验date """

        if isinstance(date, (str, datetime.date, datetime.datetime)):
            if isinstance(date, str) and not self.general_validate_date(date):
                raise ValueError("date 不是有效的日期字符串格式")
            return True
        else:
            raise ValueError("date 类型错误，请传入 str，datetime.date 或 datetime.datetime 类型")

    def get_fee_data_by_date(self, date):
        """
        根据date筛选数据
        """

        if isinstance(date, str):
            date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        self.get_fee_data = self.get_fee_data[self.get_fee_data["date"] == date]

    def get_fee_data_by_exchange(self, exchange):
        """
        根据exchange筛选数据
        """

        self.get_fee_data = self.get_fee_data[self.get_fee_data["exchange"] == exchange]

    """ get_limit_position 期货限仓数据 """

    def get_limit_position(self, order_book_ids=None, commodity=None, date=datetime.date.today()):
        """
        获取期货限仓数据接口
        :param order_book_ids: str or list--选填（和commodity二选一），合约代码
        :param commodity: str or list--选填（和order_book_ids二选一），合约品种
        :param date: datetime.date--选填（默认今天)，日期
        :return:

        """
        """ 校验数据 """
        # 校验order_book_ids和commodity
        self.get_limit_position_validate_order_book_ids_commodity(order_book_ids, commodity)

        # 校验date
        self.get_limit_position_validate_date(date)

        """ 处理数据 """
        # 根据date筛选数据
        self.get_limit_position_data_by_date(date)

        return self.get_limit_position_data

    def get_limit_position_validate_order_book_ids_commodity(self, order_book_ids, commodity):
        """ 对order_book_ids和commodity_type进行校验 """
        self.general_validate_either_or("order_book_ids", order_book_ids, "commodity", commodity)

        ''' 根据order_book_ids和commodity_type进行筛选 '''
        # 因为前面已经对数据进行校验了，所以直接根据不同的参数进行筛选即可
        if order_book_ids:
            self.get_limit_position_data = self._general_filter_data_by_field(self.get_limit_position_data,
                                                                              "order_book_ids",
                                                                              order_book_ids)
        if commodity:
            self.get_limit_position_data = self._general_filter_data_by_field(self.get_limit_position_data,
                                                                              "commodity",
                                                                              commodity)

    def get_limit_position_validate_date(self, date):
        """ 校验date """

        if isinstance(date, (str, datetime.date, datetime.datetime)):
            if isinstance(date, str) and not self.general_validate_date(date):
                raise ValueError("date 不是有效的日期字符串格式")
            return True
        else:
            raise ValueError("date 类型错误，请传入 str，datetime.date 或 datetime.datetime 类型")

    def get_limit_position_data_by_date(self, date):
        """
        根据date筛选数据
        """

        if isinstance(date, str):
            date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        self.get_limit_position_data = self.get_limit_position_data[self.get_limit_position_data["date"] == date]

    """ get_active_contract 主力/次主力合约 """

    def get_active_contract(self, code=None, begin_date=None, start_date=datetime.date.today(),
                            end_date=datetime.date.today(), asset_type=None,
                            fields=None, source="3"):
        """
        获取主力/次主力合约信息接口
        :param code: str or str list--必填，品种
        :param begin_date: datetime--必填，指定日期
        :param start_date: date--必填，默认当天
        :param end_date: date--必填，默认当天
        :param asset_type: str--必填，active指主力；next_active次主力
        :param fields: str or str list--选填，返回字段，默认全部
        :param source: str--选填，数据源，默认研究所, 3个来源可选：1-数据中台, 2-米筐, 3-研究所

        :return:
        """

        """ 校验参数 """
        # 校验必填参数
        self.get_active_contract_validate_required_params(code, begin_date, start_date, end_date, asset_type)

        # 校验日期参数类型
        self.get_active_contract_validate_date_type(begin_date, start_date, end_date)

        """ 筛选数据 """

        # 根据code筛选数据
        self.get_active_contract_validate_code(code)

        # 根据日期数据筛选数据
        self.get_active_contract_filter_by_date(begin_date, start_date, end_date)

        # 根据asset_type筛选数据
        self.get_active_contract_filter_by_asset_type(asset_type)

        # 根据fields筛选数据
        self.get_active_contract_filter_data_by_fields(fields)

        # 根据source筛选数据
        self.get_active_contract_data_by_source(source)

        return self.get_active_contract_data

    def get_active_contract_validate_required_params(self, code, begin_date, start_date, end_date, asset_type):
        """ 校验参数是否必填 """

        params_dict = {
            "code": code,
            "begin_date": begin_date,
            "start_date": start_date,
            "end_date": end_date,
            "asset_type": asset_type
        }
        for key, value in params_dict.items():
            self.general_validate_params_required(value, key)  # 校验必填参数

    def get_active_contract_validate_code(self, code):
        """ 校验code 类型 """
        self.general_validate_field_str_or_list(code, "code")
        self.get_active_contract_data = self.get_active_contract_data[
            self.get_active_contract_data["code"].isin(code)] if isinstance(code, list) else \
            self.get_active_contract_data[self.get_active_contract_data["code"] == code]

    def get_active_contract_validate_date_type(self, begin_date, start_date, end_date):
        """
        校验日期数据的类型
        """
        # 校验start_date 和 end_date 是否为datetime.date类型或者可以转换成该类型的str
        if isinstance(start_date, (str, datetime.date)) and isinstance(end_date, (str, datetime.date)):
            if isinstance(start_date, str) and not self.general_validate_date_str_is_date_type(start_date):
                raise ValueError("start_date 类型错误，请传入 datetime.date 类型")
            if isinstance(end_date, str) and not self.general_validate_date_str_is_date_type(end_date):
                raise ValueError("end_date 类型错误，请传入 datetime.date 类型")
        else:
            raise ValueError("start_date 或 end_date 类型错误，请传入datetime.date 类型")

        # 校验begin_date 是否为datetime.datetime类型或者为可以转换为该类型的字符串
        if isinstance(begin_date, (str, datetime.datetime)):
            if isinstance(begin_date, str) and not self.general_validate_date_str_is_datetime_type(begin_date):
                raise ValueError("begin_date 类型错误，请传入 datetime.datetime 类型")
        else:
            raise ValueError("begin_date 类型错误，请传入 datetime.datetime 类型")

    def get_active_contract_filter_by_date(self, begin_date, start_date, end_date):
        """
        根据日期筛选数据
        """
        print(begin_date)
        if start_date > end_date:
            raise ValueError("start_date should be earlier than end_date")

        # 根据start_date 和 end_date 筛选数据
        start_date = self.general_date_str_to_date(start_date)
        end_date = self.general_date_str_to_date(end_date)
        self.get_active_contract_data = self.get_active_contract_data[
            (self.get_active_contract_data["date"] >= start_date) & (self.get_active_contract_data["date"] <= end_date)]

        return self.get_active_contract_data

    def get_active_contract_filter_by_asset_type(self, asset_type):
        """
        根据asset_type筛选数据
        """

        self.get_active_contract_data = self.general_filter_data_by_field(self.get_active_contract_data,
                                                                          "active_type",
                                                                          asset_type)

    def get_active_contract_filter_data_by_fields(self, fields):
        """
        根据fields筛选数据
        """

        if isinstance(fields, (str, list)):
            self.get_active_contract_data = self.get_active_contract_data[fields] if isinstance(fields, str) else \
                self.get_active_contract_data[[field for field in fields]]

    @staticmethod
    def get_active_contract_data_by_source(source):
        """
        根据数据源筛选数据
        """

        if not isinstance(source, str):
            raise ValueError("source 类型错误，请传入 str 类型")

        if source == "1":
            print("数据中台")
        elif source == "2":
            print("米筐")
        elif source == "3":
            print("研究所")
        else:
            raise ValueError("source 参数错误，取值范围应该在 [1, 2, 3]")

    """ get_basic_data 库存/基差/现货价格-数据（日频） """

    def get_basic_data(self, order_book_id, asset_type, start_date, end_date):
        """
        获取库存/基差/现货价格-数据（日频）接口
        :param order_book_id: str--必填，合约代码
        :param asset_type: str--必填，枚举值：库存、基差、现货
        :param start_date: str, datetime.date, datetime.datetime, pandasTimestamp--必填，开始日期
        :param end_date: str, datetime.date, datetime.datetime, pandasTimestamp--必填，结束日期
        """

        """ 校验参数 """

        # 校验必填参数
        self.get_basic_data_validate_required_params(order_book_id, asset_type, start_date, end_date)

        # 校验order_book_id 类型
        self.get_basic_data_validate_order_book_id(order_book_id)

        # 校验asset_type 类型
        self.get_basic_data_validate_asset_type(asset_type)

        # 校验start_date 和 end_date 类型
        self.get_basic_data_validate_date(start_date, end_date)

        return None

    def get_basic_data_validate_required_params(self, order_book_id, asset_type, start_date, end_date):
        params_dict = {
            "order_book_id": order_book_id,
            "asset_type": asset_type,
            "start_date": start_date,
            "end_date": end_date
        }
        for key, value in params_dict.items():
            self.general_validate_params_required(value, key)  # 校验必填参数

    def get_basic_data_validate_order_book_id(self, order_book_id):
        """
        校验order_book_id 类型
        """

        self.general_validate_param_is_str("order_book_id", order_book_id)

    def get_basic_data_validate_asset_type(self, asset_type):
        """
        校验asset_type 类型
        """

        self.general_validate_param_is_str("asset_type", asset_type)

    def get_basic_data_validate_date(self, start_date, end_date):
        """
        校验start_date 和 end_date 类型
        """
        error_msg = "start_date 或 end_date 类型错误，datetime.date, datetime.datetime, pandasTimestamp类型或者可以转换成该类型的str"

        # 校验start_date 和 end_date 是否为datetime.date, datetime.datetime, pandasTimestamp类型或者可以转换成该类型的str
        if isinstance(start_date, (str, datetime.date, datetime.datetime, pd.Timestamp)) and isinstance(end_date, (
                str, datetime.date, datetime.datetime, pd.Timestamp)):
            if isinstance(start_date, str) and not self.general_validate_date(start_date):
                raise ValueError(error_msg)
            if isinstance(end_date, str) and not self.general_validate_date(end_date):
                raise ValueError(error_msg)
        else:
            raise ValueError(error_msg)
