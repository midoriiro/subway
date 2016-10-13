# MIT License

# Copyright (c) 2016 Alexis Bekhdadi (midoriiro) <contact@smartsoftwa.re>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

Feature: Process

    Scenario: Read 100 lines
        Given   select local repeater.py
        And     arguments -n 100
        When    set stdout as pipe
        And     set stderr as pipe
        And     set stdin as pipe
        Then    create process
        And     run a blocking call
        And     exit status equal to 0
        And     stdout lines count equal to 100
        And     stderr is empty

    Scenario: Argument error
        Given   select local repeater.py
        And     arguments -n -100
        When    set stdout as pipe
        And     set stderr as pipe
        And     set stdin as pipe
        Then    create process
        And     run a blocking call
        And     exit status equal to 1
        And     stderr lines count equal to 1
        And     stdout is empty

    Scenario: Write command interactively
        Given   select local repeater.py
        And     arguments -i
        When    set stdout as pipe
        And     set stderr as pipe
        And     set stdin as pipe
        Then    create process
        And     run a non-blocking call
        And     send data 100
        And     stdout lines count equal to 100
        And     clear buffers
        And     send data -10
        And     stderr lines count equal to 1
        And     clear buffers
        And     send data exit
        And     exit status equal to 2
        And     stdout is empty
        And     stderr is empty
        And     stdin is not empty
