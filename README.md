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

[//]: # (TODO)
  This app calculates how much of a new deposit to invest in each asset,  
  in order to keep your portfolio as balanced as possible.
  <p align="center">
    <br />
    <a href="https://github.com/dannissim/salary-calculator/issues">Report Bug</a>
    ·
    <a href="https://github.com/dannissim/salary-calculator/issues">Request Feature</a>
  </p>
</div>



<!-- ABOUT THE PROJECT -->
## About The Project
[//]: # (TODO)
app that calculates your monthly salary and your savings after taking off by-law expenses: Pension savings,
"Keren hishtalmut", Health insurance, income tax, social insurance.
Suppose you have a self-managed portfolio, and each month you add a portion of your income to your portfolio.
Suppose as well that you have a target asset allocation. For example:  
| Asset | Target Allocation |
|-------|-------------------|
| VTI   | 64%               |
| VXUS  | 16%               |
| BND   | 20%               |  

Using this app you will know how much of each asset to invest in order to be as close as possible 
to your target allocation - without selling any of your current assets.
<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python 3.10](https://python.org/)
* [Kol Zchut](https://www.kolzchut.org.il/he/%D7%A2%D7%9E%D7%95%D7%93_%D7%A8%D7%90%D7%A9%D7%99)

<p align="right">(<a href="#top">back to top</a>)</p>


## Usage

[//]: # (TODO)
1. Fill `input.json` with:
   1. `target_allocation` - the percent you would like each asset to be in your portfolio.
   2. `deposit_amount` - how many dollars you are adding to your portfolio.
   3. `current_holdings` - How much do you have of each asset currently in your portfolio. 
2. Create a virtual environment (optional):  
    a. `python -m venv venv`  
    b. `venv\Scripts\activate` or in linux `source venv/bin/activate`
3. Install the requirements: `pip install -r requirements.txt`
4. Set the environment variable API_KEY to your Free financial modeling prep API key.
5. Run `python main.py`
6. Then the result will appear in a newly created file `result.json`. 

### Results

[//]: # (TODO)
This app calculates the difference between your portfolio and the portfolio which has the same
market value but with the target allocation, then recommends you to buy the assets in such a way
that brings your portfolio as close as possible to the target portfolio allocation.  
You're welcome to take a look at the [`input.json`](input.json) currently in the repository.  
Here's an example for the content of the `result.json`:
|Gross Salary|Taxable Income|Income Tax|Health Insurance|Social Insurance|Employee Pension|Employer Pension|Employee Education Fund|Employer Education Fund|Employer Severance|Overall Savings|Net Income|Overall Income|
|------------|--------------|----------|----------------|----------------|----------------|----------------|-----------------------|-----------------------|------------------|---------------|----------|--------------|
|0           |0             |0         |0               |0               |0               |0               |0                      |0                      |0                 |0              |0         |0             |
|1000        |1000          |0         |31              |4               |70              |70              |25                     |75                     |83                |323            |870       |1193          |
|2000        |2000          |0         |62              |8               |140             |140             |50                     |150                    |166               |646            |1740      |2386          |
|3000        |3000          |0         |93              |12              |210             |210             |75                     |225                    |249               |969            |2610      |3579          |
|4000        |4000          |0         |124             |16              |280             |280             |100                    |300                    |333               |1293           |3480      |4773          |
|5000        |5000          |0         |155             |20              |350             |350             |125                    |375                    |416               |1616           |4350      |5966          |
|6000        |6000          |0         |186             |24              |420             |420             |150                    |450                    |499               |1939           |5220      |7159          |
|7000        |7000          |48        |229             |72              |490             |490             |175                    |525                    |583               |2263           |5984      |8247          |
|8000        |8000          |164       |279             |142             |560             |560             |200                    |600                    |666               |2586           |6653      |9239          |
|9000        |9000          |282       |329             |212             |630             |630             |225                    |675                    |749               |2909           |7320      |10229         |
|10000       |10000         |467       |379             |282             |700             |700             |250                    |750                    |833               |3232           |7920      |11152         |
|11000       |11000         |667       |429             |352             |770             |770             |275                    |825                    |916               |3556           |8505      |12061         |
|12000       |12000         |867       |479             |422             |840             |840             |300                    |900                    |999               |3879           |9090      |12969         |
|13000       |13000         |1067      |529             |492             |910             |910             |325                    |975                    |1082              |4202           |9675      |13877         |
|14000       |14000         |1267      |579             |562             |980             |980             |350                    |1050                   |1166              |4526           |10260     |14786         |
|15000       |15000         |1485      |629             |632             |1050            |1050            |375                    |1125                   |1249              |4849           |10827     |15676         |
|16000       |16021         |1801      |680             |703             |1120            |1120            |400                    |1200                   |1332              |5172           |11293     |16465         |
|17000       |17096         |2135      |734             |778             |1190            |1190            |425                    |1275                   |1416              |5496           |11736     |17232         |
|18000       |18171         |2468      |788             |854             |1260            |1260            |450                    |1350                   |1499              |5819           |12179     |17998         |
|19000       |19246         |2801      |842             |929             |1330            |1330            |475                    |1425                   |1582              |6142           |12621     |18763         |
|20000       |20321         |3134      |895             |1004            |1400            |1400            |500                    |1500                   |1666              |6465           |13064     |19529         |
|21000       |21396         |3499      |949             |1079            |1470            |1470            |525                    |1575                   |1749              |6789           |13476     |20265         |
|22000       |22471         |3875      |1003            |1155            |1540            |1540            |550                    |1650                   |1832              |7112           |13876     |20988         |
|23000       |23546         |4251      |1057            |1230            |1610            |1610            |575                    |1725                   |1915              |7435           |14275     |21710         |
|24000       |24621         |4627      |1110            |1305            |1680            |1680            |600                    |1800                   |1999              |7759           |14675     |22434         |
|25000       |25696         |5004      |1164            |1380            |1750            |1750            |625                    |1875                   |2082              |8082           |15075     |23157         |
|26000       |26771         |5380      |1218            |1456            |1820            |1820            |650                    |1950                   |2165              |8405           |15475     |23880         |
|27000       |27846         |5756      |1272            |1531            |1890            |1890            |675                    |2025                   |2249              |8729           |15874     |24603         |
|28000       |28921         |6132      |1325            |1606            |1960            |1960            |700                    |2100                   |2332              |9052           |16274     |25326         |
|29000       |30048         |6527      |1382            |1685            |2030            |2030            |725                    |2175                   |2415              |9375           |16649     |26024         |
|30000       |31193         |6928      |1439            |1765            |2100            |2100            |750                    |2250                   |2499              |9699           |17016     |26715         |
|31000       |32338         |7328      |1496            |1845            |2170            |2170            |775                    |2325                   |2582              |10022          |17383     |27405         |
|32000       |33483         |7729      |1553            |1925            |2240            |2240            |800                    |2400                   |2665              |10345          |17750     |28095         |
|33000       |34628         |8130      |1611            |2006            |2310            |2310            |825                    |2475                   |2748              |10668          |18117     |28785         |
|34000       |35773         |8531      |1668            |2086            |2380            |2380            |850                    |2550                   |2832              |10992          |18484     |29476         |
|35000       |36926         |8934      |1726            |2166            |2450            |2450            |875                    |2625                   |2915              |11315          |18847     |30162         |
|36000       |38154         |9364      |1787            |2252            |2520            |2520            |900                    |2700                   |2998              |11638          |19175     |30813         |
|37000       |39382         |9794      |1848            |2338            |2590            |2590            |925                    |2775                   |3082              |11962          |19502     |31464         |
|38000       |40611         |10224     |1910            |2424            |2660            |2660            |950                    |2850                   |3165              |12285          |19830     |32115         |
|39000       |41839         |10654     |1971            |2510            |2730            |2730            |975                    |2925                   |3248              |12608          |20158     |32766         |
|40000       |43067         |11102     |2033            |2596            |2800            |2800            |1000                   |3000                   |3332              |12931          |20467     |33398         |
|41000       |44295         |11680     |2094            |2682            |2870            |2870            |1025                   |3075                   |3415              |13255          |20647     |33902         |
|42000       |45524         |12257     |2133            |2737            |2940            |2940            |1050                   |3150                   |3498              |13578          |20881     |34459         |
|43000       |46752         |12834     |2133            |2737            |3010            |3010            |1075                   |3225                   |3581              |13901          |21209     |35110         |
|44000       |47980         |13411     |2133            |2737            |3080            |3080            |1100                   |3300                   |3665              |14225          |21537     |35762         |
|45000       |49209         |13989     |2133            |2737            |3150            |3150            |1125                   |3375                   |3748              |14548          |21864     |36412         |
|46000       |50437         |14566     |2133            |2737            |3220            |3220            |1150                   |3450                   |3831              |14871          |22192     |37063         |
|47000       |51665         |15143     |2133            |2737            |3290            |3290            |1175                   |3525                   |3915              |15195          |22520     |37715         |
|48000       |52894         |15721     |2133            |2737            |3360            |3360            |1200                   |3600                   |3998              |15518          |22847     |38365         |
|49000       |54122         |16298     |2133            |2737            |3430            |3430            |1225                   |3675                   |4081              |15841          |23175     |39016         |
|50000       |55350         |16878     |2133            |2737            |3500            |3500            |1250                   |3750                   |4165              |16164          |23500     |39664         |

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
  * ניכוי ממס:  The relevant sum isn't included in the gross salary at all - so it also doesn't get taxed/ insurance isn't paid for this sum.
  * זיכוי ממס: This means that the regarded sum grants you a discount off the initial income tax. Ex: You are supposed to pay ₪1000 in income tax but you received a discount of ₪200, then you only need to pay ₪800.

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