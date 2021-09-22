import unittest
from gcodeBuddy.marlin import command_to_arc, Command


class CommandToArcTestCase(unittest.TestCase):

    def setUp(self):
        self.starting_position = [100, 100]
        self.commands = ["G2 I10",  # (110, 100) ; 10 ; 180 ; 180 ; "c"
                         "G3 J-30",  # (100, 70) ; 30 ; 90 ; 90 ; "cc"
                         "G2 X120 Y100",
                         "G3 X120 I10",
                         "G3 X110 J10",
                         "G2 Y120 I-20",
                         "G2 Y70 J-15",
                         "G3 I30 J-30",
                         "G2 X110 Y110 I10",
                         "G3 Y120 I10 J10",
                         "G3 X140 Y120 J20",
                         "G3 X90 I-10 J-10",
                         "G2 X150 Y150 I25 J25",
                         "G2 R10",
                         "G3 X120 R10",
                         "G2 Y180 R50",
                         "G2 X130 Y130 R10",
                         "G2 X130 Y130 R15",
                         "G3 X180 R50",
                         "G3 X180 R-50"]
