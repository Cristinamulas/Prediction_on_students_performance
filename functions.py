import pandas as pd
import numpy as np
from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import  cross_val_score


def value__counts(df_):
    '''it takes a df and return value_counts for all the features'''
    for i in df_.columns:
        print(df_[i].value_counts())

def fig_categorical_columns(df ,list_):
    ''' it takes a feature and return a value_counts for all features'''
    for i in list_:
        plt.title('Column: ' + i)
        df[i].value_counts().plot(kind = 'barh')
        plt.show()
        
def fig_continues(df, list_):
    ''' it takes a feature and return a plot for each feature '''
    for i in list_:
        plt.title( 'Column: ' + i)
        df[i].plot(kind = 'hist')
        plt.show()

def plot_binary(df , column):
    ''' plot for the binary target '''
    plt.figure(figsize=(8,6))
    sns.countplot(df[column], order=["fail","pass"], palette='Set1')
    plt.title('Final Grade - Number of Students',fontsize=20)
    plt.xlabel('Final Grade', fontsize=16)
    plt.ylabel('Number of Student', fontsize=16)

# def plot_features_target(column , list_ , df):
#     '''it takes a feature and return plots for each categorical feature and the target feature'''
#     for col in list_ :
#         plt.figure(figsize=(12,10))
#         sns.countplot(x = col, hue = column, data = df)
#         plt.xticks(rotation='vertical')
def plot_features_target(column , list_ , df):
    '''it takes a feature and return plots for each categorical feature and the target feature'''
    l = list(list_)
    i = 0
    fig, ax = plt.subplots(9,2, figsize=(30,30))
    for m in range(9):
        for n in range(2):
            sns.countplot(x = l[i], hue = column, data = df ,ax=ax[m][n])
            i += 1
        
def encoding_features(df ,column_type = 'category',column_type1= 'object'):
    '''it takes the type of columns and used factorize to enconde them'''
    categorical_columns_target = (df.select_dtypes([column_type, column_type1]).columns)
    atts = categorical_columns_target
    dataRows = df.loc[:,atts]
    for i, u in enumerate(dataRows):
        df[atts[i]] = pd.factorize(df[atts[i]])[0]
    return df.head()

def normalizad_features(x):
    '''Nornalized features '''
    for col in x.columns:
        x[col] = (x[col]-min(x[col]))/ (max(x[col]) - min(x[col]))
    return x.head()

def metrix_classifier(x , y):
    """ calculated the accuracy and print out accuracy and classification report"""
    accuracy = round(metrics.accuracy_score(x, y) * 100 ,2)
    print(f"Accuracy: {accuracy} %")
#     f1_score = round(metrics.f1_score(x , y) * 100 , 2)
    print("F1 Score: {}".format(f1_score(x, y)))
    print(classification_report(x,  y)) # maybe remove this

def cross_val(classifier,X_train , y_train):
    """ it makes cross_validation_score for a classier, it return accuracy , f1, recall and precision score"""
    for i in ['accuracy', 'f1' , 'recall' , 'precision']:
        classifier_cv_score  = cross_val_score(classifier, X_train, y_train,  scoring= i, cv = 5)
        classifier_cv_score = round(classifier_cv_score.mean() * 100, 2)
        print(f"Mean {i} Score: {classifier_cv_score} %")
    
# def print_metrics(labels, preds):
#     print("Precision Score: {}".format(precision_score(labels, preds)))
#     print("Recall Score: {}".format(recall_score(labels, preds)))
#     print("Accuracy Score: {}".format(accuracy_score(labels, preds)))
#     print("F1 Score: {}".format(f1_score(labels, preds)))


def confusion_m(x,y,classifier):
    """ it plots a confusion matrix """
    cm = confusion_matrix(x, y)
    ax= plt.subplot()
    sns.heatmap(cm, annot=True, ax = ax)
    ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels') 
    ax.set_title('Confusion Matrix ' + classifier)
    ax.xaxis.set_ticklabels(['Fail', 'Pass']); ax.yaxis.set_ticklabels(['Fail', 'Pass'])
    

    