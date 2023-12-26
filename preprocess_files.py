import config

def split_files():
    count = 0
    uid = []
    f = open("schedule.txt", "r")
    for line in f:
        if line.__contains__("TiplocV1"):
            write_to_file(config.workingDir +"/tiploc.txt", line)
        elif line.__contains__("JsonAssociationV1"):
            write_to_file(config.workingDir +"/JsonAssociation.txt", line)
        elif line.__contains__("JsonScheduleV1"):
            write_to_file(config.workingDir +"/JsonSchedule.txt", line)
        else:
            count +=1

    print(count)

def write_to_file(filename, line):
    f = open(filename, "a")
    f.write("%s" % line)
    f.close()

if __name__ == '__main__':
    split_files()