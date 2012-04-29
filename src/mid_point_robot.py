
from random import randint

from point import Vector
from robot import Robot
from vector_maths import angle_between, midpoint, length_towards

class MidPointRobot(Robot):

    def get_target(self):
        """
        Figure out where to move towards.
        We're trying to move towards the mid-point of two other robots,
        while also keeping them at a maximal distance.
        """

        (a, b) = self.get_target_bots()

        mid = midpoint(a.location, b.location)
        dist_mid = self.dist_from(mid)

        dist_a = self.dist_from_bot(a)
        dist_b = self.dist_from_bot(b)

        # Attempt to maximise distances, while reducing distance to mid
        best = mid
        score = self.score(mid)

        def in_line():
            for i in xrange(-50, 50, 5):
                i /= 10
                v = length_towards(i, mid)
                there = self.location + v
                yield there

        def other():
            """Perpedicular to the mid point"""
            v = mid - self.location
            ref = Vector(v.y, v.x) + self.location
            for i in xrange(-50, 50, 5):
                i /= 10
                v = length_towards(i, ref)
                there = self.location + v
                yield there

        def rand():
            """Consider some random places"""
            for i in xrange(100):
                x = randint(0, self._arena.width)
                y = randint(0, self._arena.height)
                v = Vector(x, y)
                there = self.location + v
                yield there

        def possibles():
            for alg in [in_line, other, rand]:
                for pos in alg():
                    yield pos

        for pos in possibles():
            if not self._arena.position_valid(pos):
                continue
            s = self.score(pos)
            if s > score:
                best = pos

        return best

    def get_target_bots(self):
        """
        Return the bots that we're supposed to get between.
        This would be an input to an actual robot...
        """

        a_id = ( self.id + 1 ) % len(self._opponents)
        b_id = ( self.id + 2 ) % len(self._opponents)

        a = b = None
        for r in self._opponents:
            if r.id == a_id:
                a = r
            if r.id == b_id:
                b = r

            if a is not None and b is not None:
                break

        return ( a, b )

    def score(self, position):
        (a, b) = self.get_target_bots()

        mid = midpoint(a.location, b.location)
        dist_mid = abs(position - mid)

        dist_a = abs(position - a.location)
        dist_b = abs(position - b.location)

        # Minimise dist_mid, Maximise dist_{a,b}
        score = dist_a + dist_b - ( 1.5 * dist_mid )

        return score
