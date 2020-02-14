from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import GridSearchCV


def category_combine(df, columns=None, final_column=None):
    """Combine multiple one-hot encoded columns into one single column. 
    Columns in the columns list that do not match the final column 
    will be dropped from the df.
    
    df: Dataframe containing the data.
    columns: List of columns to be combined.
    final_column: Column that the rest of the columns will be combined into.
    """
    df[final_column] = df.apply(lambda x: 1 if any(x[col] == 1
                                for col in columns) else 0, axis=1)
    if final_column in columns:
        columns.remove(final_column)
    df.drop(columns=columns, inplace=True)
    

def create_model(estimator, X_train, y_train,
                 X_test, y_test, score=['MSE', 'R2']):
    """Create a model from a given estimator.
    
    INPUTS:
    estimator: Instantiated estimator for the model.
    X_train, X_test, y_train, y_test: Train/Test data to be used.
    score: List or single item for score output. (Default 'MSE' and 'R2').
    
    OUTPUTS:
    Selected score(s) printed on screen.
    """
    estimator.fit(X_train, y_train)
    train_pred = estimator.predict(X_train)
    test_pred = estimator.predict(X_test)
    print(estimator)
    for score in score:
        if score == 'MSE':
            print('Training MSE:', mean_squared_error(y_train, train_pred))
            print('Testing MSE:', mean_squared_error(y_test, test_pred))
        elif score == 'R2':
            print('Training R2:', r2_score(y_train, train_pred))
            print('Testing R2:', r2_score(y_test, test_pred))
        else:
            print('No valid score selected.') 


def gridsearch_model(estimator, X_train, y_train, X_test, y_test, param_grid,
                     scoring='r2', cv=3, title=None, verbose=0):
    """This function will fit a model using the provided classifier, dataset,
    and parameter grid. It uses GridSearchCV to determine the best model.

    INPUTS:
    estimator: Estimator to be fit.
    X_train, X_test, y_train, y_test: Train/Test data to be used.
    param_grid: Parameter grid to be used for the gridsearch.
    scoring: Scoring method to be used for the gridsearch.
    cv: Number of cross-validations.
    title: Title to print for clarity when reviewing outputs.

    OUTPUTS:
    Returns the best estimator model from GridSearch.
    Prints title and score to screen.
    """
    gridsearch = GridSearchCV(estimator=estimator, param_grid=param_grid,
                              cv=cv, scoring=scoring, verbose=verbose)
    gridsearch.fit(X_train, y_train)
    if title:
        print(title)
    print("BEST PARAMS:")
    print(gridsearch.best_params_)
    print("\nBest", scoring.capitalize(), "Score:",
          round(gridsearch.best_score_, 4))

    return gridsearch.best_estimator_