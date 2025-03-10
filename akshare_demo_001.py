import pandas as pd
import akshare as ak

def format_pandas():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 300)
    pd.set_option('display.max_rows', None)

if __name__ == "__main__":
    #data = stock_lhb_ggtj_sina("5")
    #data = ak.stock_hsgt_hist_em("BJ837403")
    #print(data)
    format_pandas()

    #df = ak.stock_zh_a_hist(symbol="837403", period="daily", start_date="20250210")
    #print(df)
    #大资金流入
    df_big = ak.stock_fund_flow_big_deal()
    #print(df_big.columns)
    df = df_big[ (df_big['大单性质']=='买盘') & (df_big['涨跌幅'] > '5%')]
    #print(df.head(100))
    #df_big.to_csv("/Users/saints/stock_data/大资金流入.csv")
    df.to_excel("/Users/saints/stock_data/大单买入20250310.xlsx")
    #df_north = ak.stock_north_funds_flow_in_out(start_date="20230101", end_date="20231231")
    #print("\n北向资金流入流出:")
    #print(df_big[df_big["大单性质"] =="买盘"])
    #业绩预告
    #data = ak.stock_yjyg_em(date="20250331")
    #data.to_excel("/Users/saints/stock_data/业绩预告20250331.xlsx")

    #print(data.head(20))
