
import pandas as pd
import pickle
data = pd.pandas.read_csv('/home/shreyank/miniproject/mini/home/static/img/excel/Cleaned_data.csv')
pipe = pickle.load(open("/home/shreyank/miniproject/mini/home/RidgeModel2.pkl", "rb"))
areaname = ""
bathroom = ""
gbhk = ""
ganswer = ""
size = ""
duplex=""
parking=""
balcony=""
print(type(data))
pickle.dump(areaname, open("variableStoringFile1.dat", "wb"))
pickle.dump(bathroom, open("variableStoringFile2.dat", "wb"))
pickle.dump(gbhk, open("variableStoringFile3.dat", "wb"))
pickle.dump(size, open("variableStoringFile4.dat", "wb"))
pickle.dump(duplex, open("variableStoringFile5.dat", "wb"))
pickle.dump(parking, open("variableStoringFile6.dat", "wb"))
pickle.dump(balcony, open("variableStoringFile7.dat", "wb"))

count = 0
pickle.dump(count, open("variableStoringFile.dat", "wb"))
location = sorted((data['location'].unique()))
locations = location


def sample_responses(input_text):
    user_message = str(input_text)
    if user_message in ('hi'):
        return 'this is house price prediction bot please enter 1 to predict'
    if user_message in ('help'):
        help = 'this is house price prediction bot please enter 1 to predict'
        return help
    if user_message in "1":
        count = pickle.load(open("variableStoringFile.dat", "rb"))
        if count == 0:
            return "enter the area name :"

    if user_message != None:
        count = pickle.load(open("variableStoringFile.dat", "rb"))
        if count == 0:

            count = count+1
            pickle.dump(count, open("variableStoringFile.dat", "wb"))
            pickle.dump(user_message, open("variableStoringFile1.dat", "wb"))
            return 'enter the size : (in sqrt)'
    if user_message != None:
        count = pickle.load(open("variableStoringFile.dat", "rb"))
        if count == 1:
            count = count+1
            # size=int(user_message)
            pickle.dump(count, open("variableStoringFile.dat", "wb"))
            pickle.dump(user_message, open("variableStoringFile4.dat", "wb"))
            return 'how many BHK ?(enter only number)'
    if user_message != None:
        count = pickle.load(open("variableStoringFile.dat", "rb"))
        if count == 2:
            # gbhk=int(user_message)
            count = count+1
            pickle.dump(count, open("variableStoringFile.dat", "wb"))
            pickle.dump(user_message, open("variableStoringFile3.dat", "wb"))
            return 'enter the number of bathrooms :(only in digits)'
    if user_message!=None:
        count = pickle.load(open("variableStoringFile.dat", "rb"))
        if count == 3:
            # bathroom=int(user_message)
            count = count+1
            pickle.dump(count, open("variableStoringFile.dat", "wb"))
            pickle.dump(user_message, open("variableStoringFile2.dat", "wb"))
            return 'Duplex House (Click 1 for Yes )'
    if user_message!=None:
        count = pickle.load(open("variableStoringFile.dat", "rb"))
        if count == 4:
            # bathroom=int(user_message)
            count = count+1
            pickle.dump(count, open("variableStoringFile.dat", "wb"))
            pickle.dump(user_message, open("variableStoringFile5.dat", "wb"))
            return 'Parking Facility (Click 1 for Yes )'
    if user_message!=None:
        count = pickle.load(open("variableStoringFile.dat", "rb"))
        if count == 5:
            # bathroom=int(user_message)
            count = count+1
            pickle.dump(count, open("variableStoringFile.dat", "wb"))
            pickle.dump(user_message, open("variableStoringFile6.dat", "wb"))
            return 'Balacony Availability (Click 1 for Yes )'
    if user_message != None:
        count = pickle.load(open("variableStoringFile.dat", "rb"))
        if count == 6:
            # bathroom=int(user_message)
            count = 0
            pickle.dump(count, open("variableStoringFile.dat", "wb"))
            pickle.dump(user_message, open("variableStoringFile7.dat", "wb"))

            reaname = str(pickle.load(open("variableStoringFile1.dat", "rb")))
            a = reaname[0].upper()
            areaname = a+reaname[1:]
            ssize = (pickle.load(open("variableStoringFile4.dat", "rb")))
            size = int(ssize)
            sbathroom = (pickle.load(open("variableStoringFile2.dat", "rb")))
            bathroom = int(sbathroom)
            sgbhk = (pickle.load(open("variableStoringFile3.dat", "rb")))
            gbhk = int(sgbhk)
            parking=(pickle.load(open("variableStoringFile6.dat", "rb")))
            balcony=(pickle.load(open("variableStoringFile7.dat", "rb")))
            duplex=(pickle.load(open("variableStoringFile5.dat", "rb")))
            print(areaname, size, bathroom, gbhk,parking,balcony,duplex)
            print(type(size))
            input = pd.DataFrame([[areaname, size, bathroom, gbhk,duplex,parking,balcony]], columns=[
                                 'location', 'total_sqft', 'bath', 'bhk','Duplex','Parking','Balcony'])
            answer = (round((pipe.predict(input)[0]*100000), 3))
            if(parking=='0'):
                parking='No'
            else:
                parking='Yes'
        
            if(duplex=='0'):
                duplex='No'
            else:
                duplex='Yes'
        
            if(balcony=='0'):
                balcony='No'
            else:
                balcony='Yes'
            fa = 'The Result\nArea Name:' + \
                str(areaname)+'\nSize:'+str(size) + \
                    '\nParking :' +str(parking)+\
                        '\nBalcony :'+str(balcony)+\
                '\nOur predicted value is : '+str(answer)
            print(answer)
            return fa
