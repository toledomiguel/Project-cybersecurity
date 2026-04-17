def analyze_log(description):
    """
    Analyzes log descriptions to identify security threats.
    Returns: (is_suspicious, rule_name)
    """
    desc = description.lower()
    
    if "failed" in desc or "invalid password" in desc:
        return True, "Brute Force Attempt"
    
    if "select" in desc or "union" in desc or "drop table" in desc:
        return True, "SQL Injection Detected"
    
    if "unauthorized" in desc or "denied" in desc:
        return True, "Unauthorized Access"

    return False, None