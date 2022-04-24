#!/bin/bash
python3 -m pip install --upgrade pip
python3 -m venv venv && . venv/bin/activate
python -m pip install -r requirements.txt

clear
python3 - << EOF
s = """
+-------------------------------------------------------+
|                                                       |
|                                                       |
|                                                       |
|                                                       |
|                                                       |
|            Run the 'application' script               |
|                                                       |
|                   ./application                       |
|                                                       |
|                                                       |
|                                                       |
|                                                       |
|                                                       |
+-------------------------------------------------------+
"""
print(s)
EOF