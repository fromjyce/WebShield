import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.ensemble import VotingClassifier

legitimate_df = pd.read_csv("structured_data_legitimate.csv")
phishing_df = pd.read_csv("structured_data_phishing.csv")

df = pd.concat([legitimate_df, phishing_df], axis=0)

df = df.sample(frac=1)

df = df.drop('URL', axis=1)

df = df.drop_duplicates()

X = df.drop('label', axis=1)
Y = df['label']

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=10)

rf_model = RandomForestClassifier(n_estimators=60)
ab_model = AdaBoostClassifier()
nn_model = MLPClassifier(alpha=1)

K = 5
total = X.shape[0]
index = int(total / K)

# 1
X_1_test = X.iloc[:index]
X_1_train = X.iloc[index:]
Y_1_test = Y.iloc[:index]
Y_1_train = Y.iloc[index:]

# 2
X_2_test = X.iloc[index:index*2]
X_2_train = X.iloc[np.r_[:index, index*2:]]
Y_2_test = Y.iloc[index:index*2]
Y_2_train = Y.iloc[np.r_[:index, index*2:]]

# 3
X_3_test = X.iloc[index*2:index*3]
X_3_train = X.iloc[np.r_[:index*2, index*3:]]
Y_3_test = Y.iloc[index*2:index*3]
Y_3_train = Y.iloc[np.r_[:index*2, index*3:]]

# 4
X_4_test = X.iloc[index*3:index*4]
X_4_train = X.iloc[np.r_[:index*3, index*4:]]
Y_4_test = Y.iloc[index*3:index*4]
Y_4_train = Y.iloc[np.r_[:index*3, index*4:]]

# 5
X_5_test = X.iloc[index*4:]
X_5_train = X.iloc[:index*4]
Y_5_test = Y.iloc[index*4:]
Y_5_train = Y.iloc[:index*4]

X_train_list = [X_1_train, X_2_train, X_3_train, X_4_train, X_5_train]
X_test_list = [X_1_test, X_2_test, X_3_test, X_4_test, X_5_test]

Y_train_list = [Y_1_train, Y_2_train, Y_3_train, Y_4_train, Y_5_train]
Y_test_list = [Y_1_test, Y_2_test, Y_3_test, Y_4_test, Y_5_test]

def calculate_measures(TN, TP, FN, FP):
    model_accuracy = (TP + TN) / (TP + TN + FN + FP)
    model_precision = TP / (TP + FP)
    model_recall = TP / (TP + FN)
    return model_accuracy, model_precision, model_recall

rf_accuracy_list, rf_precision_list, rf_recall_list = [], [], []
ab_accuracy_list, ab_precision_list, ab_recall_list = [], [], []
nn_accuracy_list, nn_precision_list, nn_recall_list = [], [], []
voting_accuracy_list, voting_precision_list, voting_recall_list = [], [], []
voting_soft_accuracy_list, voting_soft_precision_list, voting_soft_recall_list = [], [], []

voting_clf = VotingClassifier(estimators=[
    ('rf', rf_model),
    ('ab', ab_model),
    ('nn', nn_model)
], voting='hard')

voting_clf_soft = VotingClassifier(estimators=[
    ('rf', rf_model),
    ('ab', ab_model),
    ('nn', nn_model)
], voting='soft')

for i in range(0, K):
    # ----- RANDOM FOREST ----- #
    rf_model.fit(X_train_list[i], Y_train_list[i])
    rf_predictions = rf_model.predict(X_test_list[i])
    tn_rf, fp_rf, fn_rf, tp_rf = confusion_matrix(y_true=Y_test_list[i], y_pred=rf_predictions).ravel()
    rf_accuracy, rf_precision, rf_recall = calculate_measures(tn_rf, tp_rf, fn_rf, fp_rf)
    rf_accuracy_list.append(rf_accuracy)
    rf_precision_list.append(rf_precision)
    rf_recall_list.append(rf_recall)

    # ----- ADABOOST ----- #
    ab_model.fit(X_train_list[i], Y_train_list[i])
    ab_predictions = ab_model.predict(X_test_list[i])
    tn_ab, fp_ab, fn_ab, tp_ab = confusion_matrix(y_true=Y_test_list[i], y_pred=ab_predictions).ravel()
    ab_accuracy, ab_precision, ab_recall = calculate_measures(tn_ab, tp_ab, fn_ab, fp_ab)
    ab_accuracy_list.append(ab_accuracy)
    ab_precision_list.append(ab_precision)
    ab_recall_list.append(ab_recall)

    # ----- NEURAL NETWORK ----- #
    nn_model.fit(X_train_list[i], Y_train_list[i])
    nn_predictions = nn_model.predict(X_test_list[i])
    tn_nn, fp_nn, fn_nn, tp_nn = confusion_matrix(y_true=Y_test_list[i], y_pred=nn_predictions).ravel()
    nn_accuracy, nn_precision, nn_recall = calculate_measures(tn_nn, tp_nn, fn_nn, fp_nn)
    nn_accuracy_list.append(nn_accuracy)
    nn_precision_list.append(nn_precision)
    nn_recall_list.append(nn_recall)

    # ----- VOTING CLASSIFIER ----- #
    voting_clf.fit(X_train_list[i], Y_train_list[i])
    voting_predictions = voting_clf.predict(X_test_list[i])
    tn_vclf, fp_vclf, fn_vclf, tp_vclf = confusion_matrix(y_true=Y_test_list[i], y_pred=voting_predictions).ravel()
    voting_accuracy, voting_precision, voting_recall = calculate_measures(tn_vclf, tp_vclf, fn_vclf, fp_vclf)
    voting_accuracy_list.append(voting_accuracy)
    voting_precision_list.append(voting_precision)
    voting_recall_list.append(voting_recall)

    # ----- VOTING CLASSIFIER SOFT ----- #
    voting_clf_soft.fit(X_train_list[i], Y_train_list[i])
    voting_predictions_soft = voting_clf_soft.predict(X_test_list[i])
    tn_vclfs, fp_vclfs, fn_vclfs, tp_vclfs = confusion_matrix(y_true=Y_test_list[i], y_pred=voting_predictions_soft).ravel()
    voting_accuracy_s, voting_precision_s, voting_recall_s = calculate_measures(tn_vclfs, tp_vclfs, fn_vclfs, fp_vclfs)
    voting_soft_accuracy_list.append(voting_accuracy)
    voting_soft_precision_list.append(voting_precision)
    voting_soft_recall_list.append(voting_recall)


RF_accuracy = sum(rf_accuracy_list) / len(rf_accuracy_list)
RF_precision = sum(rf_precision_list) / len(rf_precision_list)
RF_recall = sum(rf_recall_list) / len(rf_recall_list)

print("Random Forest accuracy ==> ", RF_accuracy)
print("Random Forest precision ==> ", RF_precision)
print("Random Forest recall ==> ", RF_recall)

AB_accuracy = sum(ab_accuracy_list) / len(ab_accuracy_list)
AB_precision = sum(ab_precision_list) / len(ab_precision_list)
AB_recall = sum(ab_recall_list) / len(ab_recall_list)

print("AdaBoost accuracy ==> ", AB_accuracy)
print("AdaBoost precision ==> ", AB_precision)
print("AdaBoost recall ==> ", AB_recall)

NN_accuracy = sum(nn_accuracy_list) / len(nn_accuracy_list)
NN_precision = sum(nn_precision_list) / len(nn_precision_list)
NN_recall = sum(nn_recall_list) / len(nn_recall_list)

print("Neural Network accuracy ==> ", NN_accuracy)
print("Neural Network precision ==> ", NN_precision)
print("Neural Network recall ==> ", NN_recall)

voting_accuracy = sum(voting_accuracy_list) / len(voting_accuracy_list)
voting_precision = sum(voting_precision_list) / len(voting_precision_list)
voting_recall = sum(voting_recall_list) / len(voting_recall_list)

print("Voting Classifier accuracy ==> ", voting_accuracy)
print("Voting Classifier precision ==> ", voting_precision)
print("Voting Classifier recall ==> ", voting_recall)

voting_soft_accuracy = sum(voting_soft_accuracy_list) / len(voting_soft_accuracy_list)
voting_soft_precision = sum(voting_soft_precision_list) / len(voting_soft_precision_list)
voting_soft_recall = sum(voting_soft_recall_list) / len(voting_soft_recall_list)

print("Voting Classifier (soft) accuracy ==> ", voting_soft_accuracy)
print("Voting Classifier (soft) precision ==> ", voting_soft_precision)
print("Voting Classifier (soft) recall ==> ", voting_soft_recall)