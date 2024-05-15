import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

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

class AreaConverterApp(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="面積單位換算程式")
        self.set_border_width(20)

        # 建立輸入框和單位選擇下拉選單
        self.entry_area = Gtk.Entry()
        self.combo_from = Gtk.ComboBoxText()
        self.combo_to = Gtk.ComboBoxText()

        for unit in area_units:
            self.combo_from.append_text(unit)
            self.combo_to.append_text(unit)

        self.combo_from.set_active(2)
        self.combo_to.set_active(6)

        # 建立按鈕和結果標籤
        self.btn_calculate = Gtk.Button(label="換算")
        self.btn_calculate.connect("clicked", self.calculate_area)
        self.label_result = Gtk.Label(label="")
        self.label_result.set_selectable(True)

        # 將元件排列在格狀佈局中
        grid = Gtk.Grid(column_spacing=10, row_spacing=10)
        grid.attach(Gtk.Label(label="輸入面積值:"), 0, 0, 1, 1)
        grid.attach(self.entry_area, 1, 0, 1, 1)
        grid.attach(Gtk.Label(label="原始單位:"), 0, 1, 1, 1)
        grid.attach(self.combo_from, 1, 1, 1, 1)
        grid.attach(Gtk.Label(label="轉換為:"), 0, 2, 1, 1)
        grid.attach(self.combo_to, 1, 2, 1, 1)
        grid.attach(self.btn_calculate, 0, 3, 2, 1)
        grid.attach(self.label_result, 0, 4, 2, 1)

        self.add(grid)

    def calculate_area(self, button):
        try:
            input_area = float(self.entry_area.get_text())
            from_unit = self.combo_from.get_active_text()
            to_unit = self.combo_to.get_active_text()

            result_area = input_area * (area_units[from_unit] / area_units[to_unit])
            result_str = f"結果: {result_area:.4f} {to_unit}"
            self.label_result.set_text(result_str)

        except ValueError:
            self.label_result.set_text("錯誤: 請輸入有效的數值")


win = AreaConverterApp()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

