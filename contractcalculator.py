import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Frame
#选币
def vsheet(cointype):
    # Determine the sheet value based on the selected coin type
    if cointype.get() == "BTC":
        return 0.001
    elif cointype.get() in ["ETH", "BCH", "BNB"]:
        return 0.01
    elif cointype.get() in ["LTC", "FIL", "LINK", "SOL", "AVAX"]:
        return 0.1
    elif cointype.get() in ["EOS", "DOT", "ADA", "MATIC", "MANA", "AXS", "UNI", "FTT"]:
        return 1
    elif cointype.get() in ["TRX", "DOGE"]:
        return 100
    elif cointype.get() == "SHIB":
        return 1000
    else:
        return "请输入币种"
#计算平仓价
def calculate_price(long_or_short, close_price, profit_loss_rate, open_price,leverage,profit_loss):
    if long_or_short == "开多":
        if len(close_price.get()) == 0:
            if len(profit_loss_rate.get()) != 0:
                return ((float(profit_loss_rate.get())/100 * float(open_price.get()) / float(leverage.get())) + float(open_price.get()))
            elif len(profit_loss.get()) != 0:
                return ()
            else:
                return ()
        else:
            return close_price.get()
    elif long_or_short == "开空":
        if len(close_price.get()) == 0:
            if len(profit_loss_rate.get()) != 0:
                return (float(open_price.get())- (float(profit_loss_rate.get())/100 * float(open_price.get()) / float(leverage.get())))
            elif len(profit_loss.get()) != 0:
                return ()
            else:
                return ()
        else:
            return close_price.get()
    else:
        return ()

#算张数
def calculate_lot_size(sheet,deposit, open_price, leverage, sheet_value):
    try:
        if len(sheet.get()) == 0:
            dep = float(deposit.get())
            ope = float(open_price.get())
            lev = float(leverage.get())
            she = float(sheet_value)
            return round(dep / ope * lev / she, 0)
        else:
            return sheet.get()
    except ValueError:
        return ()
    #算保证金
def depcal(depos,she,lotsize,open,lev):
    if len(depos.get()) == 0:
        if she != 0:
            return (she*float(lotsize)*float(open)/float(lev))
        else:
            print()
    else:
        return(depos.get())
#计算盈亏率
def PLpes(DIREC,OPENP,CLOSP,LEV,PLL):
    ope = float(OPENP.get())
    lev = float(LEV.get())
    PLLL = PLL.get()
    if len(CLOSP.get()) == 0:
        return (PLLL)
    else:
        clo = float(CLOSP.get())
        if DIREC == "开多":
            return (round((lev * (clo - ope) / ope*100),5))
        elif DIREC == "开空":
            return (round((lev * (ope - clo) / ope*100),5))
        else:
            return ()
#盈亏公式
def profit_lose(deposit,profitloserate):
    if profitloserate !=0:
        if deposit != 0:
            print(deposit,profitloserate,type(profitloserate),type(deposit))
            return (float(profitloserate) * float(deposit)/100)
        else:
            return()
    else:
        return()

#开仓手续费公式
def opencharges(cont,dep,levv):
    if dep != 0:
        if len(levv.get()) != 0:
            if cont.get() == "永续合约":
                levvv = float(levv.get())
                depp = float(dep)
                return round((depp*levvv*0.0004),5)
            elif cont.get() == "快捷合约":
                return ("")
            else:
                return ("选择永续或快捷")
        else:
            return("请输入杠杆")
    else:
        return ("")
#平仓手续费公式
def closcharge(cont,dep,openprice,closingpricei,levv):
    if dep != 0:
        if len(openprice) != 0:
            if closingpricei != 0:
                if len(levv) != 0:
                    if cont.get() == "永续合约":
                        depp = float(dep)
                        levvv = float(levv)
                        openp = float(openprice)
                        clospp = float(closingpricei)
                        return round((depp *levvv * clospp /openp * 0.0004 ),5)
                    elif cont.get() == "快捷合约":
                        depp = float(dep)
                        levvv = float(levv)
                        openp = float(openprice)
                        clospp = float(closingpricei)
                        return round((depp * levvv * clospp / openp * 0.00075), 5)
                    else:
                        return ()
                else:
                    return()
            else:
                return
        else:
            return
    else:
        return
#计算 风险率
def calculate_hratio(contrac, direct, balance, unrealispl, depoo, closchar):
    if contrac.get() == "永续合约":
        if direct.get() == "开多":
            if len(unrealispl.get()) != 0:
                if len(balance.get()) != 0:
                    if closchar != 0:
                        bala =float(balance.get())
                        unrealis = float(unrealispl.get())
                        depo = float(depoo)
                        print("保证金", type(bala),"浮动盈亏", type(unrealis),"保证金", type(depo),"平仓手续费", type(closchar))
                        return (bala + (unrealis/100 *depo) - closchar) / depo*100
                    else:
                        return("无余额")
                else:
                    bala = float(balance.get())
                    unrealis = float(unrealispl.get())
                    depo = float(depoo)
                    print("余额", type(bala), "浮动盈亏", type(unrealis), "保证金", type(depo), "平仓手续费",
                          type(closchar))
                    return (bala + (unrealis / 100 * depo) ) / depo * 100
            else:
                return("无浮动盈亏")
        elif direct.get() == "开空":
            if len(unrealispl.get()) != 0:
                if len(balance.get()) != 0:
                    if closchar != 0:
                        bala =float(balance.get())
                        unrealis = float(unrealispl.get())
                        depo = float(depoo)
                        print("余额",type(bala),"浮动盈亏", type(unrealis),"保证金", type(depo),"平仓手续费", type(closchar))
                        return (bala + (unrealis/100 * depo) - closchar) / depo*100
                    else:
                        return("无余额")
                else:
                    bala = float(balance.get())
                    unrealis = float(unrealispl.get())
                    depo = float(depoo)
                    print("余额", type(bala), "浮动盈亏", type(unrealis), "保证金", type(depo), "平仓手续费",
                          type(closchar))
                    return (bala + (unrealis / 100 * depo) ) / depo * 100
            else:
                return("无浮动盈亏")
        else:
            return "多空异常"
    else:
        return "无风险率"
#计算按钮
def calculate():
    result = []
    for i in range(10):
        output_display[i + 3]["text"] = ""
    # Perform calculation and store results in 'result' list
    #result 1 币种 str
    output_display[1]["text"] = (coin.get())
    #result 2 多空 str
    output_display[2]["text"] = (direction.get())
    #result 3 杠杆 str
    output_display[3]["text"] = (LEVER.get())
    # result 4 开仓价 str
    output_display[4]["text"] = (OPENPRICE.get())
    # result 5 平仓价 str
    output_display[5]["text"] = (calculate_price(direction.get(),CLOSINGPRICE,LOSEP,OPENPRICE,LEVER,LOSE))
    # result 6 张数 float
    LOTSIZE = calculate_lot_size(SHEET,DEPOSIT,OPENPRICE,LEVER,vsheet(coin))
    output_display[6]["text"] = (LOTSIZE)
    # result 7 面值 float
    output_display[7]["text"] = (vsheet(coin))
    # result 8 保证金 str
    output_display[8]["text"] = (depcal(DEPOSIT,vsheet(coin),LOTSIZE,OPENPRICE.get(),LEVER.get()))
    # result 9 盈亏率 计算=float 输入=str
    output_display[9]["text"] = (PLpes(direction.get(),OPENPRICE,CLOSINGPRICE,LEVER,LOSEP),"%")
    # result 10 盈亏 float
    output_display[10]["text"] = (profit_lose(depcal(DEPOSIT,vsheet(coin),LOTSIZE,OPENPRICE.get(),LEVER.get()),PLpes(direction.get(),OPENPRICE,CLOSINGPRICE,LEVER,LOSEP)))
    # result 11 开仓手续费
    output_display[11]["text"] = opencharges(contract,depcal(DEPOSIT,vsheet(coin),LOTSIZE,OPENPRICE.get(),LEVER.get()),LEVER)
    # result 12 平仓手续费
    output_display[12]["text"] = closcharge(contract,depcal(DEPOSIT,vsheet(coin),LOTSIZE,OPENPRICE.get(),LEVER.get()),OPENPRICE.get(),calculate_price(direction.get(),CLOSINGPRICE,LOSEP,OPENPRICE,LEVER,LOSE),LEVER.get())
    # result 13 风险率
    output_display[13]["text"] =  calculate_hratio(contract,direction,BALANCE,UNREALISPL,depcal(DEPOSIT,vsheet(coin),LOTSIZE,OPENPRICE.get(),LEVER.get()),closcharge(contract,depcal(DEPOSIT,vsheet(coin),LOTSIZE,OPENPRICE.get(),LEVER.get()),OPENPRICE.get(),calculate_price(direction.get(),CLOSINGPRICE,LOSEP,OPENPRICE,LEVER,LOSE),LEVER.get()))

    for i in range(len(result)):
        output_display[i + 3]["text"] = result[i]


root = tk.Tk()
root.title("合约计算器cai")
root["background"] = "lightcyan"
style = ttk.Style(root)
style.configure("TFrame", background="lightcyan")
style.configure("TButton", background="lightsteelblue")
style.configure("TLabel", background="lightcyan")

input_frame: Frame = ttk.Frame(root, style="TFrame")
input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="W")

output_frame = ttk.Frame(root, style="TFrame")
output_frame.grid(row=1, column=0, padx=10, pady=0, columnspan=3, sticky="W")

# Input 1
ttk.Label(input_frame, text="合约          :", width=10, anchor="e").grid(row=0, column=0)
contract = tk.StringVar()
contract_options = ["", "永续合约", "快捷合约"]
contract_dropdown = ttk.OptionMenu(input_frame, contract, *contract_options)
contract_dropdown.config(width=20)
contract_dropdown.grid(row=0, column=1)

# Input 2
ttk.Label(input_frame, text="多空          :", width=10, anchor="e").grid(row=1, column=0)
direction = tk.StringVar()
direction_options = ["", "开多", "开空"]
direction_dropdown = ttk.OptionMenu(input_frame, direction, *direction_options)
direction_dropdown.config(width=20)
direction_dropdown.grid(row=1, column=1)

# Input 3
ttk.Label(input_frame, text="币种          :", width=10, anchor="e").grid(row=2, column=0)
coin = tk.StringVar()
coin_options = ["", "BTC", "ETH", "LTC", "EOS", "BCH", "XRP", "MANA", "SHIB", "MATIC", "AVAX", "UNI",
                "CHZ", "DOGE", "TRX", "LINK", "FIL", "ADA", "AXS", "SOL", "BNB", "DOT"]
coin_dropdown = ttk.OptionMenu(input_frame, coin, *coin_options)
coin_dropdown.config(width=20)
coin_dropdown.grid(row=2, column=1)

# Input 4
LEVERLABEL = ttk.Label(input_frame, text="杠杆          :", width=10, anchor="e").grid(row=3, column=0)
LEVER = tk.Entry(input_frame, width=24)
LEVER.grid(row=3, column=1)


# Input 5
ttk.Label(input_frame, text="开仓价       :", width=10, anchor="e").grid(row=4, column=0)
OPENPRICE = tk.Entry(input_frame, width=24)
OPENPRICE.grid(row=4, column=1)


# Input 6
ttk.Label(input_frame, text="张数          :", width=10, anchor="e").grid(row=5, column=0)
SHEET = tk.Entry(input_frame, width=24)
SHEET.grid(row=5, column=1)

#Input 7
ttk.Label(input_frame, text="浮动盈亏    :", width=10, anchor="e").grid(row=6, column=0)
UNREALISPL = tk.Entry(input_frame, width=24)
UNREALISPL.grid(row=6, column=1)

# Input 8
ttk.Label(input_frame, text="保证金       :", width=10, anchor="e").grid(row=7, column=0)
DEPOSIT = tk.Entry(input_frame, width=24)
DEPOSIT.grid(row=7, column=1)

# Input 9
ttk.Label(input_frame, text="平仓价       :", width=10, anchor="e").grid(row=8, column=0)
CLOSINGPRICE = tk.Entry(input_frame, width=24)
CLOSINGPRICE.grid(row=8, column=1)
# Input 10
ttk.Label(input_frame, text="亏损率       :", width=10, anchor="e").grid(row=9, column=0)
LOSEP = tk.Entry(input_frame, width=24)
LOSEP.grid(row=9, column=1)
# Input 11
ttk.Label(input_frame, text="亏损          :", width=10, anchor="e").grid(row=10, column=0)
LOSE = tk.Entry(input_frame, width=24)
LOSE.grid(row=10, column=1)
# Input 12
ttk.Label(input_frame, text="余额          :", width=10, anchor="e").grid(row=11, column=0)
BALANCE = tk.Entry(input_frame, width=24)
BALANCE.grid(row=11, column=1)

output_display = [ttk.Label(output_frame, text="", width=20, anchor="e", background="lightcyan") for i in range(1, 16)]
for i in range(15):
    output_display[i].grid(row=i, column=1)
# Output1
ttk.Label(output_frame, text=f"币种          :", anchor="w", width=10).grid(row=1, column=0)
# Output2
ttk.Label(output_frame, text=f"多空          :", anchor="w", width=10).grid(row=2, column=0)
# Output3
ttk.Label(output_frame, text=f"杠杆          :", anchor="w", width=10).grid(row=3, column=0)
# Output4
ttk.Label(output_frame, text=f"开仓价       :", anchor="w", width=10).grid(row=4, column=0)
# Output5
ttk.Label(output_frame, text=f"平仓价       :", anchor="w", width=10).grid(row=5, column=0)
# Output6
ttk.Label(output_frame, text=f"张数          :", anchor="w", width=10).grid(row=6, column=0)
# Output7
ttk.Label(output_frame, text=f"面值          :", anchor="w", width=10).grid(row=7, column=0)
# Output8
ttk.Label(output_frame, text=f"保证金       :", anchor="w", width=10).grid(row=8, column=0)
# Output9
ttk.Label(output_frame, text=f"盈亏率       :", anchor="w", width=10).grid(row=9, column=0)
# Output10
ttk.Label(output_frame, text=f"盈亏          :", anchor="w", width=10).grid(row=10, column=0)
# Output11
ttk.Label(output_frame, text=f"开仓手续费 :", anchor="w", width=10).grid(row=11, column=0)
# Output12
ttk.Label(output_frame, text=f"平仓手续费 :", anchor="w", width=10).grid(row=12, column=0)
# Output13
ttk.Label(output_frame, text=f"风险率       :", anchor="w", width=10).grid(row=13, column=0)


ttk.Button(root, text="Calculate",command=calculate, style="TButton").grid(row=3, column=0, pady=10)

root.mainloop()
