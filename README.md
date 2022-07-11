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

[//]: # (TODO)
* [Python 3.9](https://python.org/)
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

### What does it do?

[//]: # (TODO)
This app calculates the difference between your portfolio and the portfolio which has the same
market value but with the target allocation, then recommends you to buy the assets in such a way
that brings your portfolio as close as possible to the target portfolio allocation.  
You're welcome to take a look at the [`input.json`](input.json) currently in the repository.  
Here's an example for the content of the `result.json`:
```json
{
  "current_allocation": {
    "schd": 80.72,
    "vtv": 45.8,
    "upro": 28.14,
    "_cash": -54.66
  },
  "new_allocation": {
    "schd": 74.63,
    "vtv": 48.93,
    "upro": 25.55,
    "_cash": -48.76
  },
  "amount_to_purchase": {
    "_cash": 95,
    "vtv": 6,
    "schd": 2,
    "upro": 0
  }
}
```
In the above example we can see that the app recommends to purchase 6 stocks of VTV, 2 of SCHD and  
the $95 that are left from the deposited amount to leave as cash.  
We can also see that the new allocation is much closer to the targeted allocation than we were beforehand.

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