import mysql.connector

jobtracker_db = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'port': 3306,
    'database': 'job_tracker',
}

def connect_db():
    jobtracker_db = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'port': 3306,
    'database': 'job_tracker',}
    conn = mysql.connector.connect(**jobtracker_db)
    
    return  (conn)



# #users
# def save_user(email, password_hash):
#   conn = None
#   cursor = None
#   try:
#     conn = mysql.connector.connect(**jobtracker_db)
#     cursor = conn.cursor()
#     paramforemail = (email,)
#     existing_email_query = '''select email from users where email=%s
#     '''
#     cursor.execute(existing_email_query,paramforemail)
#     data = cursor.fetchone()
#     if data is  None:
      
#      query ='''INSERT INTO users (email, password_hash)
#      VALUES (%s, %s) '''
#      params=(email,password_hash)
#      cursor.execute(query,params)
#      conn.commit()
#      return("user created")
#     else:
#         return("user exists")
#   except Exception as e:
#         return (str(e))  
#   finally:
#        if cursor is not None :
#         cursor.close()
#        if conn is not None: 
#         conn.close()
        
# def login_user(email):
#      conn=None
#      cursor=None
#      try:
#       conn = mysql.connector.connect(**jobtracker_db)
#       cursor = conn.cursor()     
#       query = '''select id,password_hash from users where email=%s'''
#       params=(email,)
#       cursor.execute(query,params)
#       record = cursor.fetchone()
#       return(record)
#      except Exception as e:
#       return(str(e))  
#      finally:
#       if cursor is not None :
#         cursor.close()
#       if conn is not None: 
#        conn.close()
        
      
    
    

#companies
# def save_company(name,website,location):
#   conn = None
#   cursor = None
#   try:
#     conn = mysql.connector.connect(**jobtracker_db)
#     cursor = conn.cursor()
#     query ='''INSERT INTO companies (name, website,location)
#     VALUES (%s, %s,%s) '''
#     params=(name, website,location)
#     cursor.execute(query,params)
#     conn.commit()
#   except Exception as e:
#       return (str(e))  
#   finally:
#     if cursor is not None :
#      cursor.close()
#     if conn is not None: 
#      conn.close()
    
# def delete_company(companyId):
#     conn = mysql.connector.connect(**jobtracker_db)
#     cursor = conn.cursor()
#     query= """update companies set isActive=0,isDeleted=1 where id in ("%s")
#     """
#     params=(companyId,)
#     cursor.execute(query,params)
#     conn.commit()
#     cursor.close()
#     conn.close()
    
# def update_company(companyName,companyLocation,companySite,companyId):
#   conn = None
#   cursor = None
#   try:
#     conn = mysql.connector.connect(**jobtracker_db)
#     cursor = conn.cursor()
#     query= """update companies set name=(%s),location=(%s),website=(%s) where id = (%s)
#     """
#     params=(companyName,companyLocation,companySite,companyId)
#     cursor.execute(query,params)
#     conn.commit()
#   except Exception as e:
#       return e
#   finally:
#     if cursor is not None :
#      cursor.close()
#     if conn is not None: 
#      conn.close()
    
       
# def show_company(): 
#   conn = None
#   cursor = None    
#   try:   
#     conn = mysql.connector.connect(**jobtracker_db)
#     cursor = conn.cursor()
#     query= """select*from companies order by id desc
#     """
#     cursor.execute(query,)
#     data = cursor.fetchall()
#     return(data)
#   except Exception as e:
#       return e
#   finally:
#     if cursor is not None :
#      cursor.close()
#     if conn is not None: 
#      conn.close()
    
    
    
       
    
    
#applications    
# def save_application(userid,companyid,statusid,jobtitle,appliedAt,jobUrl):
#     conn = mysql.connector.connect(**jobtracker_db)
#     cursor = conn.cursor()
#     query = """
#     INSERT INTO applications
#     (user_id, company_id, status_id, role_title, applied_date, job_url)
#     VALUES (%s, %s, %s, %s, %s, %s)
#     """
#     params=(userid,companyid,statusid,jobtitle,appliedAt,jobUrl)
#     cursor.execute(query,params)
#     conn.commit()
#     cursor.close()
#     conn.close()
    
# def show_applications(user_id):
#     query="""select a.id,a.role_title,c.name as companyName,a.applied_date,s.name as appStatus from applications a
#     join application_statuses s on a.status_id=s.id
#     join companies c on a.company_id=c.id where a.user_id =%s
#     order by a.id desc;"""
#     params=(user_id,)
#     conn = mysql.connector.connect(**jobtracker_db)
#     cursor = conn.cursor()
#     cursor.execute(query,params)
#     data = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return(data)

# def update_application_status(application_id, new_status_id,user_id):
#     conn = mysql.connector.connect(**jobtracker_db)
#     cursor = conn.cursor()
#     query = "UPDATE applications SET status_id = %s WHERE id = %s and user_id=%s"
#     params = (new_status_id, application_id,user_id)
#     cursor.execute(query, params)
#     conn.commit()
#     cursor.close()
#     conn.close()
    
# def delete_application(application_id,userId):
#     conn = mysql.connector.connect(**jobtracker_db)
#     cursor = conn.cursor()
#     query = "UPDATE applications SET isActive=0,isDeleted=1 WHERE id = %s and user_id=%s"
#     params = ( application_id,userId)
#     cursor.execute(query, params)
#     conn.commit()
#     cursor.close()
#     conn.close()   
    
