from manim import *
class OrbitalZ(Circle):
    CONFIG={
        'radius':3
    }
    def __init__(self,**kwargs):
        Circle.__init__(self,radius=self.CONFIG['radius'])
    def orbital_in_y(self):
        dot=self.dot=Dot().move_to(
            self.point_from_proportion(0)
        )
        def update_in_y(mob,alpha):
            mob.move_to(self.point_from_proportion(alpha))
            return mob
        return UpdateFromAlphaFunc(dot,update_in_y)
class OrbitalZScene(Scene):
    def construct(self):
        orbital_z=OrbitalZ()
        animation_y=orbital_z.orbital_in_y()
        self.add(orbital_z,orbital_z.dot)
        self.play(animation_y)
        self.wait()