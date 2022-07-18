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
<table class="table table-bordered table-hover table-condensed">
<thead><tr><th title="Field #1">Gross Salary</th>
<th title="Field #2">Taxable Income</th>
<th title="Field #3">Income Tax</th>
<th title="Field #4">Health Insurance</th>
<th title="Field #5">Social Insurance</th>
<th title="Field #6">Employee Pension</th>
<th title="Field #7">Employer Pension</th>
<th title="Field #8">Employee Education Fund</th>
<th title="Field #9">Employer Education Fund</th>
<th title="Field #10">Employer Severance</th>
<th title="Field #11">Overall Savings</th>
<th title="Field #12">Net Income</th>
<th title="Field #13">Overall Income</th>
</tr></thead>
<tbody><tr>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
</tr>
<tr>
<td align="right">1000</td>
<td align="right">1000</td>
<td align="right">0</td>
<td align="right">31</td>
<td align="right">4</td>
<td align="right">70</td>
<td align="right">70</td>
<td align="right">25</td>
<td align="right">75</td>
<td align="right">83</td>
<td align="right">323</td>
<td align="right">870</td>
<td align="right">1193</td>
</tr>
<tr>
<td align="right">2000</td>
<td align="right">2000</td>
<td align="right">0</td>
<td align="right">62</td>
<td align="right">8</td>
<td align="right">140</td>
<td align="right">140</td>
<td align="right">50</td>
<td align="right">150</td>
<td align="right">166</td>
<td align="right">646</td>
<td align="right">1740</td>
<td align="right">2386</td>
</tr>
<tr>
<td align="right">3000</td>
<td align="right">3000</td>
<td align="right">0</td>
<td align="right">93</td>
<td align="right">12</td>
<td align="right">210</td>
<td align="right">210</td>
<td align="right">75</td>
<td align="right">225</td>
<td align="right">249</td>
<td align="right">969</td>
<td align="right">2610</td>
<td align="right">3579</td>
</tr>
<tr>
<td align="right">4000</td>
<td align="right">4000</td>
<td align="right">0</td>
<td align="right">124</td>
<td align="right">16</td>
<td align="right">280</td>
<td align="right">280</td>
<td align="right">100</td>
<td align="right">300</td>
<td align="right">333</td>
<td align="right">1293</td>
<td align="right">3480</td>
<td align="right">4773</td>
</tr>
<tr>
<td align="right">5000</td>
<td align="right">5000</td>
<td align="right">0</td>
<td align="right">155</td>
<td align="right">20</td>
<td align="right">350</td>
<td align="right">350</td>
<td align="right">125</td>
<td align="right">375</td>
<td align="right">416</td>
<td align="right">1616</td>
<td align="right">4350</td>
<td align="right">5966</td>
</tr>
<tr>
<td align="right">6000</td>
<td align="right">6000</td>
<td align="right">0</td>
<td align="right">186</td>
<td align="right">24</td>
<td align="right">420</td>
<td align="right">420</td>
<td align="right">150</td>
<td align="right">450</td>
<td align="right">499</td>
<td align="right">1939</td>
<td align="right">5220</td>
<td align="right">7159</td>
</tr>
<tr>
<td align="right">7000</td>
<td align="right">7000</td>
<td align="right">48</td>
<td align="right">229</td>
<td align="right">72</td>
<td align="right">490</td>
<td align="right">490</td>
<td align="right">175</td>
<td align="right">525</td>
<td align="right">583</td>
<td align="right">2263</td>
<td align="right">5984</td>
<td align="right">8247</td>
</tr>
<tr>
<td align="right">8000</td>
<td align="right">8000</td>
<td align="right">164</td>
<td align="right">279</td>
<td align="right">142</td>
<td align="right">560</td>
<td align="right">560</td>
<td align="right">200</td>
<td align="right">600</td>
<td align="right">666</td>
<td align="right">2586</td>
<td align="right">6653</td>
<td align="right">9239</td>
</tr>
<tr>
<td align="right">9000</td>
<td align="right">9000</td>
<td align="right">282</td>
<td align="right">329</td>
<td align="right">212</td>
<td align="right">630</td>
<td align="right">630</td>
<td align="right">225</td>
<td align="right">675</td>
<td align="right">749</td>
<td align="right">2909</td>
<td align="right">7320</td>
<td align="right">10229</td>
</tr>
<tr>
<td align="right">10000</td>
<td align="right">10000</td>
<td align="right">467</td>
<td align="right">379</td>
<td align="right">282</td>
<td align="right">700</td>
<td align="right">700</td>
<td align="right">250</td>
<td align="right">750</td>
<td align="right">833</td>
<td align="right">3232</td>
<td align="right">7920</td>
<td align="right">11152</td>
</tr>
<tr>
<td align="right">11000</td>
<td align="right">11000</td>
<td align="right">667</td>
<td align="right">429</td>
<td align="right">352</td>
<td align="right">770</td>
<td align="right">770</td>
<td align="right">275</td>
<td align="right">825</td>
<td align="right">916</td>
<td align="right">3556</td>
<td align="right">8505</td>
<td align="right">12061</td>
</tr>
<tr>
<td align="right">12000</td>
<td align="right">12000</td>
<td align="right">867</td>
<td align="right">479</td>
<td align="right">422</td>
<td align="right">840</td>
<td align="right">840</td>
<td align="right">300</td>
<td align="right">900</td>
<td align="right">999</td>
<td align="right">3879</td>
<td align="right">9090</td>
<td align="right">12969</td>
</tr>
<tr>
<td align="right">13000</td>
<td align="right">13000</td>
<td align="right">1067</td>
<td align="right">529</td>
<td align="right">492</td>
<td align="right">910</td>
<td align="right">910</td>
<td align="right">325</td>
<td align="right">975</td>
<td align="right">1082</td>
<td align="right">4202</td>
<td align="right">9675</td>
<td align="right">13877</td>
</tr>
<tr>
<td align="right">14000</td>
<td align="right">14000</td>
<td align="right">1267</td>
<td align="right">579</td>
<td align="right">562</td>
<td align="right">980</td>
<td align="right">980</td>
<td align="right">350</td>
<td align="right">1050</td>
<td align="right">1166</td>
<td align="right">4526</td>
<td align="right">10260</td>
<td align="right">14786</td>
</tr>
<tr>
<td align="right">15000</td>
<td align="right">15000</td>
<td align="right">1485</td>
<td align="right">629</td>
<td align="right">632</td>
<td align="right">1050</td>
<td align="right">1050</td>
<td align="right">375</td>
<td align="right">1125</td>
<td align="right">1249</td>
<td align="right">4849</td>
<td align="right">10827</td>
<td align="right">15676</td>
</tr>
<tr>
<td align="right">16000</td>
<td align="right">16021</td>
<td align="right">1801</td>
<td align="right">680</td>
<td align="right">703</td>
<td align="right">1120</td>
<td align="right">1120</td>
<td align="right">400</td>
<td align="right">1200</td>
<td align="right">1332</td>
<td align="right">5172</td>
<td align="right">11293</td>
<td align="right">16465</td>
</tr>
<tr>
<td align="right">17000</td>
<td align="right">17096</td>
<td align="right">2135</td>
<td align="right">734</td>
<td align="right">778</td>
<td align="right">1190</td>
<td align="right">1190</td>
<td align="right">425</td>
<td align="right">1275</td>
<td align="right">1416</td>
<td align="right">5496</td>
<td align="right">11736</td>
<td align="right">17232</td>
</tr>
<tr>
<td align="right">18000</td>
<td align="right">18171</td>
<td align="right">2468</td>
<td align="right">788</td>
<td align="right">854</td>
<td align="right">1260</td>
<td align="right">1260</td>
<td align="right">450</td>
<td align="right">1350</td>
<td align="right">1499</td>
<td align="right">5819</td>
<td align="right">12179</td>
<td align="right">17998</td>
</tr>
<tr>
<td align="right">19000</td>
<td align="right">19246</td>
<td align="right">2801</td>
<td align="right">842</td>
<td align="right">929</td>
<td align="right">1330</td>
<td align="right">1330</td>
<td align="right">475</td>
<td align="right">1425</td>
<td align="right">1582</td>
<td align="right">6142</td>
<td align="right">12621</td>
<td align="right">18763</td>
</tr>
<tr>
<td align="right">20000</td>
<td align="right">20321</td>
<td align="right">3134</td>
<td align="right">895</td>
<td align="right">1004</td>
<td align="right">1400</td>
<td align="right">1400</td>
<td align="right">500</td>
<td align="right">1500</td>
<td align="right">1666</td>
<td align="right">6465</td>
<td align="right">13064</td>
<td align="right">19529</td>
</tr>
<tr>
<td align="right">21000</td>
<td align="right">21396</td>
<td align="right">3499</td>
<td align="right">949</td>
<td align="right">1079</td>
<td align="right">1470</td>
<td align="right">1470</td>
<td align="right">525</td>
<td align="right">1575</td>
<td align="right">1749</td>
<td align="right">6789</td>
<td align="right">13476</td>
<td align="right">20265</td>
</tr>
<tr>
<td align="right">22000</td>
<td align="right">22471</td>
<td align="right">3875</td>
<td align="right">1003</td>
<td align="right">1155</td>
<td align="right">1540</td>
<td align="right">1540</td>
<td align="right">550</td>
<td align="right">1650</td>
<td align="right">1832</td>
<td align="right">7112</td>
<td align="right">13876</td>
<td align="right">20988</td>
</tr>
<tr>
<td align="right">23000</td>
<td align="right">23546</td>
<td align="right">4251</td>
<td align="right">1057</td>
<td align="right">1230</td>
<td align="right">1610</td>
<td align="right">1610</td>
<td align="right">575</td>
<td align="right">1725</td>
<td align="right">1915</td>
<td align="right">7435</td>
<td align="right">14275</td>
<td align="right">21710</td>
</tr>
<tr>
<td align="right">24000</td>
<td align="right">24621</td>
<td align="right">4627</td>
<td align="right">1110</td>
<td align="right">1305</td>
<td align="right">1680</td>
<td align="right">1680</td>
<td align="right">600</td>
<td align="right">1800</td>
<td align="right">1999</td>
<td align="right">7759</td>
<td align="right">14675</td>
<td align="right">22434</td>
</tr>
<tr>
<td align="right">25000</td>
<td align="right">25696</td>
<td align="right">5004</td>
<td align="right">1164</td>
<td align="right">1380</td>
<td align="right">1750</td>
<td align="right">1750</td>
<td align="right">625</td>
<td align="right">1875</td>
<td align="right">2082</td>
<td align="right">8082</td>
<td align="right">15075</td>
<td align="right">23157</td>
</tr>
<tr>
<td align="right">26000</td>
<td align="right">26771</td>
<td align="right">5380</td>
<td align="right">1218</td>
<td align="right">1456</td>
<td align="right">1820</td>
<td align="right">1820</td>
<td align="right">650</td>
<td align="right">1950</td>
<td align="right">2165</td>
<td align="right">8405</td>
<td align="right">15475</td>
<td align="right">23880</td>
</tr>
<tr>
<td align="right">27000</td>
<td align="right">27846</td>
<td align="right">5756</td>
<td align="right">1272</td>
<td align="right">1531</td>
<td align="right">1890</td>
<td align="right">1890</td>
<td align="right">675</td>
<td align="right">2025</td>
<td align="right">2249</td>
<td align="right">8729</td>
<td align="right">15874</td>
<td align="right">24603</td>
</tr>
<tr>
<td align="right">28000</td>
<td align="right">28921</td>
<td align="right">6132</td>
<td align="right">1325</td>
<td align="right">1606</td>
<td align="right">1960</td>
<td align="right">1960</td>
<td align="right">700</td>
<td align="right">2100</td>
<td align="right">2332</td>
<td align="right">9052</td>
<td align="right">16274</td>
<td align="right">25326</td>
</tr>
<tr>
<td align="right">29000</td>
<td align="right">30048</td>
<td align="right">6527</td>
<td align="right">1382</td>
<td align="right">1685</td>
<td align="right">2030</td>
<td align="right">2030</td>
<td align="right">725</td>
<td align="right">2175</td>
<td align="right">2415</td>
<td align="right">9375</td>
<td align="right">16649</td>
<td align="right">26024</td>
</tr>
<tr>
<td align="right">30000</td>
<td align="right">31193</td>
<td align="right">6928</td>
<td align="right">1439</td>
<td align="right">1765</td>
<td align="right">2100</td>
<td align="right">2100</td>
<td align="right">750</td>
<td align="right">2250</td>
<td align="right">2499</td>
<td align="right">9699</td>
<td align="right">17016</td>
<td align="right">26715</td>
</tr>
<tr>
<td align="right">31000</td>
<td align="right">32338</td>
<td align="right">7328</td>
<td align="right">1496</td>
<td align="right">1845</td>
<td align="right">2170</td>
<td align="right">2170</td>
<td align="right">775</td>
<td align="right">2325</td>
<td align="right">2582</td>
<td align="right">10022</td>
<td align="right">17383</td>
<td align="right">27405</td>
</tr>
<tr>
<td align="right">32000</td>
<td align="right">33483</td>
<td align="right">7729</td>
<td align="right">1553</td>
<td align="right">1925</td>
<td align="right">2240</td>
<td align="right">2240</td>
<td align="right">800</td>
<td align="right">2400</td>
<td align="right">2665</td>
<td align="right">10345</td>
<td align="right">17750</td>
<td align="right">28095</td>
</tr>
<tr>
<td align="right">33000</td>
<td align="right">34628</td>
<td align="right">8130</td>
<td align="right">1611</td>
<td align="right">2006</td>
<td align="right">2310</td>
<td align="right">2310</td>
<td align="right">825</td>
<td align="right">2475</td>
<td align="right">2748</td>
<td align="right">10668</td>
<td align="right">18117</td>
<td align="right">28785</td>
</tr>
<tr>
<td align="right">34000</td>
<td align="right">35773</td>
<td align="right">8531</td>
<td align="right">1668</td>
<td align="right">2086</td>
<td align="right">2380</td>
<td align="right">2380</td>
<td align="right">850</td>
<td align="right">2550</td>
<td align="right">2832</td>
<td align="right">10992</td>
<td align="right">18484</td>
<td align="right">29476</td>
</tr>
<tr>
<td align="right">35000</td>
<td align="right">36926</td>
<td align="right">8934</td>
<td align="right">1726</td>
<td align="right">2166</td>
<td align="right">2450</td>
<td align="right">2450</td>
<td align="right">875</td>
<td align="right">2625</td>
<td align="right">2915</td>
<td align="right">11315</td>
<td align="right">18847</td>
<td align="right">30162</td>
</tr>
<tr>
<td align="right">36000</td>
<td align="right">38154</td>
<td align="right">9364</td>
<td align="right">1787</td>
<td align="right">2252</td>
<td align="right">2520</td>
<td align="right">2520</td>
<td align="right">900</td>
<td align="right">2700</td>
<td align="right">2998</td>
<td align="right">11638</td>
<td align="right">19175</td>
<td align="right">30813</td>
</tr>
<tr>
<td align="right">37000</td>
<td align="right">39382</td>
<td align="right">9794</td>
<td align="right">1848</td>
<td align="right">2338</td>
<td align="right">2590</td>
<td align="right">2590</td>
<td align="right">925</td>
<td align="right">2775</td>
<td align="right">3082</td>
<td align="right">11962</td>
<td align="right">19502</td>
<td align="right">31464</td>
</tr>
<tr>
<td align="right">38000</td>
<td align="right">40611</td>
<td align="right">10224</td>
<td align="right">1910</td>
<td align="right">2424</td>
<td align="right">2660</td>
<td align="right">2660</td>
<td align="right">950</td>
<td align="right">2850</td>
<td align="right">3165</td>
<td align="right">12285</td>
<td align="right">19830</td>
<td align="right">32115</td>
</tr>
<tr>
<td align="right">39000</td>
<td align="right">41839</td>
<td align="right">10654</td>
<td align="right">1971</td>
<td align="right">2510</td>
<td align="right">2730</td>
<td align="right">2730</td>
<td align="right">975</td>
<td align="right">2925</td>
<td align="right">3248</td>
<td align="right">12608</td>
<td align="right">20158</td>
<td align="right">32766</td>
</tr>
<tr>
<td align="right">40000</td>
<td align="right">43067</td>
<td align="right">11102</td>
<td align="right">2033</td>
<td align="right">2596</td>
<td align="right">2800</td>
<td align="right">2800</td>
<td align="right">1000</td>
<td align="right">3000</td>
<td align="right">3332</td>
<td align="right">12931</td>
<td align="right">20467</td>
<td align="right">33398</td>
</tr>
<tr>
<td align="right">41000</td>
<td align="right">44295</td>
<td align="right">11680</td>
<td align="right">2094</td>
<td align="right">2682</td>
<td align="right">2870</td>
<td align="right">2870</td>
<td align="right">1025</td>
<td align="right">3075</td>
<td align="right">3415</td>
<td align="right">13255</td>
<td align="right">20647</td>
<td align="right">33902</td>
</tr>
<tr>
<td align="right">42000</td>
<td align="right">45524</td>
<td align="right">12257</td>
<td align="right">2133</td>
<td align="right">2737</td>
<td align="right">2940</td>
<td align="right">2940</td>
<td align="right">1050</td>
<td align="right">3150</td>
<td align="right">3498</td>
<td align="right">13578</td>
<td align="right">20881</td>
<td align="right">34459</td>
</tr>
<tr>
<td align="right">43000</td>
<td align="right">46752</td>
<td align="right">12834</td>
<td align="right">2133</td>
<td align="right">2737</td>
<td align="right">3010</td>
<td align="right">3010</td>
<td align="right">1075</td>
<td align="right">3225</td>
<td align="right">3581</td>
<td align="right">13901</td>
<td align="right">21209</td>
<td align="right">35110</td>
</tr>
<tr>
<td align="right">44000</td>
<td align="right">47980</td>
<td align="right">13411</td>
<td align="right">2133</td>
<td align="right">2737</td>
<td align="right">3080</td>
<td align="right">3080</td>
<td align="right">1100</td>
<td align="right">3300</td>
<td align="right">3665</td>
<td align="right">14225</td>
<td align="right">21537</td>
<td align="right">35762</td>
</tr>
<tr>
<td align="right">45000</td>
<td align="right">49209</td>
<td align="right">13989</td>
<td align="right">2133</td>
<td align="right">2737</td>
<td align="right">3150</td>
<td align="right">3150</td>
<td align="right">1125</td>
<td align="right">3375</td>
<td align="right">3748</td>
<td align="right">14548</td>
<td align="right">21864</td>
<td align="right">36412</td>
</tr>
<tr>
<td align="right">46000</td>
<td align="right">50437</td>
<td align="right">14566</td>
<td align="right">2133</td>
<td align="right">2737</td>
<td align="right">3220</td>
<td align="right">3220</td>
<td align="right">1150</td>
<td align="right">3450</td>
<td align="right">3831</td>
<td align="right">14871</td>
<td align="right">22192</td>
<td align="right">37063</td>
</tr>
<tr>
<td align="right">47000</td>
<td align="right">51665</td>
<td align="right">15143</td>
<td align="right">2133</td>
<td align="right">2737</td>
<td align="right">3290</td>
<td align="right">3290</td>
<td align="right">1175</td>
<td align="right">3525</td>
<td align="right">3915</td>
<td align="right">15195</td>
<td align="right">22520</td>
<td align="right">37715</td>
</tr>
<tr>
<td align="right">48000</td>
<td align="right">52894</td>
<td align="right">15721</td>
<td align="right">2133</td>
<td align="right">2737</td>
<td align="right">3360</td>
<td align="right">3360</td>
<td align="right">1200</td>
<td align="right">3600</td>
<td align="right">3998</td>
<td align="right">15518</td>
<td align="right">22847</td>
<td align="right">38365</td>
</tr>
<tr>
<td align="right">49000</td>
<td align="right">54122</td>
<td align="right">16298</td>
<td align="right">2133</td>
<td align="right">2737</td>
<td align="right">3430</td>
<td align="right">3430</td>
<td align="right">1225</td>
<td align="right">3675</td>
<td align="right">4081</td>
<td align="right">15841</td>
<td align="right">23175</td>
<td align="right">39016</td>
</tr>
<tr>
<td align="right">50000</td>
<td align="right">55350</td>
<td align="right">16878</td>
<td align="right">2133</td>
<td align="right">2737</td>
<td align="right">3500</td>
<td align="right">3500</td>
<td align="right">1250</td>
<td align="right">3750</td>
<td align="right">4165</td>
<td align="right">16164</td>
<td align="right">23500</td>
<td align="right">39664</td>
</tr>
</tbody></table>
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