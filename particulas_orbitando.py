from turtle import distance
from manim import *
class Elipse(Ellipse):
    CONFIG={
        'width':5,
        'height':3,
    }
    def __init__(self,**kwargs):
        Ellipse.__init__(
            self,
            width=self.CONFIG['width'],
            height=self.CONFIG['height']
        )
    def get_dot(self,invert=False):
        if invert is not False:
            self.rotate(PI)
        dot=self.dot=Dot()
        dot.move_to(
            self.point_from_proportion(0)
        )
        def update_dot(mob,alpha):
            mob.move_to(
                self.point_from_proportion(alpha)
            )
        return UpdateFromAlphaFunc(dot,update_dot)
class ParticlesScene(Scene):
    def construct(self):
        elipse1=Elipse().move_to(2*RIGHT)
        elipse2=Elipse().move_to(2*LEFT)
        animation1=elipse1.get_dot(invert=True)
        animation2=elipse2.get_dot()
        line=Line(elipse1.dot,elipse2.dot).add_updater(lambda t: t.become(Line(elipse1.dot, elipse2.dot)))
        distance_line=DecimalNumber(line.get_length()).next_to(VGroup(elipse1,elipse2),DOWN,buff=1)
        def update_number(num):
            num.set_value(line.get_length())
        distance_line.add_updater(update_number)
        self.add(elipse1,elipse2,line,distance_line)
        count=0
        while count<11:
            count+=1
            self.play(animation1,animation2,run_time=2, rate_func=linear)
        self.wait()