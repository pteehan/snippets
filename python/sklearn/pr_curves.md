
    predictions = model_selection.cross_val_predict(estimator, data, labels, cv=10, method="predict_proba")
    precision, recall, threshold = metrics.precision_recall_curve(labels, predictions)
    pr_curve = pd.DataFrame({'precision': precision[:-1],
                  'recall': recall[:-1],
                  'threshold': threshold})


