import mysql.connector

jobtracker_db = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'port': 3306,
    'database': 'job_tracker',
}

def save_user(email, password_hash):
    conn = mysql.connector.connect(**jobtracker_db)
    cursor = conn.cursor()
    query ='''INSERT INTO users (email, password_hash)
    VALUES (%s, %s) '''
    params=(email,password_hash)
    cursor.execute(query,params)
    conn.commit()
    cursor.close()
    conn.close()


def save_company(name,website,location):
    conn = mysql.connector.connect(**jobtracker_db)
    cursor = conn.cursor()
    query ='''INSERT INTO companies (name, website,location)
    VALUES (%s, %s,%s) '''
    params=(name, website,location)
    cursor.execute(query,params)
    conn.commit()
    cursor.close()
    conn.close()
    
def save_application(userid,companyid,statusid,jobtitle,appliedAt,jobUrl):
    conn = mysql.connector.connect(**jobtracker_db)
    cursor = conn.cursor()
    query ='''INSERT INTO companies (userid,companyid,statusid,jobtitle,appliedAt,jobUrl)
    VALUES (%s, %s,%s,%s,%s,%s) '''
    params=(userid,companyid,statusid,jobtitle,appliedAt,jobUrl)
    cursor.execute(query,params)
    conn.commit()
    cursor.close()
    conn.close()