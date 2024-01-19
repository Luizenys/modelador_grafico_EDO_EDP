class MyPoint:
    # classe com os métodos set e get para as
    # coordenadas x e y do ponto
    def __init__(self,_x=0,_y=0):
        self.m_x = _x
        self.m_y = _y
    def setX(self,_x):
        self.m_x = _x
    def setY(self,_y):
        self.m_y = _y
    def getX(self):
        return self.m_x
    def getY(self):
        return self.m_y

class MyCurve:
    # classe com os métodos set e get para as
    # coordenadas da curva
    # que são os pontos 1 e 2, visto que uma curva precisa
    # de 2 pontos para existir
    def __init__(self,_p1=None,_p2=None):
        self.m_p1 = _p1
        self.m_p2 = _p2
    def setP1(self,_p1):
        self.m_p1 = _p1
    def setP2(self,_p2):
        self.m_p2 = _p2
    def getP1(self):
        return self.m_p1
    def getP2(self):
        return self.m_p2

class MyModel:
    # cria lista de vértices e curvas com suas funções get e set
    def __init__(self):
        self.m_verts = []
        self.m_curves = []

    def setVerts(self,_x,_y):
        self.m_verts.append(MyPoint(_x,_y))

    def getVerts(self):
        return self.m_verts

    def setCurve(self,_x1,_y1,_x2,_y2):
        self.m_curves.append(MyCurve(MyPoint(_x1,_y1),MyPoint(_x2,_y2)))

    def getCurves(self):
        return self.m_curves

    # função que checa se o modelo está vazio,
    # ou seja, sem vértices e curvas
    def isEmpty(self):
        return (len(self.m_verts) == 0) and (len(self.m_curves) == 0)

    # retorna os limites da boundbox (xmin , xmax, ymin ,ymax)
    def getBoundBox(self):
        if (len(self.m_verts) < 1) and (len(self.m_curves) < 1):
            return 0.0,10.0,0.0,10.0
        if len(self.m_verts) > 0:
            # seta a coordenada x do primeiro ponto como sendo xmin e xmax
            # todos os procedimento dessa função seram homólogos para a coordenada y
            xmin = self.m_verts[0].getX()
            xmax = xmin
            ymin = self.m_verts[0].getY()
            ymax = ymin
            for i in range(1,len(self.m_verts)):
                # itera por todos os pontos vendo se tem um ponto com coordenada x menor que o xmin 
                # ou maior que xmax, caso tenha atualiza
                # assim redefinindo os limites da boundbox
                if self.m_verts[i].getX() < xmin:
                    xmin = self.m_verts[i].getX()
                if self.m_verts[i].getX() > xmax:
                    xmax = self.m_verts[i].getX()
                if self.m_verts[i].getY() < ymin:
                    ymin = self.m_verts[i].getY()
                if self.m_verts[i].getY() > ymax:
                    ymax = self.m_verts[i].getY()

        if len(self.m_curves) > 0:
            if len(self.m_verts) == 0:
                # é realizado um procedimento homólogo ao do if acima, porém alterando os limites
                # da bound box de acordo com as coordenadas da curva, que são os seus pontos 1 e 2
                xmin = min(self.m_curves[0].getP1().getX(),self.m_curves[0].getP2().getX())
                xmax = max(self.m_curves[0].getP1().getX(),self.m_curves[0].getP2().getX())
                ymin = min(self.m_curves[0].getP1().getY(),self.m_curves[0].getP2().getY())
                ymax = max(self.m_curves[0].getP1().getY(),self.m_curves[0].getP2().getY())
            for i in range(1,len(self.m_curves)):
                temp_xmin = min(self.m_curves[i].getP1().getX(),self.m_curves[i].getP2().getX())
                temp_xmax = max(self.m_curves[i].getP1().getX(),self.m_curves[i].getP2().getX())
                temp_ymin = min(self.m_curves[i].getP1().getY(),self.m_curves[i].getP2().getY())
                temp_ymax = max(self.m_curves[i].getP1().getY(),self.m_curves[i].getP2().getY())
                if temp_xmin < xmin:
                    xmin = temp_xmin
                if temp_xmax > xmax:
                    xmax = temp_xmax
                if temp_ymin < ymin:
                    ymin = temp_ymin
                if temp_ymax > ymax:
                    ymax = temp_ymax
        return xmin,xmax,ymin,ymax