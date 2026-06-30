from database import connect_db



def save_application(userid,companyid,statusid,jobtitle,appliedAt,jobUrl):
    conn = connect_db()
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
    
def show_applications(user_id):
    query="""select a.id,a.role_title,c.name as companyName,a.applied_date,s.name as appStatus from applications a
    join application_statuses s on a.status_id=s.id
    join companies c on a.company_id=c.id where a.user_id =%s
    order by a.id desc;"""
    params=(user_id,)
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query,params)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return(data)

def update_application_status(application_id, new_status_id,user_id):
    conn = connect_db()
    cursor = conn.cursor()
    query = "UPDATE applications SET status_id = %s WHERE id = %s and user_id=%s"
    params = (new_status_id, application_id,user_id)
    cursor.execute(query, params)
    conn.commit()
    cursor.close()
    conn.close()
    
def delete_application(application_id,userId):
   try:
    conn = connect_db()
    cursor = conn.cursor()
    query = "UPDATE applications SET isActive=0,isDeleted=1 WHERE id = %s and user_id=%s"
    params = ( application_id,userId)
    cursor.execute(query, params)
    conn.commit()
   except Exception as e:
      return (str(e))  
   finally:
    if cursor is not None :
     cursor.close()
    if conn is not None: 
     conn.close()
