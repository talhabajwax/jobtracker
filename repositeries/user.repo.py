from database import connect_db


def save_user(email, password_hash):
  conn = None
  cursor = None
  try:
    conn = connect_db()
    cursor = conn.cursor()
    paramforemail = (email,)
    existing_email_query = '''select email from users where email=%s
    '''
    cursor.execute(existing_email_query,paramforemail)
    data = cursor.fetchone()
    if data is  None:
      
     query ='''INSERT INTO users (email, password_hash)
     VALUES (%s, %s) '''
     params=(email,password_hash)
     cursor.execute(query,params)
     conn.commit()
     return("user created")
    else:
        return("user exists")
  except Exception as e:
        return (str(e))  
  finally:
       if cursor is not None :
        cursor.close()
       if conn is not None: 
        conn.close()
        
def login_user(email):
     conn=None
     cursor=None
     try:
      conn = connect_db()
      cursor = conn.cursor()     
      query = '''select id,password_hash from users where email=%s'''
      params=(email,)
      cursor.execute(query,params)
      record = cursor.fetchone()
      return(record)
     except Exception as e:
      return(str(e))  
     finally:
      if cursor is not None :
        cursor.close()
      if conn is not None: 
       conn.close()