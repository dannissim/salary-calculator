<div id="top"></div>


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/dannissim/salary-calculator">
    <img src="static/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Salary Calculator</h3>

  This app calculates all the payments made given a gross salary, 
  in order to know what to expect to see in a paycheck.
  <p align="center">
    <br />
    <a href="https://github.com/dannissim/salary-calculator/issues">Report Bug</a>
    ·
    <a href="https://github.com/dannissim/salary-calculator/issues">Request Feature</a>
  </p>
</div>



<!-- ABOUT THE PROJECT -->
## About The Project
Do you wonder where exactly your money goes, if you have a given gross salary?  
Many of the online resources are confusing, and many of the online calculators are too complicated to use.  
The aim of this project is to bridge those gaps. Below you can see all the details per gross salary, 
and in the source code and documentation you can learn what exactly happens to you gross salary.
  <p align="right">(<a href="#top">back to top</a>)</p>


### Built With

* [Python 3.10](https://python.org/)
* [Kol Zchut](https://www.kolzchut.org.il/he/%D7%A2%D7%9E%D7%95%D7%93_%D7%A8%D7%90%D7%A9%D7%99)

<p align="right">(<a href="#top">back to top</a>)</p>


### Manual Usage

1. Create a virtual environment (optional):  
    a. `python -m venv venv`  
    b. `venv\Scripts\activate` or in linux `source venv/bin/activate`
2. Install the requirements: `pip install -r requirements.txt`
3. Run `python salary_calculator.py`

## Results

Updated to 2022 Tax Brackets. All the numbers are in Israeli Shekels ₪.

<img src="static/graph.png" alt="Email Notification" max-width="100%" height="auto">


| Gross Salary        | Overall Income        | Net Income        | Overall Savings        | Taxable Income        | Income Tax        | Health Insurance        | Social Insurance        | Employee Pension        | Employer Pension        | Employee Education Fund        | Employer Education Fund        | Employer Severance        |
|---------------------|-----------------------|-------------------|------------------------|-----------------------|-------------------|-------------------------|-------------------------|-------------------------|-------------------------|--------------------------------|--------------------------------|---------------------------|
| <b>1000        </b> | <b>1193          </b> | <b>880       </b> | <b>313            </b> | 1000                  | 0                 | 31                      | 4                       | 60                      | 70                      | 25                             | 75                             | 83                        |
| <b>2000        </b> | <b>2386          </b> | <b>1760      </b> | <b>626            </b> | 2000                  | 0                 | 62                      | 8                       | 120                     | 140                     | 50                             | 150                            | 166                       |
| <b>3000        </b> | <b>3579          </b> | <b>2640      </b> | <b>939            </b> | 3000                  | 0                 | 93                      | 12                      | 180                     | 210                     | 75                             | 225                            | 249                       |
| <b>4000        </b> | <b>4773          </b> | <b>3520      </b> | <b>1253           </b> | 4000                  | 0                 | 124                     | 16                      | 240                     | 280                     | 100                            | 300                            | 333                       |
| <b>5000        </b> | <b>5966          </b> | <b>4400      </b> | <b>1566           </b> | 5000                  | 0                 | 155                     | 20                      | 300                     | 350                     | 125                            | 375                            | 416                       |
| <b>6000        </b> | <b>7159          </b> | <b>5280      </b> | <b>1879           </b> | 6000                  | 0                 | 186                     | 24                      | 360                     | 420                     | 150                            | 450                            | 499                       |
| <b>7000        </b> | <b>8222          </b> | <b>6029      </b> | <b>2193           </b> | 7000                  | 73                | 229                     | 72                      | 420                     | 490                     | 175                            | 525                            | 583                       |
| <b>8000        </b> | <b>9211          </b> | <b>6705      </b> | <b>2506           </b> | 8000                  | 192               | 279                     | 142                     | 480                     | 560                     | 200                            | 600                            | 666                       |
| <b>9000        </b> | <b>10200         </b> | <b>7381      </b> | <b>2819           </b> | 9000                  | 311               | 329                     | 212                     | 540                     | 630                     | 225                            | 675                            | 749                       |
| <b>10000       </b> | <b>11144         </b> | <b>8012      </b> | <b>3132           </b> | 10000                 | 475               | 379                     | 282                     | 600                     | 700                     | 250                            | 750                            | 833                       |
| <b>Gross Salary</b> | <b>Overall Income</b> | <b>Net Income</b> | <b>Overall Savings</b> | <b>Taxable Income</b> | <b>Income Tax</b> | <b>Health Insurance</b> | <b>Social Insurance</b> | <b>Employee Pension</b> | <b>Employer Pension</b> | <b>Employee Education Fund</b> | <b>Employer Education Fund</b> | <b>Employer Severance</b> |
| <b>11000       </b> | <b>12061         </b> | <b>8615      </b> | <b>3446           </b> | 11000                 | 667               | 429                     | 352                     | 660                     | 770                     | 275                            | 825                            | 916                       |
| <b>12000       </b> | <b>12969         </b> | <b>9210      </b> | <b>3759           </b> | 12000                 | 867               | 479                     | 422                     | 720                     | 840                     | 300                            | 900                            | 999                       |
| <b>13000       </b> | <b>13877         </b> | <b>9805      </b> | <b>4072           </b> | 13000                 | 1067              | 529                     | 492                     | 780                     | 910                     | 325                            | 975                            | 1082                      |
| <b>14000       </b> | <b>14786         </b> | <b>10400     </b> | <b>4386           </b> | 14000                 | 1267              | 579                     | 562                     | 840                     | 980                     | 350                            | 1050                           | 1166                      |
| <b>15000       </b> | <b>15676         </b> | <b>10977     </b> | <b>4699           </b> | 15000                 | 1485              | 629                     | 632                     | 900                     | 1050                    | 375                            | 1125                           | 1249                      |
| <b>16000       </b> | <b>16465         </b> | <b>11453     </b> | <b>5012           </b> | 16021                 | 1801              | 680                     | 703                     | 960                     | 1120                    | 400                            | 1200                           | 1332                      |
| <b>17000       </b> | <b>17232         </b> | <b>11906     </b> | <b>5326           </b> | 17096                 | 2135              | 734                     | 778                     | 1020                    | 1190                    | 425                            | 1275                           | 1416                      |
| <b>18000       </b> | <b>17998         </b> | <b>12359     </b> | <b>5639           </b> | 18171                 | 2468              | 788                     | 854                     | 1080                    | 1260                    | 450                            | 1350                           | 1499                      |
| <b>19000       </b> | <b>18763         </b> | <b>12811     </b> | <b>5952           </b> | 19246                 | 2801              | 842                     | 929                     | 1140                    | 1330                    | 475                            | 1425                           | 1582                      |
| <b>20000       </b> | <b>19529         </b> | <b>13264     </b> | <b>6265           </b> | 20321                 | 3134              | 895                     | 1004                    | 1200                    | 1400                    | 500                            | 1500                           | 1666                      |
| <b>Gross Salary</b> | <b>Overall Income</b> | <b>Net Income</b> | <b>Overall Savings</b> | <b>Taxable Income</b> | <b>Income Tax</b> | <b>Health Insurance</b> | <b>Social Insurance</b> | <b>Employee Pension</b> | <b>Employer Pension</b> | <b>Employee Education Fund</b> | <b>Employer Education Fund</b> | <b>Employer Severance</b> |
| <b>21000       </b> | <b>20265         </b> | <b>13686     </b> | <b>6579           </b> | 21396                 | 3499              | 949                     | 1079                    | 1260                    | 1470                    | 525                            | 1575                           | 1749                      |
| <b>22000       </b> | <b>20988         </b> | <b>14096     </b> | <b>6892           </b> | 22471                 | 3875              | 1003                    | 1155                    | 1320                    | 1540                    | 550                            | 1650                           | 1832                      |
| <b>23000       </b> | <b>21710         </b> | <b>14505     </b> | <b>7205           </b> | 23546                 | 4251              | 1057                    | 1230                    | 1380                    | 1610                    | 575                            | 1725                           | 1915                      |
| <b>24000       </b> | <b>22434         </b> | <b>14915     </b> | <b>7519           </b> | 24621                 | 4627              | 1110                    | 1305                    | 1440                    | 1680                    | 600                            | 1800                           | 1999                      |
| <b>25000       </b> | <b>23157         </b> | <b>15325     </b> | <b>7832           </b> | 25696                 | 5004              | 1164                    | 1380                    | 1500                    | 1750                    | 625                            | 1875                           | 2082                      |
| <b>26000       </b> | <b>23880         </b> | <b>15735     </b> | <b>8145           </b> | 26771                 | 5380              | 1218                    | 1456                    | 1560                    | 1820                    | 650                            | 1950                           | 2165                      |
| <b>27000       </b> | <b>24603         </b> | <b>16144     </b> | <b>8459           </b> | 27846                 | 5756              | 1272                    | 1531                    | 1620                    | 1890                    | 675                            | 2025                           | 2249                      |
| <b>28000       </b> | <b>25326         </b> | <b>16554     </b> | <b>8772           </b> | 28921                 | 6132              | 1325                    | 1606                    | 1680                    | 1960                    | 700                            | 2100                           | 2332                      |
| <b>29000       </b> | <b>26049         </b> | <b>16964     </b> | <b>9085           </b> | 29996                 | 6509              | 1379                    | 1681                    | 1740                    | 2030                    | 725                            | 2175                           | 2415                      |
| <b>30000       </b> | <b>26772         </b> | <b>17374     </b> | <b>9398           </b> | 31071                 | 6885              | 1433                    | 1757                    | 1800                    | 2100                    | 750                            | 2250                           | 2499                      |
| <b>Gross Salary</b> | <b>Overall Income</b> | <b>Net Income</b> | <b>Overall Savings</b> | <b>Taxable Income</b> | <b>Income Tax</b> | <b>Health Insurance</b> | <b>Social Insurance</b> | <b>Employee Pension</b> | <b>Employer Pension</b> | <b>Employee Education Fund</b> | <b>Employer Education Fund</b> | <b>Employer Severance</b> |
| <b>31000       </b> | <b>27495         </b> | <b>17783     </b> | <b>9712           </b> | 32146                 | 7261              | 1487                    | 1832                    | 1860                    | 2170                    | 775                            | 2325                           | 2582                      |
| <b>32000       </b> | <b>28218         </b> | <b>18193     </b> | <b>10025          </b> | 33221                 | 7637              | 1540                    | 1907                    | 1920                    | 2240                    | 800                            | 2400                           | 2665                      |
| <b>33000       </b> | <b>28940         </b> | <b>18602     </b> | <b>10338          </b> | 34298                 | 8014              | 1594                    | 1983                    | 1980                    | 2310                    | 825                            | 2475                           | 2748                      |
| <b>34000       </b> | <b>29636         </b> | <b>18984     </b> | <b>10652          </b> | 35433                 | 8412              | 1651                    | 2062                    | 2040                    | 2380                    | 850                            | 2550                           | 2832                      |
| <b>35000       </b> | <b>30326         </b> | <b>19361     </b> | <b>10965          </b> | 36576                 | 8812              | 1708                    | 2142                    | 2100                    | 2450                    | 875                            | 2625                           | 2915                      |
| <b>36000       </b> | <b>30982         </b> | <b>19704     </b> | <b>11278          </b> | 37794                 | 9238              | 1769                    | 2227                    | 2160                    | 2520                    | 900                            | 2700                           | 2998                      |
| <b>37000       </b> | <b>31638         </b> | <b>20046     </b> | <b>11592          </b> | 39012                 | 9664              | 1830                    | 2312                    | 2220                    | 2590                    | 925                            | 2775                           | 3082                      |
| <b>38000       </b> | <b>32293         </b> | <b>20388     </b> | <b>11905          </b> | 40231                 | 10091             | 1891                    | 2398                    | 2280                    | 2660                    | 950                            | 2850                           | 3165                      |
| <b>39000       </b> | <b>32949         </b> | <b>20731     </b> | <b>12218          </b> | 41449                 | 10517             | 1952                    | 2483                    | 2340                    | 2730                    | 975                            | 2925                           | 3248                      |
| <b>40000       </b> | <b>33605         </b> | <b>21074     </b> | <b>12531          </b> | 42667                 | 10944             | 2013                    | 2568                    | 2400                    | 2800                    | 1000                           | 3000                           | 3332                      |
| <b>Gross Salary</b> | <b>Overall Income</b> | <b>Net Income</b> | <b>Overall Savings</b> | <b>Taxable Income</b> | <b>Income Tax</b> | <b>Health Insurance</b> | <b>Social Insurance</b> | <b>Employee Pension</b> | <b>Employer Pension</b> | <b>Employee Education Fund</b> | <b>Employer Education Fund</b> | <b>Employer Severance</b> |
| <b>41000       </b> | <b>34144         </b> | <b>21299     </b> | <b>12845          </b> | 43885                 | 11487             | 2073                    | 2654                    | 2460                    | 2870                    | 1025                           | 3075                           | 3415                      |
| <b>42000       </b> | <b>34656         </b> | <b>21498     </b> | <b>13158          </b> | 45104                 | 12060             | 2133                    | 2737                    | 2520                    | 2940                    | 1050                           | 3150                           | 3498                      |
| <b>43000       </b> | <b>35312         </b> | <b>21841     </b> | <b>13471          </b> | 46322                 | 12632             | 2133                    | 2737                    | 2580                    | 3010                    | 1075                           | 3225                           | 3581                      |
| <b>44000       </b> | <b>35968         </b> | <b>22183     </b> | <b>13785          </b> | 47540                 | 13205             | 2133                    | 2737                    | 2640                    | 3080                    | 1100                           | 3300                           | 3665                      |
| <b>45000       </b> | <b>36624         </b> | <b>22526     </b> | <b>14098          </b> | 48759                 | 13778             | 2133                    | 2737                    | 2700                    | 3150                    | 1125                           | 3375                           | 3748                      |
| <b>46000       </b> | <b>37279         </b> | <b>22868     </b> | <b>14411          </b> | 49977                 | 14350             | 2133                    | 2737                    | 2760                    | 3220                    | 1150                           | 3450                           | 3831                      |
| <b>47000       </b> | <b>37936         </b> | <b>23211     </b> | <b>14725          </b> | 51195                 | 14923             | 2133                    | 2737                    | 2820                    | 3290                    | 1175                           | 3525                           | 3915                      |
| <b>48000       </b> | <b>38591         </b> | <b>23553     </b> | <b>15038          </b> | 52414                 | 15495             | 2133                    | 2737                    | 2880                    | 3360                    | 1200                           | 3600                           | 3998                      |
| <b>49000       </b> | <b>39246         </b> | <b>23895     </b> | <b>15351          </b> | 53632                 | 16068             | 2133                    | 2737                    | 2940                    | 3430                    | 1225                           | 3675                           | 4081                      |
| <b>50000       </b> | <b>39902         </b> | <b>24238     </b> | <b>15664          </b> | 54850                 | 16640             | 2133                    | 2737                    | 3000                    | 3500                    | 1250                           | 3750                           | 4165                      |

### Relevant Documentation
* דמי ביטוח לאומי
  * [כל זכות](https://www.kolzchut.org.il/he/%D7%93%D7%9E%D7%99_%D7%91%D7%99%D7%98%D7%95%D7%97_%D7%9C%D7%90%D7%95%D7%9E%D7%99_%D7%9C%D7%A2%D7%95%D7%91%D7%93_%D7%A9%D7%9B%D7%99%D7%A8)
  * [המוסד לביטוח לאומי](https://www.btl.gov.il/Insurance/Rates/Pages/%D7%9C%D7%A2%D7%95%D7%91%D7%93%D7%99%D7%9D%20%D7%A9%D7%9B%D7%99%D7%A8%D7%99%D7%9D.aspx)
* דמי ביטוח בריאות
  * [כל זכות](https://www.kolzchut.org.il/he/%D7%AA%D7%A9%D7%9C%D7%95%D7%9D_%D7%93%D7%9E%D7%99_%D7%91%D7%99%D7%98%D7%95%D7%97_%D7%91%D7%A8%D7%99%D7%90%D7%95%D7%AA)
  * [המסוד לביטוח לאומי](https://www.btl.gov.il/Insurance/Health_Insurance/Pages/%D7%A9%D7%99%D7%A2%D7%95%D7%A8%D7%99%20%D7%93%D7%9E%D7%99%20%D7%91%D7%99%D7%98%D7%95%D7%97%20%D7%91%D7%A8%D7%99%D7%90%D7%95%D7%AA.aspx)
* נקודות זיכוי
  * [כל זכות](https://www.kolzchut.org.il/he/%D7%A0%D7%A7%D7%95%D7%93%D7%AA_%D7%96%D7%99%D7%9B%D7%95%D7%99)
  * [מחשבון נקודות זיכוי](https://secapp.taxes.gov.il/srsimulatorNZ/#/simulator)
* [מדרגות מס הכנסה](https://www.kolzchut.org.il/he/%D7%9E%D7%93%D7%A8%D7%92%D7%95%D7%AA_%D7%9E%D7%A1_%D7%94%D7%9B%D7%A0%D7%A1%D7%94)
* [ניכוי מס הכנסה מפיצויי פיטורים](https://www.kolzchut.org.il/he/%D7%A0%D7%99%D7%9B%D7%95%D7%99_%D7%9E%D7%A1_%D7%94%D7%9B%D7%A0%D7%A1%D7%94_%D7%9E%D7%A4%D7%99%D7%A6%D7%95%D7%99%D7%99_%D7%A4%D7%99%D7%98%D7%95%D7%A8%D7%99%D7%9D)
* [זיכוי ממס הכנסה בגין הפרשות לביטוח פנסיוני](https://www.kolzchut.org.il/he/%D7%96%D7%99%D7%9B%D7%95%D7%99_%D7%9E%D7%9E%D7%A1_%D7%94%D7%9B%D7%A0%D7%A1%D7%94_%D7%91%D7%92%D7%99%D7%9F_%D7%94%D7%A4%D7%A8%D7%A9%D7%95%D7%AA_%D7%9C%D7%91%D7%99%D7%98%D7%95%D7%97_%D7%A4%D7%A0%D7%A1%D7%99%D7%95%D7%A0%D7%99)
* [פטור ממס הכנסה על הפרשות המעסיק לביטוח פנסיוני ולביטוח אובדן כושר עבודה](https://www.kolzchut.org.il/he/%D7%A4%D7%98%D7%95%D7%A8_%D7%9E%D7%9E%D7%A1_%D7%94%D7%9B%D7%A0%D7%A1%D7%94_%D7%A2%D7%9C_%D7%94%D7%A4%D7%A8%D7%A9%D7%95%D7%AA_%D7%94%D7%9E%D7%A2%D7%A1%D7%99%D7%A7_%D7%9C%D7%91%D7%99%D7%98%D7%95%D7%97_%D7%A4%D7%A0%D7%A1%D7%99%D7%95%D7%A0%D7%99_%D7%95%D7%9C%D7%91%D7%99%D7%98%D7%95%D7%97_%D7%90%D7%95%D7%91%D7%93%D7%9F_%D7%9B%D7%95%D7%A9%D7%A8_%D7%A2%D7%91%D7%95%D7%93%D7%94)
* [פטור ממס הכנסה על הפרשות המעסיק לקרן השלתמות של העובד](https://www.kolzchut.org.il/he/%D7%A7%D7%A8%D7%9F_%D7%94%D7%A9%D7%AA%D7%9C%D7%9E%D7%95%D7%AA#.D7.A4.D7.98.D7.95.D7.A8_.D7.9E.D7.9E.D7.A1_.D7.94.D7.9B.D7.A0.D7.A1.D7.94)

### Notes
* Notice the difference between ניכוי ממס and זיכוי ממס. The difference is:
  * a. ניכוי ממס:  The relevant sum isn't included in the gross salary at all - so it also doesn't get taxed/ insurance isn't paid for this sum.
  * b. זיכוי ממס: This means that the regarded sum grants you a discount off the initial income tax. Ex: You are supposed to pay ₪1000 in income tax but you received a discount of ₪200, then you only need to pay ₪800.

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/amazing-feature`)
3. Commit your Changes (`git commit -m 'Add some amazing feature'`)
4. Push to the Branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Dan Nissim - nissim.dan@gmail.com

Project Link: [https://github.com/dannissim/salary-calculator](https://github.com/dannissim/salary-calculator)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/dannissim/salary-calculator.svg?style=for-the-badge
[contributors-url]: https://github.com/dannissim/salary-calculator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/dannissim/salary-calculator.svg?style=for-the-badge
[forks-url]: https://github.com/dannissim/salary-calculator/network/members
[stars-shield]: https://img.shields.io/github/stars/dannissim/salary-calculator.svg?style=for-the-badge
[stars-url]: https://github.com/dannissim/salary-calculator/stargazers
[issues-shield]: https://img.shields.io/github/issues/dannissim/salary-calculator.svg?style=for-the-badge
[issues-url]: https://github.com/dannissim/salary-calculator/issues
[license-shield]: https://img.shields.io/github/license/dannissim/salary-calculator.svg?style=for-the-badge
[license-url]: https://github.com/dannissim/salary-calculator/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/dan-nissim-2558a785
[product-screenshot]: images/screenshot.png