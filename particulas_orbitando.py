from manim import *
conf={
    'amount':50,
    'colorSun':YELLOW,
    'hor':config['frame_width']/2,
    'ver':config['frame_height']/2,
}
class Sun(Dot):
    def __init__(self,**kwargs):
        Dot.__init__(self,**kwargs)
        rays=self.rays()
        self.add(rays)
        def rotating_update(mob,dt):
            rot=0
            rot+=dt*.3
            mob.rotate(rot)
        self.add_updater(rotating_update)
    def rays(self):
        raysSun=VGroup()
        for i in np.linspace(0,1,conf['amount']):
            ray=rotate_vector(RIGHT*3/4,TAU*i)
            ghost_circle=Circle(radius=0.5).move_to(self.get_center())
            position=ghost_circle.point_from_proportion(i)
            ray=Line(position,ray,color=conf['colorSun'],stroke_width=2)
            raysSun.add(ray)
        return raysSun
class Planetario(Scene):
    def construct(self):
        texto=Tex('El Ciclotrón').to_corner(DL).set_opacity(0.3)
        elipse=Ellipse(height=5,width=7,color=WHITE,stroke_width=2)
        elipse_copy=elipse.copy()
        sun=Sun(radius=0.5,color=conf['colorSun'])
        parts=self.get_parts(20)
        parts.add_updater(self.get_update_parts)
        self.add(elipse_copy,sun,elipse,parts,texto)
        self.my_planet(elipse_copy)
        self.wait()
    def my_planet(self,curve):
        dot=Dot(radius=.2).move_to(curve.point_from_proportion(0))
        def update_trasl(mob,alpha):
            mob.move_to(curve.point_from_proportion(alpha))
        self.add(dot)
        time=0
        TIME=30
        while time<TIME:
            Time=4
            time+=Time
            self.play(UpdateFromAlphaFunc(dot,update_trasl),run_time=Time)
    def get_parts(self,n_part):
        hor=conf['hor']
        ver=conf['ver']
        parts=VGroup()
        for _ in range(n_part):
            rand_size=np.random.random()/10
            rand_pos=np.array([
                np.random.uniform(-hor,hor),
                np.random.uniform(-ver,ver),
                0
            ])
            dot=Dot(radius=rand_size).move_to(rand_pos)
            dot.rand_pos=rand_pos
            parts.add(dot)
        return parts
    def get_update_parts(self,mobs,dt):
        for mob in mobs:
            mob.rand_pos[0]+=dt*.6
            mob.rand_pos[1]-=dt*.6
            if mob.rand_pos[1]<-conf['ver']:
                mob.rand_pos[1]=conf['ver']+np.random.uniform(-conf['hor'],conf['hor'])
            elif mob.rand_pos[0]>conf['hor']:
                mob.rand_pos[0]=-conf['hor']+np.random.uniform(-conf['ver'],conf['ver'])
            mob.move_to(mob.rand_pos)
        return mobs