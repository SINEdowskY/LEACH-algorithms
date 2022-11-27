import networkx as nx
import random

class Enviorment:
    def __init__(self, amount_of_nodes = 100, ant_color = 'black', node_alive_color = 'green', node_dead_color = 'brown'):
        self.__amount = amount_of_nodes
        self.__ant_color = ant_color
        self.__node_alive_color = node_alive_color
        self.__node_dead_color = node_dead_color

        self.__graph = nx.Graph()

        self.__nodes_colors = [self.__node_alive_color for i in range(self.__amount)]
        self.__pos = None
        self.__node_size = [50 for i in range(self.__amount)]
    
    def generate_network(self):
        self.__nodes_colors.append(self.__ant_color)
        self.__node_size.append(100)
        
        used_poses = []
        iterations = list(range(self.__amount))
        for el in iterations:
            label = f"node_{el}"
            rand_x = random.randint(0,self.__amount)
            rand_y = random.randint(0,int(self.__amount-self.__amount/10))
            if (rand_x, rand_y) not in used_poses:
                used_poses.append((rand_x, rand_y))
                self.__graph.add_node(label, pos=(rand_x,rand_y))
            else:
                iterations.append(iterations[-1]+1)

        self.__graph.add_node("antenna", pos=(int(self.__amount/2),self.__amount))
        self.__pos = nx.get_node_attributes(self.__graph, 'pos')
    
    def select_random_cluster_heades(self):
        ch_nodes = ['antenna']
        for i in range(7):
            x = random.randint(0,self.__amount-1)
            self.__nodes_colors[x] = 'red'
            ch_nodes.append(list(self.__graph)[x])
        nx.add_path(self.__graph, ch_nodes)
    
    def draw_network(self):
        nx.draw(self.__graph, pos=self.__pos, node_color=self.__nodes_colors, node_size=self.__node_size)
            