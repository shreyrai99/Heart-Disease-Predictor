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
      ![1](https://user-images.githubusercontent.com/51885421/83045954-ee64a080-a063-11ea-9399-04d8a5d8394e.png)
    5. Enter the details
       ![2](https://user-images.githubusercontent.com/51885421/83046003-fde3e980-a063-11ea-9cb4-1e8730a53794.png)
    6. The out put will be 0 or 1.
       1 means the person is having heart ailment
       0 means he is safe 
      ![3](https://user-images.githubusercontent.com/51885421/83046018-01777080-a064-11ea-9c05-182bbe4cff39.png)

       
   ## THANK YOU!


    
    


  
 
