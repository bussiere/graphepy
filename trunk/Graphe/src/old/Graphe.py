def add_node_result(self,node,result):
        node = self.get_real_node(node)
        node_coun = node
        if result not in self.liste_result.values():
            self.count += 1
            node_coun = self.count
            Graph.add_node(self,self.count)
            self.liste_node_type[self.count] = 'result'
            self.liste_result[self.count] = result
        else :
            for key in self.liste_result :
                if self.liste_result[key] == result :
                    node_coun = key
        Graph.add_edge(self,node,node_coun)






from networkx import Graph
import threading
class Graphe(Graph):
    count = 0
    liste_node_main = {}
    liste_node_type = {}
    liste_name = {}
    liste_type = {}
    liste_weight = {}
    liste_key = {}
    liste_value = {}
    liste_liaison = {}
    liste_func = {}
    liste_result = {}
    liste_free = {}

    def add_node(self,node,name='',type='',weight='',func='',data = ''):
        self.count += 1
        node_coun = self.count
        Graph.add_node(self,node_coun)
        self.liste_node_main[node] = node_coun
        self.liste_node_type[node_coun] = 'main'
        if name != '' :
            self.add_node_name(node,name)
        if type != '':
            self.add_node_type(node,type)
        if func != '':
            self.add_node_func(node,func)
        if data != '':
            self.add_node_data(node,data)
        if weight != '':
            self.add_node_weight(node,weight)


    def add_node_weight(self,node,weight):
        node = self.get_real_node(node)
        node_coun = node
        if weight not in self.liste_weight.values():
            self.count += 1
            node_coun = self.count
            Graph.add_node(self,self.count)
            self.liste_node_type[self.count] = 'weight'
            self.liste_weight[self.count] = weight
        else :
            for key in self.liste_weight :
                if self.liste_weight[key] == weight :
                    node_coun = key
        Graph.add_edge(self,node,node_coun)

    def add_node_result(self,node,result):
        node = self.get_real_node(node)
        node_coun = node
        if result not in self.liste_result.values():
            self.count += 1
            node_coun = self.count
            Graph.add_node(self,self.count)
            self.liste_node_type[self.count] = 'result'
            self.liste_result[self.count] = result
        else :
            for key in self.liste_result :
                if self.liste_result[key] == result :
                    node_coun = key
        Graph.add_edge(self,node,node_coun)

    def add_node_data(self,node,data):
        #a revoir
        node = self.get_real_node(node)
        node_coun = node
        for k in data.keys() :
            if k not in self.liste_key.values():
                self.count += 1
                node_coun = self.count
                Graph.add_node(self,self.count)
                self.liste_node_type[self.count] = 'key'
                self.liste_key[self.count] = k
            else :
                for key in self.liste_key :
                    if self.liste_key[key] == k :
                        node_coun = key
            Graph.add_edge(self,node,node_coun)
            if data[k] not in self.liste_value.values():
                self.count += 1
                nodeo_coun = self.count
                Graph.add_node(self,self.count)
                self.liste_node_type[self.count] = 'value'
                self.liste_value[self.count] = data[k]
            else :
                for key in self.liste_value :
                    if self.liste_value[key] == data[k] :
                         nodeo_coun = key
            Graph.add_edge(self,node,nodeo_coun)
            if
            print "node add data %s"%node
            Graph.add_edge(self,nodeo_coun,node_coun)

    def get_node_weight(self,node):
        node = self.get_real_node(node)
        liste = G.neighbors(node)
        for n in liste :
            if self.liste_node_type[n] == 'weight' :
                return self.liste_weight[n]

    def get_node_data(self,node):
        #a revoir
        node = self.get_real_node(node)
        liste = G.neighbors(node)
        lister = {}
        for n in liste :
            if self.liste_node_type[n] == 'value' :
                listek = G.neighbors(n)
                for k in listek :
                    if self.liste_node_type[k] == 'key' :
                        if k in liste :
                            if G.has_edge(node,k) and G.has_edge(node,n) and G.has_edge(n,k):
                                lister[self.liste_key[k]] = self.liste_value[n]
        return lister

    def get_real_node(self,node):
        return self.liste_node_main[node]

    def get_node_surname(self,node):
        k = self.liste_node_main.keys()
        for n in k :
            if self.liste_node_main[n] == node :
                return n

    def add_node_name(self,node,name):
        node = self.get_real_node(node)
        node_coun = node
        if (name not in self.liste_name.values()):
            self.count += 1
            node_coun = self.count
            Graph.add_node(self,self.count)
            self.liste_node_type[self.count] = 'name'
            self.liste_name[self.count] = name
        else :
            for key in self.liste_name :
                if self.liste_name[key] == name :
                    node_coun = key
        Graph.add_edge(self,node,node_coun)

    def get_node_name(self,node):
        node = self.get_real_node(node)
        liste = G.neighbors(node)
        for n in liste :
            if self.liste_node_type[n] == 'name' :
                return self.liste_name[n]

    def get_key_node (self,key):
        for k in self.liste_key.keys() :
            if self.liste_key[k] == key :
                return k
    def get_value_node (self,key):
        for k in self.liste_value.keys() :
            if self.liste_value[k] == key :
                return k

    def add_node_type(self,node,type):
        node = self.get_real_node(node)
        node_coun = node
        if type not in self.liste_type.values():
            self.count += 1
            node_coun = self.count
            Graph.add_node(self,self.count)
            self.liste_node_type[self.count] = 'type'
            self.liste_type[self.count] = type
        else :
            for key in self.liste_type :
                if self.liste_type[key] == type :
                    node_coun = key
        Graph.add_edge(self,node,node_coun)

    def get_node_type(self,node):
        node = self.get_real_node(node)
        liste = G.neighbors(node)
        for n in liste :
            if self.liste_node_type[n] == 'type' :
                return self.liste_type[n]

    def add_node_func(self,node,func):
        node = self.get_real_node(node)
        node_coun = node
        if func not in self.liste_func.values():
            self.count += 1
            node_coun = self.count
            Graph.add_node(self,self.count)
            self.liste_node_type[self.count] = 'func'
            self.liste_func[self.count] = func
        else :
            for key in self.liste_type :
                if self.liste_func[key] == func :
                    node_coun = key
        Graph.add_edge(self,node,node_coun)

    def get_node_func(self,node):
        node = self.get_real_node(node)
        liste = G.neighbors(node)
        for n in liste :
            if self.liste_node_type[n] == 'func' :
                return self.liste_func[n]

    def exec_func(self,func,node):
        exec(func)
        self.add_node_result(node, var)
        self.liste_free[node] = 1

    def get_node_result(self,node):
        while G.liste_free[node] != 1 :
            pass
        node = self.get_real_node(node)
        liste = G.neighbors(node)
        lister = []
        for n in liste :
            if self.liste_node_type[n] == 'result' :
                lister.append(self.liste_result[n])
        return lister

    def exec_node_func(self,node):
        self.liste_free[node] = 0
        nodec = self.get_real_node(node)
        liste = G.neighbors(nodec)
        for n in liste :
            if self.liste_node_type[n] == 'func' :
                t = threading.Thread(target=self.exec_func, args=(self.liste_func[n],node))
                t.start()

    def get_neighbors(self,node):
        node = self.get_real_node(node)
        liste = G.neighbors(node)
        lister = []
        for n in liste :
            if self.liste_node_type[n] == 'main' :
                lister.append(self.get_node_surname(n))
        return lister

    def add_edge(self,node,nodebis):
        Graph.add_edge(self,self.get_real_node(node),self.get_real_node(nodebis))

    def change_node_name(self,node,name):
        nameold = self.get_node_name(node)
        nodes = node
        node = self.get_real_node(node)
        for key in self.liste_name :
                if self.liste_name[key] == nameold :
                    node_coun = key
        Graph.delete_edge(self,node,node_coun)
        if Graph.neighbors(self,node_coun) == []:
            del self.liste_node_type[node_coun]
            del self.liste_name[node_coun]
            G.delete_node(node_coun)
        self.add_node_name(nodes,name)

    def change_node_type(self,node,type):
        typeold = self.get_node_type(node)
        nodes = node
        node = self.get_real_node(node)
        for key in self.liste_type :
                if self.liste_type[key] == typeold :
                    node_coun = key
        Graph.delete_edge(self,node,node_coun)
        if Graph.neighbors(self,node_coun) == []:
            del self.liste_node_type[node_coun]
            del self.liste_type[node_coun]
            G.delete_node(node_coun)
        self.add_node_type(nodes,type)

    def change_node_weight(self,node,weight):
        weightold = self.get_node_weight(node)
        nodes = node
        node = self.get_real_node(node)
        for key in self.liste_weight :
                if self.liste_weight[key] == weightold :
                    node_coun = key
        Graph.delete_edge(self,node,node_coun)
        if Graph.neighbors(self,node_coun) == []:
            del self.liste_node_type[node_coun]
            del self.liste_weight[node_coun]
            G.delete_node(node_coun)
        self.add_node_weight(nodes,weight)

    def change_node_func(self,node,func):
        funcold = self.get_node_func(node)
        nodes = node
        node = self.get_real_node(node)
        for key in self.liste_func :
                if self.liste_func[key] == funcold :
                    node_coun = key
        Graph.delete_edge(self,node,node_coun)
        if Graph.neighbors(self,node_coun) == []:
            del self.liste_node_type[node_coun]
            del self.liste_func[node_coun]
            G.delete_node(node_coun)
        self.add_node_func(nodes,func)

    def get_liste_node(self):
        return self.liste_node_main
    def get_nodes(self):
        listeretour = []
        for node in self.liste_node_main :
            liste = {}
            liste['number'] = node
            liste['name'] = self.get_node_name(node)
            liste['weight'] = self.get_node_weight(node)
            liste['func'] = self.get_node_func(node)
            liste['data'] = self.get_node_data(node)
            listeretour.append(liste)
        return listeretour
    def change_node_data(self,node,data):
        #a revoir
        dataold = self.get_node_data(node)
        nodes = node
        node = self.get_real_node(node)
        self.add_node_data(nodes,data)



if __name__ == "__main__":
    G=Graphe(name="I have a name!")
    G.add_node(1,"node1",'node',3,'var = 2*16',{'data1':0,'data2':'toto','data3':3})
    G.add_node(2,"node2",'nod',4,'',{'data':0,'data2':'toto','data3':3})
    G.exec_node_func(1)
    print G.get_node_result(1)
    G.add_edge(1, 2)
    l = G.get_neighbors(1)
    l = G.get_node_data(1)
    print "data"
    print l
    l = G.get_node_data(2)
    print l
    G.exec_node_func(1)
    G.change_node_name(1, 'node1bis')
    G.change_node_type(1, 'nodebis')
    G.change_node_weight(1, 4)
    print G.get_node_weight(1)
    G.change_node_func(1, 'var=2*4')
    G.exec_node_func(1)
    print G.get_key_node('data1')
    print G.get_value_node('toto')
    G.change_node_func(1, 'var=2*4*4*4*4')
    print G.get_key_node('data2')
    print G.get_value_node(0)
    print G.get_key_node('data1')
    print G.get_value_node('toto')
    print G.get_key_node('data3')
    print G.get_value_node(3)
    G.exec_node_func(1)
    print G.get_node_result(1)
    G.change_node_data(1,{'da':2})
    print G.get_node_data(1)
    G.add_node_data(1, {'d':3})
    G.add_node_data(1, {'data':3})
    print G.get_nodes()
    print G.get_node_data(1)
    print G.get_node_data(2)





