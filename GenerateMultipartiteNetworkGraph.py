#please make sure you have the following python packages. I recommend either using pip on the Anaconda IDE, or Pycharm project packages
import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

#!!!! Before running this code, please ensure:
#1. That you have the csv files that come with this document ("GenerateNetworkGraphsFiles")
#2. That any change you made with it doesn't modify the number of columns in the document (so add biases or tech only)
#3. That you have changed the path location (marked "#PATH LOCATION#, just ctrl+F it) to the location the above files
# are located on your computer
#!!!! This should be all you need to change in the code. Note: This code works on Python 3.0


### following part I got online https://www.udacity.com/wiki/creating-network-graphs-with-python and got updated
## I recommend using an online provider that just takes data input https://rhumbl.com/engine/editor/5c055bd0bda2b00010560a14


def draw_graph(graph, labels=None, graph_layout='reingold', #please don't change this
               node_size=500, #size of data dots
               node_color='#2c8ca4', #hex code or word like 'yellow'
               node_alpha=0.5, #opacity of dots
               node_text_size=5, #size of text.
               edge_color='#fcd454', edge_alpha=0.2, edge_tickness=1,
               edge_text_pos=0.3,
               text_font='sans-serif'):

    # create networkx graph
    G=nx.Graph()

    # add edges
    for edge in graph:
        G.add_edge(edge[0], edge[1]) #takes edge from edge list G (see below)


    # these are different layouts for the network you may try
    # use reingold!!
    if graph_layout == 'spring':
        graph_pos=nx.spring_layout(G)
    elif graph_layout == 'spectral':
        graph_pos=nx.spectral_layout(G)
    elif graph_layout == 'random':
        graph_pos=nx.random_layout(G)
    elif graph_layout == 'bipartite':
        graph_pos = nx.bipartite_layout(G, nodes=effortlist,
                                        align='vertical')
    elif graph_layout == 'circular':
        graph_pos=nx.circular_layout(G)
    elif graph_layout == 'kawai':
        graph_pos=nx.kamada_kawai_layout(G)
    elif graph_layout == 'rescale':
        graph_pos=nx.rescale_layout(G)
    elif graph_layout == 'reingold': #USE THIS ONE
        graph_pos=nx.fruchterman_reingold_layout(G, pos=GraphPositions, fixed=all_node_list)
    else:
        graph_pos=nx.shell_layout(G)

    # draw graph

    #modified to assigned colors/sizes on nodes of each information category (bias, effort, tech)
    nx.draw_networkx_nodes(G,graph_pos,nodelist=effortlist,node_size=node_size,
                           alpha=node_alpha, node_color='black') #assign color/size/opacity to 'effort' nodes
    nx.draw_networkx_nodes(G, graph_pos, nodelist=techlist, node_size=300,
                           alpha=node_alpha, node_color='#545454') #assign color/size/opacity to 'tech' nodes
    nx.draw_networkx_nodes(G, graph_pos, nodelist=biaslist, node_size=200,
                           alpha=node_alpha, node_color=node_color) #assign color/size/opacity to 'bias' nodes


    nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,
                           alpha=edge_alpha,edge_color=edge_color)
    nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,
                            font_family=text_font)

#below is for edge labels, which I removed from the edges
    #if labels is None:
    #    labels = range(len(graph))

    #edge_labels = dict(zip(graph, labels))
    #nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels,
     #                            label_pos=edge_text_pos)

    # show graph
    plt.show()





############################# This is input data for the graph


TechToEffort = pd.read_csv(r"C:\Users\Lenovo\Dropbox\UCL\4th year modules\TKE\MATRIX PROGRAM\GenerateNetworkGraphsFiles\TechToEffortCSV.csv",
                         delimiter= ',') #PATH LOCATION#
                        #download the CSV file and change path!


TechToEffort_py = np.array(TechToEffort.values) #convert to numpyarray
TechToEffort_py = TechToEffort_py.tolist()  #convert to python list of lists (ie, matrix)
#the above process ereases the headers, so add them back in
First_row = ['Tech & Effort',
             'Searching',
             'Storage',
             'Simplification',
             'Segregation/Synthesis',
             'Selection']
TechToEffort_py.insert(0, First_row)
#print(TechToEffort_py)


BiasToEffort = pd.read_csv(r"C:\Users\Lenovo\Dropbox\UCL\4th year modules\TKE\MATRIX PROGRAM\GenerateNetworkGraphsFiles\BiasToEffortCSV.csv",
                         delimiter= ',') #PATH LOCATION#


BiasToEffort_py = np.array(BiasToEffort.values)
BiasToEffort_py = BiasToEffort_py.tolist()
First_row = ['Bias & Effort',
             'Searching',
             'Storage',
             'Simplification',
             'Segregation/Synthesis',
             'Selection']
BiasToEffort_py.insert(0, First_row)

G = [] #create an empty graph

# creates edges, by taking input from matrix, ie (Medical Ai, 2. Effort...), (AI Interviews, 4...)
for i in range(1, len(TechToEffort_py)-1): #number of rows in the matrix (ie, numbers of technology)
    for j in range(1, 6): #iterates over number of efforts (if number of columns modified, change accordingly
        if TechToEffort_py[i][j] == 1: #checks if a link exists, ie if a '1' is in the matrix of the csv file
            G.append((TechToEffort_py[i][0], TechToEffort_py[0][j])) #if so, add the edge into the graph, ie (effort, tech) pair



biaslist = [] # create a list of all biases, tech, and efforts (minus the ones that are not linked to anything)

for i in range(1, len(BiasToEffort_py)-1): #creates edges, like above. I just added in the biaslist generator here for convenience
    for j in range(1, 6):
        if BiasToEffort_py[i][j] == 1:
            #create a list of edges in the graph ex: (x,y) is edge from x to y
            G.append((BiasToEffort_py[i][0], BiasToEffort_py[0][j]))
            #generate list of biases, to be reused down below
            biaslist.append(BiasToEffort_py[i][0])


#generating separate list of values, so that i can color the nodes differently

effortlist = ['Searching',
             'Storage',
             'Simplification',
             'Segregation/Synthesis',
             'Selection']
techlist = []
for i in range(1, len(TechToEffort_py)-1):
    techlist.append(TechToEffort_py[i][0])
#print(techlist)

biaslist = list((set(biaslist))) #remove duplicates from list of biases



########################### create a position dictionary for reingold layout, aligning efforts, tech
# https://networkx.github.io/documentation/latest/_modules/networkx/drawing/layout.html for more info


GraphPositions= {} #function takes a dictionary {node: (x,y), ...} as input

#for effort nodes, align vertically around the center of a [-1,1] matrix, +0.25 to the right to leave more space for the biases
space = float(abs(-0.75) + 0.75) #lower and upper limit of where you want the nodes to be. calculate available space
scatterEffort = float(space)/(len(effortlist)-1) #evenly space the dots in this space by calculating space between dots
effortlist.sort() #alphabetical order (or ascending numerical order)

effortPosition = []
for i in range(0,len(effortlist)): #generate a coordinate for each element of effortlist
    effortPosition.append((0.25,0.75 - (scatterEffort*i))) #(x,y) coordinates. x fixed at 0.25, y evenly spaced
for i in range(0,len(effortlist)):
    GraphPositions.update({effortlist[i]: effortPosition[i]}) #associate node name with coordinate
#print(effortPosition)
#print(GraphPositions)


#for tech, align vertically on the right (+0.75 to the right)
tspace = abs(-0.75) + 0.75
scatterTech = tspace/(len(techlist)-1)

techPosition = []
for i in range(0,len(techlist)):
    techPosition.append((0.75,-0.75 + (scatterTech*i)))
for i in range(0,len(techlist)):
    GraphPositions.update({techlist[i]: techPosition[i]})
#print(techPosition)
#print(GraphPositions)




#for bias, align vertically on left,  in 4 columns
bspace = abs(-0.9) + 0.9
biases_per_column = (len(biaslist)/4) +1 #calculate how many biases will fit in each column
scatterBias = float(bspace)/float(biases_per_column) #calculate how far apart these nodes will be, has an error rounding up that will be corrected below


biasPosition = []
bcount = 0 #count how many biases are placed so far
column_count = 0 #count how many biases are in this column so far
while bcount < (biases_per_column-1):
    bcount = bcount + 1
    biasPosition.append((-0.75,-0.9 + (scatterBias*column_count))) #(x,y), with x = -0.75, y even scattered
    column_count = column_count + 1

column_count = 0
while bcount < (biases_per_column*2 -2): #-2 to compensate for "rounding up" errors
    bcount = bcount + 1
    biasPosition.append((-0.5,-0.9 + (scatterBias*column_count))) #(x,y), with x = -0.5, y even scattered
    column_count = column_count + 1

column_count = 0
while bcount < (biases_per_column*3 -3): #-3 to compensate for "rounding up" errors
    bcount = bcount + 1
    biasPosition.append((-0.25,-0.9 + (scatterBias*column_count))) #(x,y), with x = -0.25, y even scattered
    column_count = column_count + 1

column_count = 0
while bcount < (biases_per_column*4):
    bcount = bcount + 1
    biasPosition.append((0,-0.9 + (scatterBias*column_count))) #(x,y), with x = 0, y even scattered
    column_count = column_count + 1

for i in range(0,len(biaslist)):
    GraphPositions.update({biaslist[i]: biasPosition[i]}) #match a bias to a coordinate

print(biasPosition)
print(biaslist)
print(GraphPositions)

all_node_list = biaslist + effortlist + techlist

print(G)
draw_graph(G)
