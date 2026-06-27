import mysql.connector

jobtracker_db = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'port': 3306,
    'database': 'job_tracker',
}


#users
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
    
    

#companies
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
    
def delete_company(companyId):
    conn = mysql.connector.connect(**jobtracker_db)
    cursor = conn.cursor()
    query= """update companies set isActive=0,isDeleted=1 where id in ("%s")
    """
    params=(companyId,)
    cursor.execute(query,params)
    conn.commit()
    cursor.close()
    conn.close()
    
def update_company(companyName,companyLocation,companySite,companyId):
    conn = mysql.connector.connect(**jobtracker_db)
    cursor = conn.cursor()
    query= """update companies set name=(%s),location=(%s),website=(%s) where id = (%s)
    """
    params=(companyName,companyLocation,companySite,companyId)
    cursor.execute(query,params)
    conn.commit()
    cursor.close()
    conn.close()
    
       
def show_company():        
    conn = mysql.connector.connect(**jobtracker_db)
    cursor = conn.cursor()
    query= """select*from companies order by id desc
    """
    cursor.execute(query,)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return(data)
    
    
       
    
    
#applications    
def save_application(userid,companyid,statusid,jobtitle,appliedAt,jobUrl):
    conn = mysql.connector.connect(**jobtracker_db)
    cursor = conn.cursor()
    query = """
    INSERT INTO applications
    (user_id, company_id, status_id, role_title, applied_date, job_url)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    params=(userid,companyid,statusid,jobtitle,appliedAt,jobUrl)
    cursor.execute(query,params)
    conn.commit()
    cursor.close()
    conn.close()
    
def show_applications():
    query="""select a.id,a.role_title,c.name as companyName,a.applied_date,s.name as appStatus from applications a
    join application_statuses s on a.status_id=s.id
    join companies c on a.company_id=c.id
    order by a.id desc;"""
    conn = mysql.connector.connect(**jobtracker_db)
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return(data)

def update_application_status(application_id, new_status_id):
    conn = mysql.connector.connect(**jobtracker_db)
    cursor = conn.cursor()
    query = "UPDATE applications SET status_id = %s WHERE id = %s"
    params = (new_status_id, application_id)
    cursor.execute(query, params)
    conn.commit()
    cursor.close()
    conn.close()
    
def delete_application(application_id):
    conn = mysql.connector.connect(**jobtracker_db)
    cursor = conn.cursor()
    query = "UPDATE applications SET isActive=0,isDeleted=1 WHERE id = %s"
    params = ( application_id,)
    cursor.execute(query, params)
    conn.commit()
    cursor.close()
    conn.close()   