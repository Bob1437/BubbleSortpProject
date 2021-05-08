from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        var1 = request.form['var1']
        var2 = request.form['var2']
        var3 = request.form['var3']
        var4 = request.form['var4']
        var5 = request.form['var5']
        var6 = request.form['var6']
        var7 = request.form['var7']
        var8 = request.form['var8']
        var9 = request.form['var9']
        var10 = request.form['var10']

        n1 = var1
        n2 = var2
        n3 = var3
        n4 = var4
        n5 = var5
        n6 = var6
        n7 = var7
        n8 = var8
        n9 = var9
        n10 = var10




        lst = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]



        n = len(lst)

        for j in range(0,100):
            check = False
            for i in range(0, n-1):
                if int(lst[i]) > int(lst[i + 1]):
                    swap = lst[i]
                    lst[i] = lst[i+1]
                    lst[i+1] = swap
                    check = True
            if check == False:
                break
        return render_template('home.html', var1=var1, var2=var2, var3=var3, var4=var4, var5=var5, var6=var6, var7=var7, var8=var8, var9=var9, var10=var10, sorted=lst)







if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5001")