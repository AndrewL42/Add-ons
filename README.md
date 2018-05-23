# Add-ons
A couple of programs I created to (possibly) use on a Raspberry Pi


Write File:\
  Takes the current date and time, and creates a new file with the date and time as it's name. If the file already exists, it will append to it.\
  For example, "2018-05-22 16-42" would be a file, and as long as it is that date and time it will append to that file. Once a minute passes, it will create a new file.\
  For example, "2018-05-22 16-43" would be a new file.\
  It will save the date and time in the file.\
  The file is saved as a .csv.
  
Email Script:\
  Checks to see if a file is named with the current date and time and a .csv extension (would look for a file named "2018-05-22 16-42.csv").\
  If that file exists, it will email the file to the email inputted.\
  If it doesn't exists, it fails.
