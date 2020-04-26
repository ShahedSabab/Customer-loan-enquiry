# Cutomer-loan-Inquiry
The objective of this project is to predict if a customer will get a loan given applicant income, loan amount, loan amout term, credit history, education status, self employment status, property area etc. A model is trained using the training data on previous customers' loan approval history. A web service is created which runs the trained model in the background. The service presents an interface through which any user can request to get a automated decision / prediction (i.e., chances of approval or rejection). In addition, the web service also provides a REST API which can be used to get all the customer information who used this service. Later, the additional information can be leveraged to train a bigger model. 

• To handle the unbalanced class distribution of the data SMOTE is used to create instances for the minority class (i.e., loan rejection).
• The data is normalized and preprocessed.
• The model is trained using a Multi Layer Neural Network with 
