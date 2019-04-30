import os
import pprint
import sqlite3
from collections import namedtuple


def add_payment(db, debit, credit, dollars, memo):
    db.cursor().execute('INSERT INTO payment (debit, credit, dollars, memo)'
                        'VALUES (?, ?, ?, ?)', (debit, credit, dollars, memo))


def get_payments_of(db, account):
    c = db.cursor()
    c.execute('SELECT * FROM payment  WHERE credit = ? or debit = ?'
              ' ORDER BY id', (account, account))
    Row = namedtuple('Row', [tup[0] for tup in c.description])
    return [Row(*row) for row in c.fetchall()]


def open_database(path='bank.db'):
    new = not os.path.exists(path)
    db = sqlite3.connect(path)
    if new:
        c = db.cursor()
        c.execute('CREATE TABLE payment (id INTEGER PRIMARY KEY,'
                  'debit TEXT, credit TEXT, dollars INTEGER, memo TEXT)')
        add_payment(db, 'brandon', 'psf', 125, 'Registration for PyCon kek')
        add_payment(db, 'brandon', 'sfg', 200, 'Payment for writing kek')
        add_payment(db, 'brandon', 'psf', 125, 'Registration for PyCon kek')
        db.commit()
        print('Successfully created table!')
    return db


if __name__ == '__main__':
    db = open_database()
    pprint.pprint(get_payments_of(db, 'brandon'))

