import pandas as pd

# Read the following link and complete this homework. https://www.codemag.com/Article/1711091/Implementing-Machine-Learning-Using-Python-and-Scikit-learn

# Make sure to install scikit-learn and Pandas

def step1():
    """
    # Step 1: Getting the Titanic Dataset
    Return a dataframe containing the Titantic dataset from the following URL
    # URL: https://gist.githubusercontent.com/mkzia/aa4f293661dba857b8c4459c0095ac95/raw/8075037f6f7689a1786405c1bc8ea9471d3aa9c3/train.csv

    """
    # BEGIN SOLUTION
    
    url = "https://gist.githubusercontent.com/mkzia/aa4f293661dba857b8c4459c0095ac95/raw/8075037f6f7689a1786405c1bc8ea9471d3aa9c3/train.csv"
    df = pd.read_csv(url)

    return df

    # END SOLUTION
    # return df


def step2(df):
    """
    # Step 2: Clean data
    Modify df to drop the following columns:
    PassengerId
    Name
    Ticket
    Cabin
    Hint: Just pass all the columns to the .drop() method as an array
    return dataframe
    """
    # BEGIN SOLUTION
    
    
    df = df.drop(columns = ['PassengerId', 'Name', 'Ticket', 'Cabin'])
    return df
    # END SOLUTION
    # return df


def step3(df):
    """
    # Step 3: Drop NaNs and reindex
    You want to reindex so your index does not have missing values after you drop the NaNs. Remember, index is used 
    to access a row. Notice how many rows you dropped!
    Modify df to drop NaNs and reindex
    return dataframe
    """
    # BEGIN SOLUTION
    
    df = df.dropna().reset_index(drop=True)

    return df

    # END SOLUTION
    # return df


def step4(df):
    """
    # Step 4: Encoding the Non-Numeric Fields
    Encode text fields to numbers
    Modify df to encode Sex and Embarked to encoded values.
    return dataframe
    """
    # BEGIN SOLUTION


    return df.replace({'Sex':{'male': 1, 'female': 0}, 'Embarked':{'S': 2, 'C': 0, 'Q': 1}})
    
    # END SOLUTION
    # return df


def step5(df):
    """
    # Step 5: Making Fields Categorical
    Turn values that are not continues values into categorical values
    Modify df to make Pclass, Sex, Embarked, and Survived a categorical field
    return dataframe
    """
    # BEGIN SOLUTION
    
    feature_cols = ['Pclass', 'Sex', 'Embarked', 'Survived']
    df[feature_cols] = df[feature_cols].apply(lambda x: x.astype('category'))

    return df
    # END SOLUTION
    # return df


def step6(df):
    """
    1. Split dataframe into feature and label
    2. Do train and test split; USE: random_state = 1
    4. Use LogisticRegression() for classification
    3. Return accuracy and confusion matrix

    Use  metrics.confusion_matrix to calculate the confusion matrix
    # https://towardsdatascience.com/understanding-confusion-matrix-a9ad42dcfd62
    # https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html
    # IMPORTANT !!!! 
    # https://stackoverflow.com/questions/56078203/why-scikit-learn-confusion-matrix-is-reversed

    From the confusion matrix get TN, FP, FN, TP

    return --> accuracy, TN, FP, FN, TP; 
    Hint: round accuracy to 4 decimal places

    """
    # BEGIN SOLUTION
    from sklearn.model_selection import train_test_split
    from sklearn import metrics
    from sklearn import linear_model

   

    features= df.drop("Survived", axis = 1)
    response = df["Survived"]

    

    train_data, test_data, train_label, test_label = train_test_split(features, response, test_size = 0.25, random_state = 1, stratify = df["Survived"])

     
    
    logistic_model = linear_model.LogisticRegression().fit(X = train_data, y = train_label)
    logistic_prediction = logistic_model.predict(test_data)



   

    model_acc = round(logistic_model.score(X = test_data, y = test_label),4)
    

    confusion_matrix = metrics.confusion_matrix(y_true = test_label, y_pred = logistic_prediction)

    TN = confusion_matrix[0][0]
    FN = confusion_matrix[1][0] 
    TP = confusion_matrix[1][1] 
    FP = confusion_matrix[0][1]


    return model_acc, TN, FP, FN, TP

    # END SOLUTION
    # return accuracy, TN, FP, FN, TP
