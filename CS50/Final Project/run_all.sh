#!/bin/env bash

python classifier.py Images/Live Live_test.txt
python classifier.py Images/Dead Dead_test.txt
python classifier.py Images/Live_No_Test Live_no_test.txt
python classifier.py Images/Dead_No_Test Dead_no_test.txt
