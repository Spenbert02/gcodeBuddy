====================
marlin
====================

.. py:currentmodule:: gcodeBuddy.marlin

.. automodule:: gcodeBuddy.marlin
    :members:

*********
Examples
*********

.. code-block:: python
    :caption: Basic Command Usage

    # imports Command object
    from gcodeBuddy.marlin import Command

    # creates Command object from line of Marlin g-code
    sample_command = Command("G0 X12.3 Y45.6 Z78.9")

    # prints "G0"
    print(sample_command.get_command())

    # prints 12.3
    if sample_command.has_param("X"):
        print(sample_command.get_param("X"))

    # changes value of "Y" param to 0.0
    sample_command.set_param("Y", 0.0)

    # prints "G0 X12.3 Y0.0 Z78.9"
    print(sample_command.get_string()))

.. code-block:: python
    :caption: marlin_commands() Usage

    # imports marlin_commands() function
    from gcodeBuddy.marlin import marlin_commands

    # prints every current Marlin command
    for element in marlin_commands():
        print(element)

.. code-block:: console
    :caption: Result of Printing marlin_commands()

    G0
    G1
    G2
    G3
    .
    .
    .
    G91
    G92
    G425
    M0
    M1
    M3
    .
    .
    .
    M997
    M999
    M7219
    T0
    T1
    T2
    T3
    T4
    T5
    T6


Examples using command_to_arc() function can be found in :doc:`arc module examples<arc>`.
