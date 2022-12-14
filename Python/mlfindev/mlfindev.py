#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 22:13:51 2022

@author: kyle
"""
import pandas as pd
import os
import urllib.request
import tarfile
import numpy as np
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/kcbaumga/WorkingRepo/main/Python/mlfindev/"
#HOUSING_PATH = os.path.join("datasets", "financial")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/financial/gdp_csv.csv"
#Download url onto path
#def fetch_fin_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
#    os.makedirs(housing_path, exist_ok=True)

dt=pd.read_csv(HOUSING_URL)
#origdata=data
#print(data)

#iso3, iso2, imfn, country, region, income, year, aio1, aio2,ai03,ai04,ai05,ai06,ai07,ai08


mymap= {
        'Arab World':1, 
        'Caribbean small states':2, 
        'Central Europe and the Baltics':3, 
        'Early-demographic dividend':4, 
        'East Asia & Pacific':5, 
        'East Asia & Pacific (excluding high income)':6, 
        'East Asia & Pacific (IDA & IBRD countries)':7, 
        'Euro area':8, 'Europe & Central Asia':9, 
        'Europe & Central Asia (excluding high income)':10, 
        'Europe & Central Asia (IDA & IBRD countries)':11, 
        'European Union':12, 
        'Fragile and conflict affected situations':13, 
        'Heavily indebted poor countries (HIPC)':14, 
        'High income':15, 
        'IBRD only':16, 
        'IDA & IBRD total':17, 
        'IDA blend':18, 
        'IDA only':19, 
        'IDA total':20, 
        'Late-demographic dividend':21, 
        'Latin America & Caribbean':22, 
        'Latin America & Caribbean (excluding high income)':23, 
        'Latin America & the Caribbean (IDA & IBRD countries)':24, 
        'Least developed countries: UN classification':25, 
        'Low & middle income':26, 
        'Low income':27, 
        'Lower middle income':28, 
        'Middle East & North Africa':29, 
        'Middle East & North Africa (excluding high income)':30, 
        'Middle East & North Africa (IDA & IBRD countries)':31, 
        'Middle income':32, 
        'North America':33, 
        'OECD members':34, 
        'Other small states':35, 
        'Pacific island small states':36, 
        'Post-demographic dividend':37, 
        'Pre-demographic dividend':38, 
        'Small states':39, 
        'South Asia':40, 
        'South Asia (IDA & IBRD)':41, 
        'Sub-Saharan Africa':42, 
        'Sub-Saharan Africa (excluding high income)':43, 
        'Sub-Saharan Africa (IDA & IBRD countries)':44, 
        'Upper middle income':45, 
        'World':46, 
        'Afghanistan':47, 
        'Albania':48, 
        'Algeria':49, 
        'American Samoa':50, 
        'Andorra':51, 
        'Angola':52, 
        'Antigua and Barbuda':53, 
        'Argentina':54, 
        'Armenia':55, 
        'Aruba':56, 
        'Australia':57, 
        'Austria':58, 
        'Azerbaijan':59, 
        'Bahamas, The':60, 
        'Bahrain':61, 
        'Bangladesh':62, 
        'Barbados':63, 
        'Belarus':64, 
        'Belgium':65, 
        'Belize':66, 
        'Benin':67, 
        'Bermuda':68, 
        'Bhutan':69, 
        'Bolivia':70, 
        'Bosnia and Herzegovina':71, 
        'Botswana':72, 
        'Brazil':73, 
        'Brunei Darussalam':74, 
        'Bulgaria':75, 
        'Burkina Faso':76, 
        'Burundi':77, 
        'Cabo Verde':78, 
        'Cambodia':79, 
        'Cameroon':80, 
        'Canada':81, 
        'Cayman Islands':82, 
        'Central African Republic':83, 
        'Chad':84, 
        'Channel Islands':85, 
        'Chile':86, 
        'China':87, 
        'Colombia':88, 
        'Comoros':89, 
        'Congo, Dem. Rep.':90, 
        'Congo, Rep.':91, 
        'Costa Rica':92, 
        'Cote dIvoire':93, 
        'Croatia':94, 
        'Cuba':95, 
        'Cyprus':96, 
        'Czech Republic':97, 
        'Denmark':98, 
        'Djibouti':99, 
        'Dominica':100, 
        'Dominican Republic':101, 
        'Ecuador':102, 
        'Egypt, Arab Rep.':103, 
        'El Salvador':104, 
        'Equatorial Guinea':105, 
        'Eritrea':106, 
        'Estonia':107, 
        'Ethiopia':108, 
        'Faroe Islands':109, 
        'Fiji':110, 
        'Finland':111, 
        'France':112, 
        'French Polynesia':113, 
        'Gabon':114, 
        'Gambia, The':115, 
        'Georgia':116, 
        'Germany':117, 
        'Ghana':118, 
        'Greece':119, 
        'Greenland':120, 
        'Grenada':121, 
        'Guam':122, 
        'Guatemala':123, 
        'Guinea':124, 
        'Guinea-Bissau':125, 
        'Guyana':126, 
        'Haiti':127, 
        'Honduras':128, 
        'Hong Kong SAR, China':129, 
        'Hungary':130, 
        'Iceland':131, 
        'India':132, 
        'Indonesia':133, 
        'Iran, Islamic Rep.':134, 
        'Iraq':135, 
        'Ireland':136, 
        'Isle of Man':137, 
        'Israel':138, 
        'Italy':139, 
        'Jamaica':140, 
        'Japan':141, 
        'Jordan':142, 
        'Kazakhstan':143, 
        'Kenya':144, 
        'Kiribati':145, 
        'Korea, Rep.':146, 
        'Kosovo':147, 
        'Kuwait':148, 
        'Kyrgyz Republic':149, 
        'Lao PDR':150, 
        'Latvia':151, 
        'Lebanon':152, 
        'Lesotho':153, 
        'Liberia':154, 
        'Libya':155, 
        'Liechtenstein':156, 
        'Lithuania':157, 
        'Luxembourg':158, 
        'Macao SAR, China':159, 
        'Macedonia, FYR':160, 
        'Madagascar':161, 
        'Malawi':162, 
        'Malaysia':163, 
        'Maldives':164, 
        'Mali':165, 
        'Malta':166, 
        'Marshall Islands':167, 
        'Mauritania':168, 
        'Mauritius':169, 
        'Mexico':170, 
        'Micronesia, Fed. Sts.':171, 
        'Moldova':172, 
        'Monaco':173, 
        'Mongolia':174, 
        'Montenegro':175, 
        'Morocco':176, 
        'Mozambique':177, 
        'Myanmar':178, 
        'Namibia':179, 
        'Nauru':180, 
        'Nepal':181, 
        'Netherlands':182, 
        'New Caledonia':183, 
        'New Zealand':184, 
        'Nicaragua':185, 
        'Niger':186, 
        'Nigeria':187, 
        'Northern Mariana Islands':188, 
        'Norway':189, 
        'Oman':190, 
        'Pakistan':191, 
        'Palau':192, 
        'Panama':193, 
        'Papua New Guinea':194, 
        'Paraguay':195, 
        'Peru':196, 
        'Philippines':197, 
        'Poland':198, 
        'Portugal':199, 
        'Puerto Rico':200, 
        'Qatar':201, 
        'Romania':202, 
        'Russian Federation':203, 
        'Rwanda':204, 
        'Samoa':205, 
        'San Marino':206, 
        'Sao Tome and Principe':207, 
        'Saudi Arabia':208, 
        'Senegal':209, 
        'Serbia':210, 
        'Seychelles':211, 
        'Sierra Leone':212, 
        'Singapore':213, 
        'Slovak Republic':214, 
        'Slovenia':215, 
        'Solomon Islands':216, 
        'Somalia':217, 
        'South Africa':218, 
        'South Sudan':219, 
        'Spain':220, 
        'Sri Lanka':221, 
        'St. Kitts and Nevis':222, 
        'St. Lucia':223, 
        'St. Vincent and the Grenadines':224, 
        'Sudan':225, 
        'Suriname':226, 
        'Swaziland':227, 
        'Sweden':228, 
        'Switzerland':229, 
        'Syrian Arab Republic':230, 
        'Tajikistan':231, 
        'Tanzania':232, 
        'Thailand':233, 
        'Timor-Leste':234, 
        'Togo':235, 
        'Tonga':236, 
        'Trinidad and Tobago':237, 
        'Tunisia':238, 
        'Turkey':239, 
        'Turkmenistan':240, 
        'Tuvalu':241, 
        'Uganda':242, 
        'Ukraine':243, 
        'United Arab Emirates':244, 
        'United Kingdom':245, 
        'United States':246, 
        'Uruguay':247, 
        'Uzbekistan':248, 
        'Vanuatu':249, 
        'Venezuela, RB':250, 
        'Vietnam':251, 
        'Virgin Islands (U.S.)':252, 
        'West Bank and Gaza':253, 
        'Yemen, Rep.':254, 
        'Zambia':255, 
        'Zimbabwe':256
}
dt.dtypes
#df=data
#data.applymap(lambda s: mymap.get(s) if s in mymap else s)
df=dt['Country_Name'].map(lambda s: mymap.get(s) if s in mymap else s)
#df=data
#df=data['Country_Code'].map(lambda x:x)
#df=data[]
n=pd.DataFrame({
    'Country_Name':df
    })
ne=n.join(dt["Year"])
newdf=ne.join(dt["Value"])
newdf
#dfid=newdf.reset_index()

def split_train_test(data, test_ratio):
    shuffled_indices=np.random.permutation(len(data))
    test_set_size=int(len(data)*test_ratio)
    test_indices=shuffled_indices[:test_set_size]
    train_indices=shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]
train_set, test_set=split_train_test(newdf, .2)
print(len(train_set), len(test_set))

from zlib import crc32
#Maintain dataset
def test_set_check(identifier, test_ratio):
    return crc32(np.int64(identifier)) & 0xffffffff <test_ratio*2**32

def split_train_test_by_id(data, test_ratio, id_column):
    ids=data[id_column]
    in_test_set=ids.apply(lambda id_: test_set_check(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]

fin_with_id=newdf.reset_index()
fin_with_id["id"]=newdf["Country_Name"]*10000+newdf["Year"]
train_set, test_set= split_train_test_by_id(fin_with_id, .2, "id")
print(fin_with_id)