from sklearn import datasets
digits = datasets.load_digits()
print digits

from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100)
clf.fit(digits.data[:-1], digits.target[:-1])
print "\n\nPREDICTION:\n\n", kclf.predict(digits.data[-1])
