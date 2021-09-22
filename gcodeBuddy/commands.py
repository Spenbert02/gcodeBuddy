# for dev: not error checked (what is to error check?)

from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

"""
Return tuple containing current commands, pulled from website documentation.
Supported Flavors: Marlin (MARLIN_COMMANDS)
"""


def marlin_commands():
    """
    Return tuple containing legal Marlin commands
    """

    """
    The following code should be uncommented, and the main function of this file should be run periodically.
    This will pull commands from the marlin website, which will then be printed to console. This will be
    in a tuple format, which can then be copied and pasted in the return value of the function. If it has
    to pull from the website every time this function is called, it takes an extremely long time and is
    an easy source of a difficult to detect error.
    """

    ## opening site and getting BeautifulSoup object
    # gcode_index_url = "https://marlinfw.org/meta/gcode/"
    # gcode_index_client = urlopen(gcode_index_url)
    # gcode_index_html = gcode_index_client.read()
    # gcode_index_client.close()
    #
    # first_command = "G0"
    # last_command = "T6"
    #
    # # parsing through website and extracting commands into list
    # gcode_index_soup = soup(gcode_index_html, "html.parser")
    # commands = gcode_index_soup.findAll("strong")
    # i = 0
    # while True:
    #     if not isinstance(commands[i], str):  # if isn't already string, get text from tag and convert
    #         commands[i] = str(commands[i].get_text())
    #     # splitting up website entries than encompass multiple commands. Will change as Marlin site is updated
    #     multiple_command_entries = (
    #         (  "G0-G1",      "G2-G3",          "G17-G19",                   "G38.2-G38.5",                                        "G54-G59.3",                                 "M0-M1",         "M7-M9",         "M10-M11",      "M18, M84",                                     "M810-M819",                                                                       "M860-M869",                                      "M993-M994",                   "T0-T6"),
    #         (("G1", "G0"), ("G3", "G2"), ("G19", "G18", "G17"), ("G38.5", "G38.4", "G38.3", "G38.2"), ("G59.3", "G59.2", "G59.1", "G59", "G58", "G57", "G56", "G55", "G54"), ("M1", "M0"), ("M9", "M8", "M7"), ("M11", "M10"), ("M84", "M18"), ("M819", "M818", "M817", "M816", "M815", "M814", "M813", "M812", "M811", "M810"), ("M869", "M868", "M867", "M866", "M865", "M864", "M863", "M862", "M861", "M860"), ("M994", "M993"), ("T6", "T5", "T4", "T3", "T2", "T1", "T0"))
    #     )
    #     if commands[i] in multiple_command_entries[0]:
    #         specific_commands = multiple_command_entries[1][multiple_command_entries[0].index(commands[i])]
    #         for command in specific_commands:
    #             commands.insert(i, command)
    #         commands.pop(i + len(specific_commands))
    #     if (len(commands) > (i + 1)) and commands[i] == last_command:
    #         commands = commands[:(i + 1)]
    #         break
    #     if i >= len(commands) - 1:  # safety measure, in case of unexpected website updates
    #         break
    #     i += 1
    #
    # return (tuple(commands))
    # ________________________________________

    return ("G0",
            "G1",
            "G2",
            "G3",
            "G4",
            "G5",
            "G6",
            "G10",
            "G11",
            "G12",
            "G17",
            "G18",
            "G19",
            "G20",
            "G21",
            "G26",
            "G27",
            "G28",
            "G29",
            "G29",
            "G29",
            "G29",
            "G29",
            "G29",
            "G30",
            "G31",
            "G32",
            "G33",
            "G34",
            "G35",
            "G38.2",
            "G38.3",
            "G38.4",
            "G38.5",
            "G42",
            "G53",
            "G54",
            "G55",
            "G56",
            "G57",
            "G58",
            "G59",
            "G59.1",
            "G59.2",
            "G59.3",
            "G60",
            "G61",
            "G76",
            "G80",
            "G90",
            "G91",
            "G92",
            "G425",
            "M0",
            "M1",
            "M3",
            "M4",
            "M5",
            "M7",
            "M8",
            "M9",
            "M10",
            "M11",
            "M16",
            "M17",
            "M18",
            "M84",
            "M20",
            "M21",
            "M22",
            "M23",
            "M24",
            "M25",
            "M26",
            "M27",
            "M28",
            "M29",
            "M30",
            "M31",
            "M32",
            "M33",
            "M34",
            "M42",
            "M43",
            "M43 T",
            "M48",
            "M73",
            "M75",
            "M76",
            "M77",
            "M78",
            "M80",
            "M81",
            "M82",
            "M83",
            "M85",
            "M92",
            "M100",
            "M104",
            "M105",
            "M106",
            "M107",
            "M108",
            "M109",
            "M110",
            "M111",
            "M112",
            "M113",
            "M114",
            "M115",
            "M117",
            "M118",
            "M119",
            "M120",
            "M121",
            "M122",
            "M125",
            "M126",
            "M127",
            "M128",
            "M129",
            "M140",
            "M141",
            "M143",
            "M145",
            "M149",
            "M150",
            "M154",
            "M155",
            "M163",
            "M164",
            "M165",
            "M166",
            "M190",
            "M191",
            "M192",
            "M193",
            "M200",
            "M201",
            "M203",
            "M204",
            "M205",
            "M206",
            "M207",
            "M208",
            "M209",
            "M211",
            "M217",
            "M218",
            "M220",
            "M221",
            "M226",
            "M240",
            "M250",
            "M256",
            "M260",
            "M261",
            "M280",
            "M281",
            "M282",
            "M290",
            "M300",
            "M301",
            "M302",
            "M303",
            "M304",
            "M305",
            "M350",
            "M351",
            "M355",
            "M360",
            "M361",
            "M362",
            "M363",
            "M364",
            "M380",
            "M381",
            "M400",
            "M401",
            "M402",
            "M403",
            "M404",
            "M405",
            "M406",
            "M407",
            "M410",
            "M412",
            "M413",
            "M420",
            "M421",
            "M422",
            "M425",
            "M428",
            "M430",
            "M486",
            "M500",
            "M501",
            "M502",
            "M503",
            "M504",
            "M510",
            "M511",
            "M512",
            "M524",
            "M540",
            "M569",
            "M575",
            "M600",
            "M603",
            "M605",
            "M665",
            "M665",
            "M666",
            "M666",
            "M672",
            "M701",
            "M702",
            "M710",
            "M808",
            "M810",
            "M811",
            "M812",
            "M813",
            "M814",
            "M815",
            "M816",
            "M817",
            "M818",
            "M819",
            "M851",
            "M852",
            "M860",
            "M861",
            "M862",
            "M863",
            "M864",
            "M865",
            "M866",
            "M867",
            "M868",
            "M869",
            "M871",
            "M876",
            "M900",
            "M906",
            "M907",
            "M908",
            "M909",
            "M910",
            "M911",
            "M912",
            "M913",
            "M914",
            "M915",
            "M916",
            "M917",
            "M918",
            "M928",
            "M951",
            "M993",
            "M994",
            "M995",
            "M997",
            "M999",
            "M7219",
            "T0",
            "T1",
            "T2",
            "T3",
            "T4",
            "T5",
            "T6")


# station to pull commands periodically, to update return value of marlin_commands
if __name__ == "__main__":
    commands = marlin_commands()
    print("(", sep="", end="")
    for item in commands[:-1]:
        print("\"" + item + "\", ")
    print("\"" + commands[-1] + "\")")