from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Cơ sở dữ liệu ảo
danh_sach_san_pham = [
    {"id": "SP01", "name": "Bút bi Thiên Long", "stock": 50, "price": 5000},
    {"id": "SP02", "name": "Sổ tay B5", "stock": 10, "price": 25000},
    {"id": "SP03", "name": "Tập giấy A4", "stock": 100, "price": 70000},
    {"id": "SP04", "name": "Tẩy bút chì", "stock": 30, "price": 3000}
]

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == '123456':
            return redirect(url_for('dashboard'))
        else:
            error = 'Sai tài khoản hoặc mật khẩu!'
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', products=danh_sach_san_pham)

@app.route('/hanghoa')
def hanghoa():
    return render_template('hanghoa.html', products=danh_sach_san_pham)

@app.route('/tongquan')
def tongquan():
    return render_template('tongquan.html')

@app.route('/giaodich')
def giaodich():
    return render_template('giaodich.html')

@app.route('/aidubao')
def aidubao():
    return render_template('aidubao.html')

if __name__ == '__main__':
    app.run(debug=True)