# filename      :hello.py
# author        :Cyrus Requiro  
# description   :this is a python program   
#                that prints the contents 
#                of a dictionary in a specific 
#                format

message =   "I am {}. \n" + \
            "My spirit animal is {}.\n" + \
            "because {}. \n" + \
            "When not in school, I have to {}.\n" + \
            "I dream of being a/an {} int the future."

data = {"Name": "Cyrus Kim Requiro",
        "My spirit":"Baduya",
        "Reason": "Ugama",
        "Hobby": "Parauma",
        "Profession": "Mag uma"
}

print (message.format(\
    data ["name"],\
    data ["spirit animal"],\
    data ["reason"],\
    data ["hobby"],\
    data ["profession"],\
)
)



print (message)
