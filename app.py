import pandas as pd
import uvicorn
from fastapi import FastAPI, File, Request
app = FastAPI()

@app.get("/",tags=['測試服務狀態'])
def Hello():
    return{"status":200}

@app.post("/reset",tags=['重製抽獎'])
def TestModeuel(Number:int):
    choujiang = pd.Series(["Nothing", "Bingo"])
    cnt = choujiang.sample(n=Number, replace=True, weights=([Number-1, 1]))
    cnt.to_csv('save_today.csv')
    condition = 1
    # 使用 try 開啟
    try:
        f = open('./save_today.csv', 'r')
        content = f.read()
        f.close()
    # 檔案不存在的例外處理
    except FileNotFoundError:
        print("檔案不存在。")
        condition = 0
    if condition == 1:
        return "reset success"
    else:
        return "reset failed"

@app.post("/lottery",tags=['抽獎'])
def TestModeuel(Count:int):
    df = pd.read_csv('test.csv')
    print(df.iloc[Count][1])
    return df[Count][1]

if __name__ == '__main__':
    uvicorn.run(app="app:app", host="0.0.0.0", port=8000, reload=True, debug=True)