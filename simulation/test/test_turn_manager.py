import unittest

from simulation.location import Location
from simulation.avatar_manager import AvatarManager
from simulation.turn_manager import TurnManager
from simulation.world_map import WorldMap
from simulation.world_state import WorldState
from simulation.test.dummy_avatar import DummyAvatar


class TestTurnManager(unittest.TestCase):
    def construct_turn_manager(self, *avatars):
        self.avatar_manager = AvatarManager(avatars)
        self.world_state = WorldState(WorldMap(), self.avatar_manager)
        self.turn_manager = TurnManager(self.world_state, self.avatar_manager)

    def test_run_turn(self):
        avatar = DummyAvatar(Location(0, 0))
        self.construct_turn_manager(avatar)
        self.turn_manager.run_turn()
        self.assertEqual(avatar.location, Location(1, 0))

    def test_run_several_turns(self):
        avatar = DummyAvatar(Location(0, 0))
        self.construct_turn_manager(avatar)
        [self.turn_manager.run_turn() for _ in xrange(5)]
        self.assertEqual(avatar.location, Location(5, 0))

    def test_run_several_turns_and_avatars(self):
        avatar1 = DummyAvatar(Location(0, 0))
        avatar2 = DummyAvatar(Location(0, 1))
        self.construct_turn_manager(avatar1, avatar2)
        [self.turn_manager.run_turn() for _ in xrange(5)]
        self.assertEqual(avatar1.location, Location(5, 0))
        self.assertEqual(avatar2.location, Location(5, 1))

if __name__ == '__main__':
    unittest.main()
