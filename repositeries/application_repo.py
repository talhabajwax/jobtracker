from database import connect_db



def save_application(user_id,company_id,status_id,jobtitle,appliedAt,jobUrl):
   conn=None
   cursor=None
   try:
    conn = connect_db()
    cursor = conn.cursor()
    query = """
    INSERT INTO applications
    (user_id, company_id, status_id, role_title, applied_date, job_url)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    params=(user_id,company_id,status_id,jobtitle,appliedAt,jobUrl)
    cursor.execute(query,params)
    conn.commit()
    new_app_id=cursor.lastrowid
    return(new_app_id)
   finally:
    if cursor is not None :
     cursor.close()
    if conn is not None: 
     conn.close()
    
def show_applications(user_id):
   conn=None
   cursor=None
   try:    
    query="""select a.id,a.role_title,c.name as companyName,a.applied_date,s.name as appStatus from applications a
    join application_statuses s on a.status_id=s.id
    join companies c on a.company_id=c.id where a.user_id =%s
    order by a.id desc;"""
    params=(user_id,)
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query,params)
    data = cursor.fetchall()
    return(data)
   finally:
    if cursor is not None :
     cursor.close()
    if conn is not None: 
     conn.close()
     

def update_application_status(application_id, new_status_id,user_id):
   conn=None
   cursor=None
   try:    
    conn = connect_db()
    cursor = conn.cursor()
    query = "UPDATE applications SET status_id = %s WHERE id = %s and user_id=%s and isActive=1 and isDeleted=0"
    params = (new_status_id, application_id,user_id)
    cursor.execute(query, params)
    conn.commit()
    affected_rows=cursor.rowcount
    return(affected_rows)
   finally:
    if cursor is not None :
     cursor.close()
    if conn is not None: 
     conn.close()
     
     
     
def delete_application(application_id,user_id):
   conn = None
   cursor = None
   try:
    conn = connect_db()
    cursor = conn.cursor()
    query = "UPDATE applications SET isActive=0,isDeleted=1 WHERE id = %s and user_id=%s"
    params = ( application_id,user_id)
    cursor.execute(query, params)
    conn.commit()
    affected_rows=cursor.rowcount
    return(affected_rows)

   finally:
    if cursor is not None :
     cursor.close()
    if conn is not None: 
     conn.close()
     
     
def get_application(application_id,user_id):
   conn = None
   cursor = None
   try:
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT * FROM applications WHERE id = %s and user_id=%s and isActive=1 and isDeleted=0"
    params = ( application_id,user_id)
    cursor.execute(query, params)
    application=cursor.fetchone()
    return(application)

   finally:
    if cursor is not None :
     cursor.close()
    if conn is not None: 
     conn.close()

def duplicate_application(user_id,company_id,jobtitle):
   conn = None
   cursor = None
   try:
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT id FROM applications WHERE user_id=%s and company_id=%s and role_title=%s and isActive=1 and isDeleted=0"
    params = (user_id,company_id,jobtitle)
    cursor.execute(query, params)
    application=cursor.fetchone()
    return(application)

   finally:
    if cursor is not None :
     cursor.close()
    if conn is not None: 
     conn.close()