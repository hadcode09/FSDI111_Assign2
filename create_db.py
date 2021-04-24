#!/usr/bin/env python3
#-*- coding: utf8 -*-
"""Ceate database tables from SQLAchemy classes"""

from app import db

if __name__== "__main__":
    db.create_all()
