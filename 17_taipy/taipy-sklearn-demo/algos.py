import numpy as np

from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB

import plotly.express as px


def fit(X, y, model_name):

    if model_name == "MLPClassifier":
        model = MLPClassifier(
            solver="lbfgs",
            random_state=1,
            max_iter=2000,
            early_stopping=True,
            hidden_layer_sizes=[10, 10],
        )
    elif model_name == "RandomForestClassifier":
        model = RandomForestClassifier(
            ccp_alpha=0.05
        )
    elif model_name == "SVC":
        model = SVC(
            kernel='rbf',
            C=1.0,
            random_state=1
        )
    elif model_name == "KNeighborsClassifier":
        model = KNeighborsClassifier(
            n_neighbors=5,
            algorithm='auto'
        )
    elif model_name == "LogisticRegression":
        model = LogisticRegression(
            penalty='l2',
            C=1.0,
            random_state=1
        )
    elif model_name == "AdaBoostClassifier":
        model = AdaBoostClassifier(
            n_estimators=100,
            learning_rate=1.0,
            random_state=1
        )
    elif model_name == "GradientBoostingClassifier":
        model = GradientBoostingClassifier(
            n_estimators=100,
            learning_rate=0.1,
            max_depth=3,
            random_state=1
        )

    elif model_name == "GaussianNB":
        model = GaussianNB()

    elif model_name == "DecisionTreeClassifier":
        model = DecisionTreeClassifier(
            ccp_alpha=0.005,
            random_state=1
        )


    return make_pipeline(
        StandardScaler(),
        model,
    ).fit(X, y)


def plot(X, y, model):

    x1, x2 = X[:, 0], X[:, 1]
    fig = px.scatter(x=x1, y=x2, color=y)
    fig.update_traces(marker={"size": 15})
    x1_range = np.linspace(x1.min(), x1.max(), 100)
    x2_range = np.linspace(x2.min(), x2.max(), 100)
    xx1, xx2 = np.meshgrid(x1_range, x2_range)
    y_pred_mesh = model.predict(np.c_[xx1.ravel(), xx2.ravel()]).reshape(xx1.shape)
    fig.add_contour(x=x1_range, y=x2_range, z=y_pred_mesh, showscale=False, opacity=0.2)
    return fig
