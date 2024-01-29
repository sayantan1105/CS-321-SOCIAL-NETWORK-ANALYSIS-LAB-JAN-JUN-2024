import matplotlib.pyplot as plt 
import networkx as nx 
import urllib.request
import io 
import zipfile

# DOLPHIN CLUB 
url = "http://www-personal.umich.edu/~mejn/netdata/dolphins.zip"
sock = urllib.request.urlopen (url)
sockRead = io.BytesIO (sock.read ())
sock.close ()

zf = zipfile.ZipFile (sockRead)
txt = zf.read ("dolphins.txt").decode ()
gml = zf.read ("dolphins.gml").decode ()
gml = gml.split ("\n") [1:]

G = nx.parse_gml (gml)

# Calculate degree centrality
degree_centrality = nx.degree_centrality(G)

# Print degree centrality for each node
print("\nDEGREE CENTRALITY")
for node, centrality in degree_centrality.items():
     print(f"Node {node}: = {centrality}")

# Calculate betweenness centrality
betweenness_centrality = nx.betweenness_centrality(G)

# Print betweenness centrality for each node
print("\nBETWEENESS CENTRALITY")
for node, centrality in betweenness_centrality.items():
    print(f"Node {node}: = {centrality}")

# Calculate eigenvector centrality
eigenvector_centrality = nx.eigenvector_centrality(G)

# Print eigenvector centrality for each node
print("\nEIGEN VECTOR CENTRALITY")
for node, centrality in eigenvector_centrality.items():
    print(f"Node {node}: = {centrality}")

# Visualize the network
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=800, font_size=8)
plt.title("Dolphin Club Network with Degree Centrality")
plt.show()
