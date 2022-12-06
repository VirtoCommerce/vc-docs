# Overview

Sitemaps are an easy way for webmasters to inform search engines about the pages on their websites that are available for crawling. In its simplest form, a sitemap is an XML file that lists URLs for a website along with additional metadata about each URL, i.e. when it was last updated, how often it usually gets changed, and how important it is in terms of other URLs on the website; thus, the search engines can crawl the website in a more intelligent way.

Web crawlers usually discover pages from links within the website, as well as from other websites. Sitemaps supplement this data to allow crawlers that support Sitemaps to pick up all URLs in the sitemap and learn about those using the associated metadata. Using the sitemap protocol does not guarantee that web pages are included in search engines; however, it provides hints for web crawlers to do a better job while crawling your website.

Virto Commerce provides multiple sitemap files. Each of them must not include more than 10,000 URLs (by default, the maximum value is 50,000 URLs) and must not be larger than 50MB (52,428,800 bytes). Each sitemap file will be placed in the sitemap index file,  `sitemap.xml`. In case the number of records exceeds the maximum, the file will be split into multiple ones, e.g., the  `products.xml`  sitemap file with 15,000 records will be transformed into  `products--1.xml`  (10,000 records) and  `products--2.xml`  (5,000 records). Each of these partial sitemap files will be included in the sitemap index file, too.

## Key Features

+ Getting a sitemap schema and generating a sitemap index file and sitemap files on-the-fly by an API call
+ Scheduling and configuring a recurring job to generate sitemap files
+ Getting a sitemap zip package

## Related Components

To view the source code of Virto Commerce Sitemaps module, check out our  [GitHub repository](https://github.com/VirtoCommerce/vc-module-sitemaps).

To download the latest Sitemaps module release, click [here](https://github.com/VirtoCommerce/vc-module-sitemaps/releases).

## More Info
Read on to learn how to:

+ [Configure sitemaps and create new ones](configuring-sitemaps.md)
+ [Manage sitemap settings](settings.md)
