from flask import Flask,request,jsonify,render_template
import util
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get_loc_names',methods =['GET'])
def get_loc_names():
       response = jsonify({
              
              'locations':util.get_loc_names()
       })
       response.headers.add('Access-Control-Allow-Origin', '*')
       return response


@app.route('/predict_home_price',methods =['GET','POST'])
def predict_home_price(): 
    try:  
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        balcony = float(request.form['balcony_count'])
        area = request.form['area_type']
       
       
        response = jsonify({
        
        'estimated_price': util.get_estimated_price_new(location,total_sqft,bhk,bath,balcony,area)
    })
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500
 
        
if __name__ == '__main__':
      print("Starting Python Flask Server For Home Price Prediction...")
      util.load_saved_artifacts()
      app.run()