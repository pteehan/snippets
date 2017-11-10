
    cv = cv_data()
    x = cv.next() # this returns the first entry
    data.iloc[x[0]] # train data
    data.iloc[x[1]] # test data
    labels.iloc[x[0]] # train labels
    labels.iloc[x[1]] # test labels


