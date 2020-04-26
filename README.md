![](Django-app/customerLoanUI.PNG?raw=true)
# Cutomer-loan-Inquiry
The objective of this project is to predict if a customer will get a loan given applicant income, loan amount, loan amout term, credit history, education status, self employment status, property area etc. A model is trained using the training data on previous customers' loan approval history. A web service is created which runs the trained model in the background. The service presents an interface through which any user can request to get a automated decision / prediction (i.e., chances of approval or rejection). In addition, the web service also provides a REST API which can be used to get all the customer information who used this service. Later, the additional customer information can be leveraged to train a bigger model. 

• To handle the unbalanced class distribution of the data SMOTE is used to create instances for the minority class (i.e., loan rejection).<br>
• The data is normalized and preprocessed. <br>
• To build the model Tensorflow 2.0 is used. <br>
• The model is trained using a Multi Layer Neural Network with 4 dense layers (adding l1 regularization) and 2 droupout layers. <br>
• The model can generate 2 decisions (i.e., approval or rejection) based on the given customer data. <br>
• The model has an accuracy of 80%. <br>
• The web service is developed using Django framework & REST API. <br>

# How to run:
Go inside the Django-app directory and run the following commands:
> pip install requirements.txt
> python manage.py makemigrations
> python manage.py migrate
