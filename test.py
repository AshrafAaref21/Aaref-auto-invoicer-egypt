import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import os
import glob
import json
import os
from bs4 import BeautifulSoup


img = Image.open("aaref.jpg")

st.set_page_config(
    page_title="Auto Invoice",
    page_icon=img,
    layout="wide",
    initial_sidebar_state="expanded",
    )


st.header('Egyptian Invoices Automation\nMade by Eng\\ ***Ashraf Aaref***')
st.divider()


s_p = st.selectbox('Select Invoices Type',['Procurements', 'Sales'])
st.divider()

if s_p == 'Procurements':
        
    uploaded_files = st.file_uploader('Upload your Invoices (Accept Json Formating Only)',
                                    type='json',
                                    accept_multiple_files= True,
                                     )




    if uploaded_files is not None:
        
        ls = []
        dic = {
                'Reciever ID': None,#data['receiverId'],
                'Internal ID': None,#data['internalId'],
                'Reciever Name': None,#u"{}".format(str(data['receiverName'])),
                'DateTime Issued': None,#data['dateTimeIssued'][:10] ,
                'DateTime Received': None,#data['dateTimeReceived'][:10],
                'Total Sales (EGP)': None,#data['totalSales'],
                'Total discount (EGP)': None,#data['totalDiscount'],
                'Total Items Discount (EGP)': None,#float(doc_data.html.body.document.totaldiscountamount.text),
                'Value added tax (EGP)': None,#float(doc_data.html.body.document.find_all('taxableitems')[-1].amount.text),
                'Extra Invoice Discounts (EGP)': None,#float(doc_data.html.body.document.extradiscountamount.text),
                'Total Amount (EGP)': None,#data['total'],


        }
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            # st.write("filename:", uploaded_file.name)
            # st.write(bytes_data)
            # f = open(bytes_data,encoding='utf-8')
            data = json.loads(bytes_data)

            dic['Reciever ID'] = data['receiverId']
            dic['Internal ID'] = data['internalId']
            dic['Reciever Name'] = u"{}".format(str(data['receiverName']))
            dic['DateTime Issued'] = data['dateTimeIssued'][:10]
            dic['DateTime Received'] = data['dateTimeReceived'][:10]
            dic['Total Sales (EGP)'] = data['totalSales']
            dic['Total discount (EGP)'] = data['totalDiscount']

            dic['Total Amount (EGP)'] = data['total']

            try:
                doc_data = BeautifulSoup(data['document'])

                dic['Total Items Discount (EGP)'] = float(doc_data.html.body.document.totaldiscountamount.text)
                dic['Value added tax (EGP)'] = float(doc_data.html.body.document.find_all('taxableitems')[-1].amount.text)
                dic['Extra Invoice Discounts (EGP)'] = float(doc_data.html.body.document.extradiscountamount.text)
                dic['Total Amount (EGP)'] = data['total']
    
                


            except:
                doc_data = json.loads(str(BeautifulSoup(data['document'], 'html.parser')))

                dic['Total Items Discount (EGP)'] = doc_data['totalItemsDiscountAmount']
                dic['Extra Invoice Discounts (EGP)'] =  doc_data['extraDiscountAmount']

                try:
                    dic['Value added tax (EGP)'] = doc_data['taxTotals'][0]['amount']

                except IndexError:
                    dic['Value added tax (EGP)'] = 0
                # st.write(doc_data)

            

            ls.append(dic)


        df = pd.DataFrame.from_records(ls)

        btn = st.download_button(
            "Press to Download",
            df.to_csv(index=False),
            "Aaref.csv",
            "text/csv",
            key='download-csv')
        



elif s_p == 'Sales':
        
    uploaded_files = st.file_uploader('Upload your Invoices (Accept Json Formating Only)',
                                    type='json',
                                    accept_multiple_files= True,
                                     )




    if uploaded_files is not None:
        
        ls = []
        dic = {
                'Reciever ID': None,#data['receiverId'],
                'Internal ID': None,#data['internalId'],
                'Reciever Name': None,#u"{}".format(str(data['receiverName'])),
                'DateTime Issued': None,#data['dateTimeIssued'][:10] ,
                'DateTime Received': None,#data['dateTimeReceived'][:10],
                'Total Sales (EGP)': None,#data['totalSales'],
                'Total discount (EGP)': None,#data['totalDiscount'],
                'Total Items Discount (EGP)': None,#float(doc_data.html.body.document.totaldiscountamount.text),
                'Value added tax (EGP)': None,#float(doc_data.html.body.document.find_all('taxableitems')[-1].amount.text),
                'Extra Invoice Discounts (EGP)': None,#float(doc_data.html.body.document.extradiscountamount.text),
                'Total Amount (EGP)': None,#data['total'],


        }
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            # st.write("filename:", uploaded_file.name)
            # st.write(bytes_data)
            # f = open(bytes_data,encoding='utf-8')
            data = json.loads(bytes_data)

            dic['Reciever ID'] = data['receiverId']
            dic['Internal ID'] = data['internalId']
            dic['Reciever Name'] = u"{}".format(str(data['receiverName']))
            dic['DateTime Issued'] = data['dateTimeIssued'][:10]
            dic['DateTime Received'] = data['dateTimeReceived'][:10]
            dic['Total Sales (EGP)'] = data['totalSales']
            dic['Total discount (EGP)'] = data['totalDiscount']

            dic['Total Amount (EGP)'] = data['total']

    
            doc_data = json.loads(str(BeautifulSoup(data['document'], 'html.parser')))

            dic['Total Items Discount (EGP)'] = doc_data['totalItemsDiscountAmount']
            dic['Extra Invoice Discounts (EGP)'] =  doc_data['extraDiscountAmount']

            try:
                dic['Value added tax (EGP)'] = doc_data['taxTotals'][0]['amount']

            except IndexError:
                dic['Value added tax (EGP)'] = 0
                # st.write(doc_data)

            

            ls.append(dic)


        df = pd.DataFrame.from_records(ls)

        btn = st.download_button(
            "Press to Download",
            df.to_csv(index=False),
            "Aaref.csv",
            "text/csv",
            key='download-csv')
        




        


