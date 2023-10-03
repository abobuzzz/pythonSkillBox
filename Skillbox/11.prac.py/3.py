size_file = int(input('Enter file size for download: '))
speed_download = int(input('Enter speed download: '))
procent = 0

while speed_download < size_file - speed_download * procent:
    procent += 1
    download = procent * speed_download
    print('Passed:',procent,'Installed:',download,'from', size_file ,'(',round((download / size_file) * 100, 2),'%)')
else:
    print('Passed', procent + 1,'Installed:',size_file ,'from', size_file ,'(100%)')
    

