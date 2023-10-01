

Satya Pratik Srivastava 
AISST
Amity University 
NOIDA
ks201274@gmail.com


**Abstract—Our project began as a hobbyist's quest to capture satellite images. We started with a simple V-dipole antenna, and over several months, progressed to a Yagi antenna and cross Yagi. Despite encountering many challenges, we persevered, and our project eventually evolved into a more serious endeavor to develop a better satellite antenna design.**

**Keywords—Satellite image capture, Antenna design, Noise reduction, Cloud interference, CATIA, MATLAB**


1. # WEATHER  SATELLITE
Weather satellites are satellites that observe the Earth’s weather and climate. They can have different types of orbits: either polar or geostationary. Polar orbiting satellites circle the Earth from pole to pole, while geostationary satellites stay over the same point on the equator. We focused on tracking polar orbiting weather satellites (POES), which are operated by the United States and Russia. The United States has the NOAA series of POES, such as NOAA-15, NOAA-18, NOAA-19, and NOAA-20. Russia has the METEOR series of POES.
1. ## NOAA-15
NOAA-15 is a satellite that collects and transmits data about the Earth’s weather and climate. It was launched by NASA in 1998 and is operated by NOAA, the National Oceanic and Atmospheric Administration [1]. NOAA-15 orbits the Earth from pole to pole, about 807 km above the ground, every 101 minutes. It uses a frequency of 137.62 MHz to send images of the Earth’s surface and atmosphere to ground stations. It also has a high-resolution mode that uses a special antenna to provide more detailed information. NOAA-15 is part of a series of satellites that monitor the weather and climate of the Earth, along with other satellites such as NOAA-18, NOAA-19, NOAA-20, and NOAA-21[2]. These satellites help forecasters predict weather events, such as hurricanes [3], and provide valuable data for climate research.

Orbital parameters


|Reference system|Geocentric|
| - | - |
|Regime|Sun-Synchronous|
|Semi major   axis|7,184.62 Kilometres|
|Eccentricity|` `0.001007|
|Perigee   altitude|804\.6 Kilometres|
|Apogee   altitude|821 Kilometres|
|Inclination|98\.80 degrees|
|Period|` `101.01 minutes|

1. ## NOAA  -18
NOAA-18 is a satellite that collects and transmits data about the Earth's weather and climate. It was launched by NASA on May 20, 2005, and it orbits the Earth from pole to pole, about 854 km above the ground, every 102 minutes. It is part of the Polar-orbiting Operational Environmental Satellite (POES) program, which is operated by NOAA, the National Oceanic and Atmospheric Administration¹. NOAA-18 is equipped with a Microwave Humidity Sounder (MHS), which is a five-channel microwave radiometer that measures water vapor in the atmosphere. MHS is a follow-on to the Advanced Microwave Sounding Unit-B (AMSU-B), which was flown on the previous NOAA-15, -16, and -17 satellites. MHS has improved performance and reliability over AMSU-B and provides more accurate data for weather prediction models²³. MHS works together with other instruments on board NOAA-18, such as the Advanced Very High-Resolution Radiometer (AVHRR), the High-Resolution Infrared Radiation Sounder (HIRS), and the Advanced Microwave Sounding Unit-A (AMSU-A), to provide a comprehensive picture of the Earth's weather and climate⁴.

Orbital parameters🛰️


|Reference system|Geocentric|
| - | - |
|Regime|Sun-Synchronous|
|Semi major   axis|7,230.05 Kilometres|
|Eccentricity|` `0.0014261|
|Perigee   altitude|848 Kilometres|
|Apogee   altitude|869 Kilometres|
|Inclination|99\.17 degrees|
|Period|` `101.97 minutes|



```
```(1) Microwave Humidity Sounder (MHS) | EUMETSAT. https://www.eumetsat.int/mhs.

(2) MW Sounder Humidity Sounding BT CDR | National Centers for .... https://www.ncei.noaa.gov/products/climate-data-records/amsu-b-and-mhs-brightness-temperature.

(3) Climate Data Record (CDR) Program - UMD. http://cics.umd.edu/AMSU-CDR/documentation\_files/CDRP-ATBD-0801%20Rev%201%20AMSU-B\_MHS\_Brightness%20Temp%20C-ATBD%20%2801B-38b%29.pdf.

(4) ESA - About MHS - European Space Agency. https://www.esa.int/Applications/Observing\_the\_Earth/Meteorological\_missions/MetOp/About\_MHS.

(5) Microwave Humidity Sounder (MHS) | EUMETSAT. <https://www.eumetsat.int/mhs>.
```


1. ## NOAA- 19 
NOAA-19 is the final satellite in the Polar-orbiting Operational Environmental Satellite (POES) program, which was a joint effort between the United States National Oceanic and Atmospheric Administration (NOAA) and the National Aeronautics and Space Administration (NASA). NOAA-19 was launched on February 6, 2009, from Vandenberg Air Force Base in California, aboard a Delta II rocket¹. NOAA-19 carries eight instruments that provide data for weather and climate predictions, such as the Advanced Very High Resolution Radiometer (AVHRR/3), the High Resolution Infrared Radiation Sounder (HIRS/4), and the Advanced Microwave Sounding Unit (AMSU-A)². NOAA-19 orbits the Earth from pole to pole, about 850 km above the ground, every 102 minutes³. NOAA-19 is part of a constellation of satellites that monitor the weather and climate of the Earth, along with other satellites such as Suomi NPP and NOAA-20¹. NOAA-19 is expected to operate until at least 2024. 

Orbital parameters 🛰️

|Reference system|Geocentric|
| - | - |
|Regime|Sun-Synchronous|
|Semi major   axis|7,230.910 Kilometres|
|Eccentricity|` `0. 0013582|
|Perigee   altitude|850 Kilometres|
|Apogee   altitude|869 Kilometres|
|Inclination|99\.97 degrees|
|Period|` `101.99 minutes|

```
(1) NOAA-19 - Wikipedia. https://en.wikipedia.org/wiki/NOAA-19.

(2) WMO OSCAR | Satellite: NOAA-19. https://space.oscar.wmo.int/satellites/view/noaa\_19.

(3) NOAA-19 - NASA. https://mobile.arc.nasa.gov/public/iexplore/missions/pages/51.htm.

(4) History of NOAA Satellites | NESDIS. https://www.nesdis.noaa.gov/current-satellite-missions/history-of-noaa-satellites.

(5) undefined. <https://www.bou.class.noaa.gov/saa/products/welcome>.
```


1. ## NOAA -20
NOAA-20 is a satellite that observes the Earth's weather and climate. It is the first satellite in the Joint Polar Satellite System (JPSS), which is a collaboration between NOAA and NASA. NOAA-20 was launched in 2017 and orbits the Earth from pole to pole, about 830 km above the ground, every 101 minutes. It carries five instruments that measure various aspects of the Earth's atmosphere, surface, and radiation. These instruments provide data for weather forecasting, climate monitoring, and environmental research. NOAA-20 is part of a constellation of satellites that work together to provide a comprehensive picture of the Earth's weather and climate, along with other satellites such as Suomi NPP and NOAA-21¹²³⁴. 

Orbital parameters🛰️


|Reference system|Geocentric|
| - | - |
|Regime|Sun-Synchronous|
|Semi major   axis|7,184.62 Kilometres|
|Eccentricity|0\.001007|
|Perigee   altitude|824 Kilometres|
|Apogee   altitude|833 Kilometres|
|Inclination|99\.79 degrees|
|Period|` `101.44 minutes|


```
(1) NOAA-20 - Wikipedia. https://en.wikipedia.org/wiki/NOAA-20.

(2) WMO OSCAR | Satellite: NOAA-20. https://space.oscar.wmo.int/satellites/view/noaa\_20.

(3) JPSS-1/NOAA-20 - eoPortal. https://www.eoportal.org/satellite-missions/noaa-20.

(4) NOAA-20 VIIRS - National Oceanic and Atmospheric Administration. https://ncc.nesdis.noaa.gov/NOAA-20/NOAA20VIIRS.php.

(5) undefined. http://www.jpss.noaa.gov/.

(6) undefined. <https://www.avl.class.noaa.gov/saa/products/welcome>.
```

1. ## NOAA-21
NOAA-21 is a satellite that observes the Earth's weather and climate. It is the second satellite in the Joint Polar Satellite System (JPSS), which is a collaboration between NOAA and NASA. NOAA-21 was launched on November 10, 2022, and orbits the Earth from pole to pole, about 833 km above the ground, every 102 minutes. It carries four instruments that measure various aspects of the Earth's atmosphere, surface, and radiation. These instruments provide data for weather forecasting, climate monitoring, and environmental research. NOAA-21 is part of a constellation of satellites that work together to provide a comprehensive picture of the Earth's weather and climate, along with other satellites such as Suomi NPP and NOAA-20¹²³⁴.

Orbital parameters🛰️

|Reference system|Geocentric|
| - | - |
|Regime|Sun-Synchronous|
|Semi major   axis|7,230.91 (planned)Kilometres|
|Eccentricity|0\.0013582 (planned)|
|Perigee   altitude|850 (planned)Kilometres|
|Apogee   altitude|869 (planned) Kilometres|
|Inclination|99\.97 degrees|
|Period|` `101.99 minutes|




```
(1) NOAA-21 - Wikipedia. https://en.wikipedia.org/wiki/NOAA-21.

(2) First Images Released From NOAA-21 VIIRS Instrument | NASA. https://www.nasa.gov/image-feature/first-images-released-from-noaa-21-viirs-instrument/.

(3) Earth looks stunning in full view from the NOAA-21 satellite | photos .... https://www.space.com/first-full-earth-image-noaa-21-instrument.

(4) SVS: NOAA-21, NOAA-20, and Suomi NPP satellite orbits. https://svs.gsfc.nasa.gov/cgi-bin/details.cgi?aid=5021&button=recent.

(5) undefined. http://www.jpss.noaa.gov/.
```
1. # Purpose   and  Functions
NOAA, the National Oceanic and Atmospheric Administration, is a federal agency that works to understand and protect the Earth's oceans and atmosphere. NOAA has three main functions: providing environmental information, stewardship, and research. 

- NOAA provides environmental information products to its customers and partners, such as weather warnings and forecasts, climate data, ecosystem assessments, and commerce statistics. These products help people make informed decisions about their safety, health, and well-being. NOAA delivers these products through the National Weather Service and other offices and programs.
- NOAA provides environmental stewardship services to conserve and manage the U.S. coastal and marine resources. NOAA works with federal, state, local, tribal, and international authorities to regulate fisheries and marine sanctuaries, protect threatened and endangered marine species, restore habitats, and respond to emergencies. NOAA oversees these services through the National Marine Fisheries Service, the Office of National Marine Sanctuaries, the Office of Protected Resources, and other offices and programs.
- NOAA conducts applied scientific research to improve its understanding of the Earth's ecosystems, climate, weather, water, and commerce and transportation. NOAA aims to provide accurate and objective scientific information that can support policy-making, innovation, and education. NOAA conducts this research through the Office of Oceanic and Atmospheric Research, the National Environmental Satellite Data and Information Service, the National Ocean Service, and other offices and programs.

NOAA's mission is to understand and predict changes in the Earth's environment and conserve and manage coastal and marine resources to meet our nation's economic, social, and environmental needs. 
1. ## Automatic Picture Transmission(APT)
APT, or Automatic Picture Transmission, is a system that allows weather satellites to send images of the Earth's surface and atmosphere to ground stations. APT was developed in the 1960s and has been used by many countries for weather forecasting and research. APT uses analog signals that can be received by low-cost equipment, such as radios and antennas. APT images are transmitted on frequencies around 137 MHz, which can be picked up by anyone with a suitable receiver. APT satellites orbit the Earth from pole to pole, about 840 km above the ground, and scan the Earth continuously. Each satellite passes over the same location twice a day, providing local data to users. APT images are composed of two frames, one in visible light and one in infrared, which can be combined to create color images. APT images also include synchronization and telemetry information, which help decode the image data and identify the satellite source. APT is an old but reliable system that has provided valuable information about the Earth's weather and climate for decades.



```
(1) APT Weather Satellite Reception - geo-web.org.uk. http://www.geo-web.org.uk/apt.php.

(2) Automatic picture transmission - Wikipedia. https://en.wikipedia.org/wiki/Automatic\_Picture\_Transmission.

(3) RTL-SDR Tutorial: Receiving NOAA Weather Satellite Images. https://www.rtl-sdr.com/rtl-sdr-tutorial-receiving-noaa-weather-satellite-images/.

(4) NOAA & Meteor APT and LRPT RECEPTION - USRadioguy.com. https://usradioguy.com/noaa-apt-reception/.
```
1. # Antenna
Antennas have evolved from simple telescopic antennas to more sophisticated designs such as dipoles, yagis, cross yagis, and turnstiles. Each design has its own advantages and disadvantages, making it suitable for different applications. Experiment and fabrication were carried out on all of the following antennas. 

1. ## Single telescopic antennas
Single telescopic antennas for NOAA are antennas that consist of a single metal rod or wire that is connected to a radio receiver or transmitter. They are designed to receive the signals from the NOAA weather satellites that orbit the Earth at about 840 km above the ground and transmit on frequencies around 137 MHz. Single telescopic antennas for NOAA have some advantages and disadvantages compared to other types of antennas, such as dipole, yagi, cross yagi, and turnstile antennas.

Some of the advantages of single telescopic antennas for NOAA are:

- They are simple and compact, requiring only one element and no ground plane or counterpoise.
- They are easy and cheap to make, requiring only a metal rod or wire of the appropriate length and a coaxial cable to connect it to the receiver or transmitter.
- They can be easily adjusted by changing the length of the rod or wire to tune to different frequencies.

Some of the disadvantages of single telescopic antennas for NOAA are:

- They have low efficiency and narrow bandwidth, meaning that they do not receive or transmit much power and can only operate on a small range of frequencies.
- They have low gain and omnidirectional radiation pattern, meaning that they do not amplify or focus the signals in any direction and receive or transmit equally in all directions.
- They are horizontally polarized, meaning that they are sensitive to the orientation of the electric field of the electromagnetic waves. This can cause problems when receiving circularly polarized signals from the NOAA satellites, which can have any orientation depending on their position in the sky.

This paper presents the design and performance of single telescopic antennas for NOAA applications, considering three main parameters: length, impedance, and SWR.

1. Length: The length of the rod or wire determines the resonant frequency of the antenna, which is the frequency at which the antenna has maximum efficiency and minimum impedance. The length should be equal to a quarter of the wavelength of the resonant frequency, which can be calculated by dividing the speed of light by the frequency. For example, for 137 MHz, the wavelength is approximately 2.18 m and the length should be approximately 0.55 m.
1. Impedance: The impedance is a measure of how well the antenna matches with the radio device. It depends on several factors, such as the diameter and material of the rod or wire, the distance from the ground, and the type and length of the coaxial cable. The impedance should be as close as possible to 50 ohms, which is the standard impedance for most radio devices. If the impedance is too high or low, some power will be reflected back to the source and cause losses and interference. The impedance can be adjusted by using an antenna tuner or a matching network.
1. SWR: The SWR (standing wave ratio) is a ratio of the maximum and minimum voltages along the antenna. It indicates how well the antenna is matched with the radio device. The SWR should be as close as possible to 1:1, which means that there is no reflection and all power is transferred. If the SWR is too high, some power will be reflected back to the source and cause losses and interference. The SWR can be measured by using an SWR meter or an antenna analyzer.

1. ## V-Dipole Antennas
A dipole antenna is a type of antenna that consists of two metal rods or wires of equal length that are connected to a radio device at the center. It is a simple and common antenna that can receive signals from the NOAA weather satellites that orbit the Earth at about 840 km above the ground and transmit on frequencies around 137 MHz. A dipole antenna has some advantages and disadvantages compared to other types of antennas, such as single telescopic, yagi, cross yagi, and turnstile antennas.

Some of the advantages of a dipole antenna are:

- It has a higher efficiency and a wider bandwidth than a single telescopic antenna, meaning that it can receive or transmit more power and operate on a larger range of frequencies.
- It does not need a ground plane or a counterpoise, as it is balanced, meaning that it can be mounted at any height above the ground without affecting its performance.
- It is easy and cheap to make, requiring only two metal rods or wires of the appropriate length and a coaxial cable to connect them to the radio device.

Some of the disadvantages of a dipole antenna are:

- It has a low gain and a bidirectional radiation pattern, meaning that it does not amplify or focus the signals in any direction and receives or transmits equally in two opposite directions.
- It is linearly polarized, meaning that it is sensitive to the orientation of the electric field of the electromagnetic waves. This can cause problems when receiving circularly polarized signals from the NOAA satellites, which can have any orientation depending on their position in the sky.
1. Length: The length of each rod or wire determines the resonant frequency of the dipole antenna, which is the frequency at which the antenna has maximum efficiency and minimum impedance. The length should be equal to a quarter of the wavelength of the resonant frequency, which can be calculated by dividing the speed of light by the frequency. For example, to receive signals from the NOAA satellites that transmit on frequencies around 137 MHz, the length of each rod or wire should be about 0.55 m.

1. Impedance: The impedance of the dipole antenna is a measure of how well the antenna matches with the radio device. The impedance depends on several factors, such as the diameter and material of each rod or wire, the distance between them, and the type and length of the coaxial cable. The impedance should be as close as possible to 50 ohms, which is the standard impedance for most radio devices. If the impedance is too high or low, then some power will be reflected back to the source and cause losses and interference. The impedance can be adjusted by using an antenna tuner or a matching network.

1. SWR: The SWR (standing wave ratio) of the dipole antenna is a ratio of the maximum and minimum voltages along the antenna. It indicates how well the antenna is matched with the radio device. The SWR should be as close as possible to 1:1, which means that there is no reflection and all power is transferred. If the SWR is too high, then some power will be reflected back to the source and cause losses and interference. The SWR can be measured by using an SWR meter or an antenna analyser.

1. ## Yagi Anetnenna
A Yagi antenna is a very popular form of antenna where gain and directivity are required. It is also known as a Yagi-Uda antenna, after its two Japanese inventors Hidetsugu Yagi and Shintaro Uda. The antenna design was first presented in 1928 by Yagi, who wrote the papers in English and brought the design to the international attention. The antenna has many applications in domestic and professional settings, such as television reception, radio communication, radar, and wireless networking.

The basic structure of a Yagi antenna consists of a driven element, which is connected to the transmitter or receiver, and one or more parasitic elements, which are not connected to the source. The parasitic elements are usually arranged in a line perpendicular to the driven element, and can be classified into two types: reflectors and directors. A reflector is a parasitic element that is slightly longer than the driven element, and is placed behind it. A reflector reflects the radio waves from the driven element back to the same direction, increasing the signal strength. A director is a parasitic element that is slightly shorter than the driven element, and is placed in front of it. A director directs the radio waves from the driven element to a narrower angle, increasing the directivity. By adding more directors, the antenna can achieve higher gain and directivity.

- Basic Design:

#####
![[Pasted image 20231001195854.png]]
Figure: Design of Yagi Antenna

- Driven element:  

This is the element in the Yagi  antenna  that  is  supplied  with  power.  There   are two types of dipole:  half wave dipole   and  folded  dipole.

`  `Half wave dipole is half wavelength  long.  The radiation pattern of half  wave  dipole  is   as  follows.

![[Pasted image 20231001195905.png]]
Figure.  Radiation pattern  of  half  wave  dipole

Folded wave dipole  is  the  one  with  two  conductors  connected  on  both  sides   and  folded  to  form   a  cylindrical  closed  shape  in  which  power  is  supplied   at  the  centre.  The radiation pattern of   a folded dipole  is  the  same   as  that  of   a  half  wave  dipole   antenna.  One of the  main  reasons  for  using  the  folded  dipole   antenna  is  the  increase  in  feed  impedance  that  it  provides.  If the conductors  in  the  main  dipole   and  the  second  or  "fold"  conductor   are  the  same  diameter,  then  it  is  found  that  there  is   a  fourfold  increase  (i.e.  two squared) in  the  feed  impedance.



- Reflectors:  

The reflector is made  to  be  5%longer  than  the  dipole.  The Yagi antenna  has  only  one  reflector  which  is  placed  behind  the  dipole  which  prevents   any  interference  pickups  from  behind.  Many times,  there  is   a  reflector  plate  used  instead  of a rod  to  improve  the  performance.  Typically,   a  reflector   adds  -5  dB  of  gain  in  the  forward  direction.

- Director:  

Directors   are  made  shorter  than  the  dipole.  The  directors   are  placed  before  the  dipole  in  the  direction  of  maximum  sensitivity.  Typically,  each  director   adds  1  dB  of  gain  in  the  forward  direction  which  however  reduces   as  the  no.  of  directors  increases.
![[Pasted image 20231001195913.png]]
Figure.  Yagi antenna  Radiation  pattern

The radiation  pattern  of  the  Yagi  antenna  comprises   a  main  forward  lobe   and   a  number  of  side  lobes   and   a  rear  lobe.The  main  rear  lobe  is  caused  by  the  radiation  due  to  the  reflector.  The   antenna can  be  optimised  to  either  reduce  radiation  in  reverse  direction  by   altering  the  length   and  spacing  of  the  reflector  or  it  can  be  optimised  to  produce  maximum  level  of  forward  gain.  Unfortunately the two  conditions  can’t  be  optimised   at  the  same  time  hence   a  compromise  is  to  be  made  depending  upon  the   application.  It  is  necessary  to  choose  either   a  maximum  front  to  back  ratio  or  maximum  forward  gain.
![[Pasted image 20231001195922.png]]
Figure.  The Yagi antenna used.

Antenna Dimensions:

FREQUENCY OF OPERATION   :  138MHz

DIAMETER OF  PARASITIC  ELEMENTS(mm)  :  10

GAIN  OF  ANTENNA                    :  7.99  dBd

REFLECTOR LENGTH                :  1048  mm

REFLECTOR POSITION              :  0  mm

DIPOLE  POSITION                      :  522  mm

DIRECTOR    #1  POSITION         :  685  mm

DIRECTOR    #1  LENGTH            :  988  mm

DISTANCE  DIR.  #1                      :  163mm

DIRECTOR    #2  POSITION         :  1076  mm

DIRECTOR    #2  LENGTH            :  979  mm

DISTANCE  DIR.  #1    -  dir.  #2    :  391  mm

DIRECTOR    #3  POSITION         :  1543  mm

DIRECTOR    #3  LENGTH            :  970  mm

DISTANCE  DIR.  #2    -  dir.  #3    :  467  mm

We  formulated   a  design  of  the  model  on  CATIA  with   all  the  dimensions  considered  before  constructing  it  so  that  we  have   an  idea  of  how  our  finished  model  should  look  like.
![[Pasted image 20231001195958.png]]
Figure.  CATIA model  of  Yagi-Uda   antenna*



##### We started with   a  V-Dipole   antenna   and  then  switched  to   a  5  element  Yagi-Uda   antenna.  The image quality  improved  drastically  which  has  been  discussed  in  the  minor  project  report.  Now the data transmission we  were  receiving  was  right  hand  circularly  polarized   and   as  we  can  see  from  the  radiation  pattern  of  the  half  wave  dipole,  having  radiation  in  one  plane,  we  could  not  receive  the  whole  of  the  signal  using  this   antenna.  Hence  we  switched  to  Cross-Yagi  antenna.  
1. ## *CROSS  Yagi 
![[Pasted image 20231001200040.png]]
- Figure.  Our Cross  Yagi antenna

The  basic  design  of  the  Cross  Yagi  antenna  is  similar  to  that  of  the  Yagi-Uda   antenna.  There’s   an   addition  of   a  set  of  elements  in  the  perpendicular  direction.  For  mechanical  simplifications  in  the  design   an  offset  is  maintained  between  the  two  sets.

Cross  Yagi  antennas  can  be  used  for  two  purposes:  Satellite  work  or  if  you  need  both  vertical   and  horizontal  polarization  for  terrestrial  contacts.  Two  different  feeding  mechanisms  can  be  used:  always  cross  polarization  or  switchable  for  vertical,  horizontal   and  RHS  polarization.

Depending  upon  the  feeding  mechanism  there   are  various  mountings  that  can  be  used  in  Cross  Yagi  antenna:

- The  ‘X’  mounting  is  recommended,  if  you  wish   not to  switch  between  the  polarizations  because  it  is  hard  to  get  horizontal   and  vertical  polarizations.  The   antenna  is   always  in  the  circular  polarization  mode.![[Pasted image 20231001200056.png]]


- The  ‘cross’  mounting  is  useful  for having  two  separate  coax-cables  for  each  plane   and   a  phasing  box  for  horizontal, vertical   and  circular  polarization.  For the  right  phase  shift  of  90°  two  mounting  methods   are  possible:  firstly we can either  mount the two planes with  a difference of lambda/4  on  the  boom  or   as  close   as  possible   and  then  use   a  coax  cable  which  is  lambda/4  longer  for  one  plane  for  the  90°  shift.![[Pasted image 20231001200104.png]]


- Another type of feeding mechanism is shown in figure 3. We may have two different sets of Yagi antennas mounted on the same pole  as seen in the image, one in horizontal plane  and the other in vertical plane. However this creates a space issue. Two separate cables  and the phasing box  are required. It must be  assured that the coax wires  are of same length for the both panes![[Pasted image 20231001200111.png]]





We  required   a  right  hand  circular  polarization  for  our  data  reception,  hence  following  circuit  was  used:
![[Pasted image 20231001200119.png]]
Figure.  Circuit  for  right-hand  circular  polarization  (RHCP)

The  horizontal  dipole  is  connected  to  a  vertical  dipole  with   a  phasing  line  of   a  quarter  wave  of  50Ohm-coax.  At this  point  the  impedance  is  25  Ohm,  which  is  transformed  to  50  Ohm   again  with  two  parallel  75  Ohm  quarter  wave  cables.  The  phase  shift  between  two  parallel  D1/D2   and  D3/D4  is  +90°.  It  is  possible  to  run two  cables  from  each  plane  to  the  station  with  the  box  for  circular  polarization.

Our Design:

We formulated a design of our model on CATIA with  all the dimensions feeded so  as to get  an idea of how our finished model should look like.
![[Pasted image 20231001200132.png]]
Figure.  CATIA model  of  Cross  Yagi antenna

![[Pasted image 20231001200142.png]]
Figure.  The  Crossed  Yagi antenna  used  in  the  major  project

The dimensions   are  the  same   as  the   antenna  used  in  the  minor  project.  There’s   an  offset  in  the  vertical  plane  elements  of  5mm  to   attach  them  on  the  central  boom.  The central boom  is  taken  to  be  of  rectangular  cross-section  because  it  provides  mechanical   advantage  of  easily   attaching  the  elements  in  place  of  circular  cross-section.  Apart from this, the rods taken   as elements   are   also tubes  now   as  it  reduces  weight   and  the  charge  concentration  is  purely  on  the  surface  hence  there  was  no  difference  in  power.  The dipoles of the two planes   are   attached using the  right  circular  hand  polarization  circuit   and  the  output  cable  is   attached  to  RTL-SDR.

1. # Result
High clouds   appear  white,  lower  clouds  gray  or  land/sea  coloured,  clouds  generally   appear  lighter,  but  distinguishing  between  land/sea   and  low  cloud  may  be  difficult.  Darker  colours  indicate  warmer  regions
# ![[Pasted image 20231001200155.png]]
##### **Figure.** Image  of  clouds  over  Indian  subcontinent.
![[Pasted image 20231001200222.png]]
##### Figure.  Map  of  the   area  swept  by  the  satellite  NOAA.
![[Pasted image 20231001200343.png]]
Figure.  Image  of  Middle-West  Countries   and  their  shoreline

NOAA  colour  IR  contrast  enhancement  option.  Greatly  increases  contrast  in  the  darker land/sea  regions   and  colours  the  cold  cloud  tops.  allows  fine  detail  in  land   and  sea  to  be seen   and  provides   a  very  readable  indication  of  cloud  top  temperatures.  This  enhancement  option  is  temperature  normalised.








