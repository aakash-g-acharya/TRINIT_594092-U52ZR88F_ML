import numpy as np
import pandas as pd
import streamlit as sl

soil_ph = {
    "alluvial soils": 7.25,
    "red soils": 6.0,
    "laterite soils": 5.25,
    "black soils": 7.5,
    "coastal sands": 7.25,
    "forest soils": 6.25,
    "mountain soils": 6.25,
    "deltaic soil": 6.75
}


avg_npk_ratios = {
 'alluvial soils': [0.375, 0.125, 0.5],
 'red soils': [0.3333333333333333, 0.16666666666666666, 0.5],
 'laterite soils': [0.2857142857142857,
  0.14285714285714285,
  0.5714285714285714],
 'black soils': [0.36363636363636365, 0.09090909090909091, 0.5454545454545454],
 'coastal sands': [0.36363636363636365,
  0.09090909090909091,
  0.5454545454545454],
 'forest soils': [0.375, 0.125, 0.5],
 'mountain soils': [0.3333333333333333, 0.16666666666666666, 0.5],
 'deltaic soil': [0.37037037037037035, 0.1111111111111111, 0.5185185185185185]
}

karnataka_soil_map = {
 'Bengaluru': ['red soils', 'black soils'],
 'Belagavi': ['red soils', 'black soils', 'laterite soils'],
 'Ballari': ['red soils', 'laterite soils'],
 'Bidar': ['red soils', 'black soils'],
 'Vijayapura': ['red soils', 'laterite soils'],
 'Chikkamagaluru': ['red soils', 'laterite soils', 'forest soils'],
 'Chitradurga': ['red soils', 'laterite soils'],
 'Davangere': ['red soils', 'black soils'],
 'Dharwad': ['red soils', 'laterite soils'],
 'Gadag': ['red soils', 'laterite soils'],
 'Kalaburagi': ['red soils', 'black soils'],
 'Bagalkot': ['red soils', 'black soils'],
 'Hassan': ['red soils', 'laterite soils'],
 'Haveri': ['red soils', 'black soils'],
 'Kolar': ['red soils', 'black soils'],
 'Koppal': ['red soils', 'laterite soils'],
 'Mandya': ['red soils', 'black soils'],
 'Mysuru': ['red soils', 'black soils'],
 'Raichur': ['red soils', 'black soils'],
 'Ramanagara': ['red soils', 'black soils'],
 'Shivamogga': ['red soils', 'laterite soils'],
 'Tumakuru': ['red soils', 'black soils'],
 'Udupi': ['laterite soils', 'red soils'],
 'Uttara Kannada': ['laterite soils', 'red soils', 'forest soils'],
 'Yadgir': ['red soils']
}

kerala_soil_map={
 'Thiruvananthapuram': ['laterite soils', 'red soils'],
 'Kollam': ['laterite soils', 'red soils', 'alluvial soils'],
 'Pathanamthitta': ['laterite soils', 'red soils', 'forest soils'],
 'Alappuzha': ['laterite soils', 'red soils', 'alluvial soils'],
 'Kottayam': ['laterite soils', 'red soils', 'alluvial soils'],
 'Idukki': ['laterite soils', 'red soils', 'forest soils'],
 'Ernakulam': ['laterite soils', 'red soils', 'alluvial soils'],
 'Thrissur': ['laterite soils', 'red soils', 'alluvial soils'],
 'Palakkad': ['laterite soils', 'red soils', 'alluvial soils'],
 'Malappuram': ['laterite soils', 'red soils', 'alluvial soils'],
 'Kozhikode': ['laterite soils', 'red soils', 'alluvial soils'],
 'Wayanad': ['laterite soils', 'red soils', 'forest soils'],
 'Kannur': ['laterite soils', 'red soils', 'alluvial soils'],
 'Kasaragod': ['laterite soils', 'red soils']
}

gujarat_soil_map = {
 'Ahmedabad': ['black soils', 'laterite soils'],
 'Amreli': ['black soils', 'laterite soils'],
 'Anand': ['black soils', 'alluvial soils'],
 'Banaskantha': ['black soils', 'alluvial soils'],
 'Bharuch': ['alluvial soils', 'black soils'],
 'Bhavnagar': ['black soils', 'laterite soils'],
 'Dahod': ['black soils', 'alluvial soils'],
 'Dang': ['black soils', 'laterite soils'],
 'Gandhinagar': ['black soils', 'alluvial soils'],
 'Jamnagar': ['black soils', 'laterite soils'],
 'Junagadh': ['black soils', 'laterite soils'],
 'Kachchh': ['black soils', 'laterite soils'],
 'Kheda': ['black soils', 'alluvial soils'],
 'Mehsana': ['black soils', 'alluvial soils'],
 'Narmada': ['black soils', 'alluvial soils'],
 'Navsari': ['black soils', 'alluvial soils'],
 'Panchmahal': ['black soils', 'alluvial soils'],
 'Patan': ['black soils', 'alluvial soils'],
 'Porbandar': ['black soils', 'laterite soils'],
 'Rajkot': ['black soils', 'laterite soils'],
 'Sabarkantha': ['black soils', 'alluvial soils'],
 'Surat': ['black soils', 'alluvial soils'],
 'Surendranagar': ['black soils', 'laterite soils'],
 'Tapi': ['black soils', 'alluvial soils'],
 'Vadodara': ['black soils', 'alluvial soils'],
 'Valsad': ['black soils', 'alluvial soils']
}

rajasthan_soil_map = {
"Ajmer": ["laterite soils", "red soils", "alluvial soils"],
"Alwar": ["red soils", "alluvial soils", "laterite soils"],
"Banswara": ["red soils", "laterite soils"],
"Baran": ["red soils", "alluvial soils"],
"Barmer": ["red soils", "laterite soils"],
"Bharatpur": ["alluvial soils", "red soils"],
"Bhilwara": ["red soils", "alluvial soils"],
"Bikaner": ["red soils", "laterite soils"],
"Bundi": ["red soils", "laterite soils"],
"Chittorgarh": ["red soils", "laterite soils"],
"Churu": ["red soils", "laterite soils"],
"Dausa": ["red soils", "laterite soils"],
"Dholpur": ["alluvial soils", "red soils"],
"Dungarpur": ["red soils", "laterite soils"],
"Hanumangarh": ["red soils", "laterite soils"],
"Jaipur": ["red soils", "alluvial soils", "laterite soils"],
"Jaisalmer": ["red soils", "laterite soils"],
"Jalor": ["red soils", "laterite soils"],
"Jhalawar": ["red soils", "laterite soils"],
"Jhunjhunu": ["red soils", "laterite soils"],
"Jodhpur": ["red soils", "laterite soils"],
"Karauli": ["alluvial soils", "red soils"],
"Kota": ["red soils", "laterite soils"],
"Nagaur": ["red soils", "laterite soils"],
"Pali": ["red soils", "laterite soils"],
"Rajsamand": ["red soils", "alluvial soils", "laterite soils"],
"Sawai Madhopur": ["red soils", "laterite soils"],
"Sikar": ["red soils", "laterite soils"],
"Sirohi": ["red soils", "laterite soils"],
"Tonk": ["red soils", "laterite soils"],
"Udaipur": ["red soils", "laterite soils"]
}

state_soil_map = {
"jammu and kashmir" : ["mountain soils"],
"andhra pradesh": ["red soils", "black soils", "laterite soils", "alluvial soils"],
"arunachal pradesh": ["forest soils", "mountain soils"],
"assam": ["alluvial soils", "laterite soils"],
"bihar": ["alluvial soils", "laterite soils"],
"chhattisgarh": ["red soils", "laterite soils", "black soils"],
"goa": ["laterite soils", "red soils"],
"haryana": ["alluvial soils", "black soils", "loamy soil"],
"himachal pradesh": ["mountain soils", "forest soils"],
"jharkhand": ["laterite soils", "red soils", "alluvial soils"],
"madhya pradesh": ["red soils", "laterite soils", "black soils", "alluvial soils"],
"maharashtra": ["black soils", "red soils", "laterite soils", "alluvial soils"],
"manipur": ["forest soils", "mountain soils"],
"meghalaya": ["forest soils", "mountain soils"],
"mizoram": ["mountain soils", "forest soils"],
"nagaland": ["forest soils", "mountain soils"],
"odisha": ["laterite soils", "red soils", "alluvial soils"],
"punjab": ["black soils", "alluvial soils", "loamy soil"],
"sikkim": ["mountain soils", "forest soils"],
"tamil nadu": ["red soils", "laterite soils", "alluvial soils"],
"telangana": ["red soils", "black soils", "laterite soils"],
"tripura": ["laterite soils", "alluvial soils"],
"uttar pradesh": ["alluvial soils", "laterite soils"],
"uttarakhand": ["mountain soils", "forest soils"],
"west bengal": ["alluvial soils", "laterite soils"],
"andaman and nicobar islands": ["laterite soils", "forest soils"],
"chandigarh": ["alluvial soils"],
"dadra and nagar haveli": ["laterite soils"],
"daman and diu": ["laterite soils"],
"delhi": ["alluvial soils"],
"lakshadweep": ["coral soils"],
"puducherry": ["laterite soils", "alluvial soils"]
}

D = {
    "Andhra Pradesh": [
        "Anantapur",
        "Chittoor",
        "East Godavari",
        "Guntur",
        "Krishna",
        "Kurnool",
        "Nellore",
        "Prakasam",
        "Srikakulam",
        "Visakhapatnam",
        "Vizianagaram",
        "West Godavari",
        "YSR Kadapa"
    ],
    "Arunachal Pradesh": [
        "Tawang",
        "West Kameng",
        "East Kameng",
        "Papum Pare",
        "Kurung Kumey",
        "Kra Daadi",
        "Lower Subansiri",
        "Upper Subansiri",
        "West Siang",
        "East Siang",
        "Siang",
        "Upper Siang",
        "Lower Siang",
        "Lower Dibang Valley",
        "Dibang Valley",
        "Anjaw",
        "Lohit",
        "Namsai",
        "Changlang",
        "Tirap",
        "Longding"
    ],
    "Assam": [
        "Baksa",
        "Barpeta",
        "Biswanath",
        "Bongaigaon",
        "Cachar",
        "Charaideo",
        "Chirang",
        "Darrang",
        "Dhemaji",
        "Dhubri",
        "Dibrugarh",
        "Goalpara",
        "Golaghat",
        "Hailakandi",
        "Hojai",
        "Jorhat",
        "Kamrup Metropolitan",
        "Kamrup",
        "Karbi Anglong",
        "Karimganj",
        "Kokrajhar",
        "Lakhimpur",
        "Majuli",
        "Morigaon",
        "Nagaon",
        "Nalbari",
        "Dima Hasao",
        "Sivasagar",
        "Sonitpur",
        "South Salmara-Mankachar",
        "Tinsukia",
        "Udalguri",
        "West Karbi Anglong"
    ],
    "Bihar": [
        "Araria",
        "Arwal",
        "Aurangabad",
        "Banka",
        "Begusarai",
        "Bhagalpur",
        "Bhojpur",
        "Buxar",
        "Darbhanga",
        "East Champaran",
        "Gaya",
        "Gopalganj",
        "Jamui",
        "Jehanabad",
        "Kaimur",
        "Katihar",
        "Khagaria",
        "Kishanganj",
        "Lakhisarai",
        "Madhepura",
        "Madhubani",
        "Munger",
        "Muzaffarpur",
        "Nalanda",
        "Nawada",
        "Patna",
        "Purnia",
        "Rohtas",
        "Saharsa",
        "Samastipur",
        "Saran",
        "Sheikhpura",
        "Sheohar",
        "Sitamarhi",
        "Siwan",
        "Supaul",
        "Vaishali",
        "West Champaran"
    ],
    "Chandigarh": [
        "Chandigarh"
    ],
    "Chhattisgarh": [
        "Balod",
        "Baloda Bazar",
        "Balrampur",
        "Bastar",
        "Bemetara",
        "Bijapur",
        "Bilaspur",
        "Dantewada",
        "Dhamtari",
        "Durg",
        "Gariyaband",
        "Janjgir-Champa",
        "Jashpur",
        "Kabirdham",
        "Kanker",
        "Kondagaon",
        "Korba",
        "Korea",
        "Mahasamund",
        "Mungeli",
        "Narayanpur",
        "Raigarh",
        "Raipur",
        "Rajnandgaon",
        "Sukma",
        "Surajpur  ",
        "Surguja"
    ],
    "Dadra and Nagar Haveli": [
        "Dadra & Nagar Haveli"
    ],
    "Daman and Diu": [
        "Daman",
        "Diu"
    ],
    "Delhi": [
        "Central Delhi",
        "East Delhi",
        "New Delhi",
        "North Delhi",
        "North East  Delhi",
        "North West  Delhi",
        "Shahdara",
        "South Delhi",
        "South East Delhi",
        "South West  Delhi",
        "West Delhi"
    ],
    "Goa": [
        "North Goa",
        "South Goa"
    ],
    "Gujarat": [
        "Ahmedabad",
        "Amreli",
        "Anand",
        "Aravalli",
        "Banaskantha",
        "Bharuch",
        "Bhavnagar",
        "Botad",
        "Chhota Udepur",
        "Dahod",
        "Dangs",
        "Devbhoomi Dwarka",
        "Gandhinagar",
        "Gir Somnath",
        "Jamnagar",
        "Junagadh",
        "Kachchh",
        "Kheda",
        "Mahisagar",
        "Mehsana",
        "Morbi",
        "Narmada",
        "Navsari",
        "Panchmahal",
        "Patan",
        "Porbandar",
        "Rajkot",
        "Sabarkantha",
        "Surat",
        "Surendranagar",
        "Tapi",
        "Vadodara",
        "Valsad"
    ],
    "Haryana": [
        "Ambala",
        "Bhiwani",
        "Charkhi Dadri",
        "Faridabad",
        "Fatehabad",
        "Gurgaon",
        "Hisar",
        "Jhajjar",
        "Jind",
        "Kaithal",
        "Karnal",
        "Kurukshetra",
        "Mahendragarh",
        "Mewat",
        "Palwal",
        "Panchkula",
        "Panipat",
        "Rewari",
        "Rohtak",
        "Sirsa",
        "Sonipat",
        "Yamunanagar"
    ],
    "Himachal Pradesh": [
        "Bilaspur",
        "Chamba",
        "Hamirpur",
        "Kangra",
        "Kinnaur",
        "Kullu",
        "Lahaul &amp; Spiti",
        "Mandi",
        "Shimla",
        "Sirmaur",
        "Solan",
        "Una"
    ],
    "Jammu and Kashmir": [
        "Anantnag",
        "Bandipore",
        "Baramulla",
        "Budgam",
        "Doda",
        "Ganderbal",
        "Jammu",
        "Kargil",
        "Kathua",
        "Kishtwar",
        "Kulgam",
        "Kupwara",
        "Leh",
        "Poonch",
        "Pulwama",
        "Rajouri",
        "Ramban",
        "Reasi",
        "Samba",
        "Shopian",
        "Srinagar",
        "Udhampur"
    ],
    "Jharkhand": [
        "Bokaro",
        "Chatra",
        "Deoghar",
        "Dhanbad",
        "Dumka",
        "East Singhbhum",
        "Garhwa",
        "Giridih",
        "Godda",
        "Gumla",
        "Hazaribag",
        "Jamtara",
        "Khunti",
        "Koderma",
        "Latehar",
        "Lohardaga",
        "Pakur",
        "Palamu",
        "Ramgarh",
        "Ranchi",
        "Sahibganj",
        "Seraikela-Kharsawan",
        "Simdega",
        "West Singhbhum"
    ],
    "Karnataka": [
        "Bagalkot",
        "Ballari",
        "Belagavi",
        "Bengaluru Rural",
        "Bengaluru Urban",
        "Bidar",
        "Chamarajanagar",
        "Chikballapur",
        "Chikkamagaluru",
        "Chitradurga",
        "Dakshina Kannada",
        "Davangere",
        "Dharwad",
        "Gadag",
        "Hassan",
        "Haveri",
        "Kalaburagi",
        "Kodagu",
        "Kolar",
        "Koppal",
        "Mandya",
        "Mysuru",
        "Raichur",
        "Ramanagara",
        "Shivamogga",
        "Tumakuru",
        "Udupi",
        "Uttara Kannada",
        "Vijayapura",
        "Yadgir"
    ],
    "Kerala": [
        "Alappuzha",
        "Ernakulam",
        "Idukki",
        "Kannur",
        "Kasaragod",
        "Kollam",
        "Kottayam",
        "Kozhikode",
        "Malappuram",
        "Palakkad",
        "Pathanamthitta",
        "Thiruvananthapuram",
        "Thrissur",
        "Wayanad"
    ],
    "Lakshadweep": [
        "Agatti",
        "Amini",
        "Androth",
        "Bithra",
        "Chethlath",
        "Kavaratti",
        "Kadmath",
        "Kalpeni",
        "Kilthan",
        "Minicoy"
    ],
    "Madhya Pradesh": [
        "Agar Malwa",
        "Alirajpur",
        "Anuppur",
        "Ashoknagar",
        "Balaghat",
        "Barwani",
        "Betul",
        "Bhind",
        "Bhopal",
        "Burhanpur",
        "Chhatarpur",
        "Chhindwara",
        "Damoh",
        "Datia",
        "Dewas",
        "Dhar",
        "Dindori",
        "Guna",
        "Gwalior",
        "Harda",
        "Hoshangabad",
        "Indore",
        "Jabalpur",
        "Jhabua",
        "Katni",
        "Khandwa",
        "Khargone",
        "Mandla",
        "Mandsaur",
        "Morena",
        "Narsinghpur",
        "Neemuch",
        "Panna",
        "Raisen",
        "Rajgarh",
        "Ratlam",
        "Rewa",
        "Sagar",
        "Satna",
        "Sehore",
        "Seoni",
        "Shahdol",
        "Shajapur",
        "Sheopur",
        "Shivpuri",
        "Sidhi",
        "Singrauli",
        "Tikamgarh",
        "Ujjain",
        "Umaria",
        "Vidisha"
    ],
    "Maharashtra": [
        "Ahmednagar",
        "Akola",
        "Amravati",
        "Aurangabad",
        "Beed",
        "Bhandara",
        "Buldhana",
        "Chandrapur",
        "Dhule",
        "Gadchiroli",
        "Gondia",
        "Hingoli",
        "Jalgaon",
        "Jalna",
        "Kolhapur",
        "Latur",
        "Mumbai City",
        "Mumbai Suburban",
        "Nagpur",
        "Nanded",
        "Nandurbar",
        "Nashik",
        "Osmanabad",
        "Palghar",
        "Parbhani",
        "Pune",
        "Raigad",
        "Ratnagiri",
        "Sangli",
        "Satara",
        "Sindhudurg",
        "Solapur",
        "Thane",
        "Wardha",
        "Washim",
        "Yavatmal"
    ],
    "Manipur": [
        "Bishnupur",
        "Chandel",
        "Churachandpur",
        "Imphal East",
        "Imphal West",
        "Jiribam",
        "Kakching",
        "Kamjong",
        "Kangpokpi",
        "Noney",
        "Pherzawl",
        "Senapati",
        "Tamenglong",
        "Tengnoupal",
        "Thoubal",
        "Ukhrul"
    ],
    "Meghalaya": [
        "East Garo Hills",
        "East Jaintia Hills",
        "East Khasi Hills",
        "North Garo Hills",
        "Ri Bhoi",
        "South Garo Hills",
        "South West Garo Hills ",
        "South West Khasi Hills",
        "West Garo Hills",
        "West Jaintia Hills",
        "West Khasi Hills"
    ],
    "Mizoram": [
        "Aizawl",
        "Champhai",
        "Kolasib",
        "Lawngtlai",
        "Lunglei",
        "Mamit",
        "Saiha",
        "Serchhip"
    ],
    "Nagaland": [
        "Dimapur",
        "Kiphire",
        "Kohima",
        "Longleng",
        "Mokokchung",
        "Mon",
        "Peren",
        "Phek",
        "Tuensang",
        "Wokha",
        "Zunheboto"
    ],
    "Odisha": [
        "Angul",
        "Balangir",
        "Balasore",
        "Bargarh",
        "Bhadrak",
        "Boudh",
        "Cuttack",
        "Deogarh",
        "Dhenkanal",
        "Gajapati",
        "Ganjam",
        "Jagatsinghapur",
        "Jajpur",
        "Jharsuguda",
        "Kalahandi",
        "Kandhamal",
        "Kendrapara",
        "Kendujhar",
        "Khordha",
        "Koraput",
        "Malkangiri",
        "Mayurbhanj",
        "Nabarangpur",
        "Nayagarh",
        "Nuapada",
        "Puri",
        "Rayagada",
        "Sambalpur",
        "Sonepur",
        "Sundargarh"
    ],
    "Puducherry": [
        "Karaikal",
        "Mahe",
        "Pondicherry",
        "Yanam"
    ],
    "Punjab": [
        "Amritsar",
        "Barnala",
        "Bathinda",
        "Faridkot",
        "Fatehgarh Sahib",
        "Fazilka",
        "Ferozepur",
        "Gurdaspur",
        "Hoshiarpur",
        "Jalandhar",
        "Kapurthala",
        "Ludhiana",
        "Mansa",
        "Moga",
        "Muktsar",
        "Nawanshahr",
        "Pathankot",
        "Patiala",
        "Rupnagar",
        "Sahibzada Ajit Singh Nagar",
        "Sangrur",
        "Tarn Taran"
    ],
    "Rajasthan": [
        "Ajmer",
        "Alwar",
        "Banswara",
        "Baran",
        "Barmer",
        "Bharatpur",
        "Bhilwara",
        "Bikaner",
        "Bundi",
        "Chittorgarh",
        "Churu",
        "Dausa",
        "Dholpur",
        "Dungarpur",
        "Hanumangarh",
        "Jaipur",
        "Jaisalmer",
        "Jalore",
        "Jhalawar",
        "Jhunjhunu",
        "Jodhpur",
        "Karauli",
        "Kota",
        "Nagaur",
        "Pali",
        "Pratapgarh",
        "Rajsamand",
        "Sawai Madhopur",
        "Sikar",
        "Sirohi",
        "Sri Ganganagar",
        "Tonk",
        "Udaipur"
    ],
    "Sikkim": [
        "East Sikkim",
        "North Sikkim",
        "South Sikkim",
        "West Sikkim"
    ],
    "Tamil Nadu": [
        "Ariyalur",
        "Chennai",
        "Coimbatore",
        "Cuddalore",
        "Dharmapuri",
        "Dindigul",
        "Erode",
        "Kanchipuram",
        "Kanyakumari",
        "Karur",
        "Krishnagiri",
        "Madurai",
        "Nagapattinam",
        "Namakkal",
        "Nilgiris",
        "Perambalur",
        "Pudukkottai",
        "Ramanathapuram",
        "Salem",
        "Sivaganga",
        "Thanjavur",
        "Theni",
        "Thoothukudi",
        "Tiruchirappalli",
        "Tirunelveli",
        "Tiruppur",
        "Tiruvallur",
        "Tiruvannamalai",
        "Tiruvarur",
        "Vellore",
        "Viluppuram",
        "Virudhunagar"
    ],
    "Telangana": [
        "Adilabad",
        "Bhadradri Kothagudem",
        "Hyderabad",
        "Jagtial",
        "Jangaon",
        "Jayashankar Bhoopalpally",
        "Jogulamba Gadwal",
        "Kamareddy",
        "Karimnagar",
        "Khammam",
        "Komaram Bheem Asifabad",
        "Mahabubabad",
        "Mahabubnagar",
        "Mancherial",
        "Medak",
        "Medchal",
        "Nagarkurnool",
        "Nalgonda",
        "Nirmal",
        "Nizamabad",
        "Peddapalli",
        "Rajanna Sircilla",
        "Rangareddy",
        "Sangareddy",
        "Siddipet",
        "Suryapet",
        "Vikarabad",
        "Wanaparthy",
        "Warangal (Rural)",
        "Warangal (Urban)",
        "Yadadri Bhuvanagiri"
    ],
    "Tripura": [
        "Dhalai",
        "Gomati",
        "Khowai",
        "North Tripura",
        "Sepahijala",
        "South Tripura",
        "Unakoti",
        "West Tripura"
    ],
    "Uttarakhand": [
        "Almora",
        "Bageshwar",
        "Chamoli",
        "Champawat",
        "Dehradun",
        "Haridwar",
        "Nainital",
        "Pauri Garhwal",
        "Pithoragarh",
        "Rudraprayag",
        "Tehri Garhwal",
        "Udham Singh Nagar",
        "Uttarkashi"
    ],
    "Uttar Pradesh": [
        "Agra",
        "Aligarh",
        "Allahabad",
        "Ambedkar Nagar",
        "Amethi",
        "Amroha",
        "Auraiya",
        "Azamgarh",
        "Baghpat",
        "Bahraich",
        "Ballia",
        "Balrampur",
        "Banda",
        "Barabanki",
        "Bareilly",
        "Basti",
        "Bhadohi",
        "Bijnor",
        "Budaun",
        "Bulandshahr",
        "Chandauli",
        "Chitrakoot",
        "Deoria",
        "Etah",
        "Etawah",
        "Faizabad",
        "Farrukhabad",
        "Fatehpur",
        "Firozabad",
        "Gautam Buddha Nagar",
        "Ghaziabad",
        "Ghazipur",
        "Gonda",
        "Gorakhpur",
        "Hamirpur",
        "Hapur",
        "Hardoi",
        "Hathras",
        "Jalaun",
        "Jaunpur",
        "Jhansi",
        "Kannauj",
        "Kanpur Dehat",
        "Kanpur Nagar",
        "Kanshiram Nagar",
        "Kaushambi",
        "Kushinagar",
        "Lakhimpur - Kheri",
        "Lalitpur",
        "Lucknow",
        "Maharajganj",
        "Mahoba",
        "Mainpuri",
        "Mathura",
        "Mau",
        "Meerut",
        "Mirzapur",
        "Moradabad",
        "Muzaffarnagar",
        "Pilibhit",
        "Pratapgarh",
        "RaeBareli",
        "Rampur",
        "Saharanpur",
        "Sambhal",
        "Sant Kabir Nagar",
        "Shahjahanpur",
        "Shamali",
        "Shravasti",
        "Siddharth Nagar",
        "Sitapur",
        "Sonbhadra",
        "Sultanpur",
        "Unnao",
        "Varanasi"
    ],
    "West Bengal": [
        "Alipurduar",
        "Bankura",
        "Birbhum",
        "Burdwan",
        "Cooch Behar",
        "Dakshin Dinajpur",
        "Darjeeling",
        "Hooghly",
        "Howrah",
        "Jalpaiguri",
        "Kalimpong",
        "Kolkata",
        "Malda",
        "Murshidabad",
        "Nadia",
        "North 24 Parganas",
        "Paschim Medinipur",
        "Purba Medinipur",
        "Purulia",
        "South 24 Parganas",
        "Uttar Dinajpur"
    ],
    "Andaman and Nicobar Islands": [
        "Nicobar",
        "North and Middle Andaman",
        "South Andaman",
    ]

}

header = sl.container()
dataset = sl.container()
features = sl.container()
model = sl.container()

with header:
    sl.title("CROP RECOMMENDATION")

from sklearn.model_selection import train_test_split
from sklearn import metrics

with model:
    df = pd.read_csv("C:/Users/Aakash/Desktop/hackathon/data.csv")
    df = df.drop("Unnamed: 0",axis=1)
    train_cols = [x for x in df.columns if x!='label']
    x1 = df.loc[:, train_cols]
    y1 = df['label']

    from sklearn.preprocessing import LabelEncoder

    le = LabelEncoder()
    y1 = le.fit_transform(y1)
    Map = dict(zip(le.transform(le.classes_), le.classes_))

    
    sel_col, dis_col = sl.columns(2)

    State = sel_col.selectbox("STATE:",
                              options=["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa",
                                       "Gujarat", "Haryana",
                                       "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala",
                                       "Madhya Pradesh", "Maharashtra",
                                       "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan",
                                       "Sikkim", "Tamil Nadu",
                                       "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
                                       "Andaman and Nicobar Islands",
                                       "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep",
                                       "Delhi",
                                       "Puducherry"], index=0)

    District = sel_col.selectbox("DISTRICT:", options=D[State], index=0)
    Month = sel_col.selectbox("Month:",
                              options=['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV',
                                       'DEC'], index=0)
    present = ['Karnataka','Kerala','Rajasthan','Gujarat']
    if(State in present):
            district = District
            s1=0
            s2=0
            s3=0
            s4=0
            s5=0
            s6=0
            s7=0
            s8=0
            x=None
            if(State=='Karnataka'):
                x=karnataka_soil_map
            elif (State=='Kerala'):
                x=kerala_soil_map
            elif (State=='Rajasthan'):
                x=rajasthan_soil_map
            else:
                x=gujarat_soil_map
            for soil in x[district]:
                if(soil=='coastal sands'):
                    s1=1
                elif (soil=='deltaic soils'):
                    s2=1
                elif (soil=='laterite soils'):
                    s3=1
                elif (soil=='alluvial soils'):
                    s4=1
                elif (soil=='red soils'):
                    s5=1
                elif (soil=='mountain soils'):
                    s6=1
                elif (soil=='forest soils'):
                    s7=1
                else:
                    s8=1
            

    else:
            state = State.lower()
            s1=0
            s2=0
            s3=0
            s4=0
            s5=0
            s6=0
            s7=0
            s8=0
            for soil in state_soil_map[state]:
            
                if(soil=='coastal sands'):
                    s1=1
                elif (soil=='deltaic soils'):
                    s2=1
                elif (soil=='laterite soils'):
                    s3=1
                elif (soil=='alluvial soils'):
                    s4=1
                elif (soil=='red soils'):
                    s5=1
                elif (soil=='mountain soils'):
                    s6=1
                elif (soil=='forest soils'):
                    s7=1
                else:
                    s8=1
            
    

    flag = sel_col.selectbox("Do you have soil test kit?",
                             options=['YES', 'NO'], index=0)
    if flag == 'YES':
        N = sel_col.slider("Ratio of Nitrogen content in soil:", min_value=0, max_value=150, value=35, step=1)
        P = sel_col.slider("Ratio of Phosphorous content in soil:", min_value=0, max_value=150, value=54, step=1)
        K = sel_col.slider("Ratio of Potassium content in soil:", min_value=0, max_value=210, value=15, step=1)
        Ph = sel_col.slider("PH value of the soil:", min_value=0.0, max_value=14.0, value=7.0, step=0.1)
    else:
        present = ['Karnataka','Kerala','Rajasthan','Gujarat']
        if(State in present):
            district = District
            x=None
            if(State=='Karnataka'):
                x=karnataka_soil_map
            elif (State=='Kerala'):
                x=kerala_soil_map
            elif (State=='Rajasthan'):
                x=rajasthan_soil_map
            else:
                x=gujarat_soil_map
            N=0
            P=0
            K=0
            Ph=0
            for soil in x[district]:
                N+=avg_npk_ratios[soil][0]
                P+=avg_npk_ratios[soil][1]
                K+=avg_npk_ratios[soil][2]
                Ph+=soil_ph[soil]
            N/=len(x[district])
            P/=len(x[district])
            K/=len(x[district])
            Ph/=len(x[district])

        else:
            state = State.lower()
            N=0
            P=0
            K=0
            Ph=0
            for soil in state_soil_map[state]:
                N+=avg_npk_ratios[soil][0]
                P+=avg_npk_ratios[soil][1]
                K+=avg_npk_ratios[soil][2]
                Ph+=soil_ph[soil]
            N/=len(state_soil_map[state])
            P/=len(state_soil_map[state])
            K/=len(state_soil_map[state])
            Ph/=len(state_soil_map[state])


    from geopy.geocoders import Nominatim

    geolocator = Nominatim(user_agent="MyApp")

    location = geolocator.geocode(District)

    latitude = round(location.latitude, 2)
    longitude = round(location.longitude, 2)

    url = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(latitude) + "&lon=" + str(longitude) + \
              "&appid=345ef5a50d96f8c85bc1b12a2ce088ca"

    import requests

    response = requests.get(url)
    JSON = response.json()

    R = pd.read_csv("C:/Users/Aakash/Desktop/hackathon/district_wise_rainfall_normal.csv")

    Temperature = JSON['main']['temp'] - 273.15
    Humidity = JSON['main']['humidity']
    try:
        Rainfall = R[Month.upper()].loc[(R['STATE_UT_NAME'] == State.upper()) & (R['DISTRICT'] == District.upper())].values[
        0]
    except:
        Rainfall=0

    xtrain, xtest, ytrain, ytest = train_test_split(x1, y1, test_size=0.2, random_state=2)
    import xgboost as xgb

    XB = xgb.XGBClassifier()
    XB.fit(xtrain, ytrain)
    predicted = XB.predict(xtest)

    accuracy = metrics.accuracy_score(ytest, predicted)
    dis_col.subheader("Model's Accuracy is: ")
    dis_col.write(accuracy)

    dis_col.subheader("Best crop to grow: ")
    dis_col.write(Map[XB.predict(np.asarray([[N, P, K, Temperature, Humidity, Ph, Rainfall,s1,s2,s3,s4,s5,s6,s7,s8]]))[0]])
    dis_col.subheader("Other suitable crops: ")
    Prob = XB.predict_proba(np.asarray([[N, P, K, Temperature, Humidity, Ph, Rainfall,s1,s2,s3,s4,s5,s6,s7,s8]]))[0]

    values = np.sort(Prob)[::-1]

    sorter = np.argsort(Prob)

    R = sorter[np.searchsorted(Prob, values, sorter=sorter)]
    dis_col.write(Map[R[1:5][0]])
    dis_col.write(Map[R[1:5][1]])
    dis_col.write(Map[R[1:5][2]])
    dis_col.write(Map[R[1:5][3]])
    
