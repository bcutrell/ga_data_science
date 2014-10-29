
# coding: utf-8

# ##Support Vector Machines
# First let's experiment with a purely linear kernel where the data is completely linearly separable.

# In[9]:

import numpy as np
import pylab as pl
from sklearn import svm

# we create 40 completely linearly separable points sampled from 2-d normal distributions 
#centered at (-2, -2) for class 0 and (2, 2) for class 1
np.random.seed(8)
X = np.r_[np.random.randn(20, 2) - [2, 2], np.random.randn(20, 2) + [2,2]]
Y = [0] * 20 + [1] * 20
print X


# Fit a linear SVM to the data and plot it to see that it is indeed linearly separable.

# In[13]:

# fit the model
clf = svm.SVC(kernel='linear')
clf.fit(X, Y)

# get the separating hyperplane
w = clf.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(-5, 5)
yy = a * xx - (clf.intercept_[0]) / w[1]

# plot the parallels to the separating hyperplane that pass through the
# support vectors
b = clf.support_vectors_[0]
yy_down = a * xx + (b[1] - a * b[0])
b = clf.support_vectors_[-1]
yy_up = a * xx + (b[1] - a * b[0])

# plot the line, the points, and the nearest vectors to the plane
pl.plot(xx, yy, 'k-')
pl.plot(xx, yy_down, 'k--')
pl.plot(xx, yy_up, 'k--')

pl.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1],
           s=80, facecolors='none')
pl.scatter(X[:, 0], X[:, 1], c=Y, cmap=pl.cm.Paired)

pl.axis('tight')
pl.show()



# ##Nonlinear Kernels
# Try out RBF (Gaussian), Linear, and polynomial kernels for a less separable version of the same example to see the effects.

# In[7]:

# we create 40 not linearly separable points sampled from 2-d normal distributions 
#centered at (-1, -1) for class 0 and (1, 1) for class 1
np.random.seed(8)
X = np.r_[np.random.randn(20, 2) - [1, 1], np.random.randn(20, 2) + [1,1]]
Y = [0] * 20 + [1] * 20


# Fit different kernels and plot the results:

# In[8]:

h = .02  # step size in the mesh

# we create an instance of SVM and fit out data. We do not scale our
# data since we want to plot the support vectors
C = 1.0  # SVM regularization parameter
svc = svm.SVC(kernel='linear', C=C).fit(X, Y)
rbf_svc = svm.SVC(kernel='rbf', gamma=10.7, C=C).fit(X, Y)
poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(X, Y)
lin_svc = svm.LinearSVC(C=C).fit(X, Y)

# create a mesh to plot in
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# title for the plots
titles = ['SVC with linear kernel',
          'SVC with RBF kernel',
          'SVC with polynomial (degree 3) kernel',
          'LinearSVC (linear kernel)']


for i, clf in enumerate((svc, rbf_svc, poly_svc, lin_svc)):
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    pl.subplot(2, 2, i + 1)
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    pl.contourf(xx, yy, Z, cmap=pl.cm.Paired)
    pl.axis('off')

    # Plot also the training points
    pl.scatter(X[:, 0], X[:, 1], c=Y, cmap=pl.cm.Paired)

    pl.title(titles[i])

pl.show()


# ##On Your Own:
# Try out the various classifiers we've tried so far (KNN, Logistic Regression, Naive Bayes, Decision Trees, Random Forests, SVM, and Boosting/Bagging for any of these) on this dataset: https://archive.ics.uci.edu/ml/datasets/Contraceptive+Method+Choice
# 
# Experiment to get a feel for how the different algorithms react to changes in number of records, attributes, type of attributes etc, as well as the relative performance in both computational time and accuracy (cross-validate for evaluation!).  
# 
# Just play around, this is the best way to get comfortable with these!
