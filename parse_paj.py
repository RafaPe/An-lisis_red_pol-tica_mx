def paj_to_networx(file):
    nodes = []
    nombres, year, bg = [], [], [] 
    coordinates = []
    edges = []

    with open(file) as f:
        lines = f.readlines()

    for i in range(len(lines)):
        if lines[i][:9] == '*Vertices':
            _, num_vertices = lines[i].split()
            num_vertices = int(num_vertices)
            for j in range(1, num_vertices + 1):
                node = lines[i+j].split()
                if len(node) > 2:
                    c = [float(node[-3]), float(node[-2]), float(node[-1])]
                    coordinates.append(c)
                    for _ in range(3):
                        node.pop()
                    id, nombre = [int(node[0]), ' '.join(node[1:]).strip('"')]
                    # print(id, nombre)
                    nodes.append(id)
                    nombres.append(nombre)
                else:
                    if lines[i-1][:23] == '*Partition mexican_year':
                        year.append(int(node[0])+1900)
                    elif lines[i-1][:27] == '*Partition mexican_military':
                        if int(node[0]) == 1:
                            bg.append('militar')
                        else:
                            bg.append('civil')
            i += j
            
        if lines[i][:6] == '*Edges':
            k = i + 1
            while lines[k][0] != '\n':
                edge = lines[k].split()
                edge = [int(edge[0]), int(edge[1])]
                edges.append(edge)
                k += 1
            i += k

    attributes = {}
    for n in zip(nodes, nombres, year, bg):
        attributes[n[0]] = {'nombre':n[1], 'año':n[2], 'trasfondo':n[3]}

    return nodes, edges, coordinates, attributes

if __name__ == '__main__':
    ann = paj_to_networx('data/mexican_power.paj')
    for k in ann:
        print(k)
    