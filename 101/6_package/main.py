#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sound.echo
from graphic import render

# intellij 의 경우 Ctrl+Alt+Shift+S 를 눌러 Modules 항목에서 6_package 를 추가한다.
if __name__ == '__main__':
    sound.echo.echo_test()
    render.render_test()
