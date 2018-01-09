#!/usr/bin/env python3

import sqlite3
import pandas
from random import *

""" This is a script from a project that I ended up throwing away but
might be useful in future.

The use case is: if you need to compute many scores and write them
to disk, and if computation is expensive so you don't want to re-run computations
that you've already done.  Writing to .csv doesn't work well here
because it's difficult to do partial writes.  Writing to individual files
for each score would work but it's clunky.  sqlite gives you a simple SQL
database in one file which works very well.

The script sets up a simple sqlite database on disk as a "DB" class and
provides three methods: score_exists(), write_score(), and scores_to_csv().
You have to change the DB class around so the table and keys are appropriate
to your application.

The script is executable and includes a main method with an example
computation run, whcih computes a set of scores, and exports to .csv.

Usage:

    ./sqlite_script.py

It will generate scores.csv and scores.sqlite.  The first time you run it,
it will compute all the scores.  On subsequent runs, it will read from
scores.sqlite and compute only those scores that are missing.

"""


class DB(object):
    def __init__(self):
        self.sqlite_file = 'scores.sqlite'
        self.conn = sqlite3.connect(self.sqlite_file)
        self.conn.execute('create table if not exists scores(destination TEXT, keyword TEXT, score NUMERIC)')
        self.conn.commit()
        self.conn.execute('create unique index if not exists myindex on scores(destination,keyword)')
        self.conn.commit()

    def score_exists(self, destination, keyword):
        n_row = self.conn.execute('select count(*) from scores where destination="' + \
            destination + '" and keyword="' + keyword + '"').fetchall()[0][0]
        return(n_row>0)

    def write_score(self, destination, keyword, score):
        self.conn.execute("REPLACE INTO scores (destination, keyword, score) " + \
            "VALUES ('" + destination + "', '" + keyword + "', " + str(score) + ")")
        self.conn.commit()

    def scores_to_csv(self, csv_file):
        table = pandas.read_sql('select * from scores', self.conn)
        table.to_csv(csv_file, index=False)


def write_score(destination, keyword, db):
    if not db.score_exists(destination, keyword):
        print("Computing: " + destination + ", " + keyword)
        score = random() # replace with your own function here
        db.write_score(destination, keyword, score)


def main():
    # todo: load destinations from Impala
    db = DB()
    destinations = ['London', 'Berlin', 'Hurghada', 'Mallorca', 'Paris', 'New York', 'Ibiza', 'Barcelona']
    keywords = ['beach', 'ski', 'hiking', 'diving', 'mountain', 'forest', 'city', 'museum', 'island', 'culture']
    for d in destinations:
        for k in keywords:
            write_score(d,k, db)
    db.scores_to_csv('scores.csv')

if __name__== "__main__":
    main()
