#!/usr/bin/env python3
#-*- coding: utf8 -*-
"""Sample python code that creates users and displays then"""

from app import db, User

def create_my_user(first_name, last_name, hobbies):
    """Simple user creation function"""
    db.session.add(
        User(
            first_name=first_name,
            last_name=last_name,
            hobbies=hobbies
        )
    )
    db.session.commit()

if __name__ == "__main__":
    create_my_user("M.A", "Hadley", "Gaming & Coding")
    users = User.query.all()
    print(users)
    create_my_user("John", "Doe", "Golfing")
    user = User.query.filter_by(first_name="John").first()
    print(user)