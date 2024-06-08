import json
import pickle 
import numpy as np
locations = None
locations_new = None
data_col = None
data_col_new = None
model = None
model_new = None



# def get_estimated_price(loc,sqft,bhk,bath):
#       try:
#             loc_index = data_col.index(loc.lower())
#       except:
#             loc_index = -1
      
#       x = np.zeros(len(data_col))
#       x[0] = sqft
#       x[1] = bath
#       x[2] = bhk
#       if loc_index >= 0:
#             x[loc_index]  = 1
      
#       return round(model.predict([x])[0],2)


def get_estimated_price_new(loc,sqft,bhk,bath,bal,area):
      try:
            loc_index = data_col_new.index(loc.lower())
      except:
            loc_index = -1

      try: 
            area_index = data_col_new.index(area.lower())   
      except:
            area_index = -1        
      
      x = np.zeros(len(data_col_new))
     
      x[0] = sqft
      x[1] = bath
      x[2] = bal
      x[3] = bhk
      if loc_index >= 0:
            x[loc_index]  = 1
      if area_index >= 0:
            x[area_index] = 1
      
      
      return round(model_new.predict([x])[0],2)



def get_loc_names():
      return locations_new

def load_saved_artifacts():
      print("loading saved artifacts..")

      global locations
      global locations_new
      global data_col
      global data_col_new
      with open(r"D:\House_Prediction\server\artifacts\columns.json",'r') as f:
            data_col = json.load(f)['col']
            locations = data_col[3:]
      with open(r"D:\House_Prediction\server\artifacts\columns_new.json",'r') as f:
            data_col_new = json.load(f)['col']
            locations_new = data_col_new[3:245]

      global model
      with open(r"D:\House_Prediction\server\artifacts\home_price_model.pickle","rb") as f:
            model = pickle.load(f)
      global model_new
      with open(r"D:\House_Prediction\server\artifacts\home_price_model_new.pickle","rb") as f:
            model_new = pickle.load(f)


      print("Artifacts has been loaded")
            

if __name__ == "__main__":
      load_saved_artifacts()
      # print(get_loc_names())
      print(get_estimated_price_new('1st Phase JP Nagar',1000,2,2,1,'Carpet  Area'))
      # print(get_estimated_price('1st Phase JP Nagar',1000,2,2))
      # print(get_estimated_price('Srihalli',1000,2,2))
      # print(get_estimated_price('Gulmohar',1000,2,2))


