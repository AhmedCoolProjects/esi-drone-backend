from math import radians, cos, sin, asin, sqrt

class Main:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ordre = list(range(len(x)))
    
    def distance(self, lat1, lat2, lon1, lon2):
        # The math module contains a function named
        # radians which converts from degrees to radians.
        lon1 = radians(lon1)
        lon2 = radians(lon2)
        lat1 = radians(lat1)
        lat2 = radians(lat2)
        
        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    
        c = 2 * asin(sqrt(a))
        
        # Radius of earth in kilometers. Use 3956 for miles
        r = 6371
        
        # calculate the result
        return(c * r)

    def longueur(self):
        i = self.ordre[-1]
        x0, y0 = self.x[i], self.y[i]
        d = 0
        for o in self.ordre:
            x1, y1 = self.x[o], self.y[o]
            d += self.distance(x0, x1, y0, y1)
            x0, y0 = x1, y1
            x0, y0 = x1, y1
            x0, y0 = x1, y1
        return d

    def permutation(self):
        d = self.longueur()
        d0 = d+1
        it = 1
        while d < d0:
            it += 1
            d0 = d
            for i in range(1, len(self.ordre)-1):
                for j in range(i+2, len(self.ordre)+1):
                    r = self.ordre[i:j].copy()
                    r.reverse()
                    ordre2 = self.ordre[:i] + r + self.ordre[j:]
                    self.ordre = ordre2
                    t = self.longueur()
                    if t < d:
                        d = t
                        self.ordre = ordre2
        self.ordre.append(self.ordre[0])
        return (self.ordre, d)  # (chemin optimal , longueur dyalo)

"""
[
    {
      lat: 0.8459165322899798,
      lng: -179.9835205078125
    },
    {
      lat: -0.269164049012702,
      lng: -179.4012451171875
    },
    {
      lat: -0.15380840901698828,
      lng: 178.6981201171875
    }
  ]
"""

testt = Main([0.8459165322899798, -0.269164049012702, -0.15380840901698828], [-179.9835205078125, -179.4012451171875, 178.6981201171875])
print(testt.permutation())