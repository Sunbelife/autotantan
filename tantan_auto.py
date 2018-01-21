# -*- coding: utf-8 -*-

import os
import shutil
import time
import math
import random
import json
import wda

c = wda.Client()
s = c.session()

def main():
    for i in range(1, 120):
        print("已点" + str(i) + "个")
        s(name=u'home user like button', className='Button').tap()

if __name__ == '__main__':
    main()
