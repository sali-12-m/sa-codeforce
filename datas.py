from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay

model = XGBClassifier(
    n_estimators=1000,         # ✅ high — early stopping will find best
    min_child_weight=5,
    gamma=0.5,
    subsample=0.6,
    colsample_bytree=0.6,
    max_depth=5,
    learning_rate=0.05,
    eval_metric='logloss',
    random_state=42,
    early_stopping_rounds=50,  # ✅ stops when no improvement
    verbosity=0
)
model.fit(X_Train, y_Train,
          eval_set=[(X_val, y_val)],
          verbose=False)

y_pred = model.predict(X_val)
print(f"Best n_estimators: {model.best_iteration}")
print(f"Val Accuracy: {accuracy_score(y_val, y_pred):.4f}")
print(classification_report(y_val, y_pred))

cm = confusion_matrix(y_val, y_pred)
ConfusionMatrixDisplay(confusion_matrix=cm).plot(cmap='Blues')
plt.show()