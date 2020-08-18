# Heart-Disease-Predictor #
  This Project was made to make accurate predictions about whether a person has a heart disease or not by using Neural Networks.
  I deployed the neural network model using Flask API.
  
  The Model is deployed on Heroku on the following link:  
   
   
   https://heart-diseasepredictor.herokuapp.com/
   
   
 
# Technologies Used: #
  I used the following tools and technologies in order to successfully make the project: <br />
    1. Python <br />
    2. HTML <br />
    3. CSS <br />
    4. File Handling technique <br />
    5. Flask (Framework) <br />
    6. sklearn.neural_network library for neural networks <br />
   
  # Project Structure #
   This project has four major parts :
   1. model.py : This contains code fot our Machine Learning model to predict the chances of a patient having heart ailments. 
   2. app.py: This contains Flask APIs that receives patient's details through GUI or API calls, computes the precited value based on      our model and predicts whether the patient has heart disease or not.
   3. templates: This folder contains the HTML template to allow user to enter various fields inorder to know his chances of having        disease. 
   4. static: It contains the CSS part of the project. 
    
  # Running the Model: #
   1. Ensure that you are in the project home directory. Create the machine learning model by running below command -
   python model.py 
   This would create a serialized version of our model into a file model.pkl 
   2. Run app.py using below command to start Flask API 
   python app.py <br />
   By default, flask will run on port 5000. 
   3. Navigate to URL http://localhost:5000   
   4. We will see the below home page: 
   
   
   ![Screenshot (141)](https://user-images.githubusercontent.com/51885421/90496324-4e4e7d00-e163-11ea-9813-01c9498d3d17.png)
   
   
   
   
   5. Case when the patient has heart disease
   
   
      Data Entered by the user:
      
      ![Screenshot (146)](https://user-images.githubusercontent.com/51885421/90496322-4db5e680-e163-11ea-915d-d19fe46291d0.png)
      
      
      Result Predicted by our Model:
      
      
      ![Screenshot (143)](https://user-images.githubusercontent.com/51885421/90496309-4a225f80-e163-11ea-9a10-cecef7d37019.png)
   
   
   
   6. Case when the patient does not have heart ailments:
   
   
      Data Entered by the user:
      
      
      ![Screenshot (144)](https://user-images.githubusercontent.com/51885421/90496317-4bec2300-e163-11ea-9770-7a0ae2d8e714.png)
      
      
      
      Result Predicted by our Model:
      
      
      
      ![Screenshot (142)](https://user-images.githubusercontent.com/51885421/90496302-47c00580-e163-11ea-8ed6-9b95d1b88ce1.png)
      

   
   
   
   7. Do visit my Project on predicting chances of having Diabetes by visiting the following link:
   
   
   https://github.com/shreyrai99/Diabetes-Predictor   
   
   
   
   
   # Thank You For Visiting! #
 
