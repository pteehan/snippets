Splitting input data into cross-validated [train/test set](http://scikit-learn.org/stable/modules/cross_validation.html)
	
    from sklearn.model_selection import StratifiedShuffleSplit
    skf = StratifiedShuffleSplit(n_splits=10, random_state=0)
    cv_data=lambda: skf.split(data, labels)

Then you can do this:
    cross_val_score(lm, data, labels, cv=cv_data(), scoring='f1')

The lambda function is there because the iterator needs to be reset each time you call it.

