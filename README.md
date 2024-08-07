# eBay_3ds_EDA

- Created a web scraper using the requests and beautiful soup libraries
- Conducted data cleaning and feature engineering with Pandas 
- Parsed through text to create features such as region, limited edition, and bundles
- Analyzed and created visualizations such as bar graphs and scatter plots for the data

## Data
- Data was scraped from eBay on May 24, 2024
- The data is from an eBay search of new nintendo 3ds Xl, filtering for sold items

## Cleaning
- converted price and shipping columns to type double using regex
- removed listings with multiple listings within it as they had price ranges
- created the region column, Limited column, and the bundle column from the title column

## Analysis

- Used Group by to isolate for specific variables in order to visualize the relationship between them
- Visualizations done with Matplotlib

### Conclusion:
From the graphs, a few insights emerge:
1. American versions of the console are more expensive on average compared to their japanese counterparts. In particular, the most commonly listed condition, pre-owned consoles, Japanese consoles are significantly cheaper than American consoles. On average, a pre-owned New Nintendo 3ds LL is about 30% cheaper than a pre-owned New Nintendo 3ds XL
2. About 89% of all listings are pre-owned, with the majority of the listings being the Japanese version. This could be the reason as to why the New Nintendo 3ds LL are priced lower to their American counterpart. Nintendo sold 4.93 million New Nintendo 3ds LL in Japan and 4.40 million New Nintendo 3ds Xl in The Americas, which Nintendo defines as both North and South America. The similar number of units sold in both regions do not align with the numbers of listings per region. A possible explanation for this could be the smaller demand for resale in Japan due to their larger sales per capita, and as a result there is now an excess of supply in Japan coming to the Americas via eBay. 
3. Around 22% of all listings have free shipping, with New 3ds LL listings accounting for around 74% of the free shipping listings. Furthermore, on average, every Japanese version has cheaper shipping per condition compared to American version listings, despite international shipping fees being higher than domestic shipping fees. Only 10% of XL listings 
### Possible Issues:
There were a few omitted factors in this notebook:
1. Due to the complexity, I have opted to omit listings which sell multiple versions in one listing. These listings often have multiple colours, ranging from commonly sold colours to limited edition ones, resulting in a large difference in price. For the most part these limited edition consoles have also been omitted as outliers, as they are worth astronomically more than a standard 3ds
2. Japanese 3ds are "region locked" and do not have an option to change the system language. The only way to undo the region lock is to "jailbreak" the console and install custom firmware. This could contribute to the lower prices on Japanese consoles, as American consoles do not require any software modifications. 
3. The notebook specifically compares the prices of non-auction listings as the price of these auctions are not set and change until the auction finishes. As a result, these prices are inaccurate and have been removed from the analysis, but auctions with very little time left have also been removed, which could have been an accurate reflection of the price.
4. A few of these listings are bundles, particularly the ones with an unknown condition, which can include other accessories and physical games which would raise the listing price. In the future I would like to construct a webscraper that is able to determine which listings are bundles to provide a more accurate visualization. 
5. Pre-Owned listings have their own internal quality condition, which some sellers provide photos, and sometimes their own personal grading scale. As a result, some pre-owned listings can be considered nearly brand-new and some can also be considered as nearly parts-only, which affects their price. That being said, many of the listings are posted in an "acceptable" condition, with minimal scratches and fully functioning buttons. 