import time
from datetime import datetime
from database import get_logs, insert_alerts
from detectors import analyze_log

def main():
    print("--- CyberWatch Security Engine Active ---")
    print("Monitoring database for suspicious events...")
    print("Press Ctrl+C to stop the engine.")

    while True:
        try:
           
            logs = get_logs()
            
            for log in logs:
               
                is_suspicious, rule = analyze_log(log['description'])
                
                if is_suspicious:
                    print(f"[!] THREAT DETECTED: {rule} | Source: {log['source_ip']}")
                    
                    insert_alerts(
                        datetime.now(),
                        log['host_name'],
                        log['user_name'],
                        rule,
                        log['severity'],
                        log['description'],
                        log['source_ip']
    )
            
        except Exception as e:
            print(f"[ERROR] Engine encountered a problem: {e}")
            
       
        time.sleep(10)

if __name__ == "__main__":
    main()