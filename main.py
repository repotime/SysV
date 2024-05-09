import streamlit as st
import system
import time

def main():
    st.set_page_config(page_title="SysV - System Monitor", layout="wide")

    # Create a row with columns
    col1, col2 = st.columns([8, 2])  # Adjust the ratio as needed for your layout

    # Title in the first column
    with col1:
        st.markdown("""
        <style>
        .big-font {
            font-size:30px !important;
            font-weight: bold;
        }
        </style>
        <p class='big-font'>System Resource Monitor</p>
        """, unsafe_allow_html=True)

    # Button in the second column
    with col2:
        # Use a little CSS to vertically align the button
        st.markdown("""
        <style>
        div.stButton > button:first-child {
            display: inline-block;
            vertical-align: middle;
        }
        </style>
        """, unsafe_allow_html=True)
        if st.button('Refresh Data'):
            st.experimental_rerun()
    
    uptime = system.get_system_uptime()  # Fetching system uptime
    st.text("System Uptime: " + uptime['uptime'])
    
    st.markdown('<br><br>', unsafe_allow_html=True)

    if 'init' not in st.session_state:
        st.session_state['init'] = True
        time.sleep(1)  # Delay to simulate real-time updates
        st.rerun()

    # Layout using columns
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.subheader("Kernel Information")
        kernel_info = system.get_kernel_info()  # Fetching kernel info
        uptime = system.get_system_uptime()  # Fetching system uptime
        st.json(kernel_info)
        
        st.subheader("Process Information")
        processes = system.get_process_info()
        st.json(processes)

    with col2:
        st.subheader("CPU Information")
        cpu_info = system.get_cpu_info()  # Fetching CPU info
        st.json(cpu_info)

    with col3:
        st.subheader("Memory Information")
        memory_info = system.get_memory_info()  # Fetching memory info
        st.json(memory_info)
        
        st.subheader("Load Average")
        load_avg = system.get_load_average()  # Fetching load average
        st.json(load_avg)
        
    with col4:
        st.subheader("Network Traffic")
        network_info = system.get_network_info()  # Fetching network info
        st.json(network_info)
        
        st.subheader("Disk I/O Counters")
        disk_io_counters = system.get_disk_io_counters()
        st.json(disk_io_counters)
        
    with col5:
        st.subheader("Disk Information")
        disk_info = system.get_disk_info()  # Fetching disk info
        st.json(disk_info)
        
        
if __name__ == "__main__":
    main()
