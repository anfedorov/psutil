#!/usr/bin/env python
#
# $Id$
#
# Copyright (c) 2009, Jay Loden, Giampaolo Rodola'. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
A clone of 'free' cmdline utility.
"""

import psutil
from psutil._compat import print_

def main():
    virt = psutil.virtual_memory()
    swap = psutil.swap_memory()
    templ = "%-7s %10s %10s %10s %10s %10s %10s"
    print_(templ % ('', 'total', 'used', 'free', 'shared', 'buffers', 'cache'))
    print_(templ % ('Mem:', virt.total / 1024,
                            virt.used / 1024,
                            virt.free / 1024,
                            getattr(virt, 'shared', 0) / 1024,
                            getattr(virt, 'buffers', 0) / 1024,
                            getattr(virt, 'cached', 0) / 1024))
    print_(templ % ('Swap:', swap.total / 1024,
                             swap.used / 1024,
                             swap.free / 1024,
                             '', '', ''))

if __name__ == '__main__':
    main()
