#!/usr/bin env python3
import os
import sys

import application


sys.path.append(os.path.dirname(os.path.abspath(__file__)))


if __name__ == '__main__':
    app = application.Application()
    app.main()
