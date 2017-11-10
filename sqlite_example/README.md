# SQLite example

This is a script from a project that I ended up throwing away but
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
