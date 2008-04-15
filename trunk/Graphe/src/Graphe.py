import threading

class Graph:
    def __init__(self,name):
        self.name = name
        self.list_neighbor = {}
        self.list_node = {}
    def add_node(self,node):
        self.list_node[node] = True

    def add_edge(self,node,nodebis):
        try :
            self.list_neighbor[node].append(nodebis)
        except :
            self.list_neighbor[node] = []
            self.list_neighbor[node].append(nodebis)
        try :
            self.list_neighbor[nodebis].append(node)
        except :
            self.list_neighbor[nodebis] = []
            self.list_neighbor[nodebis].append(node)
    def neighbors(self,node):
        try :
            return self.list_neighbor[node]
        except :
            return []
    def nodes(self):
        return self.list_node.keys()
    def delete_edge(self,node,nodebis):
        self.list_neighbor[node].remove(nodebis)
        self.list_neighbor[nodebis].remove(node)
    def delete_node(self,node):
        del self.list_node[node]
        try :
            for nodebis in self.list_neighbor[node] :
                self.list_neighbor[nodebis].remove(node)
            del self.list_neighbor[node]
        except :
            return "error"







class Graphe(Graph):
    count = 0
    liste_node_main = {}
    liste_node_type = {}
    liste_name = {}
    liste_type = {}
    liste_weight = {}
    liste_key = {}
    liste_value = {}
    liste_link = {}
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
            print node_coun
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
        nodes = node
        node = self.get_real_node(node)
        for key in data.keys() :
            if key not in self.liste_key.values() :
                self.count += 1
                node_coun = self.count
                Graph.add_node(self,self.count)
                self.liste_node_type[self.count] = 'key'
                self.liste_key[self.count] = key
            else :
                for keys in self.liste_key :
                    if self.liste_key[keys] == key :
                        node_coun = keys
            Graph.add_edge(self,node,node_coun)
            if data[key] not in self.liste_value.values() :
                self.count += 1
                node_counv = self.count
                Graph.add_node(self,self.count)
                self.liste_node_type[self.count] = 'value'
                self.liste_value[self.count] = data[key]
            else :
                for keys in self.liste_value :
                    if self.liste_value[keys] == data[key] :
                        node_counv = keys
            Graph.add_edge(self,node,node_counv)
            Graph.add_edge(self,node_coun,node_counv)
            if [node,node_coun,node_counv] not in self.liste_link.values() :
                self.count += 1
                node_counl = self.count
                Graph.add_node(self,self.count)
                self.liste_node_type[self.count] = 'link'
                self.liste_link[self.count] = [node,node_coun,node_counv]
            else :
                for key in self.liste_link :
                   if self.liste_link[key] == [node,node_coun,node_counv] :
                         node_counl = key
            Graph.add_edge(self,node,node_counl)
            Graph.add_edge(self,node_coun,node_counl)
            Graph.add_edge(self,node_counv,node_counl)









    def get_node_weight(self,node):
        node = self.get_real_node(node)
        liste = Graph.neighbors(self,node)
        for n in liste :
            if self.liste_node_type[n] == 'weight' :
                return self.liste_weight[n]

    def get_node_data(self,node):
        node = self.get_real_node(node)
        liste = Graph.neighbors(self,node)
        lister = {}
        for n in liste :
            if self.liste_node_type[n] == 'link' :
                lister[self.liste_key[self.liste_link[n][1]]] = self.liste_value[self.liste_link[n][2]]
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
        liste = Graph.neighbors(self,node)
        for n in liste :
            if self.liste_node_type[n] == 'name' :
                return self.liste_name[n]

    def get_key_node (self,key):
        for k in self.liste_key.keys() :
            if self.liste_key[k] == key :
                return k
    def get_value_node (self,value):
        for k in self.liste_value.keys() :
            if self.liste_value[k] == value :
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
        liste = Graph.neighbors(self,node)
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
        liste = Graph.neighbors(self,node)
        for n in liste :
            if self.liste_node_type[n] == 'func' :
                return self.liste_func[n]

    def __exec_func(self,func,node):
        dataold = self.get_node_data(node)
        data = self.get_node_data(node)
        exec(func)
        var = None
        for key  in data.keys():
            if data[key] != dataold[key] :
                self.change_node_data(node, data)
        self.add_node_result(node, var)
        self.liste_free[node] = 1

    def get_node_result(self,node):
        while self.liste_free[node] != 1 :
            pass
        node = self.get_real_node(node)
        liste = Graph.neighbors(self,node)
        lister = []
        for n in liste :
            if self.liste_node_type[n] == 'result' :
                lister.append(self.liste_result[n])
        return lister

    def exec_node_func(self,node):
        self.liste_free[node] = 0
        nodec = self.get_real_node(node)
        liste = Graph.neighbors(self,nodec)
        for n in liste :
            if self.liste_node_type[n] == 'func' :
                t = threading.Thread(target=self.__exec_func, args=(self.liste_func[n],node))
                t.start()

    def get_neighbors(self,node):
        node = self.get_real_node(node)
        liste = Graph.neighbors(self,node)
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
            Graph.delete_node(self,node_coun)
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
            Graph.delete_node(self,node_coun)
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
            Graph.delete_node(self,node_coun)
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
            Graph.delete_node(self,node_coun)
        self.add_node_func(nodes,func)

    def get_liste_node(self):
        return self.liste_node_main
    def get_nodes(self):
        listeretour = []
        for node in self.liste_node_main :
            liste = {}
            liste['number'] = node
            liste['type'] = self.get_node_type(node)
            liste['name'] = self.get_node_name(node)
            liste['weight'] = self.get_node_weight(node)
            liste['func'] = self.get_node_func(node)
            liste['data'] = self.get_node_data(node)
            listeretour.append(liste)
        return listeretour

    def change_node_data(self,node,data):
        dataold = self.get_node_data(node)
        for keys in data.keys() :
            key = keys
            value = dataold[keys]
        nodev = self.get_value_node(value)
        nodek = self.get_key_node(key)
        listen = Graph.neighbors(self, nodev)
        for noden in listen :
            if self.liste_node_type[noden] == 'link' and self.liste_link[noden] == [node,nodek,nodev] :
                Graph.delete_edge(self, nodev, node)
                Graph.delete_edge(self, nodev, nodek)
                Graph.delete_edge(self, nodev, noden)
                Graph.delete_edge(self, nodek, noden)
                Graph.delete_node(self, noden)
                print "n %s"%Graph.neighbors(self, nodev)
                if Graph.neighbors(self, nodev) == [] :
                    Graph.delete_node(self, nodev)
        node = self.get_real_node(node)
        self.add_node_data(node,data)

    def debug(self):
        j = 0
        for node in Graph.nodes(self):
            j +=1
            if self.liste_node_type[node] == 'link' :
                print "node : %s type : %s value : %s neighbors : %s"%(node,self.liste_node_type[node],self.liste_link[node],Graph.neighbors(self,node))
            else :
                if self.liste_node_type[node] == 'value' :
                    print "node : %s type : %s value : %s neighbors : %s"%(node,self.liste_node_type[node],self.liste_value[node],Graph.neighbors(self,node))
                else :
                    if self.liste_node_type[node] == 'key' :
                        print "node : %s type : %s value : %s neighbors : %s"%(node,self.liste_node_type[node],self.liste_key[node],Graph.neighbors(self,node))
                    else :
                        if self.liste_node_type[node] == 'main' :
                            print "node : %s type : %s neighbors : %s"%(node,self.liste_node_type[node],Graph.neighbors(self,node))
                        else:
                            if self.liste_node_type[node] == 'weight' :
                                print "node : %s type : %s value : %s neighbors : %s"%(node,self.liste_node_type[node],self.liste_weight[node],Graph.neighbors(self,node))
                            else :
                                if self.liste_node_type[node] == 'type' :
                                    print "node : %s type : %s value : %s neighbors : %s"%(node,self.liste_node_type[node],self.liste_type[node],Graph.neighbors(self,node))
                                else :
                                    if self.liste_node_type[node] == 'name' :
                                        print "node : %s type : %s value : %s neighbors  : %s"%(node,self.liste_node_type[node],self.liste_name[node],Graph.neighbors(self,node))
                                    else :
                                        if self.liste_node_type[node] == 'func' :
                                            print "node : %s type : %s value : %s neighbors : %s"%(node,self.liste_node_type[node],self.liste_func[node],Graph.neighbors(self,node))

        return j

    def get_meta_graphe(self):
        liste = {}
        for node in Graph.nodes(self):
            if self.liste_node_type[node] == 'link' :
                liste[node] = {'type' : self.liste_node_type[node],'value' :self.liste_link[node],'neighbors':Graph.neighbors(self,node)}
            else :
                if self.liste_node_type[node] == 'value' :
                    liste[node] = {'type' : self.liste_node_type[node],'value' :self.liste_value[node],'neighbors':Graph.neighbors(self,node)}
                else :
                    if self.liste_node_type[node] == 'key' :
                        liste[node] = {'type' : self.liste_node_type[node],'value' :self.liste_key[node],'neighbors':Graph.neighbors(self,node)}
                    else :
                        if self.liste_node_type[node] == 'main' :
                            liste[node] = {'type' : self.liste_node_type[node],'value' : '','neighbors':Graph.neighbors(self,node)}
                        else:
                            if self.liste_node_type[node] == 'weight' :
                                liste[node] = {'type' : self.liste_node_type[node],'value' :self.liste_weight[node],'neighbors':Graph.neighbors(self,node)}
                            else :
                                if self.liste_node_type[node] == 'type' :
                                    liste[node] = {'type' : self.liste_node_type[node],'value' : self.liste_type[node],'neighbors':Graph.neighbors(self,node)}
                                else :
                                    if self.liste_node_type[node] == 'name' :
                                        liste[node] = {'type' : self.liste_node_type[node],'value' : self.liste_name[node],'neighbors':Graph.neighbors(self,node)}
                                    else :
                                        if self.liste_node_type[node] == 'func' :
                                            liste[node] = {'type' : self.liste_node_type[node],'value' :self.liste_func[node],'neighbors':Graph.neighbors(self,node)}
        return liste





if __name__ == "__main__":
    G=Graphe(name="I have a name!")
    G.add_node(1,"node1",'node',3,"data['data1'] = 2*data['data3']",{'data1':1,'data2':'toto','data3':4})
    G.add_node(2,"node2",'nod',4,'self.add_node_data(node,self.get_node_data(node-1))',{'data':0,'data2':'toto','data3':3})
    print G.get_node_data(1)
    print G.get_node_data(2)
    print G.get_nodes()
    G.change_node_weight(2, 6)
    print G.debug()
    print G.get_node_weight(2)
    G.exec_node_func(1)
    print "result : %s"%G.get_node_result(1)
    print G.get_node_data(1)
    G.exec_node_func(2)
    G.get_node_result(2)
    print G.get_node_data(2)
    print G.get_meta_graphe()







