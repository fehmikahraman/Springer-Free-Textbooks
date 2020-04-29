import requests as req
import pandas as pd
import wget
import os

#create downloads directory
if not os.path.exists('./downloads'):
        os.makedirs('./downloads')
#excel list url        
books_url = 'https://resource-cms.springernature.com/springer-cms/rest/v1/content/17858272/data/v4'
#read data
books = pd.read_excel(books_url)
#save to excel
books.to_excel('./downloads/books_v4.xlsx')
#group books by subject
grouped=books.groupby('English Package Name')

for group_name, df_group in grouped:
    print(f"  Downloading books of {group_name}  subject ")
    #for each group create a directory under downloads
    path='./downloads/'+group_name
    if not os.path.exists(path):
        os.makedirs(path)
    #loop over grouped dataframe
    for index, row in df_group.iterrows():
        # loop through each group
        book_name = f"{row.at['Book Title']}-{row.at['Edition']}".replace('/','-').replace(':','-')
        book_url = f"{row.at['OpenURL']}"
        request = req.get(book_url)      
        download_url = f"{request.url.replace('book','content/pdf')}.pdf"
        print(f" Downlading {book_name}.pdf ...")
        wget.download(download_url, f"{path}/{book_name}.pdf") 
        print(" Download Finished")
