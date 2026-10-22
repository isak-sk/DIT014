"""
In this experiment we intend to apply electromagnetic and coulumbs force to a set amount of particles. 
In coulumbs forces the particels should repuls particels of the same charge and attract opposit charges. 
This happens becuse the elektrostatic forces deppend on the product of these two charges and the distance between themc according to cuolumbs law.

The magnetic field affects moving charged particles by applying a force perpendicular to their velocity. This is based on the magnetic Lorentz force.
Since the force is perpendicular to the velocity, it changes the direction of the particle's motion rather than its speed, ideally causing the particle to move in a circular path.

The observed behavior is expected to follow these physicle principle, although these movements also deppend on the given velocity, 
the strenght of the forces and the given timesteps.

---------

Discussion: Effect of the timestep:
The simulation moves the particles in steps. In each step the force is calculated once and treated as a constant
for the whole time of dt.

The smaller dt is, the closer this is to real "motion". The cost is that more steps are needed to simulate the same
amount of time.

Coloumb experiment:
If dt is too large, the change in velocity in a single step becomes as large as the velocity itself.
When 2 differently charged particles pass close to eachother, they get a huge impulse that is applied for too long.
They fly apart faster than they came in, which breaks the expected behaviour.

The r < 4 in the function softens this by capping the force at shorter distances.
But it doesnt remove the whole problem. A smaller dt gives more accurate moves, but each frame
covers less time, so the motion looks slower.



Electromagnetic experiment:
Theoretically, the magnetic force is perpendicular to the velocity.
Meaning it only changes direction and the particles should move in perfect circles at constant speed.
In our simulation, each step adds a small sideways kick to the velocity, and because that kick is perpendicular,
the speed increases a bit each step. With a large dt this adds up and the particles spiral our instead of staying
on a circle. With a smaller dt the circles are almost perfect, but a full circle takes more time.


Conclusion:
Choosing the right timestep is a tradeoff between accuracy and stability.
The right value depends on how strong the forces are, which is why these two experiments
needed very different timesteps.

The expected phyics behaviour is only produces when dt is small enough compared to the strength of the forces.


"""

from view import *
import sys
from model import coulomb_force, electromagnetic_field, Vec, Particle


try:
    experiment = sys.argv[1]
except IndexError:
    print("Argument not given. Please choose electro or coulomb as first argument")
    sys.exit()



p1 = Particle(1, Vec(-5, 5), Vec(5, -5), 0.5)
p1.set_charge(5)

p2 = Particle(1, Vec(-5, -5), Vec(5, 5), 0.5)
p2.set_charge(-5)

p3 = Particle(1, Vec(5, 5), Vec(-5, -5), 0.5)
p3.set_charge(5)

p4 = Particle(1, Vec(5, -5), Vec(-5,5),0.5)
p4.set_charge(-5)


particles = [p1,p2,p3,p4]



if experiment == "electro":

    simulation_loop(electromagnetic_field, 0.00005, particles)

elif experiment == "coulomb":

    simulation_loop(coulomb_force, 0.000000001, particles)

else:
    print("Unknown experiment")
    sys.exit()


