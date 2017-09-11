#!/usr/bin/env python

import psycopg2

DBNAME = "news"


q1_query = """select title, count(*) as total_views
            from articles left join log
            on log.path=concat('/article/', articles.slug)
            group by articles.title
            order by total_views desc limit 3"""

q2_query = """select name, auth_total
            from (select author, sum(total_views) as auth_total
                from (select title, count(*) as total_views
                    from articles left join log
                    on log.path=concat('/article/', articles.slug)
                    group by articles.title
                    order by total_views desc) as art_views, articles
                where articles.title = art_views.title
                group by author) as atotal, authors
            where authors.id = atotal.author
            order by auth_total desc"""

q3_query = """select * from
            (select date, (sum(log_errors.error)/count(*)::real) as error_rate
            from
            (select date(time), (case when status = '200 OK' then 0 else 1 end)
            as error from log) as log_errors
            group by date
            order by date asc) as over1
            where error_rate > 0.01;"""


def get_query(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    return c.fetchall()
    db.close()


def question1(query):
    results = get_query(query)
    print('\nThe 3 most popular articles are:')
    for x in results:
        print x[0], "-", x[1], "views"


def question2(query):
    results = get_query(query)
    print('\nRanked by popularity, the authors are:')
    for x in results:
        print x[0], "-", x[1], "views"


def question3(query):
    results = get_query(query)
    print "\nDay(s) where more than 1% of requests led to errors:"
    for x in results:
        print x[0].strftime("%B %-d, %Y"), "-", "{:.3%}".format(x[1]), "\n"


question1(q1_query)
question2(q2_query)
question3(q3_query)
