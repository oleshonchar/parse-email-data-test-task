import re


with open('mbox.txt') as f:
    text = f.read()

sender_list = re.findall(r'From: ([\w.-_]+@[\w.-_]+)', text)
date_list = re.findall(r'Date: \w+, (\d+ \w{3} \d{4})', text)
subject_list = re.findall(r'Subject: (.+)', text)

for i in range(len(sender_list)):
    print('{} ({}): {}'.format(sender_list[i], date_list[i], subject_list[i]))

unique_senders = {}
for sender in sender_list:
    if sender in unique_senders:
        unique_senders[sender] += 1
    else:
        unique_senders[sender] = 1

print('\n', '*' * 200, '\n')

for sender in unique_senders:
    print(sender, ':', unique_senders[sender])
