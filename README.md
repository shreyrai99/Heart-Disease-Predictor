# Heart-Disease-Predictor
  This Project was made to make accurate predictions about whether a person has a heart disease or not by using Neural Networks.
  I deployed the neural network model using Flask API.
 
## Technologies Used:
  I used the following tools and technologies in order to successfully make the project:
    1. Python 
    2. HTML
    3. CSS 
    4. File Handling technique
    5. Flask (Framework)
    6. sklearn.neural_network library for neural networks
   
  ## Project Structure
    This project has four major parts :
     1. model.py : This contains code fot our Machine Learning model to predict the chances of a patient having heart ailments.
     2. app.py: This contains Flask APIs that receives patient's details through GUI or API calls, computes the precited value based on         our model and predicts whether the patient has heart disease or not.
     3. templates: This folder contains the HTML template to allow user to enter various fields inorder to know his chances of having           disease.
     4. static: It contains the CSS part of the project.
    
  ## Running the Model:
    1. Ensure that you are in the project home directory. Create the machine learning model by running below command -
       **python model.py**
       This would create a serialized version of our model into a file model.pkl
    2. Run app.py using below command to start Flask API
       **python app.py**
       By default, flask will run on port 5000.
    3. Navigate to URL http://localhost:5000
    4. We will see the below home page:
       <div align="center">
            <img src="/Working/1.png"</img> 
        </div>
    5. Enter the details
       <div align="center">
            <img src="/Working/2.png"</img> 
        </div>
    6. The out put will be 0 or 1.
       1 means the person is having heart ailment
       0 means he is safe 
      <div align="center">
            <img src="/Working/3.png"</img> 
        </div>
       
   ## THANK YOU!


    
    


  
 
