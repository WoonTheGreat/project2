import os
import streamlit as st

# EDA Pkgs
import pandas as pd

# Viz Pkgs
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


def main():
    """ Common ML Dataset Explorer """
    st.title("Dataset Explorer")
    st.subheader("Datasets For ML Explorer with Streamlit")
    # upload CSV file to read data
    uploaded_file = st.file_uploader("Upload CSV file", type=['CSV'])
    st.info("You Selected {}".format(uploaded_file))
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

    if st.checkbox("Show Dataset"):
        st.write(df)

    if st.button("Column Names"):
        st.write(df.columns)

    # Show Shape
    if st.checkbox("Shape of Dataset"):
        data_dim = st.radio("Show Dimension By ", ("Rows", "Columns"))
        if data_dim == 'Rows':
            st.text("Number of Rows")
            st.write(df.shape[0])
        elif data_dim == 'Columns':
            st.text("Number of Columns")
            st.write(df.shape[1])
        else:
            st.write(df.shape)

    if st.checkbox("Select Columns To Show"):
        all_columns = df.columns.tolist()
        selected_columns = st.multiselect("Select", all_columns)
        new_df = df[selected_columns]
        st.dataframe(new_df)

    # Show Summary
    if st.checkbox("Summary"):
        st.write(df.describe().T)

    # Pie Chart
    if st.checkbox("Pie Plot"):
        all_columns_names = df.columns.tolist()
        selected_columns_names = st.multiselect(
            "Select Values", all_columns_names)
        if st.button("Generate Pie Plot"):
            st.success("Generating A Pie Plot".format(selected_columns_names))
            st.write(
                df.iloc[:, -1].value_counts().plot.pie(autopct="%1.1f%%"))
            st.pyplot()

    # Count Plot
    if st.checkbox("Plot of Value Counts"):
        st.text("Value Counts By Target")
        all_columns_names = df.columns.tolist()
        primary_col = st.selectbox(
            "Primary Columm to GroupBy", all_columns_names)
        selected_columns_names = st.multiselect(
            "Select Columns", all_columns_names)
        if st.button("Plot"):
            st.text("Generate Plot")
            if selected_columns_names:
                vc_plot = df.groupby(primary_col)[
                    selected_columns_names].count()
            else:
                vc_plot = df.iloc[:, -1].value_counts()
            st.write(vc_plot.plot(kind="bar"))
            st.pyplot()
        st.set_option('deprecation.showPyplotGlobalUse', False)

    # Customizable Plot

    st.subheader("Customizable Plot")
    all_columns_names = df.columns.tolist()
    type_of_plot = st.selectbox("Select Type of Plot", [
        "area", "bar", "line"])
    selected_columns_names = st.multiselect(
        "Select Columns To Plot", all_columns_names)

    if st.button("Generate Plot"):
        st.success("Generating Customizable Plot of {} for {}".format(
            type_of_plot, selected_columns_names))

        # Plot By Streamlit
        if type_of_plot == 'area':
            cust_data = df[selected_columns_names]
            st.area_chart(cust_data)

        elif type_of_plot == 'bar':
            cust_data = df[selected_columns_names]
            st.bar_chart(cust_data)

        elif type_of_plot == 'line':
            cust_data = df[selected_columns_names]
            st.line_chart(cust_data)


if __name__ == '__main__':
    main()
