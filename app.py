from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    kpd = None
    error = None
    
    if request.method == 'POST':
        try:
            useful_work = float(request.form['useful_work'])
            total_energy = float(request.form['total_energy'])
            
            if total_energy <= 0:
                error = "Затраченная энергия должна быть больше нуля!"
            elif useful_work < 0:
                error = "Полезная работа не может быть отрицательной!"
            elif useful_work > total_energy:
                error = "Полезная работа не может быть больше затраченной энергии (КПД > 100%)."
            else:
                kpd = round((useful_work / total_energy) * 100, 2)
                
        except ValueError:
            error = "Пожалуйста, введите корректные числовые значения."

    return render_template('index.html', kpd=kpd, error=error)

if __name__ == '__main__':
    app.run(debug=True)
