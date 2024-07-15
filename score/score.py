# Function to parse the classification report
def parse_classification_report(report):
    lines = report.strip().split('\n')
    classes = []
    precision = []
    recall = []
    f1_score = []
    support = []
    
    for line in lines[2:]:
        row = line.strip().split()
        if len(row) >= 5 and row[0] != 'accuracy' and row[0] != 'macro' and row[0] != 'weighted':
            classes.append(row[0])
            precision.append(float(row[1]))
            recall.append(float(row[2]))
            f1_score.append(float(row[3]))
            support.append(int(row[4]))
    
    return classes, precision, recall, f1_score, support

# Example classification report string (replace this with your actual report)
classification_report_str = """
              precision    recall  f1-score   support

       apple       1.00      1.00      1.00        13
      banana       1.00      1.00      1.00        17
   blackgram       0.94      1.00      0.97        16
    chickpea       1.00      1.00      1.00        21
     coconut       1.00      1.00      1.00        21
      coffee       1.00      1.00      1.00        22
      cotton       1.00      1.00      1.00        20
      grapes       1.00      1.00      1.00        18
        jute       0.90      1.00      0.95        28
 kidneybeans       1.00      1.00      1.00        14
      lentil       1.00      1.00      1.00        23
       maize       1.00      1.00      1.00        21
       mango       1.00      1.00      1.00        26
   mothbeans       1.00      0.95      0.97        19
    mungbean       1.00      1.00      1.00        24
   muskmelon       1.00      1.00      1.00        23
      orange       1.00      1.00      1.00        29
      papaya       1.00      1.00      1.00        19
  pigeonpeas       1.00      1.00      1.00        18
 pomegranate       1.00      1.00      1.00        17
        rice       1.00      0.81      0.90        16
  watermelon       1.00      1.00      1.00        15
    accuracy                           0.99       440
   macro avg       0.99      0.99      0.99       440
weighted avg       0.99      0.99      0.99       440
"""

# Parsing the classification report
classes, precision, recall, f1_score, support = parse_classification_report(classification_report_str)

# Calculating weighted average F1 score
weighted_f1_score = sum([f1 * sup for f1, sup in zip(f1_score, support)]) / sum(support)

print(f"Weighted Average F1 Score: {weighted_f1_score}")
