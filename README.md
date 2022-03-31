# ZSSN -> ZSSN (Zombie Survival Social Network). The world as we know it has fallen into an apocalyptic scenario. A laboratory-made virus is transforming human beings and animals into zombies, hungry for fresh flesh.

# ZSSN API
1. Creat Survivor - "http://127.0.0.1:8000/survivors/", Method = "POST"
2. List Survivor - "http://127.0.0.1:8000/survivors/", Method = "GET"
3. Update Location - "http://127.0.0.1:8000/survivors/<<int(ID)>>" Method = "PUT"
4. SurvivorPercentage - "http://127.0.0.1:8000/survivor/reports/" Method = "GET"

# For Python Packages kimdly refer to requirements.txt 

# DATABASE - MYSQL

# Payload 
1. For Create Survivor
{
            "name": "Text-field",
            "age": Integer,
            "gender": "CharField/choice",
            "location":{
                    "longitude": 18.1222,
                    "latitude": 17.000014455
            },
            "is_infected": "CharField/choice"
        }

2. For List of All Survivor
 Run this URL "http://127.0.0.1:8000/survivors/", Method = "GET"

3. Payload For Update location on the basis of passing ID in QueryParam
 
        {
            "longitude": 153.1222,
            "latitude": 17.000014455      
        }
    -> http://127.0.0.1:8000/survivors/<<int(ID)>>/


4. Survivor Percentage
    -> http://127.0.0.1:8000/survivor/reports/


