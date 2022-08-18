import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

data_frame = pd.read_csv('finalstars.csv')

#gravity = data_frame.sort('gravity')
mass = data_frame['mass']
radius = data_frame['radius']

fig = px.scatter(x=mass,y=radius)
fig.show()

#-----Clustering-----

x=data_frame.iloc[:,[0,1]].values

data_ray=[]
for i in range(1,11):
  k=KMeans(n_clusters=i, init='k-means++', random_state=42)
  k.fit(x)
  data_ray.append(k.inertia_)

plt.figure(figsize=(10,5))
sns.lineplot(range(1,11), data_ray, marker='o', color='red')
plt.title('Elbow Plot')
plt.show()