from flask import Flask, render_template, request

app = Flask(__name__, template_folder="")

@app.route("/", methods=["GET","POST"]) 
def home():
   if (request.method == "GET"):
      return render_template("index.html")
   else:
      if (request.form["numero1"] != "" and request.form["numero2"] != ""):
         num1 = request.form ["numero1"]
         num2 = request.form ["numero2"]

         if (request.form['opc'] == "mult"):
            mult = int(num1) * int(num2)
            return { 
               "Resultado": str(mult)
               }

         elif (request.form['opc'] == "subt"):
            subt = int(num1) - int(num2)
            return {
               "Resultado": str(subt)
            }
         elif (request.form['opc'] == "soma"):
            soma = int(num1) + int(num2)
            return {
               "Resultado": str(soma)
            }
         else:
            divi = int(num1) // int(num2)
            return {
               "Resultado": str(divi)
            }
      else:
         return "Valor inválido!"   


app.run(port=8080, debug=True)     
