def say_hello():
    print('Hello, World')

for i in range(5):
    say_hello()


# 
# Your previous Plain Text content is preserved below:
# 
# campaign:
# starts at 8am 07/17 ends at 9am,7/17
# starts at 10am 7/17 ends at 11am, 7/17
#.   ------              -------
# ------      ------
# ^    ^      ^.   ^
# 8    9      10   11
# ...
# start at 8:30 ends at 9:30 => not allowed, it overlaps
# start at 12pm ends at 1pm => allowed. 
# 
# edit function for a campaign
# add a new pair of start and end time
# 
# implement this editCampaign function 
# 
# 8am => 150023213 //secs since epoch
# 9am => 150023213 + 3600 //secs since epoch
# 8:30:10 => 150023213 + 1800 + 10 sec
# 
# editCampaign(campaign:obj, startTime:int, endTime:int)

class Campaign:
    def __int__(self, startTime, endTime):
        self.startTime = startTime
        self.endTime = endTime
    pass

# case 1
# start time cannot conflict between start and end of another campaign
# 8am  -> 12345678
# 9am  -> 13476970  <---- another startime
# 9am  -> 23456789


#case 2
# 7:30am
# 7:59.59 am -< endtime
# 8am  -> 12345678
# 8:30 -> 13476970  <---- another endtime
# 9am  -> 23456789
# return false
# because end time cannot conflict with another campiagn

#campaign : start = 8am, end =9am
#startTime = 6am, endTime = 7am => not overlapping 
# if endTime < campaign.startTime:
#    return False # why false?
schedules = []

def checkCampaign(campaign, startTime, endTime):
    
    if startTime >= campaign.startTime and startTime <= campaign.endTime:
        return False
    if endTime >= campaign.startTime and endTime <= campaign.endTime:
        return False
    if startTime < campaign.startTime and endTime > campaign.endTime:
        return False
    
    return True


def editCampgin(schedules, startTime,endTime):
    
    for schedule in schedules:
        if checkCampaign(schedule, startTime,endTime) == False:
            return False
    return True


def addScheduleToCampaign(startTime,endTime):
    if editCampgin(schedules, startTime, endTime):
        schedules.append(Campaign(startTime,endTime))
    else:
        print("the new scheulde you added was wrong?, double check your schedule")
