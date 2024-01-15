from re import A
import ipywidgets as widgets
from IPython.display import display
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Tạo widget FloatText để nhập số
loaded_model = pickle.load(open('model.sav', 'rb'))

lb1 = widgets.HTML(value='Nhập số tiền muốn vay:')
lb2 = widgets.HTML(value='Nhập lãi suất:')
lb3 = widgets.HTML(value='Nhập tỉ lệ nợ trên thu nhập:')
lb4 = widgets.HTML(value='Nhập số tiền vay đã trả: ')
lb5 = widgets.HTML(value='Số lượng hồ sơ:   ')
lb6 = widgets.HTML(value='Chọn loại kì hạn:   ')
lb7 = widgets.HTML(value='Chọn bên vay:   ')

loan_amnt = widgets.FloatText()
int_rate = widgets.FloatText()
dti = widgets.FloatText()
total_pymnt = widgets.FloatText()
pub_rec = widgets.IntText()
term = widgets.Dropdown(options=['36 tháng', '60 tháng'], disable = False)
application_type = widgets.Dropdown(options=['Cá nhân', 'Tổ chức'], disable = False)
predict_button = widgets.Button(description='Xác nhận')

# Hàm xử lý sự kiện khi người dùng nhấn nút Xác nhận
def predict(b):
    a= loan_amnt.value
    b = int_rate.value
    c = dti.value
    d = pub_rec.value
    e = total_pymnt.value
    f = 0
    g = 0
    h = 0
    i = 0
    if term.value == '36 tháng': f = 1
    else: g = 1
    if application_type.value == 'Cá nhân': h = 1
    else: i = 1

    newCus= pd.DataFrame([
                {'loan_amnt':a,
                'int_rate':b,
                'dti':c,
                'pub_rec':d,
                'total_pymnt':e,
                'term_ 36 months':f,
                'term_ 60 months':g,
                'application_type_Individual':h,
                'application_type_Joint App':i,}], columns = ['loan_amnt','int_rate','dti','pub_rec','total_pymnt','term_ 36 months','term_ 60 months','application_type_Individual','application_type_Joint App'])
    result = loaded_model.predict(newCus)
    if result: print("Dự đoán: Khách hàng này sẽ trả được nợ")
    else: print("Dự đoán: Khách hàng này sẽ không trả được nợ")
    # print(f"Kết quả: {result}")

# Gắn hàm xử lý sự kiện vào nút Xác nhận
predict_button.on_click(predict)

# Hiển thị widget
display(widgets.HBox([lb1, loan_amnt]))
display(widgets.HBox([lb2, int_rate]))
display(widgets.HBox([lb3, dti]))
display(widgets.HBox([lb4, total_pymnt]))
display(widgets.HBox([lb5, pub_rec]))
display(widgets.HBox([lb6, term]))
display(widgets.HBox([lb7, application_type]))
display(widgets.HBox([predict_button]))
