# Overview

Virto Commerce Marketing is a dedicated module for managing various marketing activities, campaigns, and promotions you may run within your online store. This section will guide you through its key features and concepts, and will briefly tell you how to work with those.

## Related Components
To view the source code of Virto Commerce Marketing module, check out our [GitHub repository](https://github.com/VirtoCommerce/vc-module-marketing).

To download the latest Marketing module release, click [here](https://github.com/VirtoCommerce/vc-module-marketing/releases).

## Key Features
Virto's Marketing module provides the following key features:
 
+ Managing [dynamic content](#dynamic-content) for Storefront
+ Managing [published content](#working-with-dynamic-content)
+ Creating and running [promotions](#promotions)

## Dynamic Content

The Dynamic Content feature allows you to create personalized shopping experiences for customers. Using this feature, you can deliver elements of shopping experience based on a set of conditions or context.

When displaying Dynamic Content to your customers, you will need to consider the following:

* Type of content you are going to display
* Target audience who will see the content
* Time frame within which the content will be visible
* Content location (which part of the webpage will house the content in question)

Dynamic Content is configurable through Virto Commerce Platform Manager, which means your marketing team can set it up without any developer or system admin effort. For images or Flash animations, they may need a graphic designer to create a file and upload it to Assets. However, once this is done, marketing can configure rules for displaying content without any assistance from technical teams.

Dynamic Content consists of four independent components:

+ ***Dynamic Content***
+ ***Published Content***
+ ***Content Type***
+ ***Content Placeholder***

The first two components, ***Dynamic Content*** and ***Published Content***, can be configured through Virto Commerce Platform Manager by your marketing team members. ***Dynamic Content*** provides a name and a description of the type of content to be displayed, while ***Published Content*** objects specify when, under what conditions, and where the Dynamic Content will appear.

***Content Placeholders*** are also created through Virto Commerce Platform Manager; however, this requires some effort from developers, web designers, and system management. As soon as a web developer adds a content placeholder to a template, another developer or user with appropriate permissions must register it in Virto Commerce Platform Manager.

***Content Type*** is a template used to define the dynamic content type, i.e. how a particular content type is displayed and what is required for it to appear.

!!! note
	Virto Commerce offers varuious content types out-of-the-box. For example, there is a content type to display banners, i.e. images with links, and another one to display product data (product with an image and price).

The table below shows the content types supplied by Virto Commerce by default. Each of them requires one or more parameter values to specify such things as image files, links to web pages, etc.


| Content Type | Description | Parameters |
|--------------|-------------|------------|
|Flash | Displays an animated Flash file that includes three images, each having a clickable link that leads to a different promotion. You will need to specify the URLs for each link within the Flash file.| *FlashFilePath:* Path to the Flash animation file.<br>*Link1Url, Link2Url, Link3Url:* Full URL to the target page (item, promotion, etc.)|
| Html | Displays HTML content | *RawHtml:* Raw HTML formatted text. |
|ImageClickable |Displays an image that can be clicked to perform an action, e.g., redirect to another page, product, or promotion. |*Alternative text:* Text that is displayed in case the image cannot be opened.<br>*ImageUrl:* Link to the image.<br>TargetUrl: Link to the page the clickable image leads to.<br>Title: Optional title text.|
| ImageNonClickable |Displays a non-clickable image, e.g., to let the customers know about a promotion. |*Alternative text:* Text that is displayed in case the image cannot be opened.<br>*ImageFilePath:* Path to the image file.|
|ProductsWithinCategory |Displays products within a specific category as a slideshow. |*Category code:* Code of the category in question.<br>*Title:* User friendly title of the category.<br>*Item count:* Number of items in the slideshow.<br>*New items:* Switch to show only new items.|

For more information on managing dynamic content, please refer to these dedicated guides:

[Managing Content Items](managing-content-items.md)

[Managing Content Placeholders](managing-content-placeholders.md)

[Managing Content Publishing](managing-published-content.md)

### Tags

You can use the dynamic content feature to display specific content to the customers being targeted. Technically, this targeting is managed through tags. Virto Commerce incorporates a tagging system that is used to set and evaluate tags used to segment customers and to decide when, where, and to which customer the relevant piece of content should be displayed.

The tagging data about a customer is captured in a variety of ways, including the following:

1. Information provided upon customer signup.
2. Information entered by a customer service agent about a customer during the call.
3. Target and referring URLs and search terms captured when a user clicks a link that brings them to Storefront.
4. Customer location.

The data captured by the tags is stored within the user session while the user continues shopping in Storefront. This data can then be used to evaluate whether the customer meets the conditions set for displaying the dynamic content. You can set those conditions whenever you have the ***Dynamic Content*** permissions.

!!! tip
	Refer to [this article](publishing-conditions.md) if you want to learn more about publishing conditions.

## Promotions

***Promotion*** is a marketing tool used to boost sales. In Virto Commerce, you can add a lot of various kinds of promotions to your stores that would yield such rewards as discounts, shipping discounts, or gifts. You can also create or import coupons that could be later used by your customers.

Each promotion is valid under specific [conditions](promotion-rules.md) you can configure, and may provide one or more rewards.

!!! note
	In Virto, promotions are highly customizable and include conditions for customers matching speficic criteria, currencies, products, stock quantity, etc.
	
	For instance, you can configure that customers residing in NYC and grabbing two last spartphones would get 75% off for shipping and two phone cases as a gift.

!!! note
	Promotions may be both store-specific and shared across multiple stores.

For more information on managing promotions, please refer to these dedicated guides:

[Promotion Rules](promotion-rules.md)

[Managing Promotions](managing-promotions.md)

[Promotion Combination Policies](combining-active-promotions.md)