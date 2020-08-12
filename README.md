# Heart-Disease-Predictor #
  This Project was made to make accurate predictions about whether a person has a heart disease or not by using Neural Networks.
  I deployed the neural network model using Flask API.
 
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
   
   
   ![1](https://user-images.githubusercontent.com/51885421/83054548-34bffc80-a070-11ea-8952-b9a526707945.png)
   
   
   5. Enter the details <br />   
   
   ![2](https://user-images.githubusercontent.com/51885421/83054774-8e282b80-a070-11ea-82eb-6165409ea42b.png)
   
   
   6. The out put will be 0 or 1. <br />
      1 means the person is having heart ailment <br />
      0 means he is safe  <br />
      

   ![3](https://user-images.githubusercontent.com/51885421/83054908-c2035100-a070-11ea-94f2-d00d37dc7322.png)
   
   
   7. Do visit my Project on predicting chances of having Diabetes by visiting the following link:
   
   
   https://github.com/shreyrai99/Diabetes-Predictor
   
   
   
   # Thank You ! #
 
