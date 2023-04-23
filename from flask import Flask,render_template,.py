from flask import Flask,render_template,request
import pickle
app = Flask(__name__)
model = pickle.load(open('CKD.pkl','rb'))
@app.route('/')
def home():
  return render_template('home.html')
@app.route('/predection',methods=['POST','GET'])
def predection():
  return render_template('indexnew.html')
@app.route('/Home',methods=['POST','GET'])
def my_home():
  return render_template('home,html')
@app.route('/predict',methods=['POST'])
def predict():
 input_features=[float(x)for x in request.form.values()]
 features_value=[np.array(input_features)]
features_name=['blood_urea','blood gloucose random','anemia','coronary_artery_disease','pus_cell','red_blood_cells','diabetesmellitus','pedal_edema']
df = pd.DataFrame(features_value,columns=features_name)
output=model.predict(df)
return render_template('result.html',prediction_text=output)
if_name_=='_main_'
app.run(debug=True)