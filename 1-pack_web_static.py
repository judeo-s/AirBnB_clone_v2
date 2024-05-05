#!/usr/bin/python3
"""Generates a Compress (tgz) archive"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Function to compress files"""
    local("mkdir -p versions")
    result = local("tar -czvf versions/web_static_{}.tgz web_static"
                   .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    if result.failed:
        return None
    return result
