# IsMyHamsterRunning
For months I've wondered when and how far my hamster runs. Thanks to an Arduino and this very simple script, I can now find out.
Using the arduino program found in the IMHR directory, it has become very easy to see how many revolutions my hamster, Bartha, makes
on her wheel per night. The circuit used is simple: 3.3 V is fed to a reed switch, whenever Bartha makes a revolution on her wheel, 
a magnet triggers the read switch, feeding a logical 1 to pin 4 on my Arduino Nano. After reading the revolution, the python script,
IsMyHamsterRunningSerialReader, uploads the revolution number and time the revolution was made to an SQLite3 database.
