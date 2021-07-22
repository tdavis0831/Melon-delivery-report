print("Day 1")
the_file = open("um-deliveries-20140519.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))
the_file.close()


print("Day 2")
the_file = open("um-deliveries-20140520.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))
the_file.close()


print("Day 3")
the_file = open("um-deliveries-20140521.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))
the_file.close()



def produce_report(day, path):

    print("Day", day_num)
    delivery_log = open(path)

    for line in delivery_log:
        line=line.rstrip()
        words=line.split('|')

        melon=words[0]
        count=words[1]
        amount=words[2]

        print(f"Delivered {count} {melon}s for a total of {amount})
    
    delivery_log.close()

produce_report(1, "um-deliveries-20140519.txt")