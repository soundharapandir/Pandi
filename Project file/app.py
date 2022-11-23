
from flask import Flask,request,jsonify,render_template
import pickle 
#importing inputscript file used to analyse the url



#load model
app=Flask(__name__)


#redirects the page given user input
@app.route('/predict')
def predict():
    return render_template('final.html')

    #fetch the url by and pases to inputscript
@app.route('/y_predict',methods=['post'])
def y_predict():

    #for rendering results on html gui

    url=request.form['URL']
    checkprediction=inputscript.main(url)
    prediction=model.prediction(checkprediction)
    print(prediction)
    output=prediction[0]
    if(output==1):
        pred="you are safe!! this is a legitimate website."
    else:
        pred="you are in wrong site.be cautious!"
    return render_template('final.html',prediction_text='{}'.format(pred),url=url) 
#takes input parameters fetched from the url by inputscript and returns the predictions
@app.route('/predict_api',methods=['post'])
def predict_api():
    #for direct api callls throught request
    data=request.get_json(force=True)
    prediction=model.y_predict([np.array(list(data.values()))])

    output=prediction[0]
    return jsonify(output)
   
if __name__== '__main__':
    app.run(debug=True)