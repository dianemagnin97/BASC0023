import pandas as pd
import networkx as nx
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt

#remember to download files + change path for CSV imports

###### this part I got online https://www.udacity.com/wiki/creating-network-graphs-with-python
## I recommend using an online provider that just takes data input https://rhumbl.com/engine/editor/5c055bd0bda2b00010560a14


#the body of this code was copied and modified from https://www.udacity.com/wiki/creating-network-graphs-with-python
def draw_graph(graph, labels=None, graph_layout='reingold',
               node_size=600, node_color='#2c8ca4', node_alpha=0.7,
               node_text_size=5,
               edge_color='#fcd454', edge_alpha=0.3, edge_tickness=1,
               edge_text_pos=0.3,
               text_font='sans-serif'):

    # create networkx graph
    G=nx.Graph()

    # add edges
    for edge in graph:
        G.add_edge(edge[0], edge[1])

    # these are different layouts for the network you may try
    # use reingold!!
    if graph_layout == 'spring': #ok
        graph_pos=nx.spring_layout(G)
    elif graph_layout == 'spectral': #illegible
        graph_pos=nx.spectral_layout(G)
    elif graph_layout == 'random': #messy
        graph_pos=nx.random_layout(G)
    elif graph_layout == 'bipartite': #illegible, try a tripartite perhaps?
        graph_pos = nx.bipartite_layout(G, nodes=effortlist,
                                        align='vertical')
    elif graph_layout == 'circular': #illegible
        graph_pos=nx.circular_layout(G)
    elif graph_layout == 'kawai': #ok
        graph_pos=nx.kamada_kawai_layout(G)
    elif graph_layout == 'rescale': #do not use
        graph_pos=nx.rescale_layout(G)
    elif graph_layout == 'reingold': #USE THIS ONE
        graph_pos=nx.fruchterman_reingold_layout(G, pos=GraphPositions, fixed=all_node_list)
    else:
        graph_pos=nx.shell_layout(G) #illegible

    # draw graph

    #modified to assigned colors/sizes on nodes of each information category (bias, effort, tech)
    nx.draw_networkx_nodes(G,graph_pos,nodelist=effortlist,node_size=node_size,
                           alpha=node_alpha, node_color='black')
    nx.draw_networkx_nodes(G, graph_pos, nodelist=techlist, node_size=300,
                           alpha=node_alpha, node_color='#545454')
    nx.draw_networkx_nodes(G, graph_pos, nodelist=biaslist, node_size=500,
                           alpha=node_alpha, node_color=node_color)


    nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,
                           alpha=edge_alpha,edge_color=edge_color)
    nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,
                            font_family=text_font)

#below is for labels, which I removed from the edges
    #if labels is None:
    #    labels = range(len(graph))

    #edge_labels = dict(zip(graph, labels))
    #nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels,
     #                            label_pos=edge_text_pos)

    # show graph
    plt.show()





############################# This is input data for the graph


TechToEffort = pd.read_csv(r"C:\Users\Lenovo\Dropbox\UCL\4th year modules\TKE\MATRIX PROGRAM\TechToEffortCSV.csv",
                         delimiter= ',') #download the CSV file and change path
TechToEffort_py = np.array(TechToEffort.values) #convert to numpyarray
TechToEffort_py = TechToEffort_py.tolist()  #convert to python list of lists (ie, matrix)
#the above process ereases the headers, so add them back in
First_row = ['Tech & Effort',
               '1. Examining fewer cues.',
               '2. Reducing the difficulty associated with retrieving and storing cue values.',
               '3. Simplifying the weighting principles for cues.',
               '4. Integrating less information.',
               '5. Examining fewer alternatives.']
TechToEffort_py.insert(0, First_row)
#print(TechToEffort_py)


#BiasToEffort = pd.read_csv(r"C:\Users\Lenovo\Dropbox\UCL\4th year modules\TKE\MATRIX PROGRAM\BiasToEffortCSV.csv",
#                         delimiter= ',')
#BiasToEffort_py = np.array(BiasToEffort.values)
#BiasToEffort_py = BiasToEffort_py.tolist()
#First_row = ['Bias & Effort',
#               '1. Examining fewer cues.',
#               '2. Reducing the difficulty associated with retrieving and storing cue values.',
#               '3. Simplifying the weighting principles for cues.',
#               '4. Integrating less information.',
#               '5. Examining fewer alternatives.']
#BiasToEffort_py.insert(0, First_row)

#BiasClusterToEffort_input = pd.read_csv(r"C:\Users\Lenovo\Dropbox\UCL\4th year modules\TKE\MATRIX PROGRAM\30Clusters.csv"
#                            , delimiter= ',', skip_blank_lines= True).dropna()
#print(BiasClusterToEffort_input)
#BiasClusterToEffort = BiasClusterToEffort_input.values.tolist()
#First_row = ['Bias',
#             'Cluster',
#               '1. Examining fewer cues.',
#               '2. Reducing the difficulty associated with retrieving and storing cue values.',
#               '3. Simplifying the weighting principles for cues.',
#               '4. Integrating less information.',
#               '5. Examining fewer alternatives.']
#BiasClusterToEffort.insert(0, First_row)

ClusterOnly_input = pd.read_csv(r"C:\Users\Lenovo\Dropbox\UCL\4th year modules\TKE\MATRIX PROGRAM\ClustersOnly.csv"
                            , delimiter= ',')
ClusterOnly = ClusterOnly_input.values.tolist()
First_row = [  'Cluster',
               '1. Examining fewer cues.',
               '2. Reducing the difficulty associated with retrieving and storing cue values.',
               '3. Simplifying the weighting principles for cues.',
               '4. Integrating less information.',
               '5. Examining fewer alternatives.']
ClusterOnly.insert(0, First_row)
print(ClusterOnly)

G = [] #create an empty graph


biaslist = [] # create a list of all biases, tech, and efforts (minus the ones that are not linked to anything)
# creates edges, by taking input from matrix, ie (Medical Ai, 2. Effort...), (AI Interviews, 4...)
for i in range(1, len(ClusterOnly)-1): #number of rows in the matrix (ie, numbers of technology)
    biaslist.append(ClusterOnly[i][0])
    for j in range(1, 6): #iterates over number of efforts
        if ClusterOnly[i][j] == 1: #checks if a link exists, ie if a '1' is in the matrix
            G.append((ClusterOnly[i][0], ClusterOnly[0][j])) #if so, add the edge into the graph, ie (effort, tech) pair

print("bias list")
print(biaslist)

for i in range(1, len(TechToEffort_py)-1): #creates edges, like above. I just added in the biaslist generator here for convenience
    for j in range(1, 6):
        if TechToEffort_py[i][j] == 1:
            #create a list of edges in the graph ex: (x,y) is edge from x to y
            G.append((TechToEffort_py[i][0], TechToEffort_py[0][j]))
            #generate list of biases, to be reused down below

#generating separate list of values, so that i can color the nodes differently

effortlist = ['1. Examining fewer cues.',
               '2. Reducing the difficulty associated with retrieving and storing cue values.',
               '3. Simplifying the weighting principles for cues.',
               '4. Integrating less information.',
               '5. Examining fewer alternatives.']
techlist = []
for i in range(1, len(TechToEffort_py)-1):
    techlist.append(TechToEffort_py[i][0])
#techlist = list(set(techlist))
#print(techlist)

#biaslist = list((set(biaslist))) #remove duplicates from list of biases



###########################3 create a position dictionary for reingold layout, aligning efforts, tech
# https://networkx.github.io/documentation/latest/_modules/networkx/drawing/layout.html for more info


GraphPositions= {} #function takes a dictionary {node: (x,y), ...} as input

#for effort, align vertically around the center of a [-1,1] matrix, +0.25 to the right
space = float(abs(-0.75) + 0.75) #lower and upper limt of where you want the nodes to be. calculate available space
scatterEffort = float(space)/(len(effortlist)-1) #evenly space the dots in this space
effortlist.sort() #alphabetical order

effortPosition = []
for i in range(0,len(effortlist)): #generate a coordinate for each element of effortlist
    effortPosition.append((0.25,0.75 - (scatterEffort*i)))
for i in range(0,len(effortlist)):
    GraphPositions.update({effortlist[i]: effortPosition[i]}) #associate node name with coordinate
#print(effortPosition)
#print(GraphPositions)

#for tech, align vertically on the right, 0.75 to the right
tspace = abs(-0.75) + 0.75
scatterTech = tspace/(len(techlist)-1) #potentially scatter in 2 batches?

techPosition = []
for i in range(0,len(techlist)):
    techPosition.append((0.75,-0.75 + (scatterTech*i)))
for i in range(0,len(techlist)):
    GraphPositions.update({techlist[i]: techPosition[i]})
#print(techPosition)
#print(GraphPositions)

#for bias, align vertically on left,  in 4 columns
bspace = abs(-0.9) + 0.9
biases_per_column = (len(biaslist)/3)  #calculate how many biases will fit in each column
print(biases_per_column)
scatterBias = float(bspace)/float(biases_per_column) #calculate how far apart these nodes will be
print(scatterBias)

biasPosition = []
bcount = 0 #count how many biases are placed so far
column_count = 0 #count how many biases are in this column so far
while bcount < (biases_per_column):
    bcount = bcount + 1
    biasPosition.append((-0.75,-0.9 + (scatterBias*column_count)))
    column_count = column_count + 1

column_count = 0
while bcount < (biases_per_column*2):
    bcount = bcount + 1
    biasPosition.append((-0.5,-0.9 + (scatterBias*column_count)))
    column_count = column_count + 1

column_count = 0
while bcount < (biases_per_column*3):
    bcount = bcount + 1
    biasPosition.append((-0.25,-0.9 + (scatterBias*column_count)))
    column_count = column_count + 1

for i in range(0,len(biaslist)):
    GraphPositions.update({biaslist[i]: biasPosition[i]})
print(biasPosition)
print(biaslist)
print(GraphPositions)

all_node_list = biaslist + effortlist + techlist

print(G)
draw_graph(G)

#to do next: find a way to cluster efforts
