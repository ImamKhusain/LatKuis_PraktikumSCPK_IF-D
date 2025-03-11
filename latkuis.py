import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset yang sudah dibersihkan
data_path = "Air_Traffic_Passenger_Statistics_Cleaned.csv"
data = pd.read_csv(data_path)

# Konversi Activity Period ke format datetime agar bisa difilter
data['Activity Period'] = pd.to_datetime(data['Activity Period'], format='%Y%m')

def main():
    st.title("Dashboard Analisis Data Air Traffic Passenger Statistics")
    st.sidebar.header("Navigasi")
    
    tab1, tab2, tab3, tab4 = st.tabs(["Informasi", "Dataset", "Visualisasi", "Filter Data"])
    
    with tab1:
        st.subheader("Informasi Praktikan")
        st.write("**Nama:** Imam Khusain")
        st.write("**NIM:** 123230018")
        st.write("**Kelas:** IF-D")
    
    with tab2:
        st.subheader("Dataset - Air Traffic Passenger Statistics")
        st.write("Berikut adalah dataset hasil preprocessing:")
        st.dataframe(data)
    
    with tab3:
        st.subheader("Visualisasi Data")
        if st.button("Tampilkan Bar Plot"):
            top_airlines = data.groupby('Operating Airline')['Passenger Count'].sum().reset_index()
            top_airlines = top_airlines.sort_values('Operating Airline').head(10)
            
            fig, ax = plt.subplots()
            ax.bar(top_airlines['Operating Airline'], top_airlines['Passenger Count'], color='skyblue')
            ax.set_xlabel("Operating Airline")
            ax.set_ylabel("Passenger Count")
            ax.set_title("Top 10 Operating Airlines")
            plt.xticks(rotation=45)
            st.pyplot(fig)
        
        if st.button("Tampilkan Pie Chart"):
            geo_summary = data['GEO Summary'].value_counts()
            
            fig, ax = plt.subplots()
            ax.pie(geo_summary, labels=geo_summary.index, autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
            ax.set_title("Distribution of Geo Summary")
            st.pyplot(fig)
    
    with tab4:
        st.subheader("Filter Data - Line Plot")
        min_year = st.number_input("Tahun Minimum", min_value=data['Activity Period'].dt.year.min(), 
                                    max_value=data['Activity Period'].dt.year.max(), 
                                    value=data['Activity Period'].dt.year.min())
        max_year = st.number_input("Tahun Maksimum", min_value=data['Activity Period'].dt.year.min(), 
                                    max_value=data['Activity Period'].dt.year.max(), 
                                    value=data['Activity Period'].dt.year.max())
        
        if st.button("Tampilkan Line Plot"):
            filtered_data = data[(data['Activity Period'].dt.year >= min_year) & (data['Activity Period'].dt.year <= max_year)]
            activity_summary = filtered_data.groupby('Activity Period')['Passenger Count'].sum().reset_index()
            
            fig, ax = plt.subplots()
            ax.plot(activity_summary['Activity Period'], activity_summary['Passenger Count'], marker='o', linestyle='-')
            ax.set_xlabel("Activity Period")
            ax.set_ylabel("Passenger Count")
            ax.set_title("Passenger Count Over Time")
            plt.xticks(rotation=45)
            st.pyplot(fig)

if __name__ == "__main__":
    main()