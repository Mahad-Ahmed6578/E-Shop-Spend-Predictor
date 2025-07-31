def evaluate_prediction(actual, predicted):
    error = abs(actual - predicted)
    percentage_error = (error / actual) * 100
    result = {
        'Actual Value': actual,
        'Predicted Value': predicted,
        'Absolute Error': round(error, 2),
        'Percentage Error': round(percentage_error, 2)
    }
    return result
