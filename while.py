
#1.1
#My answer
count = 1
while count <= 10:
    print(count, '/n---')
    count += 1

#Clint answer
number = 1
sep = '------'
while number <= 10:
    print(number)
    print(sep)
    number += 1



#1.2
#My answer
download_left = 100
downloaded = 0
while downloaded >= 0:
    if download_left >= 0 and downloaded != 30 and download_left != 50: 
        print('%s%% downloaded, %s%% download_left' % (downloaded, download_left))
    download_left -= 10
    downloaded += 10

#Clint answer
number = 100
dec_by = 10
while number >= 0:
    if number != 50 and number != 30:
        print('%s%% downloaded %s%% remaining.' % (100-number, number))
    number -= dec_by
    
