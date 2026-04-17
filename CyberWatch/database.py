import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="projeto",
        user="root",
        password="",
        database="cyberwatch"
    )
def get_logs():
    conm:get_connection()
    cursor:conm.cursor(dictionary=true)

    cursor.execute("SELECT * FROM logs ORDER BY event_time DESC")
    rows = cursor.fetchall()
    
    cursor.close()
    conm.close()

    return rows
def insert_alerts(alert_time, host_name, user_name, rule_name, severity, description, source_ip):
    conm = get_connection()
    cursor = conm.cursor()

    query = """
        INSERT INTO alerts
        (alert_time, host_name, user_name, severity, description, source_ip)
        values
        (%s, %s, %s, %s, %s, %s, %s)
        """

    values = (
        alert_time,
        host_name,
        user_name,
        severity,
        description,
        source_ip
    )
    cursor.execute(query, values)
    conm.commit()
    
    cursor.close()
    conm.close()
def get_alerts():
    conm = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM alerts ORDER BY alert_time DESC")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows
def clear_alerts():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM alerts")
    conn.commit()

    cursor.close()
    conn.close()