"""
I want to get into more python stuff

This project is all about sql integration with python & Pycharm Professional IDE

Author: Franzlombao
GIT: github.com/franzlom

Use Cases:
    * Data Fits in memory
    * volume of data not a a performance issue
    * Ease of using sql
    * Don't need a fully functional SQL Server database

From:
    https://github.com/yhat/pandasql/tree/master/examples
"""

import pandas as pd
from pandasql import sqldf
from pandasql import load_births


def run(births):
    """
    main run method
    :return: None
    """
    # print(births)

    print(sqldf(
        'SELECT * FROM births where births > 250000 limit 5;',
        locals()
    ))

    # its complaining (pycharm professional IDE
    # cause its looking for a DB
    # which we are importing from pandasql from yHat

    # drop the time from date
    query = """
        SELECT
            date(date) as DOB,
            Sum(births) as "Total Births"
        FROM
            births
        group by
            date limit 10;
    """

    print('new query')
    # print(sqldf(query, locals()))

    # Using the new method pysql
    print(pysqldf(query))


def initialise():
    """
    initialise the db
    :return: sql_imports
    """
    births = load_births()
    return births


def pysqldf(q):
    """
    To drop adding locals to the end of query
    :param q: sql query
    :return: query response
    """
    # locals() = local variables
    # globals() = global variables
    return sqldf(q, globals())


if __name__ == "__main__":
    births = initialise()
    run(births)
