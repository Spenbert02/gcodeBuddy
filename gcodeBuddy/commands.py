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
    # opening site and getting BeautifulSoup object
    gcode_index_url = "https://marlinfw.org/meta/gcode/"
    gcode_index_client = urlopen(gcode_index_url)
    gcode_index_html = gcode_index_client.read()
    gcode_index_client.close()

    first_command = "G0"
    last_command = "T6"

    # parsing through website and extracting commands into list
    gcode_index_soup = soup(gcode_index_html, "html.parser")
    commands = gcode_index_soup.findAll("strong")
    i = 0
    while True:
        if not isinstance(commands[i], str):  # if isn't already string, get text from tag and convert
            commands[i] = str(commands[i].get_text())
        # splitting up website entries than encompass multiple commands. Will change as Marlin site is updated
        multiple_command_entries = (
            (  "G0-G1",      "G2-G3",          "G17-G19",                   "G38.2-G38.5",                                        "G54-G59.3",                                 "M0-M1",         "M7-M9",         "M10-M11",      "M18, M84",                                     "M810-M819",                                                                       "M860-M869",                                      "M993-M994",                   "T0-T6"),
            (("G1", "G0"), ("G3", "G2"), ("G19", "G18", "G17"), ("G38.5", "G38.4", "G38.3", "G38.2"), ("G59.3", "G59.2", "G59.1", "G59", "G58", "G57", "G56", "G55", "G54"), ("M1", "M0"), ("M9", "M8", "M7"), ("M11", "M10"), ("M84", "M18"), ("M819", "M818", "M817", "M816", "M815", "M814", "M813", "M812", "M811", "M810"), ("M869", "M868", "M867", "M866", "M865", "M864", "M863", "M862", "M861", "M860"), ("M994", "M993"), ("T6", "T5", "T4", "T3", "T2", "T1", "T0"))
        )
        if commands[i] in multiple_command_entries[0]:
            specific_commands = multiple_command_entries[1][multiple_command_entries[0].index(commands[i])]
            for command in specific_commands:
                commands.insert(i, command)
            commands.pop(i + len(specific_commands))
        if (len(commands) > (i + 1)) and commands[i] == last_command:
            commands = commands[:(i + 1)]
            break
        if i >= len(commands) - 1:  # safety measure, in case of unexpected website updates
            break
        i += 1

    return tuple(commands)
