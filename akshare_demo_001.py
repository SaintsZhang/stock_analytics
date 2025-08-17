import datetime

import pandas as pd
import akshare as ak

def format_pandas():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 300)
    pd.set_option('display.max_rows', None)

def big_deal():
    # 大资金流入
    df_big = ak.stock_fund_flow_big_deal()
    # print(df_big.columns)
    df = df_big[(df_big['大单性质'] == '买盘') & (df_big['涨跌幅'] > '5%')]
    # print(df.head(100))
    # df_big.to_csv("/Users/saints/stock_data/大资金流入.csv")
    #%H: 小时（24小时制）%M: 分钟 %S: 秒 %f: 微秒 %p: AM/PM标识 %Y表示四位数的年份，%m表示两位数的月份，%d表示两位数的日期
    today = datetime.datetime.now().strftime("%Y-%m-%d") # %H:%M:%S"
    df.to_excel("/Users/saints/stock_data/大单买入" + today+".xlsx")

def yjyg_forcase(forecast_date):
    # 业绩预告
    data = ak.stock_yjyg_em(date = forecast_date)
    data.to_excel("/Users/saints/stock_data/业绩预告" + forecast_date + ".xlsx")

if __name__ == "__main__":
    #data = stock_lhb_ggtj_sina("5")
    #data = ak.stock_hsgt_hist_em("BJ837403")
    #print(data)
    format_pandas()

    #df = ak.stock_zh_a_hist(symbol="837403", period="daily", start_date="20250210")
    #print(df)

    #df_north = ak.stock_north_funds_flow_in_out(start_date="20230101", end_date="20231231")
    yjyg_forcase("20250630")
    big_deal()

