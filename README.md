# CRS: Customer Retention and Segmentation for Banks

## Inspiration

Customer churning in bank happens when customers discontinue services with the bank. While there can be many reasons for this to happen, one of the primary reason is generalized banking and investment policies. This results on banks incurring heavy revenue losses. The need of the hour is for the banks to devise customer-curated policies. With different data analytics and predictive modelling, we developed a tool to predict potential bank churners and provide different insights to help banks come up with customized policies to retain their customers.

## What it does

The CRS tools has two parts
1. Churn Prediction - This uses Random Forests, a supervised machine learning algorithm, to predict the probability of a customer churning the bank.
2. Customer Segmentation - This uses K-means, an unsupervised machine learning algorithm, to cluster customers to different groups.

## How we built it

1. Churn prediction is built with the Random Forest algorithm using scikit-learn API. The model is trained on a financial dataset and predicts the probability of a person churning the bank. The model was first deployed locally on flask and then on heroku.

2. Customer Segmentation is built with Kmeans algorithm using the scikit-learn API. The model is trained on a financial dataset and groups customers into different clusters. First, the algorithm learns the number of optimal clusters from the data and then clusters the data accordingly using distance metrics. The model along with the cluster map is deployed on voila dashboard. By changing the input parameters, the cluster group of a customer can be predicted. Finally, this is deployed on heroku.

## Challenges we ran into

For churn prediction, the major challenge for us was to deal with a highly skewed dataset. Secondly, for the customer segmentation part, the major challenge was to determine the optimal number of clusters. Apart from these challenges, one of the most important was to figure out deployment on heroku.

## Accomplishments that we're proud of

We have successfully deployed our churn model on a highly skewed dataset. We used SMOTE sampling technique to handle the class imbalance and developed a model with a relatively good performance. 

## What we learned

Technically, we learned a lot about front end development. Deploying flask and voila on Heroku was new for us and we thoroughly enjoyed learning it. Also, working with the group helped us to identify our strengths and weaknesses, and with focus and collaboration we were able to solve all the challenges faced. We also learned about the problems faced in the banking world and how to tackle some of them.


## What's next for Customer Retention and Segmentation for Banks
The CRS tool can further be modified to include credit risk and loan risk analysis to provide a complete tool to increase revenue. Also, it can further be extended to predict if a customer should be provided with line of credit or loan, based on their credit history.
