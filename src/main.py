import tkinter as tk
from tkinter import ttk

# 定義面積單位之間的換算比例
area_units = {
    '平方公尺 (m²)': 1,
    '公畝(are)': 100,
    '公頃(ha)': 10000,
    '平方公里(km²)': 1000000,
    '市畝': 10000/15,
    '甲': 9699,
    '坪': 10000/3025
}

def calculate_area():
    try:
        # 讀取輸入的值和單位
        input_area = float(entry_area.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()

        # 根據選擇的單位換算面積
        result_area = input_area * (area_units[from_unit] / area_units[to_unit])

        # 顯示換算後的結果
        result_str = f"結果: {result_area:.4f} {to_unit}"
        label_result.config(text=result_str)

    except ValueError:
        label_result.config(text="錯誤: 請輸入有效的數值")

# 複製結果到剪貼簿
def copy_result():
    result_str = label_result.cget("text")
    if result_str.startswith("結果:"):
        result_str = result_str.replace("結果: ", "")  # 移除前綴的 "結果: "
        root.clipboard_clear()  # 清除剪貼簿內容
        root.clipboard_append(result_str)  # 將結果添加到剪貼簿
        label_result.config(text="已複製到剪貼簿")

# 建立主視窗
root = tk.Tk()
root.title("面積單位換算程式")

# 添加輸入框和標籤
label_area = ttk.Label(root, text="輸入面積值:")
label_area.grid(row=0, column=0, padx=10, pady=10)
entry_area = ttk.Entry(root)
entry_area.grid(row=0, column=1, padx=10, pady=10)

# 添加單位選擇下拉選單
label_from = ttk.Label(root, text="原始單位:")
label_from.grid(row=1, column=0, padx=10, pady=10)
combo_from = ttk.Combobox(root, values=list(area_units.keys()))
combo_from.grid(row=1, column=1, padx=10, pady=10)
combo_from.current(0)  # 預設選擇第一個單位

label_to = ttk.Label(root, text="轉換為:")
label_to.grid(row=2, column=0, padx=10, pady=10)
combo_to = ttk.Combobox(root, values=list(area_units.keys()))
combo_to.grid(row=2, column=1, padx=10, pady=10)
combo_to.current(1)  # 預設選擇第二個單位

# 添加計算按鈕和結果標籤
btn_calculate = ttk.Button(root, text="換算", command=calculate_area)
btn_calculate.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

label_result = ttk.Label(root, text="")
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# 添加複製結果的按鈕
btn_copy = ttk.Button(root, text="複製結果", command=copy_result)
btn_copy.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# 啟動主視窗的事件迴圈
root.mainloop()

