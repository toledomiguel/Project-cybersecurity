import streamlit as st
import pandas as pd
from database import get_alerts 


st.set_page_config(page_title="CyberWatch Dashboard", layout="wide")

st.title("🛡️ CyberWatch - Security Monitoring")
st.markdown("Real-time analysis of detected threats")


if st.sidebar.button('Refresh Data'):
    st.rerun()


try:
    data = get_alerts()
    df = pd.DataFrame(data)

    if not df.empty:
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Alerts", len(df))
        col2.metric("Critical Threats", len(df[df['severity'] == 'High']))
        col3.metric("Last Source IP", df['source_ip'].iloc[0])

        
        st.subheader("Threat Distribution")
        chart_data = df['rule_name'].value_counts()
        st.bar_chart(chart_data)

        
        st.subheader("Recent Alert Logs")
        st.dataframe(df, use_container_width=True)
    else:
        st.write("No alerts detected yet. Monitoring is active...")

except Exception as e:
    st.error(f"Error connecting to Dashboard: {e}")