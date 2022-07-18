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
|5000        |5000          |0         |139             |18              |350             |350             |125                    |375                    |416               |1616           |4367      |5983          |
|6000        |6000          |0         |139             |18              |420             |420             |150                    |450                    |499               |1939           |5272      |7211          |
|7000        |7000          |48        |139             |18              |490             |490             |175                    |525                    |583               |2263           |6128      |8391          |
|8000        |8000          |164       |139             |18              |560             |560             |200                    |600                    |666               |2586           |6918      |9504          |
|9000        |9000          |282       |139             |18              |630             |630             |225                    |675                    |749               |2909           |7705      |10614         |
|10000       |10000         |467       |139             |18              |700             |700             |250                    |750                    |833               |3232           |8424      |11656         |
|11000       |11000         |667       |139             |18              |770             |770             |275                    |825                    |916               |3556           |9129      |12685         |
|12000       |12000         |867       |139             |18              |840             |840             |300                    |900                    |999               |3879           |9834      |13713         |
|13000       |13000         |1067      |139             |18              |910             |910             |325                    |975                    |1082              |4202           |10539     |14741         |
|14000       |14000         |1267      |139             |18              |980             |980             |350                    |1050                   |1166              |4526           |11244     |15770         |
|15000       |15000         |1485      |139             |18              |1050            |1050            |375                    |1125                   |1249              |4849           |11931     |16780         |
|16000       |16021         |1801      |139             |18              |1120            |1120            |400                    |1200                   |1332              |5172           |12520     |17692         |
|17000       |17096         |2135      |139             |18              |1190            |1190            |425                    |1275                   |1416              |5496           |13092     |18588         |
|18000       |18171         |2468      |139             |18              |1260            |1260            |450                    |1350                   |1499              |5819           |13663     |19482         |
|19000       |19246         |2801      |139             |18              |1330            |1330            |475                    |1425                   |1582              |6142           |14235     |20377         |
|20000       |20321         |3134      |139             |18              |1400            |1400            |500                    |1500                   |1666              |6465           |14807     |21272         |
|21000       |21396         |3499      |139             |18              |1470            |1470            |525                    |1575                   |1749              |6789           |15348     |22137         |
|22000       |22471         |3875      |139             |18              |1540            |1540            |550                    |1650                   |1832              |7112           |15876     |22988         |
|23000       |23546         |4251      |139             |18              |1610            |1610            |575                    |1725                   |1915              |7435           |16405     |23840         |
|24000       |24621         |4627      |139             |18              |1680            |1680            |600                    |1800                   |1999              |7759           |16934     |24693         |
|25000       |25696         |5004      |139             |18              |1750            |1750            |625                    |1875                   |2082              |8082           |17463     |25545         |
|26000       |26771         |5380      |139             |18              |1820            |1820            |650                    |1950                   |2165              |8405           |17991     |26396         |
|27000       |27846         |5756      |139             |18              |1890            |1890            |675                    |2025                   |2249              |8729           |18520     |27249         |
|28000       |28921         |6132      |139             |18              |1960            |1960            |700                    |2100                   |2332              |9052           |19049     |28101         |
|29000       |30048         |6527      |139             |18              |2030            |2030            |725                    |2175                   |2415              |9375           |19559     |28934         |
|30000       |31193         |6928      |139             |18              |2100            |2100            |750                    |2250                   |2499              |9699           |20064     |29763         |
|31000       |32338         |7328      |139             |18              |2170            |2170            |775                    |2325                   |2582              |10022          |20568     |30590         |
|32000       |33483         |7729      |139             |18              |2240            |2240            |800                    |2400                   |2665              |10345          |21072     |31417         |
|33000       |34628         |8130      |139             |18              |2310            |2310            |825                    |2475                   |2748              |10668          |21576     |32244         |
|34000       |35773         |8531      |139             |18              |2380            |2380            |850                    |2550                   |2832              |10992          |22081     |33073         |
|35000       |36926         |8934      |139             |18              |2450            |2450            |875                    |2625                   |2915              |11315          |22582     |33897         |
|36000       |38154         |9364      |139             |18              |2520            |2520            |900                    |2700                   |2998              |11638          |23057     |34695         |
|37000       |39382         |9794      |139             |18              |2590            |2590            |925                    |2775                   |3082              |11962          |23532     |35494         |
|38000       |40611         |10224     |139             |18              |2660            |2660            |950                    |2850                   |3165              |12285          |24007     |36292         |
|39000       |41839         |10654     |139             |18              |2730            |2730            |975                    |2925                   |3248              |12608          |24483     |37091         |
|40000       |43067         |11102     |139             |18              |2800            |2800            |1000                   |3000                   |3332              |12931          |24939     |37870         |
|41000       |44295         |11680     |139             |18              |2870            |2870            |1025                   |3075                   |3415              |13255          |25267     |38522         |
|42000       |45524         |12257     |139             |18              |2940            |2940            |1050                   |3150                   |3498              |13578          |25594     |39172         |
|43000       |46752         |12834     |139             |18              |3010            |3010            |1075                   |3225                   |3581              |13901          |25922     |39823         |
|44000       |47980         |13411     |139             |18              |3080            |3080            |1100                   |3300                   |3665              |14225          |26250     |40475         |
|45000       |49209         |13989     |139             |18              |3150            |3150            |1125                   |3375                   |3748              |14548          |26577     |41125         |
|46000       |50437         |14566     |139             |18              |3220            |3220            |1150                   |3450                   |3831              |14871          |26905     |41776         |
|47000       |51665         |15143     |139             |18              |3290            |3290            |1175                   |3525                   |3915              |15195          |27233     |42428         |
|48000       |52894         |15721     |139             |18              |3360            |3360            |1200                   |3600                   |3998              |15518          |27560     |43078         |
|49000       |54122         |16298     |139             |18              |3430            |3430            |1225                   |3675                   |4081              |15841          |27888     |43729         |
|50000       |55350         |16878     |139             |18              |3500            |3500            |1250                   |3750                   |4165              |16164          |28213     |44377         |

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