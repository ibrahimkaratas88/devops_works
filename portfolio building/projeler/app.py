from flask import Flask, render_template,request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        num = request.form ["number"]
        if num.isdigit() :
            num = int(num)
            return render_template("result_yeni_1.html", developer_name = "E2501-İbrahim", not_valid= True)
        else:
            if num >= 4000 or num < 1 :
                return render_template("result_yeni_1.html", developer_name = "E-2501-İbrahim", not_valid= True)
            else:
                val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
                syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
                number_roman = ''
                number_decimal = num
                i = 0
                while  num > 0:
                    for _ in range(num // val[i]):
                        number_roman += syb[i]
                        num -= val[i]
                        i += 1
                    return render_template("result_yeni_1.html", developer_name = "E2501-İbrahim", number_decimal = number_decimal, number_roman=number_roman)
    else:
        return render_template("result_yeni_1.html", developer_name = "E2501-İbrahim")


if __name__ == '__main__':
    app.run(debug = True)
   #app.run(host='0.0.0.0', port=80) 

