# NewsArticleContent ==~object~==

This type defines the structure of a news article and contains its main content, metadata, and SEO information.

## Fields

| Field                                                         | Description                                                                           |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `id` ==String!==                                              | The Id of the news article.                                            |
| `publishDate` ==DateTime==                                    | The date and time when the article was published.                                     |
| `title` ==String==                                            | The title of the news article.                                                        |
| `content` ==String==                                          | The full content of the news article.                                                 |
| `contentPreview` ==String==                                   | A short preview or excerpt of the news article content.                               |
| `seoInfo` [ ==SeoInfo!== ](/platform/developer-guide/latest/GraphQL-Storefront-API-Reference-xAPI/Catalog/objects/SeoInfo)  | SEO metadata for the article, such as semantic URL, page title, and meta description. |

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../queries/newsArticles">← NewsArticles query</a>
    <a href="../NewsArticleContentConnection">NewsArticleContentConnection →</a>
</div>
