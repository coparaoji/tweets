import sqlite3

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn
def create_team(conn, team):
    """
    Create a new project into the projects table
    :param conn:
    :param team:
    :return: project id
    """
    sql = ''' INSERT INTO team(team_name,num_tweets,score)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, team)
    conn.commit()
    return cur.lastrowid

    
def create_team(conn, team):
    """
    Create a new project into the projects table
    :param conn:
    :param team:
    :return: project id
    """
    sql = ''' INSERT INTO team(team_name,num_tweets,score)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, team)
    conn.commit()
    return cur.lastrowid


def create_player(conn, player):
    """
    Create a new task
    :param conn:
    :param player:
    :return:
    """

    sql = ''' INSERT INTO player(number,name,team_name,player_id)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, player)
    conn.commit()
    return cur.lastrowid

def create_tweet(conn, tweet):
    """
    Create a new task.
    :param conn:
    :param tweet:
    :return:
    """

    sql = ''' INSERT INTO tweet(unique_id,tweet_id,player_id,text,score,magnitude,resultant,created_at)
              VALUES(?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, tweet)
    conn.commit()
    return cur.lastrowid

def create_tweets(conn, tweets):
    for tweet in tweets:
        create_tweet(conn,tweet)


def get_players():
    database = "/home/alex/GreyCroc/tweets/db/tweets.db"
    conn =  create_connection(database)
    sql_query = '''SELECT name,player_id FROM player'''
    cursor = conn.cursor()
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    rows = list(map((lambda x:(x[0],x[1])), rows))
    return rows


def get_data():
   database = "/home/alex/GreyCroc/tweets/db/tweets.db"
   conn =  create_connection(database)
   sql_query = '''SELECT number,name,num_tweets,res_avg FROM player'''
   cursor = conn.cursor()
   cursor.execute(sql_query)
   rows = cursor.fetchall()
   return rows