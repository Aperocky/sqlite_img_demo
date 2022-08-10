## Demo Sqlitedao App

This is an survey webapp where different images will be graded by different responders.

## Guide

Install Dependencies:

    pip install flask
    pip install sqlitedao

Run:

    python main.py

This will create a file `data.db` with randomly generated mock data. Subsequent runs will not overwrite the data unless this file is deleted.

Peek into data:

    sqlite3 data.db
    > select * from users;
    > select * from images;
    > select * from user_images;

Web Portal:

    http://0.0.0.0:5001
