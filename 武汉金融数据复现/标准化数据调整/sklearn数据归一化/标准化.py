from sklearn.preprocessing import StandardScaler

data=[[-1,2],[-0.5,6],[0,10],[1,18]]
scaler=StandardScaler().fit(data)
print(scaler.transform(data))
